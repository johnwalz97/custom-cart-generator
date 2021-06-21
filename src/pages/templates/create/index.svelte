<script>
  import { Button } from 'svelte-materialify';

  import { goto } from '@roxi/routify';
  import pluralize from 'pluralize';

  import { getDiscount } from '../../stores/discounts';
  import { getProduct } from '../../stores/products';
  import { templates } from '../../stores/templates';

  const settings = {
    createButton: {
      title: 'Create Cart Template',
      callback: () => $goto('./choose_products'),
    },
    searchableFields: ['name'],
    title: 'Templates',
  };

  const productNames = async templateProducts => {
    const productNames = templateProducts.map(async product => {
      const title = (await getProduct(product.id)).title;
      const name = product.quantity > 1 ? pluralize(title) : title;

      return `${product.quantity}-"${name}"`;
    });

    return (await Promise.all(productNames)).join(', ');
  };
</script>

<
