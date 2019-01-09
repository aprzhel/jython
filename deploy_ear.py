##########
## FUNC ##
##########

## Save
def save():
   print " - Saving"
   AdminConfig.save()
   print "   Done\n"
   return 0

## Save & Sync
def ss():
   print " - Saving"
   AdminConfig.save()
   print " - Synchronizing"
   for node in AdminConfig.list('Node').strip().split(lineSeparator):
      node_name = AdminConfig.showAttribute(node, 'name')
      if node_name.find('Manager') <= 0:
         print "   node: "+node_name
         node_id = AdminControl.completeObjectName('type=NodeSync,node='+node_name+',*')
         if node_id != "":
            AdminControl.invoke(node_id, 'sync')
   print "   Done\n"
   return 0


##########
## INIT ##
##########

import ConfigParser
import sys

## Get config file location
config_file = sys.argv[0]

## Import Agent Enablement Tool Configuration
parser = ConfigParser.ConfigParser()
parser.read(config_file)

## read config
app_name = parser.get('app', 'name')
#app_edition = parser.get('app', 'edition')
app_src = parser.get('app', 'source')
dest_cluster_pattern = parser.get('dest', 'cluster_pattern')


##########
## MAIN ##
##########

print " "
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
print " - Removing existing app " + app_name
try:
   for app_nm in AdminApp.list().split():
      if app_nm == app_name:
         AdminApp.uninstall(app_nm)
   print "   Done\n"
except Exception, erm:
   print "\nError: Failed to uninstall existing app.\n---\n" + str(erm) + "\n---\n"
   sys.exit(1)

## install app
print " - Installing app " + app_name
try:
   AdminApp.install(app_src, '[-MapWebModToVH [[.* .* default_host]]' +
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
   			' ]')
   print "   Done\n"
except Exception, edp:
   print "\nError: Failed to install.\n---\n" + str(edp) + "\n---\n"
   sys.exit(1)

## create lists of web modules and other modules
try:
   web_mods = ''
   other_mods = ''
   for mdl in AdminApp.listModules(app_name).split():
      mdl_name = ''
      mdl_uri = ''
      for mdl_prop in AdminApp.view(mdl, ['-MapModulesToServers']).split('\n'):
         if mdl_prop.find('Module:') >= 0:
            mdl_name = mdl_prop.replace('Module:', '').strip()
         if mdl_prop.find('URI:') >= 0:
            mdl_uri = mdl_prop.replace('URI:', '').strip()
      if mdl_uri.find('web.xml') >=0:
         web_mods = web_mods + ';' + str(mdl_name) + '&' + str(mdl_uri)
      else:
         other_mods = other_mods + ';' + str(mdl_name) + '&' + str(mdl_uri)
except Exception, elm:
   print "\nError: Failed to create list of modules for app " + app_name + ".\n---\n" + str(elm) + "\n---\n"
   sys.exit(1)

## map all web modules to servers (web+cluster)
print " - Mapping web modules to servers"
try:
   for web_mod in list(filter(None,web_mods.strip()[1:].split(';'))):
      web_mod_name = web_mod.split('&')[0]
      web_mod_uri = web_mod.split('&')[1]
      AdminApp.edit(app_name, '[ -MapModulesToServers [[ ' + 
				web_mod_name + ' ' + 
				web_mod_uri + ' ' + 
				tgt_cluster + '+' + tgt_web + ' ]]]' ) 
   print "   Done\n"
except Exception, emw:
   print "\nError: Failed to map web modules to servers for app " + app_name + ".\n---\n" + str(emw) + "\n---\n"
   sys.exit(1)

## map all other modules to servers (cluster only)
print " - Mapping other modules to servers"
try:
   for other_mod in list(filter(None,other_mods.strip()[1:].split(';'))):
      other_mod_name = other_mod.split('&')[0]
      other_mod_uri = other_mod.split('&')[1]
      AdminApp.edit(app_name, '[ -MapModulesToServers [[ ' + 
				other_mod_name + ' ' + 
				other_mod_uri + ' ' + 
				tgt_cluster + ' ]]]' ) 
   print "   Done\n"
except Exception, emo:
   print "\nError: Failed to map other modules to servers for app " + app_name + ".\n---\n" + str(emo) + "\n---\n"
   sys.exit(1)


## map web modules to VH
print " - Mapping web modules to Virtual Host"
try:
   virt_host_map = ''
   for web_mod in list(filter(None,web_mods.strip()[1:].split(';'))):
      web_mod_name = web_mod.split('&')[0].strip()
      web_mod_uri = web_mod.split('&')[1].strip()
      try:
         virt_host_map = virt_host_map + ' [' + web_mod_name + ' ' + web_mod_uri + ' ' + parser.get('vhost_map', web_mod_name).strip() + ']'
      except:
         virt_host_map = virt_host_map + ' [' + web_mod_name + ' ' + web_mod_uri + ' default_host]'
   if virt_host_map:
      AdminApp.edit(app_name, '[ -MapWebModToVH [ ' + virt_host_map + ' ]]' ) 
   print "   Done\n"
except Exception, emv:
   print "\nError: Failed to map modules to virtual host " + dest_virtual_host + ".\n---\n" + str(emv) + "\n---\n"
   sys.exit(1)

## map context root(s) for web module(s)
print " - Mapping context roots for web modules"
try:
   ctx_root_map = ''
   for web_mod in list(filter(None,web_mods.strip()[1:].split(';'))):
      web_mod_name = web_mod.split('&')[0].strip()
      web_mod_uri = web_mod.split('&')[1].strip()
      try:
         ctx_root_map = ctx_root_map + ' [' + web_mod_name + ' ' + web_mod_uri + ' ' + parser.get('context_map', web_mod_name).strip() + ']'
      except:
         print "   no context root for module " + web_mod_name + " found in config file. Will use binding from the *.ear."
   if ctx_root_map:
      AdminApp.edit(app_name, '[ -CtxRootForWebMod [ ' + ctx_root_map + ']]')
   print "   Done\n"
except Exception, ect:
   print "\nError: Failed to map context root for web module " + web_mod_name + ".\n---\n" + str(ect) + "\n---\n"
   sys.exit(1)

## map roles to groups
print " - Mapping roles to groups"
try:
   group_map = ''
   try:
      cfg_group_map = list(filter(None,parser.get('role_group_map','groups').split('-brk-')))
   except:
      cfg_group_map = []
   for grp_map in cfg_group_map:
      group_map = group_map + \
         '["' + grp_map.split('^')[0].strip() + \
         '" "' + grp_map.split('^')[1].strip() + \
         '" "' + grp_map.split('^')[2].strip() + \
         '" "' + grp_map.split('^')[3].strip() + \
         '" "' + grp_map.split('^')[4].strip() + '"]'
   if group_map:
      AdminApp.edit(app_name, '[ -MapRolesToUsers [ ' + group_map + ']]')
   print "   Done\n"
except Exception, erg:
   print "\nError: Failed to map roles to groups.\n---\n" + str(erg) + "\n---\n"
   sys.exit(1)

## save/sync
ss()
