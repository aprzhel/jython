#!/usr/bin/ksh

while read NM PW;do
   echo "print \"Creating user $NM\""
   #echo "name: $NM\tpass: $PW"
   echo "alias = ['alias', 'ppone1_$NM']"
   echo "userid = ['userId', '$NM']"
   echo "password = ['password', '$PW']"
   echo "jaasAttrs = [alias, userid, password]"
   echo "AdminConfig.create('JAASAuthData', security, jaasAttrs)"
   #echo "AdminTask.modifyAuthDataEntry('[-alias ppone1_$NM -user $NM -password $PW -description ]')"
   echo "\n"
done < user.txt
