#------------------------------------------------------------------------------
# Admin console cookie security script
#
# Installing the console:
# wsadmin.sh -f secureConsole.py install
#
# Uninstalling the console:
# wsadmin.sh -f secureConsole.py remove
#------------------------------------------------------------------------------
import sys

#------------------------------------------------------------------------------
# Print script usage
#------------------------------------------------------------------------------
def printUsage():
	print "Usage: wsadmin secureConsole.py enable"
	print "  or:  wsadmin secureConsole.py disable"
	print ""


#------------------------------------------------------------------------------
# Main entry point
#------------------------------------------------------------------------------

if len(sys.argv) < 1 or len(sys.argv) > 1:
	sys.stderr.write("Invalid number of arguments\n")
	printUsage()
	sys.exit(101)
else:
	if len(sys.argv) == 1:
		mode = sys.argv[0]
		enabledisable = "enable"
	if mode == "enable":
		print "Enabling secure flag for JSESSIONID cookie"
		enabledisable = "true"
	elif mode == "disable":
		print "Disabling secure flag for JSESSIONID cookie"
		enabledisable = "false"	
	else:
		sys.stderr.write("Invalid command:  " + mode + "\n")
		printUsage()
		sys.exit(103)

	print "Updating the deployment.xml for the Administrative Console isclite.ear"
	deployments = AdminConfig.getid('/Deployment:isclite/')
	appDeploy = AdminConfig.showAttribute(deployments, 'deployedObject')
	configs = AdminConfig.showAttribute (appDeploy, 'configs')
	appConfig = configs[1:len(configs)-1] 
	SM = AdminConfig.showAttribute (appConfig, 'sessionManagement') 
	COOK=AdminConfig.showAttribute(SM,'defaultCookieSettings')
	csetting = AdminConfig.show(COOK)
	kuki = ['secure', enabledisable]
	cookie = [kuki]
	AdminConfig.modify(COOK, cookie)
	csetting = AdminConfig.show(COOK)
	print ("If you choose to continue, the deployment.xml will be updated and the islite application (adminconsole) will be immediately restarted.")
	response = raw_input("Do you wish to save your changes? Please enter a Y/N: ")
	if response not in  ('y', 'Y'):
		print ("Your changes will be discarded")
		sys.exit(104)
	AdminConfig.save()
	print("JSESSIONID cookie is now " + mode +"d")

