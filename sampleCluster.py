##########
# INIT
##########

import sys


##########
#  FUNC  #
##########

## Save
def save():
   print "saving..."
   AdminConfig.save()
   print "done"
   return 0

## Save & Sync
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

## get cell id, just for printing reasons
def printCell():
   cell = AdminConfig.list('Cell')
   return cell

## from cell id, get cell name, again just for printing
def printCellName():
   cell_name = AdminConfig.showAttribute(cell, 'name')
   return cell_name

## get list of node id's
def printNodes():
   nodes = AdminConfig.list('Node')
   # format node id's for jython
   nodes1 = nodes.split(lineSeparator)
   return nodes1

## create cluster
def createCluster(ccClusterName='c1'):
   if AdminClusterManagement.checkIfClusterExists(ccClusterName) == 'false':
      try:
         AdminTask.createCluster('[-clusterConfig [-clusterName ' + ccClusterName + ' -preferLocal true]]')
      except Exception, e_ccl:
         print "\nError: Failed to create cluster.\n---\n" + str(e_ccl) + "\n---\n"
         sys.exit(1)
      
## create first cluster member
def createFirstMember(fmClusterName,fmNodeName,fmMemberName):
   if AdminClusterManagement.checkIfClusterMemberExists(fmClusterName,fmMemberName) == 'false':
      try:
         AdminTask.createClusterMember( '[-clusterName ' + fmClusterName + 
      				     ' -memberConfig   [-memberNode ' + fmNodeName + 
                  		       	     ' -memberName ' + fmMemberName +
      				     ' -memberWeight 2'
      				     ' -genUniquePorts true'
      				     ' -replicatorEntry false]'
      				     ' -firstMember    [-templateName HCSMiddlewareTemplate'
      				     ' -nodeGroup DefaultNodeGroup'
      				     ' -coreGroup DefaultCoreGroup'
      				     ' -resourcesScope cluster]]')
      except Exception, e_cfm:
         print "\nError: Failed to create cluster member.\n---\n" + str(e_cfm) + "\n---\n"
         sys.exit(1)
      
## create first cluster member
def createOtherMember(omClusterName,omNodeName,omMemberName):
   if AdminClusterManagement.checkIfClusterMemberExists(omClusterName,omMemberName) == 'false':
      try:
         AdminTask.createClusterMember( '[-clusterName ' + omClusterName + 
      				     ' -memberConfig   [-memberNode ' + omNodeName + 
                  		       	     ' -memberName ' + omMemberName +
      				     ' -memberWeight 2'
      				     ' -genUniquePorts true'
      				     ' -replicatorEntry false]]')
      except Exception, e_com:
         print "\nError: Failed to create cluster member.\n---\n" + str(e_com) + "\n---\n"
         sys.exit(1)

## create cluster members
def createMembers(cmClusterName='c1'):
   cmFirstNode = 0
   for cmNode in printNodes():
      cmNodeName = AdminConfig.showAttribute(cmNode, 'name')
      #print "      NODE: " + cmNodeName
      if (cmNodeName.find('Manager') < 0) and (cmNodeName.find('web') < 0):
         if cmFirstNode == 0:
            createFirstMember(cmClusterName,cmNodeName,cmClusterName + '-' + cmNodeName[-6:])
            cmFirstNode = 1
         else:
            createOtherMember(cmClusterName,cmNodeName,cmClusterName + '-' + cmNodeName[-6:])

## find name of web module
def webModName(mnPath):
   try:
      mnName = ''
      for mod_info in AdminApp.taskInfo(mnPath,'MapWebModToVH').split('\n'):
         if mod_info.find('Web module:') >= 0:
            mnName = mod_info.split(':')[1].lstrip().rstrip()
   except Exception, e_wmn:
      print "\nError: Failed to find the name of web module.\n---\n" + str(e_wmn) + "\n---\n"
      sys.exit(1)
   
   if mnName == '':
      print "\nError: unable to determine web module name for file " + mnPath + "! Unable to continue.\n"
      sys.exit(1)
   
   return mnName
   
## find URI of web module
def webModUri(muPath):
   try:
      muUri = ''
      for mod_info in AdminApp.taskInfo(muPath,'MapWebModToVH').split('\n'):
         if mod_info.find('URI:') >= 0:
            muUri = mod_info.split(':')[1].lstrip().rstrip()
   except Exception, e_wmu:
      print "\nError: Failed to find the URI of web module.\n---\n" + str(e_wmu) + "\n---\n"
      sys.exit(1)
   
   if muUri == '':
      print "\nError: unable to determine web module URI for file " + muPath + "! Unable to continue.\n"
      sys.exit(1)
   
   return muUri

## map modules to virtual hosts
def mapModVh(mvModName,mvModUri,mvVirtHost):
   try:
      mvMapVh = '-MapWebModToVH [[' + '"' + mvModName + '" ' + mvModUri + ' ' + mvVirtHost + ']]'
   except Exception, e_mvh:
      print "\nError: Failed to map to virtual host.\n---\n" + str(e_mvh) + "\n---\n"
      sys.exit(1)

   return mvMapVh

## install app
def installApp(iaFilePath='/it/mnmid/mnmidroot/tmp_volatile/aleks/share/apps/hello-world.war',iaAppName='hello_world',iaContextRoot='/hell',iaClusterName='c1',iaVirtHost='default_host'):
   if iaAppName in AdminApp.list():
      print "*** Found existing application " + iaAppName + ". Will not override. ***"
   else:
      print "Installing app " + iaAppName
      iaWebModName = webModName(iaFilePath)
      iaWebModUri = webModUri(iaFilePath)
      iaMapModToVh = mapModVh(iaWebModName,iaWebModUri,iaVirtHost)
      try:
         AdminApp.install(iaFilePath, '[' +
                        ' -nopreCompileJSPs' +
                        ' -distributeApp' +
                        ' -nouseMetaDataFromBinary' +
                        ' -nodeployejb' +
                        ' -appname ' + iaAppName +
                        ' -createMBeansForResources' +
                        ' -noreloadEnabled' +
                        ' -nodeployws' +
                        ' -validateinstall warn' +
                        ' -noprocessEmbeddedConfig' +
                        ' -filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755' +
                        ' -noallowDispatchRemoteInclude' +
                        ' -noallowServiceRemoteInclude' +
                        ' -asyncRequestDispatchType DISABLED' +
                        ' -nouseAutoLink' +
                        ' -noenableClientModule' +
                        ' -clientMode isolated' +
                        ' -novalidateSchema' +
                        ' -contextroot ' + iaContextRoot +
                        ' -cluster ' + iaClusterName +
                        ' ' + iaMapModToVh +
                        ' ]')
      except Exception, e_dpl:
         print "\nError: Failed to install.\n---\n" + str(e_dpl) + "\n---\n"
         sys.exit(1)


##########
#  MAIN  #
##########

## set update function list
execFunctions = ('createCluster() \
                  createMembers() \
		  installApp()')

## execute update functions
for execFunction in execFunctions.split():
   print " "
   print "  - executing: " + execFunction
   try:
      exec(execFunction)
      print "    complete successfully"
   except Exception, e_exe:
      print "\n    ERROR: faild to execute " + execFunction + "! Please review logs for more info.\n---\n" + str(e_exe) + "\n---\n"
print " "

## save & sync
ss()
