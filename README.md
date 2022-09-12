## learnStackStorm
Learn StackStorm

### setup a ubuntu 20.04 ... 
* goto portal.azure.com ==> create VM ==> East US2 
  * > Network - static IP ; open port 8080, 9100, 9101, 9102 for st2web
  * > sudo apt update ; sudo apt upgrade ; sudo apt install net-tools
  * > bash <(curl -sSL https://stackstorm.com/packages/install.sh) --user=st2admin --password=ChangeMe
  * 
* install docker ub20.04 docs.docker.com
  

### pack manage
* packs/packname/config.schema.yaml ==>  what are needed to config pack before use
* configs/packname.yaml  ==> provide the value as required in config.schema.yaml
* overrides/_global.yaml ==> topdown overrides out of the gate
* overrides/packname.yaml ==>  exception to _global.yaml

### Install and remove pack on new Docker instance.
* Install and configure - [https://docs.stackstorm.com/install/index.html](https://docs.stackstorm.com/install/docker.html)
* > git clone https://github.com/stackstorm/st2-docker
* > cd st2-docker
* > docker-compose up -d
* > docker-compose exec st2actionrunner bash 
  * IMPORTANTE - (need to run as root or just copy sshkey to /root/.ssh/) *AND* from sudo -i do a local git clone to get value for "known_hosts"
  * ==>  check:  sshkey need to be owned by the user -- NOT root
  * ==> sudo -i ==>  cd /root ==> ssh-keygen (accept all) 
  * ==> copy .pub public key ==> gren to git in next step

Need to create ssh and allow st2 to sync code from github 
* https://github.com/jcn2020/learnStackStorm ==> setting ==> deployKey ==> add new ==> paste .pub from previous step.
* now ready to install 
* > docker-compose exec st2client bash
* > st2 login st2admin -p "Ch@ngeMe" 
* to get token 
* > st2 auth st2admin -p "st2admin"
* Install Pack 
  > st2 pack install git@github.com:jcn2020/learnSt2 
  > st2 pack install https://jcn2020:<PATtoken>@github.com/jcn2020/learnSt2.git
* Execute an action 
  > st2 action execute learn_stackstorm.say_hello 
* Get log file and status 
  > st2 execution list ; st2 execution get xxxxx
* Remove a pack
  > st2 pack remove learn_stackstorm
* to get token 
  > st2 auth st2admin -p "st2admin"
* > docker-compose down 

### s2ctl commands
* st2ctl {start, stop, restart, status}
  * > sudo st2ctl start
* st2ctl {restart-component}
  * component =  st2actionrunner st2api st2stream st2auth st2garbagecollector st2notifier st2rulesengine st2sensorcontainer st2chatops st2timersengine st2workflowengine st2scheduler
* st2ctl {reload, clean}
  * > sudo st2ctl reload --register-all --verbose
### Basic Stackstorm locations 
* /opt/stackstorm
  * packs: "all packs".  st2ctl will look into this first.  then search for path in pack_base_paths in /etc/st2/st2.conf
  * configs: "pack configuration"
  * st2: 
  * rbac:
  * virtualenvs:  for python as part of pip -r requirements.txt
  * overrides: override resource. eg: sensor: { defaults: {enabled: false} }, actions: { defaults: {enabled: false}}, 
    * /_global.yaml: default state of a particular resource type: sensors, actions, aliases, rules
      * { defaults: {enabled: false} }, actions: { defaults: {enabled: false}}, 
    * /<packagename>.yaml 
      * actions: { defaults: {enabled: false}} , {exceptions: myaction1: {enabled: true}} }
* /etc/st2: 
  * st2.conf: config for st2 
  * keys
  
  * sudo st2ctl reload 
### shared pack library
* https://exchange.stackstorm.org/
  * > st2 pack search core
  * > st2 pack show core
  * > st2 pack install github
  * > st2 pack install st2 pack install git@github.com/jcn2020/learnStackStorm=dev
  * > st2 pack install st2 pack install git@github.com/jcn2020/learnStackStorm=<hash>
  * > sudo st2ctl reload --register-configs


### Setup a local stackstorm instance. 
* Install and configure - https://docs.stackstorm.com/install/index.html
* Example here using docker build

* to login
  * > ssh jnguyen@>xx.xx.xx.xx
  * > st2 login st2admin <st2admin>

* to get token 
  * > st2 auth st2admin -p "st2admin"

### Locations
* container directory - /opt/stackstorm
chatops  configs  exports  packs  st2  static  virtualenvs

* logging  -- /ect/st2
htpasswd                   logging.auth.gunicorn.conf     logging.stream.conf           syslog.api.conf               syslog.sensorcontainer.conf
keys                       logging.garbagecollector.conf  logging.stream.gunicorn.conf  syslog.auth.conf              syslog.stream.conf
logging.actionrunner.conf  logging.notifier.conf          logging.timersengine.conf     syslog.garbagecollector.conf  syslog.timersengine.conf
logging.api.conf           logging.rulesengine.conf       logging.workflowengine.conf   syslog.notifier.conf          syslog.workflowengine.conf
logging.api.gunicorn.conf  logging.scheduler.conf         st2.conf                      syslog.rulesengine.conf
logging.auth.conf          logging.sensorcontainer.conf   syslog.actionrunner.conf      syslog.scheduler.conf


* 

### Reload configuration 
* st2ctl reload --register-configs
* st2ctl reload --register-all

### sample commands - 
* check for core package and run some commands 
  * > st2 pack search jenkins
  * > st2 pack install jenkins 
  * > st2 action list -p jenkins

#### run
  * > st2 run  core.local -- uname -a
  * > st2 run  core.remote hosts="local-host"  -- date -R
  * > st2 run core.http --help 

  * > st2 run --json core.http url="https://docs.stackstorm.com" method:"GET"
  
#### execution
  * > st2 execution list -n 10
  * > st2 execution get <execution_id>

#### trigger 
  * > st2 trigger list 

#### rule
  * > st2 rule list --pack=core

#### policy  <=== concurrent or retry
  * > concurrency  # max instance can run concurrently
  policy_type: action.concurrency
  parameters:
    action: delay
    threshold: 10

  policy_type: action.concurrency
  parameters:
     action: cancel
     threshold: 1
  * > concurrency.attr  # further constraint to an action attribute
 policy_type: action.concurrency.attr
 parameters:
     action: delay
     threshold: 10
     attributes:
         - hostname


#### deployment
  * > sudo  cp -r  /usr/share/doc/st2/examples   /opt/stackstorm/packs
  * > sudo  chown  -R  root:st2packs  /opt/stackstorm/packs/examples
  * > sudo  chmod  -R g+w  /opt/stackstorm/packs/example

  * > st2 run packs.setup_virtualenv   packs=examples

  * > st2ctl reload --register-all 

#### flow  - webhook trigger st2
  * > st2 auth st2admin -p "st2admin"
  * > curl -k https://localhost/api/v1/webhook/sample  \
      -d '{"name":"james", "work":"ssc"} \
      -H 'Content-Type: application/json' \
      -H 'X-Auth-Token:<token-here'>
  * > st2 execution list -n 1
  * > sudo tail /home/stanley/st2.webhoodk_sample.out
  * > st2 run core.http  method=POST  \
      body='{"name":"james"}' \
      url=https://localhost/api/v1/webhooks/sample \
      headers='x-auth-token=<putTokenHere>' \
      verify_ssl_cert=False

#### Datastore
* > st2 key list 
* > st2 key set user stanley


####  Create and install pack
* >  create a repo
* >  populate actions, rules, triggers, workflow
* >  (st2 pack remove <packName> )
* >  st2 pack install file://$CWD
* >  st2 pack install https://github.com/jcn2020/learnStackStorm.git 
* >  st2ctl reload --register-all

* >  st2 run learn_stackstorm.say_hello greetings="howdy"

