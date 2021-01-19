import redis from 'redis';
const { promisify } = require("util");


const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('connect', function() {
    console.log('Redis client connected to the server');
});

client.on('error', function(error) {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const Value = await getAsync(schoolName);
  console.log(Value);
}

(async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}());
