// backend calls must be prefixed with the same path as frontend calls in production
// to make nginx forwarding rules in cloudogu/CES work.
export const API_LOCATION = process.env.NODE_ENV === 'production' ? '/estimo/api' : '/api';

// Websocket location and websocket path
export const WS_LOCATION = '/';
export const WS_PATH = '/estimo/api-ws/socket.io';

console.info('config:');
console.info(process.env.NODE_ENV);
console.info(API_LOCATION);
console.info(WS_LOCATION);
