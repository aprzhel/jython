#----------------------------------------
# deploy a *.war file
# we expect a .cfg file as an argument
# assuming .war contains a single web module
# assuming there is a single target cluster
# will map web mod to all web servers
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

import ConfigParser
import sys
import os

## Get config file location
config_file = sys.argv[0]
if os.path.isfile(sys.argv[0]):
   config_file = sys.argv[0]
else:
   print "\nError: Failed to find cfg file! Unable to continue.\n"
   sys.exit(1)

## Import Agent Enablement Tool Configuration
parser = ConfigParser.ConfigParser()
parser.read(config_file)

## read config
app_name = parser.get('app', 'name')
#app_edition = parser.get('app', 'edition')
app_ctxt_root = parser.get('app', 'context_root')
app_src = parser.get('app', 'source')
dest_cluster_pattern = parser.get('dest', 'cluster_pattern')
dest_virtual_host = parser.get('dest', 'virtual_host')

##########
# MAIN
##########

## find all web servers
try:
   web_servers = []
   for svr in AdminConfig.list("Server").split():
      svr_type = AdminConfig.showAttribute(svr,'serverType')
      svr_name = AdminConfig.showAttribute(svr,'name')
      if svr_type.find('WEB_SERVER') >=0:
         svr_cell = svr[svr.find("cells/")+6:svr.find("nodes/")-1]
         svr_node = svr[svr.find("nodes/")+6:svr.find("servers/")-1]
         web_servers.append('WebSphere:cell=' + svr_cell + ',node=' + svr_node +',server=' + svr_name)
   # convert list to string joined by '+'
   tgt_web = "+".join(map(str,web_servers))
except Exception, efw:
   print "\nError: Failed to find web servers.\n---\n" + str(efw) + "\n---\n"
   sys.exit(1)

## find a cluster matching pattern
try:
   tgt_cluster = ''
   for clstr in AdminConfig.list("ServerCluster").split():
      clstr_name = AdminConfig.showAttribute(clstr,'name')
      if clstr_name.find(dest_cluster_pattern) >=0:
         clstr_cell = clstr[clstr.find("cells/")+6:clstr.find("clusters/")-1]
         tgt_cluster = 'WebSphere:cell=' + clstr_cell + ',cluster=' + clstr_name
except Exception, efc:
   print "\nError: Failed to find cluster.\n---\n" + str(efc) + "\n---\n"
   sys.exit(1)

if tgt_cluster == "":
   print "\nError: unable to find suitable cluster to deploy to! Unable to continue.\n"
   sys.exit(1)

## remove app if installed
try:
   for app_nm in AdminApp.list().split():
      if app_nm.find(app_name) >= 0:
         AdminApp.uninstall(app_nm)
except Exception, erm:
   print "\nError: Failed to uninstall existing app.\n---\n" + str(erm) + "\n---\n"
   sys.exit(1)

## find the name and URI of web module
try:
   web_mod_name = ''
   web_mod_uri = ''
   for mod_info in AdminApp.taskInfo(app_src,'MapWebModToVH').split('\n'):
      if mod_info.find('Web module:') >= 0:
         web_mod_name = mod_info.split(':')[1].lstrip().rstrip()
      if mod_info.find('URI:') >= 0:
         web_mod_uri = mod_info.split(':')[1].lstrip().rstrip()
except Exception, ewm:
   print "\nError: Failed to find the name/URI of web module.\n---\n" + str(ewm) + "\n---\n"
   sys.exit(1)

if web_mod_name == "" or web_mod_uri == "":
   print "\nError: unable to determine web module name/URI for file " + app_src + "! Unable to continue.\n"
   sys.exit(1)

## construct MapModulesToServers option
try:
   map_mod_servers = '-MapModulesToServers [[' + '"' + web_mod_name + '" ' + web_mod_uri + ' ' + tgt_cluster + '+' + tgt_web + ']]'
except Exception, ems:
   print "\nError: Failed to construct MapModulesToServers option.\n---\n" + str(ems) + "\n---\n"
   sys.exit(1)

## construct MapWebModToVH option
try:
   map_mod_vh = '-MapWebModToVH [[' + '"' + web_mod_name + '" ' + web_mod_uri + ' ' + dest_virtual_host + ']]'
except Exception, evh:
   print "\nError: Failed to construct MapWebModToVH option.\n---\n" + str(evh) + "\n---\n"
   sys.exit(1)

## install app
try:
   AdminApp.install(app_src, '[' +
   			' -nopreCompileJSPs' +
   			' -distributeApp' +
   			' -nouseMetaDataFromBinary' +
   			' -nodeployejb' +
   			' -appname ' + app_name +
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
   			' -contextroot ' + app_ctxt_root +
			' ' + map_mod_servers +
			' ' + map_mod_vh +
   			' ]')
except Exception, edp:
   print "\nError: Failed to install.\n---\n" + str(edp) + "\n---\n"
   sys.exit(1)

## save & sync
ss()
