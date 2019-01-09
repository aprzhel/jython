# load the script
def slib():
   this_file = "/export/home/wsadmin/work/aleks/jython/p1_dbPool.py"
   print "now loading "+this_file+" ..."
   execfile(this_file)
   print "execfile('"+this_file+"')"
   print "Done"
   return 0

# Save
def save():
   print "saving..."
   AdminConfig.save()
   print "done"
   return 0

# Save & Sync
def ss():
   print "saving..."
   AdminConfig.save()
   print "synchronizing..."
   for node in printNodes():
      node_name = AdminConfig.showAttribute(node, 'name')
      if node_name.find('Manager') <= 0: 
         print "NODE: "+node_name
         sync1 = AdminControl.completeObjectName('type=NodeSync,node='+node_name+',*')
         if sync1 != "":
            AdminControl.invoke(sync1, 'sync')

   print "done"
   return 0

# get cell id, just for printing reasons
def printCell():
    cell = AdminConfig.list('Cell')
    return cell

# from cell id, get cell name, again just for printing
def printCellName():
    #cell_name = AdminConfig.showAttribute(cell, 'name')
    cell_name = AdminControl.getCell()
    return cell_name

# get list of node id's
def printNodes():
    nodes = AdminConfig.list('Node')
    # format node id's for jython
    nodes1 = nodes.split(lineSeparator)
    return nodes1

# get list of datasource id's
def printDS():
    ds_ls = AdminConfig.list('DataSource')
    # format DataSource id's for jython
    ds_list = ds_ls.split(lineSeparator)
    return ds_list

