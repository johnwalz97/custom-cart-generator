import { writable, get as getValue } from 'svelte/store';

import { get, post } from '../api';

export const templates = writable([]);

export const createTemplate = async newTemplate => {
  const res = await post('/templates', newTemplate);

  templates.set([...getValue(templates), newTemplate]);

  return res;
};

(async () => {
  const res = await get('/templates', {});
  templates.set(res);
})();
