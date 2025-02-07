import csv
import redis

client = redis.Redis(host = 'localhost', port=6379, decode_responses=True)
client.ping()

with open(r'C:\Users\ariji\OneDrive\Documents\Code\2025\data\Top 1000 IMDB movies (1).csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

# pipeline basically runs multiple commands in a single network request 
'''
Redis Pipelining is an optimization technique that allows clients to send multiple commands to the Redis server without waiting for the responses of each command.
This reduces the Round Trip Time (RTT), which is the time taken for a request to travel from the client to the server and back.
By batching commands, Redis can process them more efficiently, leading to faster execution and improved performance.

Reduced Latency: By sending multiple commands at once, the time spent waiting for responses is minimized.
Increased Throughput: Allows for a higher number of operations per second, making it suitable for high-performance applications.
Atomic Transactions: Ensures that all commands in the pipeline are executed in the order they were queued, maintaining data consistency.
'''
pipeline = client.pipeline()

for i, movie in enumerate(data, start=1):
    redis_key = f'movie:{i:05}'
    pipeline.json().set(redis_key, '$', movie)

pipeline.execute()


    #print(data[0])
