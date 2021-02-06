export const API_LOCATION = process.env.NODE_ENV === 'production' ? 'http://localhost/api' : 'http://localhost:8000/api';

console.info("node env");
console.info(process.env.NODE_ENV);
console.info(API_LOCATION);
