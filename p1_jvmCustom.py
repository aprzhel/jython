# load the script
def slib():
   this_file = "/export/home/wsadmin/work/aleks/jython/p1_jvmCustom.py"
   print "now loading "+this_file+" ..."
   execfile(this_file)
   print "execfile('"+this_file+"')"
   print "Done"
   return 0

# Save
def save():
   print "saving..."
   AdminConfig.save()
   print "done"
   return 0

# Save & Sync
def ss():
   print "saving..."
   AdminConfig.save()
   print "synchronizing..."
   for node in printNodes():
      node_name = AdminConfig.showAttribute(node, 'name')
      if node_name.find('Manager') <= 0: 
         print "NODE: "+node_name
         sync1 = AdminControl.completeObjectName('type=NodeSync,node='+node_name+',*')
         if sync1 != "":
            AdminControl.invoke(sync1, 'sync')

   print "done"
   return 0

# get cell id, just for printing reasons
def printCell():
    cell = AdminConfig.list('Cell')
    return cell

# from cell id, get cell name, again just for printing
def printCellName():
    cell_name = AdminConfig.showAttribute(cell, 'name')
    return cell_name

# get list of node id's
def printNodes():
    nodes = AdminConfig.list('Node')
    # format node id's for jython
    nodes1 = nodes.split(lineSeparator)
    return nodes1

# Update JVM Custom Properties
def jvmCustom():
    for node in printNodes():
       print "NODE: "+node
       node_name = AdminConfig.showAttribute(node, 'name')
       servers = AdminConfig.list('Server', node)
       server_list = servers.split(lineSeparator)
       # for every server get type and name
       for server in server_list:
          serv_name = AdminConfig.showAttribute(server, 'name')
          serv_type = AdminConfig.showAttribute(server, 'serverType')
          # don't want webservers, DM's or nodeagents
          if serv_type == 'APPLICATION_SERVER':
               # set 'JASYPT_KEY' for requested servers
               if serv_name.find('AdminAS') >= 0 or serv_name.find('CAPSAS') >= 0 or serv_name.find('CFMX1AS') >= 0 or serv_name.find('CFMX2AS') >= 0 or serv_name.find('CFMXAS') >= 0 or serv_name.find('MXMLAdmAS') >= 0 or serv_name.find('MailXMLAS') >= 0 or serv_name.find('PBVFSAS') >= 0 or serv_name.find('PFSTIAS') >= 0 or serv_name.find('POFSAS') >= 0 or serv_name.find('POSASP') >= 0 or serv_name.find('POSAS') >= 0 or serv_name.find('PSHDDAS') >= 0 or serv_name.find('RBVSAS') >= 0 or serv_name.find('SingleAS') >= 0 or serv_name.find('eDocAS') >= 0:
                  print "-------------------------- 1"
                  print "SERVER: "+server
                  prop_name = 'JASYPT_KEY'
                  prop_value = 'Yx9(PO)2B'
		  prop_attr = [['name',prop_name],['value',prop_value]]
                  jid = AdminConfig.list('JavaVirtualMachine',server)
                  AdminConfig.create('Property',jid,prop_attr,'systemProperties')
                  print "PROPS: "+AdminConfig.showAttribute(jid,'systemProperties')
               # set 'ADMIN_KEY' for requested servers
               if serv_name.find('CAPSAS') >= 0 or serv_name.find('MXMLAdmAS') >= 0 or serv_name.find('MailXMLAS') >= 0 or serv_name.find('PBVFSAS') >= 0 or serv_name.find('PFSTIAS') >= 0 or serv_name.find('POFSAS') >= 0 or serv_name.find('POSASP') >= 0 or serv_name.find('PSHDDAS') >= 0 or serv_name.find('RBVSAS') >= 0 or serv_name.find('SingleAS') >= 0 or serv_name.find('eDocAS') >= 0:
                  print "-------------------------- 2"
                  print "SERVER: "+server
                  prop_name = 'ADMIN_KEY'
                  prop_value = 'HhdeOjTgum/vGwy/HgODEhulPH/0Ltmr'
		  prop_attr = [['name',prop_name],['value',prop_value]]
                  jid = AdminConfig.list('JavaVirtualMachine',server)
                  AdminConfig.create('Property',jid,prop_attr,'systemProperties')
                  print "PROPS: "+AdminConfig.showAttribute(jid,'systemProperties')
               # set 'HttpSessionIdReuse' for requested servers
               if serv_name.find('CAPSAS') >= 0 or serv_name.find('CFMX1AS') >= 0 or serv_name.find('CFMX2AS') >= 0 or serv_name.find('CFMXAS') >= 0 or serv_name.find('PBVFSAS') >= 0 or serv_name.find('RBVSAS') >= 0:
                  print "-------------------------- 3"
                  print "SERVER: "+server
                  prop_name = 'HttpSessionIdReuse'
                  prop_value = 'true'
		  prop_attr = [['name',prop_name],['value',prop_value]]
                  jid = AdminConfig.list('JavaVirtualMachine',server)
                  AdminConfig.create('Property',jid,prop_attr,'systemProperties')
                  print "PROPS: "+AdminConfig.showAttribute(jid,'systemProperties')
               # set 'java.awt.fonts' for requested servers
               if serv_name.find('CFMX1AS') >= 0 or serv_name.find('CFMX2AS') >= 0 or serv_name.find('CFMXAS') >= 0:
                  print "-------------------------- 4"
                  print "SERVER: "+server
                  prop_name = 'java.awt.fonts'
                  prop_value = '/opt/WebSphere/AppServer61/java/jre/lib/fonts'
		  prop_attr = [['name',prop_name],['value',prop_value]]
                  jid = AdminConfig.list('JavaVirtualMachine',server)
                  AdminConfig.create('Property',jid,prop_attr,'systemProperties')
                  print "PROPS: "+AdminConfig.showAttribute(jid,'systemProperties')
               # set 'java.awt.headless' for requested servers
               if serv_name.find('CFMX1AS') >= 0 or serv_name.find('CFMX2AS') >= 0:
                  print "-------------------------- 5"
                  print "SERVER: "+server
                  prop_name = 'java.awt.headless'
                  prop_value = 'true'
		  prop_attr = [['name',prop_name],['value',prop_value]]
                  jid = AdminConfig.list('JavaVirtualMachine',server)
                  AdminConfig.create('Property',jid,prop_attr,'systemProperties')
                  print "PROPS: "+AdminConfig.showAttribute(jid,'systemProperties')
               # set 'com.ibm.ws.webservices.serializeDetailElementUsingDefaultNamespace' for requested servers
               if serv_name.find('POSAS') >= 0:
                  print "-------------------------- 6"
                  print "SERVER: "+server
                  prop_name = 'com.ibm.ws.webservices.serializeDetailElementUsingDefaultNamespace'
                  prop_value = 'true'
		  prop_attr = [['name',prop_name],['value',prop_value]]
                  jid = AdminConfig.list('JavaVirtualMachine',server)
                  AdminConfig.create('Property',jid,prop_attr,'systemProperties')
                  print "PROPS: "+AdminConfig.showAttribute(jid,'systemProperties')
