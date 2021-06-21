import { readable } from 'svelte/store';

import { get } from '../api';
import { shop } from '../config';

const discountCache = {};

export const discounts = readable({}, async set => {
  const discounts = await get('/discounts', { shop });

  set(Object.fromEntries(discounts.map(discount => [discount.id, discount])));
});

export const getDiscount = async discountId => {
  if (!(discountId in discountCache)) {
    discountCache[discountId] = await get(`/discounts/${discountId}`, { shop });
  }

  return discountCache[discountId];
};
