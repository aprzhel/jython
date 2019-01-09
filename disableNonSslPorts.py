### This requirement is PCI Only. To be finished.

execfile('/it/mnmid/scripts/jython/common_jython.py')


def httpSsl():
   print('Hello')
   templateServerName = "templateServer"
   serverId = AdminConfig.getid("/Server:" + templateServerName + "/" )
   chainList = AdminConfig.list("Chain")
   print(chainList)
   #HttpQueueInboundDefault
   #WCInboundAdmin 
   #WCInboundAdminSecure 
   #WCInboundDefault 
   #AdminConfig.modify('(cells/eagnmnmbd09cNetwork/nodes/eagnmnmbd09c/servers/c1s1_bd09c|server.xml#Chain_1371501767826)', '[[name "HttpQueueInboundDefault"] [enable "false"]]') 
