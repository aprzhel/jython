# get list of node id's
def printNodes():
    nodes = AdminConfig.list('Node')
    # format node id's for jython
    node_list = nodes.split(lineSeparator)
    return node_list

# Save & Sync
def ss():
   print "saving..."
   AdminConfig.save()
   repID = AdminControl.completeObjectName('WebSphere:type=ConfigRepository,process=dmgr,*')
   AdminControl.invoke(repID, "refreshRepositoryEpoch")
   print "synchronizing..."
   for node in printNodes():
      node_name = AdminConfig.showAttribute(node, 'name')
      if node_name.find('Manager') <= 0:
         print "NODE: "+node_name
         sync1 = AdminControl.completeObjectName('type=NodeSync,node='+node_name+',*')
         if sync1 != "":
            AdminControl.invoke(sync1, 'sync')
   print "done"

# Update JVM Generic Arguments
def jvmGenericArgs():
   for node in printNodes():
      servers = AdminConfig.list('Server', node)
      server_list = servers.split(lineSeparator)
      # for every server get type
      for server in server_list:
         serv_type = AdminConfig.showAttribute(server, 'serverType')
         # only want the NA
         if (serv_type == 'DEPLOYMENT_MANAGER') or (serv_type == 'NODE_AGENT') or (serv_type == 'APPLICATION_SERVER'):
            ## disable Java Attach API
            serv_name = AdminConfig.showAttribute(server, 'name')
            jid = AdminConfig.list('JavaVirtualMachine',server)
            jvm_arg_before=AdminConfig.showAttribute(jid,'genericJvmArguments')
            jvm_arg_append='-Dcom.ibm.tools.attach.enable=no ' + jvm_arg_before
            if jvm_arg_before.find('com.ibm.tools.attach.enable') <= 0:
               AdminTask.setGenericJVMArguments('[-serverName ' + serv_name + ' -genericJvmArguments "' + jvm_arg_append + '"]')
            
jtFunctions = ('jvmGenericArgs()')

for jtFunction in jtFunctions.split():
   print "  - executing: " + jtFunction
   try:
      exec(jtFunction)
      ss()
      print "    complete successfully"
   except:
      print "    ERROR: faild to execute " + jtFunction + "! Please review logs for more info."
   print " "
