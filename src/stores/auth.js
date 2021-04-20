import { writable } from 'svelte/store';
import { v4 as uuid4 } from 'uuid';

import { post } from '../api';

const authScopes = Object.freeze([
  'write_products',
  'read_products',
  'read_discounts',
  'read_price_rules',
  'write_price_rules',
  'write_discounts',
  'read_script_tags',
  'write_script_tags',
]);

export const authToken = writable(localStorage.getItem('jwtToken'));

export const initiateAuth = async () => {
  const urlParams = new URLSearchParams(window.location.search);
  const url = encodeURIComponent(`${window.location.origin}/oauth/redirect`);

  let oauthUrl = `https://${urlParams.get('shop')}/admin/oauth/authorize?`;
  oauthUrl += `client_id=${process.env.SHOPIFY_API_KEY}&`;
  oauthUrl += `redirect_uri=${url}&`;
  oauthUrl += `scope=${authScopes.join(',')}&`;
  oauthUrl += `state=${uuid4()}`;

  window.location.href = oauthUrl;
};

export const finishAuth = async () => {
  const urlParams = new URLSearchParams(window.location.search);

  const res = await post('/get_access_token', {
    code: urlParams.get('code'),
    shop: urlParams.get('shop'),
  });

  authToken.set(res.access_token);

  return await post('/shops', {
    access_token: res.access_token,
    shop: urlParams.get('shop'),
  });
};

authToken.subscribe(token => {
  if (token && token !== '') {
    localStorage.setItem('jwtToken', token);
  }
});
