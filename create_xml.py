#! /usr/bin/env python3

import sys
import getopt
import logging
import xml.etree.ElementTree as et

TagName = 'Create_xml'
n = len(sys.argv)

manifestfilename = "manifest.xml"

from datetime import datetime
LogFilename = datetime.now().strftime('create_xml_%H:%M:%S_%d-%m-%Y.log')
for handler in logging.root.handlers[:]:
      logging.root.removeHandler(handler)


logging.basicConfig(handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(f"{LogFilename}", mode="w"),
    ] , format='%(asctime)s %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

##########################################################################################################################

#information usage

def usage():
 
 print("Usage: <package> <name> <type> <version> <hardware>")
 print(" -p, --package                : package name")
 print(" -n, --name                   : name")
 print(" -t, --typehandler            : type handler")
 print(" -v, --version                : component version/update version")
 print(" -d, --hardware               : hardware information")
 print(" -h, --help                   : usage information")
 exit(1)

#################################################################################################################################################

#parsing input argument


def parse():


 global package
 global name
 global typehandler 
 global version
 global hardware

 package = None
 name = None
 typehandler = None
 version =None
 hardware = None
 argv = sys.argv[1:]
 if n >= 11:
      try:
       opts, args = getopt.getopt(argv, "p:n:t:v:d:h:", ["package=", "name=", "typehandler=", "version=", "hardware=", "password=", "help="])
      
      except:
       print("Error")
       
      for opt, arg in opts:
        if opt in ['-p', '--package']:
             package = arg
        elif opt in ['-n', '--name']:
             name = arg
        elif opt in ['-t', '--typehandler']:
             typehandler = arg
        elif opt in ['-h', '--help']:
             usage()
        elif opt in ['-v', '--version']:
             version = arg
        elif opt in ['-d', '--hardware']:
             hardware = arg


      if package == None:
         logging.error(f"[{TagName}]: package name is empty")
         usage()
      elif name == None:
         logging.error(f"[{TagName}]:  File name is empty")
         usage()
      elif typehandler == None:
         logging.error(f"[{TagName}]: typehandler is empty")
         usage()
      elif version == None:
         logging.error(f"[{TagName}]: version is empty")
         usage()
      elif hardware == None:
         logging.error(f"[{TagName}]: hardware is empty")
         usage()    
 else:
  usage()


############################################################################################################################################


#generate manifest.xml file

def GenerateXML(fileName) :
	
	root = et.Element("xl4_pkg_update_manifest")
	
	b1 = et.SubElement(root, "package")
	b1.text = package
	b2 = et.SubElement(root, "name")
	b2.text = name
	
	c1 = et.SubElement(root, "type")
	c1.text = typehandler
	c2 = et.SubElement(root, "version")
	c2.text = version
	
	d1 = et.SubElement(root, "hardware")
	d1.text = hardware

	tree = et.ElementTree(root)

	from xml.dom import minidom
	xmlstr = minidom.parseString(et.tostring(root)).toprettyxml(indent="   ")
	with open(fileName, "w") as f:
		f.write(xmlstr)


############################################################################################################################################

#main function

def main():

 if n < 11  : 
   usage()
 
 parse()
 
 logging.info(f"[{TagName}]:Parsing input argument successfully Done..")

 logging.info(f"[{TagName}]:package : {package} ")
 logging.info(f"[{TagName}]:name : {name} ")
 logging.info(f"[{TagName}]:typehandler : {typehandler} ")
 logging.info(f"[{TagName}]:version : {version} ")
 logging.info(f"[{TagName}]:hardware : {hardware} ")
 
 logging.info(f"[{TagName}]:Creating manifest.xml file..")

 
 GenerateXML(manifestfilename)
 logging.info(f"[{TagName}]:manifest.xml file created successfully!")


if __name__ == "__main__":
    main()
