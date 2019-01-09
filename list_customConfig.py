###############################################
# This script will display all USPS-customized 
# settings 
###############################################
# load common functions 
execfile('/it/mnmid/scripts/jython/common_jython.py')

# load the script
#def slib():
#   this_file = "/export/home/wsadmin/work/aleks/jython/list_serverConfig.py"
#   print "now loading "+this_file+" ..."
#   execfile(this_file)
#   print "execfile('"+this_file+"')"
#   print "Done"
#   return 0

# List Resource attribute
def listAttr(serverId,rType,aName):
   rid = AdminConfig.list(rType,serverId)
   attrValue=AdminConfig.showAttribute(rid,aName)
   return attrValue

# List custom JVM property
def jvmListCustProp(serverId,pName):
   pValue="NULL"
   propList=[]
   jid = AdminConfig.list('JavaVirtualMachine',serverId)
   propList=AdminConfig.showAttribute(jid, "systemProperties")
   for prop in splitProps(propList)[:]:
      propName=AdminConfig.showAttribute(prop, "name")
      propValue=AdminConfig.showAttribute(prop, "value")
      if propName == pName:
         pValue=propValue
   return pValue

# List Resource property
def listProp(serverId,rType,pName):
   pValue="NULL"
   propList=AdminConfig.showAttribute(serverId,rType)
   pValue=AdminConfig.showAttribute(propList,pName)
   return pValue

###############################################
# List Config for each server
def listServerConfig():
    for node in printNodes():
       #node_name = AdminConfig.showAttribute(node, 'name')
       #print "NODE: "+node_name
       servers = AdminConfig.list('Server', node)
       server_list = servers.split(lineSeparator)
       # for every server get type and name
       print "SERVER(s) =========================="
       for server in server_list:
          serv_name = AdminConfig.showAttribute(server, 'name')
          serv_type = AdminConfig.showAttribute(server, 'serverType')
          # don't want webservers, DM's or nodeagents
          if serv_type == 'APPLICATION_SERVER':
             print "jvm args --------------------------"
             print "SERVER="+serv_name
 	     print "MIN-HEAP="+listAttr(server,'JavaVirtualMachine','initialHeapSize')
             print "MAX-HEAP="+listAttr(server,'JavaVirtualMachine','maximumHeapSize')
             print "VERBOSE_ClassLoad="+listAttr(server,'JavaVirtualMachine','verboseModeClass')
             print "VERBOSE_GC="+listAttr(server,'JavaVirtualMachine','verboseModeGarbageCollection')
             print "VERBOSE_JNI="+listAttr(server,'JavaVirtualMachine','verboseModeJNI')
             print "HPROF="+listAttr(server,'JavaVirtualMachine','runHProf')
             print "DEBUGMODE="+listAttr(server,'JavaVirtualMachine','debugMode')
             print "JVMCUSTOM_HTTP_ONLY="+jvmListCustProp(server,'com.ibm.ws.security.addHttpOnlyAttributeToCookies')
             print "session  --------------------------"
             print "ACCESS_ON_TIMEOUT="+listAttr(server,'SessionManager','accessSessionOnTimeout')
             print "ENABLE_SEC_INTEGRATION="+listAttr(server,'SessionManager','enableSecurityIntegration')
             print "MAX_WAIT="+listAttr(server,'SessionManager','maxWaitTime')
             print "ALLOW_SERIALIZED="+listAttr(server,'SessionManager','allowSerializedSessionAccess')
             print "ENABLE_SSL_TRACK="+listAttr(server,'SessionManager','enableSSLTracking')
             print "ENABLE_COOKIES="+listAttr(server,'SessionManager','enableCookies')
             print "ENABLE="+listAttr(server,'SessionManager','enable')
             print "ENABLE_PROTO_SWITCH="+listAttr(server,'SessionManager','enableProtocolSwitchRewriting')
             print "ENABLE_URL_REWRITE="+listAttr(server,'SessionManager','enableUrlRewriting')
             print "SysOut   --------------------------"
             print "ROLLOVER_TYPE="+listProp(server,'outputStreamRedirect','rolloverType')
             print "ROLLOVER_SIZE="+listProp(server,'outputStreamRedirect','rolloverSize')
             print "BASE_HOUR="+listProp(server,'outputStreamRedirect','baseHour')
             print "ROLL_PERIOD="+listProp(server,'outputStreamRedirect','rolloverPeriod')
             print "NUM_GENERATIONS="+listProp(server,'outputStreamRedirect','maxNumberOfBackupFiles')
             print "SysErr   --------------------------"
             print "ROLLOVER_TYPE="+listProp(server,'errorStreamRedirect','rolloverType')
             print "ROLLOVER_SIZE="+listProp(server,'errorStreamRedirect','rolloverSize')
             print "BASE_HOUR="+listProp(server,'errorStreamRedirect','baseHour')
             print "ROLL_PERIOD="+listProp(server,'errorStreamRedirect','rolloverPeriod')
             print "NUM_GENERATIONS="+listProp(server,'errorStreamRedirect','maxNumberOfBackupFiles')
             print "IHSout   --------------------------"
             print "ENABLED="+listAttr(server,'HTTPAccessLoggingService','enable')
             accessId=listAttr(server,'HTTPAccessLoggingService','accessLog')
             print "NUM_GENERATIONS="+AdminConfig.showAttribute(accessId,'maximumBackupFiles')
             print "ROLLOVER_SIZE="+AdminConfig.showAttribute(accessId,'maximumSize')
             print "IHSerr   --------------------------"
             print "ENABLED="+listAttr(server,'HTTPAccessLoggingService','enable')
             errorId=listAttr(server,'HTTPAccessLoggingService','errorLog')
             print "NUM_GENERATIONS="+AdminConfig.showAttribute(errorId,'maximumBackupFiles')
             print "ROLLOVER_SIZE="+AdminConfig.showAttribute(errorId,'maximumSize')

