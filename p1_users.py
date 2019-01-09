# load the script
def slib():
   this_file = "/it/mnmid/tmp/x.py"
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
    cell_name = AdminConfig.showAttribute(cell, 'name')
    return cell_name

# get list of node id's
def printNodes():
    nodes = AdminConfig.list('Node')
    # format node id's for jython
    nodes1 = nodes.split(lineSeparator)
    return nodes1

############################################################
# create users
security = AdminConfig.getid('/Cell:' + cellName + '/Security:/')

#-----------------------------------------------------------
print "Creating user ADMIN_USER"
alias = ['alias', 'ppone1_ADMIN_USER']
userid = ['userId', 'ADMIN_USER']
password = ['password', '{xor}Lz4sLCg7az47Mn4qLDot']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user CAPSPCPMT"
alias = ['alias', 'ppone1_CAPSPCPMT']
userid = ['userId', 'CAPSPCPMT']
password = ['password', '{xor}Lm0ofC0ubSh8Oi5tKHw6']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user CAPS_APP"
alias = ['alias', 'ppone1_CAPS_APP']
userid = ['userId', 'CAPS_APP']
password = ['password', '{xor}Lm0ofC0ubSh8Oi5tKHw6']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user CTASAUTOP"
alias = ['alias', 'ppone1_CTASAUTOP']
userid = ['userId', 'CTASAUTOP']
password = ['password', '{xor}FSVqOTk1JgdsazR+Zj0s']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user EVS"
alias = ['alias', 'ppone1_EVS']
userid = ['userId', 'EVS']
password = ['password', '{xor}FTY+fBEsEm0nCxI5fhEP']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user MID_USER"
alias = ['alias', 'ppone1_MID_USER']
userid = ['userId', 'MID_USER']
password = ['password', '{xor}ETU0ZygvKx44aQ1rNXwS']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user MMS"
alias = ['alias', 'ppone1_MMS']
userid = ['userId', 'MMS']
password = ['password', '{xor}DydmaG5nLGk2bnw7EjcH']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user MX_DSMS_USER"
alias = ['alias', 'ppone1_MX_DSMS_USER']
userid = ['userId', 'MX_DSMS_USER']
password = ['password', '{xor}ETU+ZmcVFgpqMm9nfDcJ']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user MX_EDOC_USER"
alias = ['alias', 'ppone1_MX_EDOC_USER']
userid = ['userId', 'MX_EDOC_USER']
password = ['password', '{xor}ETU+bxkNPjlpFwd+GC4Y']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user MX_HMADMIN_USER"
alias = ['alias', 'ppone1_MX_HMADMIN_USER']
userid = ['userId', 'MX_HMADMIN_USER']
password = ['password', '{xor}JT4ubnwuPiUuKDotKyYq']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user MX_MAILXML_USER"
alias = ['alias', 'ppone1_MX_MAILXML_USER']
userid = ['userId', 'MX_MAILXML_USER']
password = ['password', '{xor}ETA1bxNsazJtLSZrN3wG']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user MX_PFSTI_USER"
alias = ['alias', 'ppone1_MX_PFSTI_USER']
userid = ['userId', 'MX_PFSTI_USER']
password = ['password', '{xor}ETU+MQkTNDtuK3wJDylt']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user MX_POACS_USER"
alias = ['alias', 'ppone1_MX_POACS_USER']
userid = ['userId', 'MX_POACS_USER']
password = ['password', '{xor}Lm0ofC0ubSh8Oi5tKHw6']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user MX_POFIWS_USER"
alias = ['alias', 'ppone1_MX_POFIWS_USER']
userid = ['userId', 'MX_POFIWS_USER']
password = ['password', '{xor}Lm0ofC0ubSh8Oi5tKHw6']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user MX_POFS_USER"
alias = ['alias', 'ppone1_MX_POFS_USER']
userid = ['userId', 'MX_POFS_USER']
password = ['password', '{xor}ETU+MT5nOmt+CAwNaRsV']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user MX_POSASP_USER"
alias = ['alias', 'ppone1_MX_POSASP_USER']
userid = ['userId', 'MX_POSASP_USER']
password = ['password', '{xor}ETU+MS18aBpubX5sOSob']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user MX_PSHDD_USER"
alias = ['alias', 'ppone1_MX_PSHDD_USER']
userid = ['userId', 'MX_PSHDD_USER']
password = ['password', '{xor}ETU+bH4pDQ0THj5sDBgp']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user NP1960"
alias = ['alias', 'ppone1_NP1960']
userid = ['userId', 'NP1960']
password = ['password', '{xor}HTAlfDl8BjU0MBULEgVt']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user PERMIT_P"
alias = ['alias', 'ppone1_PERMIT_P']
userid = ['userId', 'PERMIT_P']
password = ['password', '{xor}HiU0MG9nMxR8Zwc0JhsG']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user PE_AUTH"
alias = ['alias', 'ppone1_PE_AUTH']
userid = ['userId', 'PE_AUTH']
password = ['password', '{xor}Lm0ofC0ubSh8Oi5tKHw6']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user POSTALWIZARD_P"
alias = ['alias', 'ppone1_POSTALWIZARD_P']
userid = ['userId', 'POSTALWIZARD_P']
password = ['password', '{xor}Pj0naTMaCBtpLRB8Nw8J']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user RBVS"
alias = ['alias', 'ppone1_RBVS']
userid = ['userId', 'RBVS']
password = ['password', '{xor}KChubQkSDxw2HnwJOj0V']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user SESSION_PERSISTENCE"
alias = ['alias', 'ppone1_SESSION_PERSISTENCE']
userid = ['userId', 'SESSION_PERSISTENCE']
password = ['password', '{xor}MhMwFGcUFX4dbW0XOWob']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user SOA_USER"
alias = ['alias', 'ppone1_SOA_USER']
userid = ['userId', 'SOA_USER']
password = ['password', '{xor}Lzo6L24xOCtvMnxrJjAq']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user STAFFING"
alias = ['alias', 'ppone1_STAFFING']
userid = ['userId', 'STAFFING']
password = ['password', '{xor}ByVsaxMPEzIwJjoQfjwm']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)


print "Creating user V13P1180"
alias = ['alias', 'ppone1_V13P1180']
userid = ['userId', 'V13P1180']
password = ['password', '{xor}Pmc5ZjgyGwkQazJpFX4m']
jaasAttrs = [alias, userid, password]
AdminConfig.create('JAASAuthData', security, jaasAttrs)

ss()
