This is a zookeeper & kafka cluster docker file.
run ./start to boot up kafka, zookeeper & python3 container

$ docker exec -ti python3 bash
root@eclipse:/home/python3# ls
consumer.py  producer.py
root@eclipse:/home/python3#

run producer.py to send msg
run consumer.py to receive msgs
