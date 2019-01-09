########################################
# disable email notification for cert  #
# expiration monitor.                  #
#				       #	
# options:			       #
#  h   - print usage 		       #
#  l   - list current, no changes      #
#  u   - update (default)	       #
########################################

execfile('/it/mnmid/scripts/jython/common_jython.py')
import sys

##########
# FUNC
##########

def printUsage():
  print 'optional arguments:'
  print '  h - this help message'
  print '  l - list only - no changes'
  print '  u - update (default if ommited)'

def getExpMonCfg():
  emcDict = AdminTask.getWSCertExpMonitor ('[-name "Certificate Expiration Monitor"]')
  return emcDict

def parseEm(peList,peName):
  peValue = peList.split(peName)[1].split(']')[0].replace('[','')
  return peValue

def displayCfg(dcList):
  emName = parseEm(dcList,'name')
  emAutoReplace = parseEm(dcList,'autoReplace')
  emDeleteOld = parseEm(dcList,'deleteOld')
  emDays = parseEm(dcList,'daysBeforeNotification')
  emSchedule = parseEm(dcList,'wsSchedule')
  emNotify = parseEm(dcList,'wsNotification')
  emEnabled = parseEm(dcList,'isEnabled')
  print '  name:\t\t' +   emName
  print '  autoReplace:\t' +   emAutoReplace
  print '  deleteOld:\t' +   emDeleteOld
  print '  daysNotify:\t' +   emDays
  print '  wsSchedule:\t' +   emSchedule
  print '  wsNotify:\t' +   emNotify
  print '  isEnabled:\t' +   emEnabled

def updateExpMonNotify(ueCfgList,ueNotify):
  ueName = parseEm(ueCfgList,'name')
  ueAutoReplace = parseEm(ueCfgList,'autoReplace')
  ueDeleteOld = parseEm(ueCfgList,'deleteOld')
  ueDays = parseEm(ueCfgList,'daysBeforeNotification')
  ueSchedule = parseEm(ueCfgList,'wsSchedule')
  #ueNotify = parseEm(ueCfgList,'wsNotification')
  ueEnabled = parseEm(ueCfgList,'isEnabled')
  AdminTask.modifyWSCertExpMonitor ('[-name "Certificate Expiration Monitor"'
				' -autoReplace ' + ueAutoReplace + 
				' -deleteOld ' + ueDeleteOld + 
				' -daysBeforeNotification ' + ueDays + 
				' -wsNotificationName ' + ueNotify +
				' -isEnabled ' + ueEnabled + ']')


##########
# MAIN
##########

## process arguments
try:
  actionTask = sys.argv[0]
except:
  actionTask = 'u'

if actionTask == 'h':
  printUsage()
  sys.exit(0)
elif actionTask == 'l':
  emCfgList = getExpMonCfg()
  print 'List of current settings for Certificate Expiration Monitor'
  displayCfg(emCfgList)
elif actionTask == 'u':
  emCfgList = getExpMonCfg()
  print 'List of settings for Certificate Expiration Monitor -- before update --'
  displayCfg(emCfgList)
  try:
    print "\nUPDATING notification...\n"
    updateExpMonNotify(emCfgList,'MessageLog')
  except e_update:
    print "ERROR: Update Failed.\n***\n" + e_update + "\n***\n" 
  print 'List of settings for Certificate Expiration Monitor -- after update --'
  emCfgList = getExpMonCfg()
  displayCfg(emCfgList)
else:
  print "Unknown argument: " + actionTask
  printUsage()
  sys.exit(0)

ss()
