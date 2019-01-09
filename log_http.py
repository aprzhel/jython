# load common functions 
execfile('/it/mnmid/scripts/jython/common_jython.py')

# Update retention for App Server HTTP logs
def updateAsWebLog():
    for node in printNodes():
       node_name = AdminConfig.showAttribute(node, 'name')
       print "NODE: "+node_name
       servers = AdminConfig.list('Server', node)
       server_list = servers.split(lineSeparator)
       # for every server get type and name
       for server in server_list:
          serv_name = AdminConfig.showAttribute(server, 'name')
          serv_type = AdminConfig.showAttribute(server, 'serverType')
          # don't want webservers, DM's or nodeagents
          if serv_type == 'APPLICATION_SERVER':
               # update required servers
               print "--------------------------"
               print "SERVER: "+serv_name
	       serverVar = AdminConfig.list('Server', server)
	       httpLog = AdminConfig.list('HTTPAccessLoggingService', serverVar)
               #AdminConfig.modify(httpLog, '[[enable "true"]]')
               accessLog = AdminConfig.showAttribute(httpLog, 'accessLog')
               errorLog = AdminConfig.showAttribute(httpLog, 'errorLog')
               AdminConfig.modify(accessLog, '[[maximumBackupFiles 10] [maximumSize 2]]')
               AdminConfig.modify(errorLog, '[[maximumBackupFiles 10] [maximumSize 2]]')



#	       var_name = 'SERVER_LOG_ROOT'
#              var_value = '/opt/WebSphere/applications/logs/'+serv_name
#              vars = AdminConfig.list('VariableSubstitutionEntry',server).split(lineSeparator)
#	       for variable in vars:
#	          if AdminConfig.showAttribute(variable,'symbolicName') == var_name:
#		     print "old -> LOG_ROOT: "+AdminConfig.showAttribute(variable,'value')
#               	     AdminConfig.modify(variable,[['value',var_value]])
#		     print "new -> LOG_ROOT: "+AdminConfig.showAttribute(variable,'value')
#

updateAsWebLog()
ss()
