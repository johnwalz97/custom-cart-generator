import { writable, get as getValue } from 'svelte/store';

import { get, post } from '../api';
import { shop } from '../config';

export const templates = writable([]);

export const createTemplate = async newTemplate => {
  const res = await post('/templates', newTemplate);

  templates.set([...getValue(templates), newTemplate]);

  return res;
};

(async () => {
  const res = await get('/templates', { shop });
  templates.set(res);
})();
