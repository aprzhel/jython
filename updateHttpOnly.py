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

## find WebContainer property
def getWcProp(gwpServerId,gwpPropName):
   gwpPropIdRtn = ''
   gwpWcId = AdminConfig.list('WebContainer',gwpServerId)
   for gwpPropId in AdminConfig.list('Property',gwpWcId).split(lineSeparator):
      if (gwpPropId.strip() != '') and ((AdminConfig.showAttribute(gwpPropId,'name').strip()) == gwpPropName):
         gwpPropIdRtn = gwpPropId
   return gwpPropIdRtn
   
## create new WebContainer property 
def createWcCustom(choServerId,choPropName,choPropValue):
   choWcId = AdminConfig.list('WebContainer',choServerId)
   AdminConfig.create('Property', choWcId, '[[ name ' +  choPropName + '] [value ' + choPropValue + ' ] [required "false"]]')

## update Webcontainer Custom Property
def updateWcHttpOnly():
   for node in printNodes():
      node_name = AdminConfig.showAttribute(node, 'name')
      print "      NODE: " + node_name
      servers = AdminConfig.list('Server', node)
      ## for every server get type and name
      for serverId in servers.split(lineSeparator):
         serv_name = AdminConfig.showAttribute(serverId, 'name')
         serv_type = AdminConfig.showAttribute(serverId, 'serverType')
         ## only want app servers
         if serv_type == 'APPLICATION_SERVER':
            propName = 'com.ibm.ws.webcontainer.HTTPOnlyCookies'
            propValue = 'JsessionID,EntReg,EntRegEX'
            httpPropId = getWcProp(serverId,propName)
            if httpPropId and (httpPropId.strip() != ''):
               print "        Found existing " + propName + " property " + AdminConfig.showAttribute(httpPropId,'value') + " in WebContainer on server " + AdminConfig.showAttribute(serverId,'name') + ". Will not modify."
            else:
               print "        Creating new WebContainer property " + propName + " for server " + AdminConfig.showAttribute(serverId,'name') + "."
               createWcCustom(serverId,propName,propValue)

## find JVM property
def getJvmProp(gjpServerId,gjpPropName):
   gjpPropIdRtn = ''
   gjpJvmId = AdminConfig.list('JavaVirtualMachine',gjpServerId)
   for gjpPropId in AdminConfig.list('Property',gjpJvmId).split(lineSeparator):
      if (gjpPropId.strip() != '') and ((AdminConfig.showAttribute(gjpPropId,'name').strip()) == gjpPropName):
         gjpPropIdRtn = gjpPropId
   return gjpPropIdRtn

## create new JVM Custom property 
def createJvmCustom(cjcServerId,cjcPropName,cjcPropValue):
   cgcJvmId = AdminConfig.list('JavaVirtualMachine',cjcServerId)
   AdminConfig.create('Property',cgcJvmId,'[[ name ' + cjcPropName + '] [ value ' + cjcPropValue + ' ]]','systemProperties')

## update JVM Custom Property
def updateJvmHttpOnly():
   for node in printNodes():
      node_name = AdminConfig.showAttribute(node, 'name')
      print "      NODE: " + node_name
      servers = AdminConfig.list('Server', node)
      for serverId in servers.split(lineSeparator):
         serv_name = AdminConfig.showAttribute(serverId, 'name')
         serv_type = AdminConfig.showAttribute(serverId, 'serverType')
         ## only want app servers
         if serv_type == 'APPLICATION_SERVER':
            ## set com.ibm.ws.security.addHttpOnlyAttributeToCookies  
            propName = 'com.ibm.ws.security.addHttpOnlyAttributeToCookies'
            propValue = 'true'
            propId1 = getJvmProp(serverId,propName)
            if propId1 and (propId1.strip() != ''):
               print "        Found existing " + propName + " property " + AdminConfig.showAttribute(propId1,'value') + " in JVM on server " + AdminConfig.showAttribute(serverId,'name') + ". Will not modify."
            else:
               print "        Creating new JVM property " + propName + " for server " + AdminConfig.showAttribute(serverId,'name') + "."
               createJvmCustom(serverId,propName,propValue)
            ## set com.ibm.ws.webcontainer.HTTPOnlyCookies
            propName = 'com.ibm.ws.webcontainer.HTTPOnlyCookies'
            propValue = 'JsessionID,EntReg,EntRegEX '
            propId2 = getJvmProp(serverId,propName)
            if propId2 and (propId1.strip() != ''):
               print "        Found existing " + propName + " property " + AdminConfig.showAttribute(propId1,'value') + " in JVM on server " + AdminConfig.showAttribute(serverId,'name') + ". Will not modify."
            else:
               print "        Creating new JVM property " + propName + " for server " + AdminConfig.showAttribute(serverId,'name') + "."
               createJvmCustom(serverId,propName,propValue)


##########
#  MAIN  #
##########

## set update function list
httpFunctions = ('updateWcHttpOnly() \
		  updateJvmHttpOnly()')

## execute update functions
for httpFunction in httpFunctions.split():
   print " "
   print "  - executing: " + httpFunction
   try:
      exec(httpFunction)
      print "    complete successfully"
   except Exception, eex:
      print "\n    ERROR: faild to execute " + httpFunction + "! Please review logs for more info.\n---\n" + str(eex) + "\n---\n"
print " "

## save & sync
ss()
