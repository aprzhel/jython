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
    cell = printCell()
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
	       #
               # update ports for each server
	       #
               if serv_name.find('AdminAS') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
		  new_http_port = '9180'
		  new_https_port = '9280'
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost -host * -port '+new_http_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" http port: "+new_http_port
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost_secure -host * -port '+new_https_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" https port: "+new_https_port
	       #
               if serv_name.find('CAPSAS') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
		  new_http_port = '9184'
		  new_https_port = '9284'
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost -host * -port '+new_http_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" http port: "+new_http_port
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost_secure -host * -port '+new_https_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" https port: "+new_https_port
	       #
               if serv_name.find('CFMX1AS') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
		  new_http_port = '9182'
		  new_https_port = '9282'
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost -host * -port '+new_http_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" http port: "+new_http_port
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost_secure -host * -port '+new_https_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" https port: "+new_https_port
	       #
               if serv_name.find('CFMX2AS') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
		  new_http_port = '9183'
		  new_https_port = '9283'
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost -host * -port '+new_http_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" http port: "+new_http_port
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost_secure -host * -port '+new_https_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" https port: "+new_https_port
	       #
               if serv_name.find('CFMXAS') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
		  new_http_port = '9181'
		  new_https_port = '9281'
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost -host * -port '+new_http_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" http port: "+new_http_port
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost_secure -host * -port '+new_https_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" https port: "+new_https_port
	       #
               if serv_name.find('MIDAS') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
		  new_http_port = '9186'
		  new_https_port = '9286'
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost -host * -port '+new_http_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" http port: "+new_http_port
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost_secure -host * -port '+new_https_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" https port: "+new_https_port
	       #
               if serv_name.find('MXMLAdmAS') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
		  new_http_port = '9187'
		  new_https_port = '9287'
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost -host * -port '+new_http_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" http port: "+new_http_port
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost_secure -host * -port '+new_https_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" https port: "+new_https_port
	       #
               if serv_name.find('MailXMLAS') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
		  new_http_port = '9188'
		  new_https_port = '9288'
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost -host * -port '+new_http_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" http port: "+new_http_port
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost_secure -host * -port '+new_https_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" https port: "+new_https_port
	       #
               if serv_name.find('PBVFSAS') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
		  new_http_port = '9189'
		  new_https_port = '9289'
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost -host * -port '+new_http_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" http port: "+new_http_port
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost_secure -host * -port '+new_https_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" https port: "+new_https_port
	       #
               if serv_name.find('PFSTIAS') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
		  new_http_port = '9190'
		  new_https_port = '9290'
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost -host * -port '+new_http_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" http port: "+new_http_port
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost_secure -host * -port '+new_https_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" https port: "+new_https_port
	       #
               if serv_name.find('POFSAS') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
		  new_http_port = '9191'
		  new_https_port = '9291'
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost -host * -port '+new_http_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" http port: "+new_http_port
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost_secure -host * -port '+new_https_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" https port: "+new_https_port
	       #
               if serv_name.find('POSASPAS') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
		  new_http_port = '9193'
		  new_https_port = '9293'
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost -host * -port '+new_http_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" http port: "+new_http_port
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost_secure -host * -port '+new_https_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" https port: "+new_https_port
	       #
               if serv_name.find('PSHDDAS') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
		  new_http_port = '9194'
		  new_https_port = '9294'
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost -host * -port '+new_http_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" http port: "+new_http_port
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost_secure -host * -port '+new_https_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" https port: "+new_https_port
	       #
               if serv_name.find('RBVSAS') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
		  new_http_port = '9195'
		  new_https_port = '9295'
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost -host * -port '+new_http_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" http port: "+new_http_port
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost_secure -host * -port '+new_https_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" https port: "+new_https_port
	       #
               if serv_name.find('SOAAS') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
		  new_http_port = '9195'
		  new_https_port = '9295'
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost -host * -port '+new_http_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" http port: "+new_http_port
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost_secure -host * -port '+new_https_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" https port: "+new_https_port
	       #
               if serv_name.find('SingleAS') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
		  new_http_port = '9196'
		  new_https_port = '9296'
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost -host * -port '+new_http_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" http port: "+new_http_port
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost_secure -host * -port '+new_https_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" https port: "+new_https_port
	       #
               if serv_name.find('eDocAS') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
		  new_http_port = '9185'
		  new_https_port = '9285'
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost -host * -port '+new_http_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" http port: "+new_http_port
  		  AdminTask.modifyServerPort(serv_name, '[-nodeName '+node_name+' -endPointName WC_defaulthost_secure -host * -port '+new_https_port+' -modifyShared true]') 
		  print "node: "+node_name+" server: "+serv_name+" https port: "+new_https_port
