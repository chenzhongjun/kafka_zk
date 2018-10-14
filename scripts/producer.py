#! /usr/bin/env python3

from kafka import KafkaProducer

class Producer:
    def __init__(self, server_ip = "127.0.0.1", port = 9092):
        self.server_ip = server_ip
        self.port      = port
        self.topic     = None
        self.producer = KafkaProducer(bootstrap_servers = "%s:%s" %(self.server_ip, self.port))

    def genMsg(self, topic, msg):
        self.topic = topic
        self.producer.send(self.topic, bytes(str(msg), encoding = 'utf-8'))

if __name__ == "__main__":
    msgs = ["hello engineer", "this is kafka test line."]
    test = Producer("172.22.20.10")
    for msg in msgs:
        test.genMsg("test", msg)


