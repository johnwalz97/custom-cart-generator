import App from './App.svelte';

// ShopifyApp.init({
//   apiKey: '{{ config.SHOPIFY_API_KEY }}',
//   shopOrigin: 'https://{{ shop.shop }}',
//   debug: true,
// });
// ShopifyApp.ready(function() {
//   ShopifyApp.Bar.initialize({
//     title: 'Custom Cart Generator - Select Products',
//   });
// });

export const app = new App({ target: document.body });
