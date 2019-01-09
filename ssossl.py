execfile("/it/mnmid/scripts/jython/common_jython.py")

def ssoSsl():
   cellName = printCellName()
   print("cell: "+cellName)
   AdminTask.configureSingleSignon('-enable true -requiresSSL true -interoperable false -attributePropagation true')
