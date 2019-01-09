# load the script
def slib():
   this_file = "/it/mnmid/tmp/x.py"
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

# Update AppServer ports
def updatePort():
    for node in printNodes():
       print "NODE: "+node
       node_name = AdminConfig.showAttribute(node, 'name')
       servers = AdminConfig.list('Server', node)
       server_list = servers.split(lineSeparator)
       # for every server get type and name
       for server in server_list:
          serv_name = AdminConfig.showAttribute(server, 'name')
          serv_type = AdminConfig.showAttribute(server, 'serverType')
          # don't want webservers, DM's or app servers
          if serv_type == 'NODE_AGENT':
                  print "--------------------------"
                  print "NODE: "+node_name
                  # ORB port
                  new_orb_port = 9900
                  oid = AdminConfig.list('ObjectRequestBroker',server)
                  host = AdminConfig.showAttribute(AdminConfig.showAttribute(oid,'ORB_LISTENER_ADDRESS'),'host')
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(oid,'ORB_LISTENER_ADDRESS'),'port')
                  print "old -> ORB_LISTENER_ADDRESS: "+port+"   HOST: "+host 
                  AdminConfig.modify(oid, [['ORB_LISTENER_ADDRESS', [['host', host],  ['port', new_orb_port]]]])
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(oid,'ORB_LISTENER_ADDRESS'),'port')
                  print "new -> ORB_LISTENER_ADDRESS: "+port+"   HOST: "+host 
