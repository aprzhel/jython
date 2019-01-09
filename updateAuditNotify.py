######################################################
# This script will update mailrelay@usps.gov to
# mailrelay.usps.gov
######################################################
## enable common functions
execfile('/it/mnmid/scripts/jython/common_jython.py')

## update mailrelay@usps.gov to mailrelay.usps.gov
def fixSMTPhost():
   notifyList = AdminTask.listAuditNotifications()
   for notify in notifyList.split(lineSeparator):
      #print "notify="+notify
      notRef = findInBracketPairs(notify,'notificationRef')
      emailList = findInBracketPairs(notify,'emailList')
      #print "notRef="+notRef+"   emailList="+emailList
      print "BEFORE - email: "+emailList
      print "..."
      if emailList.find('mailrelay@usps.gov') > 0:
         AdminTask.modifyAuditNotification('[-notificationRef '+notRef+' -sendEmail true -emailList ecsmiddleware@usps.gov(mailrelay.usps.gov) -logToSystemOut true ]') 
      else:
         print "No SMTP hosts matching mailrelay@usps.gov found."
   notifyList = AdminTask.listAuditNotifications()
   for notify in notifyList.split(lineSeparator):
      #print "notify="+notify
      notRef = findInBracketPairs(notify,'notificationRef')
      emailList = findInBracketPairs(notify,'emailList')
      #print "notRef="+notRef+"   emailList="+emailList
      print "AFTER  - email: "+emailList
 
fixSMTPhost()
ss()
