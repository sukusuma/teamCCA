from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092', request_timeout_ms=1000000, api_version_auto_timeout_ms=1000000)
filename = r"data\aminer_papers_0.txt"

with open(filename, encoding="UTF-8") as json_file:
    for line_number, line in enumerate(json_file):
        if line_number <= 100:
            print(line)
            producer.send('aminer', bytes(line,'utf-8'))
        else:
            break

#i=0
#while i <= 1000:
#    i += 1
#    producer.send('foobar',bytes("This is a very long test!",'utf-8'))