<script>
  import { Button } from 'svelte-materialify';
  import { DataTable, rows } from '../../components/DataTable';

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

<DataTable settings={settings} data={$templates}>
  <thead>
    <tr>
      <td>Name</td>
      <td>Products</td>
      <td>Discount</td>
      <td class="text-center">Actions</td>
    </tr>
  </thead>
  <tbody>
    {#each $rows as row}
      <tr>
        <td>{row.name}</td>
        {#await productNames(row.products) then names}
          <td>{names}</td>
        {/await}
        {#await getDiscount(row.discount) then discount}
          <td>{discount.title}</td>
        {/await}
        <td class="text-center">
          <Button>Cart Link</Button>
          <Button>Mass Cart Link</Button>
        </td>
      </tr>
    {/each}
  </tbody>
</DataTable>
