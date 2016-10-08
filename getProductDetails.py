###################################################
#   Sainsbury's Software Engineering Test         #
#   ver. 1.0, 07/10/2016                          #
#                                                 #
#   Author: Matias Ariel Taranto                  #
#   Language: Python 2.7.12                       #
#                                                 #
#   To install libraries:                         #
#   - pip install lxml                            #
#   - xcode-install --install (just in the        #
#     case lxml fails)                            #
#   - pip install requests                        #
#                                                 #
###################################################

# Import three libraries for my script
# html from lxml: to scrape HTML code from an url
# requests: to send HTTP/1.1 requests
# urllib2: module defines functions and classes which help in opening URLs
from lxml import html
import requests
import urllib2
import sys

# Useful function to string format file sizes
def sizeof_fmt(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def buildDescription (pos):
    field = "%s" % productTree.xpath('//div[@class="productText"][%s]/p/text()' % pos)[0]
    if field:
        return "%s -" % field
    else:
        return ""

INITIAL_URL = 'http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html'

# Get the HTML code from the given initial URL, parse its content and sace the list of links for each product
try:
    page = requests.get(INITIAL_URL)
    print "Getting HTML code from the initial URL"
    tree = html.fromstring(page.content)
    print "Parsing HTML code"
    productNamesList = tree.xpath('//div[@class="productInfo"]/h3/a/@href')
    print "Getting the list of product links"
except:
    e = sys.exc_info()[1]
    print "Error: %s" % e
    sys.exit(1)

# Initialize the single product details list, the response list and the total variable
productDetails = {}
response = {}
total = 0

# This For-loop gets the HTML code from each product link
try:
    if not productNamesList:
        sys.exit("Sorry. No products found.")

    for productLink in productNamesList:
        singleProduct = requests.get(productLink) # single product link
        productTree = html.fromstring(singleProduct.content)

        # Calculate the size of the page
        try:
            f = urllib2.urlopen(productLink)
            size = len(f.read())
            productDetails["size"] = sizeof_fmt(size) # Put the value in the product list
        except:
            e = sys.exc_info()[0]
            print "Error: %s" % e
            productDetails["size"] = ""

        # Get the product price per unit and update total value
        price = str(productTree.xpath('//p[@class="pricePerUnit"]/text()')[0][2:])
        if not price:
            productDetails["unit_price"] = ""
        else:
            productDetails["unit_price"] = price # Put the value in the product list
            total = total + float(price)

        # Build the description value from few details in each page: Description, Country of Origin, Size and Storage
        description = buildDescription(1)
        cor = buildDescription(3)
        productSize = buildDescription(4)
        storage = buildDescription(5)
        description = "%s %s %s %s" % (description, cor, productSize, storage)
        productDetails["description"] = description # Put the value in the product list

        # Get the product title
        title = productTree.xpath('//div[@class="productTitleDescriptionContainer"]/h1/text()')[0]
        if not price:
            productDetails["title"] = ""
        else:
            productDetails["title"] = title # Put the value in the product list

        # If the "result" list is not in the list, the script creates it and then appen the product list
        if "results" not in response:
            response["results"] = list()
        response["results"].append( productDetails )
        print "Adding the product details list to the response list"

    response["total"] = ("%.2f" % total) # Put the total value in the response list
    print "Adding the total to the response list"

    print response # Print out the response list
except:
    e = sys.exc_info()[0]
    print "Error: %s" % e
    sys.exit(1)
