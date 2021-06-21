import { apiUrl } from './config';

export const get = async (path, params) => {
  const paramPath = params ? `?${Object.entries(params).map(([key, value]) => `${key}=${value}`).join('&')}` : '';
  const response = await fetch(apiUrl + path + paramPath, { mode: 'cors' });

  return response.json();
};

export const post = async (path, data) => {
  const response = await fetch(apiUrl + path, {
    method: 'POST',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });

  return response.json();
};
