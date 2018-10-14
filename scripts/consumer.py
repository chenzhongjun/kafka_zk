from kafka import KafkaConsumer

class Consumer:
    def __init__(self, server_ip = "localhost", port = 2181):
        self.server_ip = server_ip
        self.port      = port
        self.consumer = KafkaConsumer(bootstrap_servers = "%s:%s" %(self.server_ip, self.port))

    def getMsg(self, topic = "test"):
        self.consumer.subscribe(topic)
        for msg in self.consumer:
            print(msg)


if __name__ == "__main__":
    test = Consumer()
    test.getMsg()
