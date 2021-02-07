export const API_LOCATION = process.env.NODE_ENV === 'production' ? 'http://localhost/api' : 'http://localhost:8080/api';
export const WS_LOCATION = process.env.NODE_ENV === 'production' ? 'http://localhost/' : 'http://localhost:8080/';
export const WS_PATH = '/api-ws/socket.io';

console.info('config:');
console.info(process.env.NODE_ENV);
console.info(API_LOCATION);
console.info(WS_LOCATION);
