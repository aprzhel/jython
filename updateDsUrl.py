###############################################
# we expect a config file as an input
# format of config file:
#
# datasource_name   datasource_url
###############################################
import sys
  
##########
# INIT
##########

if len(sys.argv) == 1:
   ds_url_file = sys.argv[0]
else:
   print "\nPlease supply fqn of config file as an argument!\n"
   sys.exit(1)

## enable common functions
execfile('/it/mnmid/scripts/jython/common_jython.py')


##########
# FUNC
##########

def updateDatasource(ud_name,ud_url):
  cell_name = AdminConfig.showAttribute(AdminConfig.list("Cell"), "name")
  ds_list = AdminConfig.list('DataSource', AdminConfig.list('Cell', AdminConfig.getid('/Cell:' + cell_name)))
  ## loop through all datasources
  for d_source in ds_list.split():
    ## find correct datasource 
    if d_source.split('(')[0] == ud_name:
      print "    --- --- ---"
      print "    DataSource: " + d_source.split('(')[0]
      props = AdminConfig.showAttribute(d_source, 'propertySet')
      proplist = AdminConfig.list('J2EEResourceProperty',props)
      ## loop through all DS properties
      for prop in proplist.splitlines():
        ## find URL and replace it
        if (AdminConfig.showAttribute(prop, 'name') == 'URL'):
          old_url= AdminConfig.showAttribute(prop, 'value')
          print '\told url: ' + old_url + '\n\tnew url: ' + ud_url
          try:
            url_attr = [['name', 'URL' ], ['value', ud_url ], ['type', 'java.land.String'], ['required','true']]
            AdminConfig.modify(prop,url_attr)
            print "\tstatus: success"
          except Exception, e_upd:
            print "    Update failed!" + "!\n*****\n" + str(e_upd) + "\n*****\n"
      print " "
 

##########
# MAIN
##########
try:
  ds_url_fh = open(ds_url_file,'r')
except:
  print "ERROR: unable to open file " + ds_url_file

ds_url_list = ds_url_fh.read()

try:
  for ds_url_line in ds_url_list.split('\n'):
    ds_name = ds_url_line.split()[0]
    ds_url = ds_url_line.split()[1]
    print "-- Now processing DataSource  " + ds_name + "\t --"
    updateDatasource(ds_name,ds_url)
except:
  print " "

ds_url_fh.close()

ss()

