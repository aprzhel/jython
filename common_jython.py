## load the script

# define lineSeparator
import  java.lang.System  as sys
lineSeparator = sys.getProperty('line.separator')

#def slib():
   #this_file = "/it/mnmid/tmp/x.py"
   #print "now loading "+this_file+" ..."
   #execfile(this_file)
   #print "execfile('"+this_file+"')"
   #print "Done"
   #return 0
   #print "done"
   #return 0

# get cell id, just for printing reasons
def printCell():
    cell = AdminConfig.list('Cell')
    return cell

# from cell id, get cell name, again just for printing
def printCellName():
    cell = printCell()
    cell_name = AdminConfig.showAttribute(cell, 'name')
    return cell_name

# get list of node id's
def printNodes():
    nodes = AdminConfig.list('Node')
    # format node id's for jython
    nodes1 = nodes.split(lineSeparator)
    return nodes1

# get list of cluster id's
def printClusters():
    clusters = AdminConfig.list('ServerCluster')
    # format cluster id's for jython
    clusters1 = clusters.split(lineSeparator)
    return clusters1

# get list of app id's
def printApps():
    apps = AdminApp.list()
    # format app id's for jython
    apps1 = apps.split(lineSeparator)
    return apps1

# Save
def save():
   print "saving..."
   AdminConfig.save()

# Save & Sync
def ss():
   print "saving..."
   AdminConfig.save()
   repID = AdminControl.completeObjectName('WebSphere:type=ConfigRepository,process=dmgr,*')
   AdminControl.invoke(repID, "refreshRepositoryEpoch")
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

# Revert unsaved changes
def revert():
   print "rolling back..."
   AdminConfig.reset()
   print "Done."
   return 0

# Start all servers in cell
def startAll():
   for node in printNodes():
      node_name = AdminConfig.showAttribute(node, 'name')
      # don-t want Manager nodes
      if node_name.find('Manager') <= 0:
         print "---------- Starting all servers on node "+node_name
         AdminServerManagement.startAllServers(node_name)

# Stop all servers in cell
def stopAll():
   for node in printNodes():
      node_name = AdminConfig.showAttribute(node, 'name')
      # don-t want Manager nodes
      if node_name.find('Manager') <= 0:
         print "---------- Stopping all servers on node "+node_name
         AdminServerManagement.stopAllServers(node_name)

# restart all servers and node agents
def restartAllServers():
   for node in printNodes():
      nodeName = AdminConfig.showAttribute(node, 'name')
      ## exclude manager and web nodes
      if nodeName.find('Manager') < 0 and nodeName.find('-web') < 0:
         nodeId = AdminControl.queryNames('type=NodeAgent,node=' + nodeName + ',*')
         AdminControl.invoke(nodeId,'restart','true true')

# restart all node agents, but not servers
def restartAllNodes():
   for node in printNodes():
      nodeName = AdminConfig.showAttribute(node, 'name')
      ## exclude manager and web nodes
      if nodeName.find('Manager') < 0 and nodeName.find('-web') < 0:
         nodeId = AdminControl.queryNames('type=NodeAgent,node=' + nodeName + ',*')
         AdminControl.invoke(nodeId,'restart','true false')

# Generate a Heap Dump for specific server
def heapDump(serverName):
   serverJVM = AdminControl.queryNames("type=JVM,process="+serverName+",*")
   print "Dumping heap for server: "+serverJVM
   AdminControl.invoke(serverJVM,"generateHeapDump")

# Generate a Thread Dump for specific server
def threadDump(serverName):
   serverJVM = AdminControl.queryNames("type=JVM,process="+serverName+",*")
   print "Dumping threads for server: "+serverJVM
   AdminControl.invoke(serverJVM,"dumpThreads")

#
################################################################################
#
# splitProps(propString)
#
# The Jython return value of the AdminConfig.showAttribute() method for
# attributes defined as containing a variable length list of values rather than
# a single value does not return a true Jython list.  The splitProps method
# parses the return string and converts it into a list.
#
# propString    a return value of a Jython AdminConfig.showAttribute() method
#               for an attribute defined to contain a variable length list of
#               values instead of just a single value
#
################################################################################
def splitProps(propString):
    #entry("splitProps", [propString])
    propList = []
    tempProp = ''
    inQuotes = 0
    for char in propString[1:-1]:
        if char == ' ':
            if inQuotes == 0:
                propList.append(tempProp)
                tempProp = ''
            else:
                tempProp = tempProp + char
        elif char == '"':
            if inQuotes == 0:
                inQuotes = 1
            else:
                inQuotes = 0
        else:
            tempProp = tempProp + char
    if tempProp != '':
        propList.append(tempProp)
    #exit("splitProps", propList)
    return propList
