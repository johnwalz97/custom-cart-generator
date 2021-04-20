// const apiUri = 'https://8bg2fa9sl6.execute-api.us-east-1.amazonaws.com/dev';
const apiUri = 'http://localhost:5001/dev';

export const get = async (path) => {
  const response = await fetch(apiUri + path, { mode: 'cors' });

  return response.json();
};

export const post = async (path, data) => {
  const response = await fetch(apiUri + path, {
    method: 'POST',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });

  return response.json();
};