###############################################
# List Config for DM
def listDmConfig():
    print "DM =========================="
    for node in printNodes():
       #node_name = AdminConfig.showAttribute(node, 'name')
       #print "NODE: "+node_name
       servers = AdminConfig.list('Server', node)
       server_list = servers.split(lineSeparator)
       # for every server get type and name
       for server in server_list:
          serv_name = AdminConfig.showAttribute(server, 'name')
          serv_type = AdminConfig.showAttribute(server, 'serverType')
          # don't want webservers, DM's or nodeagents
          if serv_type == 'DEPLOYMENT_MANAGER':
             print "jvm args --------------------------"
             print "SERVER="+serv_name
             print "JVMCUSTOM_HTTP_ONLY="+jvmListCustProp(server,'com.ibm.ws.security.addHttpOnlyAttributeToCookies')
             print "JVMCUSTOM_CSRF_CHECK="+jvmListCustProp(server,'adminconsole.csrf.check')
             print "JVMCUSTOM_PASS_NO-AUTOCOMPLETE="+jvmListCustProp(server,'adminconsole.password.autocompleteoff')

###############################################
# List Config for Cell
def listCellConfig():
    print "CELL =========================="
    # list Global Security status
    print "GLOBAL_SECURITY="+AdminTask.isAppSecurityEnabled()
    # list CORBA naming service Groups (must be EVERYONE)
    print "CORBA_NAME_GROUPS="+findInNamValPairs(AdminTask.listGroupsForNamingRoles(),'CosNamingRead')
    # list SSO SSL status
    ssoAttr = AdminTask.getSingleSignon()
    print "SSO_SSL_REQUIRED="+findInBracketPairs(ssoAttr,'requiresSSL')
    print "SSO_INTEROPER_MODE="+findInBracketPairs(ssoAttr,'com.ibm.ws.security.ssoInteropModeEnabled')
    # list LDAP SSL status
    ldapAttr = AdminTask.getUserRegistryInfo('[-userRegistryType LDAPUserRegistry]')
    print "LDAP_SSL="+findInBracketPairs(ldapAttr,'sslEnabled')
    # list running apps
    print "RUNNING_APPS="+AdminApp.list()
    # list securityLevel and ciphers
    secLevel=findInBracketPairs(AdminTask.getSSLConfig('[-alias CellDefaultSSLSettings ]'),'securityLevel')
    print "CIPHERS=",AdminTask.listSSLCiphers('[-sslConfigAliasName CellDefaultSSLSettings -securityLevel '+secLevel+']')
    # list transport for each core group
    cgList = AdminTask.getAllCoreGroupNames()
    for cgName in cgList.split(lineSeparator):
       try:
          cgId = AdminConfig.getid('/Cell:'+cellName+'/CoreGroup:'+cgName+'/')
       except:
          cgId = 'none'
       if cgId.find('none') < 0:
          print "coreGroup:"+cgName+" --------------------------"
          try:
             chanChain=AdminConfig.showAttribute(cgId,'channelChainName') # list SIB SSL status
          except:
             chanChain="none"
          print "CHANNEL_CHAIN="+chanChain
    try:
       busses =  AdminConfig.showAttribute(AdminTask.listSIBuses() ,'name')
    except:
       busses = 'none'
    if busses.find('none') < 0:
       for busName in busses.split():
          print "BUS="+busName+"   SSL_STATUS="+findInNamValPairs(AdminTask.showSIBus('[-bus '+busName+' ]'),'secure')
    # list CSI SSL status
    print "csi inbound --------------------------"
    csiInAttr = AdminTask.getCSIInboundInfo() 
    print "MESSAGE_AUTH="+findInBracketPairs(csiInAttr,'messageLevelAuth')
    print "AUTH_MECH="+findInBracketPairs(csiInAttr,'supportedAuthMechList')
    print "CLIENT_AUTH="+findInBracketPairs(csiInAttr,'clientCertAuth')
    print "TRANSPORT_LAYER="+findInBracketPairs(csiInAttr,'transportLayer')
    print "SSL_CONF="+findInBracketPairs(csiInAttr,'sslConfiguration')
    print "IDENTITY_ASSERT="+findInBracketPairs(csiInAttr,'enableIdentityAssertion')
    print "STATEFULL_SESSION="+findInBracketPairs(csiInAttr,'statefulSession')
    print "ATTR_PROPAGATION="+findInBracketPairs(csiInAttr,'enableAttributePropagation')
    print "TRUSTED_IDENTITIES="+findInBracketPairs(csiInAttr,'trustedIdentities')
    print "csi outbound --------------------------"
    csiOutAttr = AdminTask.getCSIOutboundInfo() 
    print "MESSAGE_AUTH="+findInBracketPairs(csiOutAttr,'messageLevelAuth')
    print "AUTH_MECH="+findInBracketPairs(csiOutAttr,'supportedAuthMechList')
    print "CLIENT_AUTH="+findInBracketPairs(csiOutAttr,'clientCertAuth')
    print "TRANSPORT_LAYER="+findInBracketPairs(csiOutAttr,'transportLayer')
    print "SSL_CONF="+findInBracketPairs(csiOutAttr,'sslConfiguration')
    print "IDENTITY_ASSERT="+findInBracketPairs(csiOutAttr,'enableIdentityAssertion')
    print "STATEFULL_SESSION="+findInBracketPairs(csiOutAttr,'statefulSession')
    print "ATTR_PROPAGATION="+findInBracketPairs(csiOutAttr,'enableAttributePropagation')
    print "TRUSTED_IDENTITIES="+findInBracketPairs(csiOutAttr,'trustedIdentities')
    # list Audit Policy
    print "audit --------------------------"
    auditAttr = AdminTask.getAuditPolicy() 
    print "AUDIT_ENABLED="+findInBracketPairs(auditAttr,'auditEnabled')
    print "AUDIT_POLICY="+findInBracketPairs(auditAttr,'auditPolicy')

###############################################
listCellConfig()
listDmConfig()
listServerConfig()