# Update JDBC Pool info
def updatePool():
   ds_set1 = ('session_persistence')
   ds_set2 = ('J2EE_DS,ppone1')
   ds_set3 = ('APSAdminDS,CAPSPostalOneDB,CAPS_REPORT_DS,Data Source 1,Data Source 2,EVS_DS,EVS_DS_XA,HealthMonitorDS,MID_DS,Nonprofit_DS,OracleDataSource,PE_AUTH,PFSTIBATCHMGR_DS,PFSTI_DS,POFS_DS,PSHDD_DS,PosPostalOne,PostalOneDB,Staffing_DS,adminDS,bmidatasourcexa,caps_connection,dsmsdatasourcexa,pbvfsDS_XA,pbvfsDS_nonXA,pevs,poacsdatasourcexa,postalwizard,rbvdatasource,rbvdatasourcexa')
   ds_set4 = ('MLXMLSVC_DS,eDocFullServiceDB')
   ds_set5 = ('pofiwsDS_XA,pofiwsDS_nonXA,posaspdatasourcexa,wwsDB')
   for ds_id in printDS():
      #print "DATASOURCE_ID: "+ds_id
      ds_name = AdminConfig.showAttribute(ds_id, 'name')
      # ignode Default datasources
      if ds_name.find('Default') < 0:
         #print "DATASOURCE: "+ds_name 
         # process set1
         for ds_name1 in ds_set1.split(','):
            if ds_name.find(ds_name1) >= 0:
               print "_ UPDATING: "+ds_name+" SET1" 
               cp = AdminConfig.showAttribute(ds_id,'connectionPool')
	       AdminConfig.modify(cp,'[[connectionTimeout "200"]]')
               print "connectionTimeout="+AdminConfig.showAttribute(cp,'connectionTimeout')
	       #
	       AdminConfig.modify(cp,'[[maxConnections "500"]]')
               print "maxConnections="+AdminConfig.showAttribute(cp,'maxConnections')
	       #
	       AdminConfig.modify(cp,'[[minConnections "50"]]')
               print "minConnections="+AdminConfig.showAttribute(cp,'minConnections')
	       #
	       AdminConfig.modify(cp,'[[reapTime "250"]]')
               print "reapTime="+AdminConfig.showAttribute(cp,'reapTime')
	       #
	       AdminConfig.modify(cp,'[[unusedTimeout "300"]]')
               print "unusedTimeout="+AdminConfig.showAttribute(cp,'unusedTimeout')
	       #
	       AdminConfig.modify(cp,'[[agedTimeout "0"]]')
               print "agedTimeout="+AdminConfig.showAttribute(cp,'agedTimeout')
         # process set2
         for ds_name2 in ds_set2.split(','):
            if ds_name.find(ds_name2) >= 0:
               print "_ UPDATING: "+ds_name+" SET2"
               cp = AdminConfig.showAttribute(ds_id,'connectionPool')
               AdminConfig.modify(cp,'[[connectionTimeout "360"]]')
               print "connectionTimeout="+AdminConfig.showAttribute(cp,'connectionTimeout')
               #
               AdminConfig.modify(cp,'[[maxConnections "90"]]')
               print "maxConnections="+AdminConfig.showAttribute(cp,'maxConnections')
               #
               AdminConfig.modify(cp,'[[minConnections "0"]]')
               print "minConnections="+AdminConfig.showAttribute(cp,'minConnections')
               #
               AdminConfig.modify(cp,'[[reapTime "360"]]')
               print "reapTime="+AdminConfig.showAttribute(cp,'reapTime')
               #
               AdminConfig.modify(cp,'[[unusedTimeout "360"]]')
               print "unusedTimeout="+AdminConfig.showAttribute(cp,'unusedTimeout')
               #
               AdminConfig.modify(cp,'[[agedTimeout "0"]]')
               print "agedTimeout="+AdminConfig.showAttribute(cp,'agedTimeout')
         # process set3
         for ds_name3 in ds_set3.split(','):
            if ds_name.find(ds_name3) >= 0:
               print "_ UPDATING: "+ds_name+" SET3"
               cp = AdminConfig.showAttribute(ds_id,'connectionPool')
               AdminConfig.modify(cp,'[[connectionTimeout "180"]]')
               print "connectionTimeout="+AdminConfig.showAttribute(cp,'connectionTimeout')
               #
               AdminConfig.modify(cp,'[[maxConnections "30"]]')
               print "maxConnections="+AdminConfig.showAttribute(cp,'maxConnections')
               #
               AdminConfig.modify(cp,'[[minConnections "0"]]')
               print "minConnections="+AdminConfig.showAttribute(cp,'minConnections')
               #
               AdminConfig.modify(cp,'[[reapTime "180"]]')
               print "reapTime="+AdminConfig.showAttribute(cp,'reapTime')
               #
               AdminConfig.modify(cp,'[[unusedTimeout "180"]]')
               print "unusedTimeout="+AdminConfig.showAttribute(cp,'unusedTimeout')
               #
               AdminConfig.modify(cp,'[[agedTimeout "0"]]')
               print "agedTimeout="+AdminConfig.showAttribute(cp,'agedTimeout')
         # process set4
         for ds_name4 in ds_set4.split(','):
            if ds_name.find(ds_name4) >= 0:
               print "_ UPDATING: "+ds_name+" SET4"
               cp = AdminConfig.showAttribute(ds_id,'connectionPool')
               AdminConfig.modify(cp,'[[connectionTimeout "180"]]')
               print "connectionTimeout="+AdminConfig.showAttribute(cp,'connectionTimeout')
               #
               AdminConfig.modify(cp,'[[maxConnections "30"]]')
               print "maxConnections="+AdminConfig.showAttribute(cp,'maxConnections')
               #
               AdminConfig.modify(cp,'[[minConnections "0"]]')
               print "minConnections="+AdminConfig.showAttribute(cp,'minConnections')
               #
               AdminConfig.modify(cp,'[[reapTime "180"]]')
               print "reapTime="+AdminConfig.showAttribute(cp,'reapTime')
               #
               AdminConfig.modify(cp,'[[unusedTimeout "1800"]]')
               print "unusedTimeout="+AdminConfig.showAttribute(cp,'unusedTimeout')
               #
               AdminConfig.modify(cp,'[[agedTimeout "1200"]]')
               print "agedTimeout="+AdminConfig.showAttribute(cp,'agedTimeout')
         # process set5
         for ds_name5 in ds_set5.split(','):
            if ds_name.find(ds_name5) >= 0:
               print "_ UPDATING: "+ds_name+" SET5"
               cp = AdminConfig.showAttribute(ds_id,'connectionPool')
               AdminConfig.modify(cp,'[[connectionTimeout "180"]]')
               print "connectionTimeout="+AdminConfig.showAttribute(cp,'connectionTimeout')
               #
               AdminConfig.modify(cp,'[[maxConnections "30"]]')
               print "maxConnections="+AdminConfig.showAttribute(cp,'maxConnections')
               #
               AdminConfig.modify(cp,'[[minConnections "0"]]')
               print "minConnections="+AdminConfig.showAttribute(cp,'minConnections')
               #
               AdminConfig.modify(cp,'[[reapTime "180"]]')
               print "reapTime="+AdminConfig.showAttribute(cp,'reapTime')
               #
               AdminConfig.modify(cp,'[[unusedTimeout "180"]]')
               print "unusedTimeout="+AdminConfig.showAttribute(cp,'unusedTimeout')
               #
               AdminConfig.modify(cp,'[[agedTimeout "0"]]')
               print "agedTimeout="+AdminConfig.showAttribute(cp,'agedTimeout')
