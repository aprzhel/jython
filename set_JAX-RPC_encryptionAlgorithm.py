### execfile("/it/mnmid/mnmidroot/tmp_volatile/aleks/scripts/jython/set_JAX_encryption.py")
execfile("/it/mnmid/scripts/jython/common_jython.py")

def updateEncAlg(ueaObjId, ueaAlg):
   AdminConfig.modify(ueaObjId, '[[algorithm ' + ueaAlg + ']]')

wsTypes = ('com.ibm.etools.webservice.wssecurity.Consumer \
            com.ibm.etools.webservice.wssecurity.Generator')

for wsType in wsTypes.split():
   print " "
   #print "=================================="
   #print "TYPE: " + wsType
   #print "=================================="
   try:
      #print "---------- attributes ----------"
      typAttrs = AdminConfig.attributes(wsType)
      #print typAttrs
      #print "----------  objects   ----------"
      typObj = AdminConfig.list(wsType)
      #print typObj
      try:
         #print "----------  crypt ID  ----------"
         objCryptId = AdminConfig.showAttribute(typObj, 'encryptionInfo')[1:-1]
         #print objCryptId
         msgName = AdminConfig.showAttribute(objCryptId, 'name')
         print "crypt name: " + msgName
         #print "---------- crypt prop ----------"
         cryptProps = AdminConfig.show(objCryptId)
         #print cryptProps
         #print "---------- msg method ----------"
         msgAlgID = AdminConfig.showAttribute(objCryptId, 'encryptionMethod')
         #print msgAlgID
         #print "---------- method atr ----------"
         msgAlg = AdminConfig.showAttribute(msgAlgID, 'algorithm')
         print "msg algorithm before: " + msgAlg
         try:
            updateEncAlg(msgAlgID,'http://www.w3.org/2001/04/xmlenc#aes256-cbc')
            msgAlg = AdminConfig.showAttribute(msgAlgID, 'algorithm')
            print "msg algorithm after: " + msgAlg
         except:
            print "ERROR: failed to update encryption algorithm for " + msgAlgID + "!"
         #print "---------- key method ----------"
         keyAlgID = AdminConfig.showAttribute(objCryptId, 'keyEncryptionMethod')
         #print keyAlgID
         #print "---------- method atr ----------"
         keyAlg = AdminConfig.showAttribute(keyAlgID, 'algorithm')
         print "key algorithm before: " + keyAlg
         try:
            updateEncAlg(keyAlgID,'http://www.w3.org/2001/04/xmlenc#kw-aes256')
            keyAlg = AdminConfig.showAttribute(keyAlgID, 'algorithm')
            print "key algorithm after: " + keyAlg
         except:
            print "ERROR: failed to update encryption algorithm for " + keyAlgID + "!"
      except:
         print "ERROR: unable to find encryption attributes for object " + typObj + "!"
   except:
      print "ERROR: unable to find any objects of type " + wsType + "!"

print " "
