import redis from 'redis';
const client = redis.createClient();
client.on('connect', function() {
    console.log('Redis client connected to the server');
});
client.on('error', function(error) {
    console.error(`Redis client not connected to the server: ${error.message}`);
});
