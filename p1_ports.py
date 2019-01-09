# load the script
def slib():
   this_file = "/export/home/wsadmin/work/aleks/jython/p1_ports.py"
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
          # don't want webservers, DM's or nodeagents
          if serv_type == 'APPLICATION_SERVER':
               # update CFMX2AS1twe* servers
               if serv_name.find('CFMX2AS1twe') >= 0:
                  print "--------------------------"
                  print "SERVER_ID: "+server
                  # ORB port
                  new_orb_port = 9510
                  oid = AdminConfig.list('ObjectRequestBroker',server)
                  host = AdminConfig.showAttribute(AdminConfig.showAttribute(oid,'ORB_LISTENER_ADDRESS'),'host')
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(oid,'ORB_LISTENER_ADDRESS'),'port')
                  print "old -> ORB_LISTENER_ADDRESS: "+port+"   HOST: "+host 
                  AdminConfig.modify(oid, [['ORB_LISTENER_ADDRESS', [['host', host],  ['port', new_orb_port]]]])
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(oid,'ORB_LISTENER_ADDRESS'),'port')
                  print "new -> ORB_LISTENER_ADDRESS: "+port+"   HOST: "+host 
                  # Boottstrap port
                  new_bootstrap_port = 9500
                  nid = AdminConfig.list('NameServer',server)
                  host = AdminConfig.showAttribute(AdminConfig.showAttribute(nid,'BOOTSTRAP_ADDRESS'),'host')
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(nid,'BOOTSTRAP_ADDRESS'),'port')
                  print "old -> BOOTSTRAP_ADDRESS: "+port+"   HOST: "+host
                  AdminConfig.modify(nid, [['BOOTSTRAP_ADDRESS', [['host', host],  ['port', new_bootstrap_port]]]])
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(nid,'BOOTSTRAP_ADDRESS'),'port')
                  print "new -> BOOTSTRAP_ADDRESS: "+port+"   HOST: "+host
               # update CFMX2AS2twe* servers
               if serv_name.find('CFMX2AS2twe') >= 0:
                  print "--------------------------"
                  print "SERVER_ID: "+server
                  # ORB port
                  new_orb_port = 9511
                  oid = AdminConfig.list('ObjectRequestBroker',server)
                  host = AdminConfig.showAttribute(AdminConfig.showAttribute(oid,'ORB_LISTENER_ADDRESS'),'host')
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(oid,'ORB_LISTENER_ADDRESS'),'port')
                  print "old -> ORB_LISTENER_ADDRESS: "+port+"   HOST: "+host 
                  AdminConfig.modify(oid, [['ORB_LISTENER_ADDRESS', [['host', host],  ['port', new_orb_port]]]])
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(oid,'ORB_LISTENER_ADDRESS'),'port')
                  print "new -> ORB_LISTENER_ADDRESS: "+port+"   HOST: "+host 
                  # Boottstrap port
                  new_bootstrap_port = 9501
                  nid = AdminConfig.list('NameServer',server)
                  host = AdminConfig.showAttribute(AdminConfig.showAttribute(nid,'BOOTSTRAP_ADDRESS'),'host')
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(nid,'BOOTSTRAP_ADDRESS'),'port')
                  print "old -> BOOTSTRAP_ADDRESS: "+port+"   HOST: "+host
                  AdminConfig.modify(nid, [['BOOTSTRAP_ADDRESS', [['host', host],  ['port', new_bootstrap_port]]]])
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(nid,'BOOTSTRAP_ADDRESS'),'port')
                  print "new -> BOOTSTRAP_ADDRESS: "+port+"   HOST: "+host
               # update CFMX2AS3twe* servers
               if serv_name.find('CFMX2AS3twe') >= 0:
                  print "--------------------------"
                  print "SERVER_ID: "+server
                  # ORB port
                  new_orb_port = 9512
                  oid = AdminConfig.list('ObjectRequestBroker',server)
                  host = AdminConfig.showAttribute(AdminConfig.showAttribute(oid,'ORB_LISTENER_ADDRESS'),'host')
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(oid,'ORB_LISTENER_ADDRESS'),'port')
                  print "old -> ORB_LISTENER_ADDRESS: "+port+"   HOST: "+host 
                  AdminConfig.modify(oid, [['ORB_LISTENER_ADDRESS', [['host', host],  ['port', new_orb_port]]]])
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(oid,'ORB_LISTENER_ADDRESS'),'port')
                  print "new -> ORB_LISTENER_ADDRESS: "+port+"   HOST: "+host 
                  # Boottstrap port
                  new_bootstrap_port = 9502
                  nid = AdminConfig.list('NameServer',server)
                  host = AdminConfig.showAttribute(AdminConfig.showAttribute(nid,'BOOTSTRAP_ADDRESS'),'host')
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(nid,'BOOTSTRAP_ADDRESS'),'port')
                  print "old -> BOOTSTRAP_ADDRESS: "+port+"   HOST: "+host
                  AdminConfig.modify(nid, [['BOOTSTRAP_ADDRESS', [['host', host],  ['port', new_bootstrap_port]]]])
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(nid,'BOOTSTRAP_ADDRESS'),'port')
                  print "new -> BOOTSTRAP_ADDRESS: "+port+"   HOST: "+host
               # update SingleAS* servers
               if serv_name.find('SingleAS') >= 0:
                  print "--------------------------"
                  print "SERVER_ID: "+server
                  # ORB port
                  new_orb_port = 9513
                  oid = AdminConfig.list('ObjectRequestBroker',server)
                  host = AdminConfig.showAttribute(AdminConfig.showAttribute(oid,'ORB_LISTENER_ADDRESS'),'host')
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(oid,'ORB_LISTENER_ADDRESS'),'port')
                  print "old -> ORB_LISTENER_ADDRESS: "+port+"   HOST: "+host 
                  AdminConfig.modify(oid, [['ORB_LISTENER_ADDRESS', [['host', host],  ['port', new_orb_port]]]])
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(oid,'ORB_LISTENER_ADDRESS'),'port')
                  print "new -> ORB_LISTENER_ADDRESS: "+port+"   HOST: "+host 
                  # Boottstrap port
                  new_bootstrap_port = 9503
                  nid = AdminConfig.list('NameServer',server)
                  host = AdminConfig.showAttribute(AdminConfig.showAttribute(nid,'BOOTSTRAP_ADDRESS'),'host')
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(nid,'BOOTSTRAP_ADDRESS'),'port')
                  print "old -> BOOTSTRAP_ADDRESS: "+port+"   HOST: "+host
                  AdminConfig.modify(nid, [['BOOTSTRAP_ADDRESS', [['host', host],  ['port', new_bootstrap_port]]]])
                  port = AdminConfig.showAttribute(AdminConfig.showAttribute(nid,'BOOTSTRAP_ADDRESS'),'port')
                  print "new -> BOOTSTRAP_ADDRESS: "+port+"   HOST: "+host
