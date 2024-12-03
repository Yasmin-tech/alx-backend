// Connect node to redis client

import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// get and set values

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
  client.GET(schoolName, (_err, reply) => {
    console.log(reply);
  });
};

async function main() {
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
}

client.on('connect', async () => {
    await main();
});
