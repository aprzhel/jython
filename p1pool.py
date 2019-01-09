#####################################
#####################################
#Configuring the WebContainer Threadpool Using Wsadmin:-

serid = AdminConfig.getid('/Server:server1')
webid = AdminConfig.list('WebContainer',serid)
AdminConfig.modify(webid,[['tuningParams', [['invalidationTimeout', '1800'], ['maxInMemorySessionCount', '40']]]])
AdminConfig.modify(webid,[['threadPool', [['inactivityTimeout', '1800'], ['isGrowable', 'false'], ['maximumSize', '29'], ['minimumSize', '5']]]])

# Conguring WebContainer Database Session management  using wsadmin:-

serid = AdminConfig.getid('/Server:server1')
webid = AdminConfig.list('SessionManager',serid)
sessid = AdminConfig.showAttribute(webid, "sessionDatabasePersistence" )
AdminConfig.modify(webid,[['sessionPersistenceMode', 'DATABASE']])
AdminConfig.modify(sessid,[['datasourceJNDIName', 'jdbc/Sess/SESS'], ['password', 'dbpassword'], ['userId', 'dbusername'], ['db2RowSize', 'ROW_SIZE_4KB']])

#####################################
#####################################
#that will handle some, this handles things like connection pools
proc modifythreadpool {cellName nodeName serverName min max timeout} {

#--------------------------------------------------------------
# set up globals variables
#--------------------------------------------------------------

global AdminConfig
set server [$AdminConfig getid /Cell:$cellName/Node:$nodeName/Server:$serverName/]
set webContainer [$AdminConfig list WebContainer $server]
set threadPool [$AdminConfig list ThreadPool $webContainer]
set minArg[list minimumSize $min]
set maxArg[list maximumSize $max]
set timeoutArg[list inactivityTimeout $timeout]
set fullArgs[list $minArg $maxArg $timeoutArg]

$AdminConfig modify $threadPool $fullArgs
$AdminConfig save
}

#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------

if {($argc 6) } {
puts "sessiontimeout: this script requires at four three parameters: cellNode nodeName serverName min max"
puts "e.g.: sessiontimeout mycell mynode WebSphere_Portal 70 70"
} elseif {$argc == 6} {
# do some checking
set cellName [lindex $argv 0]
set nodeName [lindex $argv 1]
set serverName [lindex $argv 2]
set min [lindex $argv 3]
set max [lindex $argv 4]
set timeout [lindex $argv 5]

modifythreadpool $cellName $nodeName $serverName $min $max $timeout
}


#####################################
#####################################
#This one handles connection pools for datasources

proc createjdbcds {cellName nodeName jdbcName jdbcDSName timeout max min reap unused aged} {

#--------------------------------------------------------------
# set up globals variables
#--------------------------------------------------------------

global AdminConfig
global AdminApp

set ds [$AdminConfig getid /Cell:$cellName/Node:$nodeName/JDBCProvider:$jdbcName/DataSource:$jdbcDSName/]

#set properties the connection pool
set connectionPool [$AdminConfig list ConnectionPool $ds]

set conTimeout[list connectionTimeout $timeout]
set maxConn[list maxConnections $max]
set minConn[list minConnections $min]
set reapTime[list reapTime $reap]
set unTimeout[list unusedTimeout $unused]
set agedTimeout[list agedTimeout $aged]
set purgePolicy[list purgePolicy "FailingConnectionOnly"]

set fullArgs[list $conTimeout $maxConn $minConn $reapTime $unTimeout $agedTimeout $purgePolicy]

$AdminConfig modify $connectionPool $fullArgs
$AdminConfig save

}

#-----------------------------------------------------------------
# Main
#-----------------------------------------------------------------

if {($argc 10) } {
puts "modifydsconnectionpool: this script requires at least sie parameters: cellName nodeName jdbcName connectiontimeout maxcon mincon reaptime unusedtimeout agedtimeout"
puts "e.g.: modifydsconnectionpool mycell mynode SPSESS51JDBC SPSESS51DS 600 50 10 180 180 0"
} elseif {$argc == 10} {
# do some checking
set cellName [lindex $argv 0]
set nodeName [lindex $argv 1]
set jdbcName [lindex $argv 2]
set jdbcDSName [lindex $argv 3]
set timeout [lindex $argv 4]
set max [lindex $argv 5]
set min [lindex $argv 6]
set reap [lindex $argv 7]
set unused [lindex $argv 8]
set aged [lindex $argv 9]

createjdbcds $cellName $nodeName $jdbcName $jdbcDSName $timeout $max $min $reap $unused $aged
}
