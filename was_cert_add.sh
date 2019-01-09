#!/bin/ksh +x

umask 000

#CUR_DIR=${PWD}
CUR_DIR=`dirname $0`
WAS_HOME="/opt/WebSphere/AppServer7"

WORK_DIR=/home/kubx/scripts/was7.0_setup/signer_certs

cd $WORK_DIR

UNIX_ID=`whoami`

if [ $UNIX_ID = wsadmin ]
then

  function add_signer_cert
  {
    set +x
     $WAS_HOME/bin/wsadmin.sh -c "\$AdminTask addSignerCertificate  {-keyStoreName CellDefaultTrustStore -certificateAlias $1 -certificateFilePath $WORK_DIR/cert/$2 -base64Encoded true}"

    $WAS_HOME/bin/wsadmin.sh -c "\$AdminConfig save"
  }

  cd $WORK_DIR/cert
  
  ls -1 *.cer > $WORK_DIR/tmp/temp_cert_list.txt
  
  cd $WORK_DIR
  
  echo "Please verify certificate names(y or n):"
  echo
  more $WORK_DIR/tmp/temp_cert_list.txt
  echo
  echo "  ---->"
  read REPLY_VAR
  
  if [ $REPLY_VAR = y ] || [ $REPLY_VAR = Y ]
  then
    CERT_LIST=`cat $WORK_DIR/tmp/temp_cert_list.txt`
    
    for CERT_FILE in $CERT_LIST;
    do
      CERT_ALIAS=${CERT_FILE%.*}
      add_signer_cert $CERT_ALIAS $CERT_FILE
    done
  fi
else
  echo "Please sudo as wsadmin and re-run the script"
fi

cd $CUR_DIR
