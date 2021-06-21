export const apiUrl = process.env.NODE_ENV === 'dev' ?
  'http://localhost:5001/dev' :
  'https://8bg2fa9sl6.execute-api.us-east-1.amazonaws.com/dev';

const urlParams = new URLSearchParams(window.location.search);
export const shop = urlParams.get('shop') || process.env.NODE_ENV === 'dev' && 'awesome-test-fake-store.myshopify.com';
