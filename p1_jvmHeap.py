# load the script
def slib():
   this_file = "/export/home/wsadmin/work/aleks/jython/p1_jvmHeap.py"
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

# Update JVM Heap Size
def jvmHeap():
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
               # set MaxHeap = 512 for requested servers
               if serv_name.find('CAPSAS') >= 0 or serv_name.find('PFSTIAS') >= 0 or serv_name.find('POSAS') >= 0 or serv_name.find('PSHDDAS') >= 0 or serv_name.find('RBVSAS') >= 0 or serv_name.find('SingleAS') >= 0:
                  print "-------------------------- 512"
                  print "SERVER: "+server
                  heap_val = 512
                  max_heap = [['maximumHeapSize',heap_val]]
                  jid = AdminConfig.list('JavaVirtualMachine',server)
		  print "old -> MAX-HEAP: "+AdminConfig.showAttribute(jid,'maximumHeapSize')
		  AdminConfig.modify(jid,max_heap)
		  print "new -> MAX-HEAP: "+AdminConfig.showAttribute(jid,'maximumHeapSize')
               # set MaxHeap = 1024 for requested servers
               if serv_name.find('MailXMLAS') >= 0 or serv_name.find('eDocAS') >= 0:
                  print "-------------------------- 1024"
                  print "SERVER: "+server
                  heap_val = 1024
                  max_heap = [['maximumHeapSize',heap_val]]
                  jid = AdminConfig.list('JavaVirtualMachine',server)
		  print "old -> MAX-HEAP: "+AdminConfig.showAttribute(jid,'maximumHeapSize')
		  AdminConfig.modify(jid,max_heap)
		  print "new -> MAX-HEAP: "+AdminConfig.showAttribute(jid,'maximumHeapSize')
               # set MaxHeap = 768 for requested servers
               if serv_name.find('AdminAS') >= 0:
                  print "-------------------------- 768"
                  print "SERVER: "+server
                  heap_val = 768
                  max_heap = [['maximumHeapSize',heap_val]]
                  jid = AdminConfig.list('JavaVirtualMachine',server)
		  print "old -> MAX-HEAP: "+AdminConfig.showAttribute(jid,'maximumHeapSize')
		  AdminConfig.modify(jid,max_heap)
		  print "new -> MAX-HEAP: "+AdminConfig.showAttribute(jid,'maximumHeapSize')
               # set MaxHeap = 2048 for requested servers
               if serv_name.find('CFMXAS') >= 0:
                  print "-------------------------- 2048"
                  print "SERVER: "+server
                  heap_val = 2048
                  max_heap = [['maximumHeapSize',heap_val]]
                  jid = AdminConfig.list('JavaVirtualMachine',server)
		  print "old -> MAX-HEAP: "+AdminConfig.showAttribute(jid,'maximumHeapSize')
		  AdminConfig.modify(jid,max_heap)
		  print "new -> MAX-HEAP: "+AdminConfig.showAttribute(jid,'maximumHeapSize')
               # set MaxHeap = 1536 for requested servers
               if serv_name.find('CFMX1AS') >= 0 or serv_name.find('CFMX2AS') >= 0:
                  print "-------------------------- 1280"
                  print "SERVER: "+server
                  heap_val = 1280
                  max_heap = [['maximumHeapSize',heap_val]]
                  jid = AdminConfig.list('JavaVirtualMachine',server)
		  print "old -> MAX-HEAP: "+AdminConfig.showAttribute(jid,'maximumHeapSize')
		  AdminConfig.modify(jid,max_heap)
		  print "new -> MAX-HEAP: "+AdminConfig.showAttribute(jid,'maximumHeapSize')
