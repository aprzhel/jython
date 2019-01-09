installed_apps = AdminApp.list()
for app_name in installed_apps.split():
  print "\n--- " + app_name
  print "  default:\t" + AdminTask.listJSFImplementation(app_name)
  print "  available:\t" + AdminTask.listJSFImplementations(app_name)

## update JSF
#AdminTask.modifyJSFImplementation('hello_war-edition1.1', '[-implName MyFaces2.2]') 
