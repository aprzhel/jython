#################################################
# This script will enable cookie security for
# dm app.
#################################################
# load common functions 
execfile('/it/mnmid/scripts/jython/common_jython.py')

# enable Security integration & SSL cookies for DM
def enableSecInt():
    for node in printNodes():
       node_name = AdminConfig.showAttribute(node, 'name')
       servers = AdminConfig.list('Server', node)
       servers1 = servers.split(lineSeparator)
       # for every server get type and name
       for server in servers1:
          serv_name = AdminConfig.showAttribute(server, 'name')
          serv_type = AdminConfig.showAttribute(server, 'serverType')
          # only want  DM
          if serv_type == 'DEPLOYMENT_MANAGER':
                print "--------------------------"
                smid = AdminConfig.list('SessionManager',server)
                print "Enabling SSL for DM cookies on node: "+node_name+" with session manager: "+smid
		print "BEFORE UPDATE - Attr: CookieSSL = "+ AdminConfig.showAttribute(smid,'enable')
		print "BEFORE UPDATE - Attr: SecIntegr = "+ AdminConfig.showAttribute(smid,'enableSecurityIntegration')
		print "..."
                AdminConfig.modify(smid,[['enable',"true"]])
                ###AdminConfig.modify(smid,[['enableSecurityIntegration',"false"]])
		print "AFTER UPDATE - Attr: CookieSSL = "+ AdminConfig.showAttribute(smid,'enable')
		print "AFTER UPDATE - Attr: SecIntegr = "+ AdminConfig.showAttribute(smid,'enableSecurityIntegration')

def enableIscLiteSec():
        print "--------------------------"
 	print "Enabling Cookie SSL for isclite"
	iscDep = AdminConfig.getid('/Deployment:isclite/')
	appDeploy = AdminConfig.showAttribute(iscDep, 'deployedObject')
	configs = AdminConfig.showAttribute (appDeploy, 'configs')
	appConfig = configs[1:len(configs)-1] 
	SM = AdminConfig.showAttribute (appConfig, 'sessionManagement') 
	COOK=AdminConfig.showAttribute(SM,'defaultCookieSettings')
	csetting = AdminConfig.show(COOK)
	kuki = ['secure', "true"]
	#kuki = ['secure', "false"]
	cookie = [kuki]
	csetting = AdminConfig.show(COOK)
	print "BEFORE UPDATE - Cookie SSL: "+AdminConfig.showAttribute(COOK,'secure')
	print "..."
	AdminConfig.modify(COOK, cookie)
	print "After UPDATE - Cookie SSL: "+AdminConfig.showAttribute(COOK,'secure')

#enableSecInt()
enableIscLiteSec()
ss()
