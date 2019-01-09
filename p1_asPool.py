# load the script
def slib():
   this_file = "/export/home/wsadmin/work/aleks/jython/p1_asPool.py"
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

# Update App Server Default Thread pool
def asPool():
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
               # set MaxPool = 50 for requested servers
               if serv_name.find('CFMX1AS') >= 0 or serv_name.find('CFMX2AS') >= 0:
                  print "-------------------------- 50"
                  print "SERVER: "+server
                  pool_val = 50
                  max_pool = [['maximumSize',pool_val]]
                  pools = AdminConfig.list('ThreadPool',server)
                  for pool in pools.split(lineSeparator):
		     if pool.find('Default') >= 0:
		        print "old -> MAX-POOL: "+AdminConfig.showAttribute(pool,'maximumSize')
		        AdminConfig.modify(pool,max_pool)
		        print "old -> MAX-POOL: "+AdminConfig.showAttribute(pool,'maximumSize')
               # set MaxPool = 100 for requested servers
               if serv_name.find('CFMXAS') >= 0:
                  print "-------------------------- 100"
                  print "SERVER: "+server
                  pool_val = 100
                  max_pool = [['maximumSize',pool_val]]
                  pools = AdminConfig.list('ThreadPool',server)
                  for pool in pools.split(lineSeparator):
		     if pool.find('Default') >= 0:
		        print "old -> MAX-POOL: "+AdminConfig.showAttribute(pool,'maximumSize')
		        AdminConfig.modify(pool,max_pool)
		        print "old -> MAX-POOL: "+AdminConfig.showAttribute(pool,'maximumSize')
