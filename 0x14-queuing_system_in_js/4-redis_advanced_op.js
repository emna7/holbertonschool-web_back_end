import redis from 'redis'
const { promisify } = require("util");

const client = redis.createClient();
const hgetall = promisify(client.hgetall).bind(client);

async function main () {
    const values = {
        Portland: 50,
        Seattle: 80,
        'New York': '20',
        Bogota: '20',
        Cali: '40',
        Paris: '2'
    };
    for (const value in values) {
        client.hset('HolbertonSchools', value, values[value], redis.print);
    }

    const storedObject = await hgetall('HolbertonSchools');
    console.log(storedObject);
}
main();
