#################################################
# This script will enable cookie security for
# dm app.
#################################################
# load common functions 
execfile('/it/mnmid/scripts/jython/common_jython.py')

def enableIscLiteSec():
        print "--------------------------"
	iscDep = AdminConfig.getid('/Deployment:isclite/')
	appDeploy = AdminConfig.showAttribute(iscDep, 'deployedObject')
	configs = AdminConfig.showAttribute (appDeploy, 'configs')
	appConfig = configs[1:len(configs)-1] 
	SM = AdminConfig.showAttribute (appConfig, 'sessionManagement') 
	COOK=AdminConfig.showAttribute(SM,'defaultCookieSettings')
	print "ADMIN_CONSOLE_COOKIE_SSL_ENABLED="+AdminConfig.showAttribute(COOK,'secure')

enableIscLiteSec()
