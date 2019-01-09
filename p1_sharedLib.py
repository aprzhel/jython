# load the script
def slib():
   this_file = "/export/home/wsadmin/work/aleks/jython/p1_sharedLib.py"
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

# create Shared Libraries
def createSL():
   cell_id = printCell() 
   #
   print "LIB1:"
   nm = 'Coldfusion'
   ds = 'Coldfusion Libraries for Java based EARs only (DO NOT ADD TO CFUSION.EAR)'
   cp = '/postal1/ppostal1/apps/CFMX/lib/cfusion.jar;/postal1/ppostal1/apps/CFMX/lib/CfusionPostalone.jar'
   sl1 = AdminConfig.create('Library', cell_id, [['name', nm],['description',ds],['classPath',cp]])
   print AdminConfig.show(sl1)
   #
   print "LIB2:"
   nm = 'SharedSession'
   ds = 'Library for ALL EARs sharing Coldfusion Session data(MUST INCLUDE CFUSION.EAR)'
   cp = '/postal1/ppostal1/apps/CFMX/lib/SharedSession.jar'
   sl2 = AdminConfig.create('Library', cell_id, [['name', nm],['description',ds],['classPath',cp]])
   print AdminConfig.show(sl2)
   #
   print "LIB3:"
   nm = 'pja'
   ds = 'eTerks Pure Java AWT Toolkit for drawing graphics'
   cp = '/postal1/ppostal1/apps/CFMX/lib/pja.jar;/postal1/ppostal1/apps/CFMX/lib/pjatools.jar'
   sl3 = AdminConfig.create('Library', cell_id, [['name', nm],['description',ds],['classPath',cp]])
   print AdminConfig.show(sl3)
