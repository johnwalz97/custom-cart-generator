import { readable, get as getValue } from 'svelte/store';

import { get } from '../api';
import { shop } from '../config';

const productCache = {};

export const products = readable({}, async set => {
  const products = await get('/products', { shop });

  set(Object.fromEntries(products.map(product => [product.id, product])));

  return () => {
  };
});

export const getVariant = variantId => {
  let variant;

  for (const product of Object.values(getValue(products))) {
    variant = product.variants.find(variant => `${variant.id}` === variantId);

    if (variant) {
      break;
    }
  }

  return variant;
};

export const getProduct = async productId => {
  if (!(productId in productCache)) {
    productCache[productId] = await get(`/products/${productId}`, { shop });
  }

  return productCache[productId];
};
