execfile('/it/mnmid/scripts/jython/common_jython.py')

def csiSsl():
   AdminTask.configureCSIInbound('[-messageLevelAuth Supported -supportedAuthMechList LTPA|BASICAUTH -clientCertAuth Supported -transportLayer Required -sslConfiguration -enableIdentityAssertion false -statefulSession true -enableAttributePropagation true -trustedIdentities ]') 

   AdminTask.configureCSIOutbound('[-messageLevelAuth Supported -supportedAuthMechList LTPA|BASICAUTH -clientCertAuth Never -transportLayer Required -sslConfiguration -enableIdentityAssertion false -statefulSession true -enableAttributePropagation true -trustedId -trustedTargetRealms -enableCacheLimit false]') 
