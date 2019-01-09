# load the script
def slib():
   this_file = "/export/home/wsadmin/work/aleks/jython/p1_vars.py"
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

# Update WebSphere Variables
def updateVar():
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
               # update required servers
               if serv_name.find('CAPS') >= 0 or serv_name.find('CFMX') >= 0 or serv_name.find('PFSTI') >= 0 or serv_name.find('POS') >= 0 or serv_name.find('RBVS') >= 0 or serv_name.find('Single') >= 0:
                  print "--------------------------"
                  print "SERVER: "+serv_name
	   	  var_name = 'SERVER_LOG_ROOT'
                  var_value = '/postal1/ppostal1/logs/'+serv_name
                  vars = AdminConfig.list('VariableSubstitutionEntry',server).split(lineSeparator)
		  for variable in vars:
		     if AdminConfig.showAttribute(variable,'symbolicName') == var_name:
		        print "old -> LOG_ROOT: "+AdminConfig.showAttribute(variable,'value')
                  	AdminConfig.modify(variable,[['value',var_value]])
		        print "new -> LOG_ROOT: "+AdminConfig.showAttribute(variable,'value')