## Install Ear File to a Cluster
# appName - name of the application to be installed
# earFile - ear file including pathe
# clusterName - name of the cluster to install to
def installEarCluster(appName, earFile, clusterName):
   print "installing ear "+appName+" from "+earFile+" to cluster "+clusterName
   AdminApplication.installAppWithClusterOption(appName, earFile, clusterName)

import re
###########################################
# this function will find name/value pairs
# in the square-bracket list such as:
# [[a b] [c ] [d e]]
# !> This function requires "import re" <!
###########################################
def splitBracketPairs(inString):
   # find outer parens
   outer = re.compile("\[(.+)\]")
   m = outer.search(inString)
   inner_str = m.group(1)
   
   # find inner pairs
   #innerre = re.compile("\['([^']+)', '([^']+)'\]")
   innerre = re.compile("\[([^\]]+)\]")
   
   results = innerre.findall(inner_str)
   for pair in results:
      args=pair.split()
      if len(args) == 1:
         name = args[0]
         value = args[0]
      elif len(args) == 2:
         name = args[0]
         value = args[1]
      print "pair="+pair+" name="+name+" value="+value

###########################################
# this function will return a single value 
# matching the first name in [name value]
# pair square-bracket list such as:
# [[a b] [c ] [d e]]
# !> This function requires "import re" <!
###########################################
def findInBracketPairs(inString,matchName):
   rtValue="notFound"
   # find outer parens
   outer = re.compile("\[(.+)\]")
   m = outer.search(inString)
   inner_str = m.group(1)
   
   # find inner pairs
   #innerre = re.compile("\['([^']+)', '([^']+)'\]")
   innerre = re.compile("\[([^\]]+)\]")
   
   results = innerre.findall(inner_str)
   for pair in results:
      args=pair.split()
      if len(args) == 1:
         name = args[0]
         value = args[0]
      elif len(args) == 2:
         name = args[0]
         value = args[1]
      else:
         name = args[0]
         value = args[0]
      if name == matchName:
         rtValue = value
   return rtValue

###########################################
# this function will return a single value 
# matching the first name in name=value
# pair comma-separated list such as:
# {a=[b], c=[], foo=[bar]}
# !> This function requires "import re" <!
###########################################
def findInNamValPairs(inList,searchName):
   outValue="NULL"
   groups=re.sub('[{}()<>\[\]]','',inList)
   groupList=groups.strip().split(',')
   for listPair in groupList:
      pairName=listPair.split('=')[0].strip()
      pairValue=listPair.split('=')[1].strip()
      if pairName == searchName:
         outValue=pairValue
   return outValue

## set notification e-mail to ecsmiddleware@usps.gov
def setNotification(snNotify='y'):
   if snNotify.lower().strip() == 'y':
      snSendMail = 'true'
   else:
      snSendMail = 'false'
   AdminTask.createWSNotifier('[-name MiddlewareEmail' +
                              ' -sendEmail ' + snSendMail +
                              ' -emailList ecsmiddleware@usps.gov(mailrelay.usps.gov)' +
                              ' -logToSystemOut true ]')

## set certificate expiration monitor to test every Wednesday @ 1:30 am
def setCertMonitor():
   AdminTask.modifyWSSchedule ('[-name ExpirationMonitorSchedule' +
                               ' -frequency 7' +
                               ' -dayOfWeek 3' +
                               ' -hour 1' +
                               ' -minute 30 ]')

   AdminTask.modifyWSCertExpMonitor ('[-name "Certificate Expiration Monitor"' +
                                     ' -autoReplace true' +
                                     ' -deleteOld true' +
                                     ' -daysBeforeNotification 30' +
                                     ' -wsScheduleName ExpirationMonitorSchedule' +
                                     ' -wsNotificationName MessageLog' +
                                     ' -isEnabled true]')

