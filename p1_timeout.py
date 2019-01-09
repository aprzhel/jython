# load the script
def slib():
   this_file = "/it/mnmid/tmp/x.py"
   print "now loading "+this_file+" ..."
   execfile(this_file)
   print "execfile('"+this_file+"')"
   print "Done"
   return 0

# load common
def slibc():
   this_file = "/it/mnmid/scripts/jython/common_jython.py"
   print "now loading "+this_file+" ..."
   execfile(this_file)
   print "execfile('"+this_file+"')"
   print "Done"
   return 0

# Update ConnectTimeout & ServerIOTimeout
def connTout():
   for plugin_setting in  AdminConfig.list( 'WebserverPluginSettings' ).splitlines() :
      print '-' * 50
      print plugin_setting
      print "BEFORE - ConnectTimeout: "+AdminConfig.showAttribute(plugin_setting,'ConnectTimeout')
      ct_pair = [['ConnectTimeout',0]]
      AdminConfig.modify(plugin_setting,ct_pair)
      print "AFTER - ConnectTimeout: "+AdminConfig.showAttribute(plugin_setting,'ConnectTimeout')
      print '---'
      print "BEFORE - ServerIOTimeout: "+AdminConfig.showAttribute(plugin_setting,'ServerIOTimeout')
      ct_pair = [['ServerIOTimeout',0]]
      AdminConfig.modify(plugin_setting,ct_pair)
      print "AFTER - ServerIOTimeout: "+AdminConfig.showAttribute(plugin_setting,'ServerIOTimeout')
      print '-' * 50
      print

### load common
slibc()
