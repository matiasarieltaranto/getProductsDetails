###################################################
#   Sainsbury's Software Engineering Test         #
#   ver. 1.0, 07/10/2016                          #
#                                                 #
#   Author: Matias Ariel Taranto                  #
#   Language: Python 2.7.12                       #
#                                                 #
###################################################

Installation:

OS - MAC / Linux:

  To install libraries:                         
    - pip install lxml                            
    - xcode-install --install (just in the        
      case lxml fails)                            
    - pip install requests  

Windows:

  python:
    go to the Python webpage to download the installer

  To install libraries:                         
    - lxml: For MS Windows, recent lxml releases feature community donated binary distributions, although you might still want to take a look at the related FAQ entry. If you fail to build lxml on your MS Windows system from the signed and tested sources that we release, consider using the binary builds from PyPI or the unofficial Windows binaries that Christoph Gohlke generously provides.                            
    - curl -OL https://github.com/kennethreitz/requests/tarball/master
      # optionally, zipball is also available (for Windows users).

Run:      

To run the script, just open a window of your Terminal application and type:

python getProductDetails.py
