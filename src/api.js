const apiUri = 'https://8bg2fa9sl6.execute-api.us-east-1.amazonaws.com';
// const apiUri = 'http://localhost:5001';

const get = async (path, parameters) => {
  const res = await fetch(apiUri + path)
  const json = await res.json();

  return json;
};
