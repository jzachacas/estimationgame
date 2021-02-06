export const API_LOCATION = process.env.NODE_ENV === 'production' ? 'http://localhost/api' : 'http://localhost:8000/api';
export const WS_LOCATION = process.env.NODE_ENV === 'production' ? 'http://localhost/' : 'http://localhost:8000/';

console.info('node env');
console.info(process.env.NODE_ENV);
console.info(API_LOCATION);
