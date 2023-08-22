
const request = require('supertest');
const app = require('../../src/javascript/nodejs/server.js');

describe('Test the root path', () => {
    test('It should response the GET method', async () => {
        const response = await request(app).get('/');
        expect(response.statusCode).toBe(200);
    });
});

describe('Test agent endpoint', () => {
    test('It should response the GET method and return agent', async () => {
        const response = await request(app).get('/agent');
        expect(response.statusCode).toBe(200);
        expect(response.body).toHaveProperty('agent');
    });
});
