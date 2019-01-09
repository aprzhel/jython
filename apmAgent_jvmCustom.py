#################################################
# This script will add the Generic JVM argument 
# -javaagent: to each app server
#################################################
# load common functions 
execfile('/it/mnmid/scripts/jython/common_jython.py')

# Update JVM Custom Properties for APM
def jvmCustomApm():
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
         if (serv_type == 'APPLICATION_SERVER') and (serv_name != ""):
            # set '-javaagent'
            print "--------------------------"
            print "SERVER: "+serv_name
            jvm_arg_append='[-javaagent:/opt/bmc_appdiag/ADOPsInstall/adops-agent.jar]'
            jid = AdminConfig.list('JavaVirtualMachine',server)
            jvm_arg_before=AdminConfig.showAttribute(jid,'genericJvmArguments')
            print "Generig JVM Arguments [original]: "+jvm_arg_before
            if jvm_arg_before.find('javaagent') <= 0:
               AdminTask.setGenericJVMArguments(['-serverName', serv_name, '-genericJvmArguments', jvm_arg_before+jvm_arg_append])
            jvm_arg_after=AdminConfig.showAttribute(jid,'genericJvmArguments')
            print "Generig JVM Arguments [updated]: "+jvm_arg_after

jvmCustomApm()
ss()