## update all keystore passwords
def updateKeystorePass():
   AdminTask.changeMultipleKeyStorePasswords('[-keyStorePassword WebAS' +
                                             ' -newKeyStorePassword 4bidden!' +
                                             ' -newKeyStorePasswordVerify 4bidden!]')

## UninstallApp
# appName - name of the application to be uninstalled
def uninstallApp(appName):
   print "uninstalling app: "+appName
   AdminApplication.uninstallApplication(appName)

## List all modules of an app
# appName - name of the application
def printModules(appName):
   modlist = AdminApp.listModules(appName)
   # format module id's for jython
   mods = modlist.split(lineSeparator)
   return mods

## Map Roles to Users
# appName - name of the application
# user - application user
# role - LDAP role
def mapUser(appName,user,role):
   print "mapping user "+user+" for app "+appName
   mapInfo=[user,"No","No",role,""]
   mapRoles=["-MapRolesToUsers", [mapInfo]]
   AdminApp.edit(appName,mapRoles)

## Map Groups to Users
# appName - name of the application
# user - application user
# group - LDAP group
def mapGroup(appName,user,group):
   print "mapping group "+user+" for app "+appName
   mapInfo=[user,"No","No","",group]
   mapRoles=["-MapRolesToUsers", [mapInfo]]
   AdminApp.edit(appName,mapRoles)

### Map all Modules to servers
## appName - name of the application
## srv - server to map to
#def mapModServ(appName,srv):
#   print "mapping all modules of app "+appName+" to server(s)"+srv
#   for module in printModules(appName):
#      mapAttr = [[module srv]]
#      mapping = [-MapModulesToServers,mapAttr]
#      AdminApp.edit(appName,mapping) 
#
### Map  all Modules to Virtual Hosts
## appName - name of the application
## vh - virtual host to map to
#def mapModServ(appName,vh):
#   print "mapping all modules of app "+appName+" to Vhost "+vh
#   for module in printModules(appName):
#      mapAttr = [[module vh]]
#      mapping = [-MapWebModToVH,mapAttr]
#      AdminApp.edit(appName,mapping) 
#
## Map WorkManager
# appName - name of the application
# wmResName - WorkManager resource name
# wmJndiName - WorkManager JNDI name
def mapWM(appName,wmResName,wmJndiName):
   print "mapping  work manager "+wmResName+"["+wmJndiName+"] for app "+appName
   mapAttr = [[ ".*", "", ".*,WEB-INF/web.xml", wmResName, "com.ibm.websphere.asynchbeans.WorkManager", wmJndiName, "", "" ]]
   mapping = ['-MapResRefToEJB',mapAttr]
   AdminApp.edit(appName,mapping) 
#
### Map Datasource
## appName - name of the application
## dsJndiName - datasource name
#def mapDS(appName,dsJndiName):
#   print "mapping all modules of app "+appName+" to datasource "+dsJndiName
#   mapAttr = [[ ".*" "" ".*",WEB-INF/web.xml dsJndiName javax.sql.DataSource dsJndiName DefaultPrincipalMapping "" "" ]]
#   mapping = [-MapResRefToEJB,mapAttr]
#   AdminApp.edit(appName,mapping) 
#
### Map Role
#
### Class Loader Policy (ParentFirst)
## appName - name of the application
#def parentF(appName):
#   print "changing class loader policy to PARENT_FIRST"
#   AdminApplication.configureClassLoaderLoadingModeForAnApplication(appName,"PARENT_FIRST")
#
### Class Loader Policy (ParentLast)
## appName - name of the application
#def parentL(appName):
#   print "changing class loader policy to PARENT_LAST"
#   AdminApplication.configureClassLoaderLoadingModeForAnApplication(appName,"PARENT_LAST")
#
### Set StartingWeight to "1"
## appName - name of the application
#def sw1(appName):
#   print "setting starting weight to 1 for app appName"
#   AdminApplication.configureStartingWeightForAnApplication(appName,"1")
#
### Set StartingWeight to "9"
## appName - name of the application
#def sw9(appName):
#   print "setting starting weight to 9 for app appName"
#   AdminApplication.configureStartingWeightForAnApplication(appName,"9")
#
#
