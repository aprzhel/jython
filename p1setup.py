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

# Disable persistence for new servers
def UpdatePersistence():
    for node in printNodes():
       print "NODE: "+node
       node_name = AdminConfig.showAttribute(node, 'name')
       servers = AdminConfig.list('Server', node)
       servers1 = servers.split(lineSeparator)
       # for every server get type and name
       for server in servers1:
          serv_name = AdminConfig.showAttribute(server, 'name')
          serv_type = AdminConfig.showAttribute(server, 'serverType')
          # don't want webservers, DM's or nodeagents
          if serv_type == 'APPLICATION_SERVER':
             # only list new servers
             if serv_name.find('CFMX') >=0 or serv_name.find('CAPSAStwe') >=0 or serv_name.find('PFSTIAStwe') >=0  or serv_name.find('POSAStwe') >=0 or serv_name.find('RBVSAStwe') >=0 or serv_name.find('SingleAStwe') >=0:
                print "--------------------------"
                #print "SERVER_NAME: "+serv_name+" SERVER_TYPE: "+serv_type
                print "SERVER_ID: "+server
                smid = AdminConfig.list('SessionManager',server)
                AdminConfig.modify(smid,[['sessionPersistenceMode',"NONE"]])
                print "SESSION_MANAGER_ID: "+smid+"   "+ AdminConfig.showAttribute(smid,'sessionPersistenceMode')

