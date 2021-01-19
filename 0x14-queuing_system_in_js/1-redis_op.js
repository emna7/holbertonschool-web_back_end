import redis from 'redis';
const client = redis.createClient();
client.on('connect', function() {
    console.log('Redis client connected to the server');
});
client.on('error', function(error) {
    console.error(`Redis client not connected to the server: ${error.message}`);
});
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}
function displaySchoolValue(schoolName) {
  const Value = client.get(schoolName, redis.print);
  console.log(Value);
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

