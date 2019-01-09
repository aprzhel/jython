# load the script
def slib():
   this_file = "/export/home/wsadmin/work/aleks/jython/p1_classLoader.py"
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

# Update Class Loader
def classLoader():
    for node in printNodes():
       node_name = AdminConfig.showAttribute(node, 'name')
       print "NODE: "+node_name
       servers = AdminConfig.list('Server', node)
       server_list = servers.split(lineSeparator)
       libs = AdminConfig.list('Library')
       lib_list = libs.split(lineSeparator)
       # for every server get type and name
       for server in server_list:
          serv_name = AdminConfig.showAttribute(server, 'name')
          serv_type = AdminConfig.showAttribute(server, 'serverType')
          # don't want webservers, DM's or nodeagents
          if serv_type == 'APPLICATION_SERVER':
               # set associate 'Admin' library with requested servers
               if serv_name.find('AdminAS') >= 0 or serv_name.find('CAPSAS') >= 0:
                  print "-------------------------- Admin"
                  print "SERVER: "+AdminConfig.showAttribute(server,'name')
		  # identify the App Server
		  app_server = AdminConfig.list('ApplicationServer',server)
		  # identify SharedLibrary
                  lib_nm = 'Admin'
		  for library in lib_list:
                     if AdminConfig.showAttribute(library,'name').lower().find(lib_nm.lower()) >= 0:
                        lib_name = AdminConfig.showAttribute(library,'name') 
                  # create a classloader
		  cloader = AdminConfig.create('Classloader',app_server,[['mode','PARENT_FIRST']])
       		  # associate library with app server thropugh the classloader
                  print "old -> CLASS-LOADERS: "+AdminConfig.showAttribute(app_server,'classloaders')
		  AdminConfig.create('LibraryRef',cloader,[['libraryName',lib_name]])
                  print "new -> LIB: "+lib_name+" CLASS-LOADERS: "+AdminConfig.showAttribute(app_server,'classloaders')
               # set associate 'Coldfusion' library with requested servers
               if serv_name.find('CAPSAS') >= 0 or serv_name.find('CFMX1AS') >= 0 or serv_name.find('CFMX2AS') >= 0 or serv_name.find('PBVFSAS') >= 0:
                  print "-------------------------- Coldfusion"
                  print "SERVER: "+AdminConfig.showAttribute(server,'name')
		  # identify the App Server
		  app_server = AdminConfig.list('ApplicationServer',server)
		  # identify SharedLibrary
                  lib_nm = 'Coldfusion'
		  for library in lib_list:
                     if AdminConfig.showAttribute(library,'name').lower().find(lib_nm.lower()) >= 0:
                        lib_name = AdminConfig.showAttribute(library,'name') 
                  # create a classloader
		  cloader = AdminConfig.create('Classloader',app_server,[['mode','PARENT_FIRST']])
       		  # associate library with app server thropugh the classloader
                  print "old -> CLASS-LOADERS: "+AdminConfig.showAttribute(app_server,'classloaders')
		  AdminConfig.create('LibraryRef',cloader,[['libraryName',lib_name]])
                  print "new -> LIB: "+lib_name+" CLASS-LOADERS: "+AdminConfig.showAttribute(app_server,'classloaders')
               # set associate 'Sharedsession' library with requested servers
               if serv_name.find('CAPSAS') >= 0 or serv_name.find('CFMX1AS') >= 0 or serv_name.find('CFMX2AS') >= 0 or serv_name.find('PBVFSAS') >= 0:
                  print "-------------------------- Sharedsession"
                  print "SERVER: "+AdminConfig.showAttribute(server,'name')
		  # identify the App Server
		  app_server = AdminConfig.list('ApplicationServer',server)
		  # identify SharedLibrary
                  lib_nm = 'Sharedsession'
		  for library in lib_list:
                     if AdminConfig.showAttribute(library,'name').lower().find(lib_nm.lower()) >= 0:
                        lib_name = AdminConfig.showAttribute(library,'name') 
                  # create a classloader
		  cloader = AdminConfig.create('Classloader',app_server,[['mode','PARENT_FIRST']])
       		  # associate library with app server thropugh the classloader
                  print "old -> CLASS-LOADERS: "+AdminConfig.showAttribute(app_server,'classloaders')
		  AdminConfig.create('LibraryRef',cloader,[['libraryName',lib_name]])
                  print "new -> LIB: "+lib_name+" CLASS-LOADERS: "+AdminConfig.showAttribute(app_server,'classloaders')
               # set associate 'pja' library with requested servers
               if serv_name.find('CFMX1AS') >= 0 or serv_name.find('CFMX2AS') >= 0:
                  print "-------------------------- pja"
                  print "SERVER: "+AdminConfig.showAttribute(server,'name')
		  # identify the App Server
		  app_server = AdminConfig.list('ApplicationServer',server)
		  # identify SharedLibrary
                  lib_nm = 'pja'
		  for library in lib_list:
                     if AdminConfig.showAttribute(library,'name').lower().find(lib_nm.lower()) >= 0:
                        lib_name = AdminConfig.showAttribute(library,'name') 
                  # create a classloader
		  cloader = AdminConfig.create('Classloader',app_server,[['mode','PARENT_FIRST']])
       		  # associate library with app server thropugh the classloader
                  print "old -> CLASS-LOADERS: "+AdminConfig.showAttribute(app_server,'classloaders')
		  AdminConfig.create('LibraryRef',cloader,[['libraryName',lib_name]])
                  print "new -> LIB: "+lib_name+" CLASS-LOADERS: "+AdminConfig.showAttribute(app_server,'classloaders')
