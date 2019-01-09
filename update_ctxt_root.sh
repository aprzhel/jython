#----------------------------------------
# update context root for installed app
#
# You must update variables app_name and
# app_ctxt_root below to match your needs
#----------------------------------------

##########
# FUNC
##########

## save & sync to all nodes
def ss():
   ## save
   try:
      AdminConfig.save()
      print "Changes saved to master repository."
   except Exception, e_sav:
      print "\nError: Failed to save.\n---\n" + str(e_sav) + "\n---\n"
      sys.exit(1)
   ## sync all nodes
   try:
      ss_repo = AdminControl.completeObjectName('WebSphere:type=ConfigRepository,process=dmgr,*')
      AdminControl.invoke(ss_repo, 'refreshRepositoryEpoch')
      for ss_node in AdminControl.completeObjectName('type=NodeSync,process=nodeagent,*').split():
         AdminControl.invoke(ss_node, 'sync')
      print "Changes synchronized to all nodes."
   except Exception, e_syn:
      print "\nError: Failed to synchronize.\n---\n" + str(e_syn) + "\n---\n"
      sys.exit(1)

##########
# INIT
##########

import sys

app_name = 'hello_war'
app_ctxt_root = '/show'

##########
# MAIN
##########

## update context root
try:
   AdminApp.edit(app_name, '[  -CtxRootForWebMod [[ .* .* ' + app_ctxt_root + ']]]')
except Exception, ecr:
   print "\nError: Failed to update context root for app " + app_name + ".\n---\n" + str(ecr) + "\n---\n"
   sys.exit(1)

## save & sync
ss()
