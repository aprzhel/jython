# load the script
def slib():
   this_file = "/export/home/wsadmin/work/aleks/jython/p1_virtualHost.py"
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

# get list of VH id's
def printVH():
    vh_ls = AdminConfig.list('VirtualHost')
    # format VH id's for jython
    vh_list = vh_ls.split(lineSeparator)
    return vh_list

# Update default VirtualHost aliases info
def updateVH():
   vh_nm = ('default_host')
   for vh_id in printVH():
      vh_name = AdminConfig.showAttribute(vh_id, 'name')
      # only work with default_host
      if vh_name.find(vh_nm) >= 0:
         print "UPDATING VH: "+vh_name 
         #AdminConfig.modify(vh_id, [['aliases', []]])  
         AdminConfig.modify(vh_id, [['aliases', [[['port',9082],['hostname','*']],[['port',9445],['hostname','*']],[['port',9083],['hostname','*']],[['port',9446],['hostname','*']],[['port',9084],['hostname','*']],[['port',9447],['hostname','*']],[['port',9085],['hostname','*']],[['port',9448],['hostname','*']],[['port',9086],['hostname','*']],[['port',9449],['hostname','*']],[['port',9087],['hostname','*']],[['port',9450],['hostname','*']],[['port',9088],['hostname','*']],[['port',9451],['hostname','*']],[['port',9089],['hostname','*']],[['port',9452],['hostname','*']],[['port',9090],['hostname','*']],[['port',9453],['hostname','*']],[['port',9091],['hostname','*']],[['port',9454],['hostname','*']],[['port',9092],['hostname','*']],[['port',9455],['hostname','*']],[['port',9093],['hostname','*']],[['port',9459],['hostname','*']]]]])  
         print "UPDATE COMPLETE"
         print "NEW ALIASES:"
         alias_list = AdminConfig.showAttribute(vh_id,'aliases')
         for ai in alias_list.split(' '):
            ai1=ai.replace('[','').replace(']','')
            print "ALIAS: "+ai1+" ATTR: "+AdminConfig.showall(ai1)
