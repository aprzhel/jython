execfile('/it/mnmid/scripts/jython/common_jython.py')

def coreGroupSsl():
   cellName = printCellName()
   cgList = AdminTask.getAllCoreGroupNames()
   for cgName in cgList.split(lineSeparator):
      cgId = AdminConfig.getid('/Cell:'+cellName+'/CoreGroup:'+cgName+'/')
      AdminConfig.modify(cgId, [['channelChainName', "DCS-Secure"]])
