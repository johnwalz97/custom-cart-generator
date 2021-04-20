<script>
  import { Checkbox } from 'svelte-materialify';

  import { DataTable, rows } from '../../components/DataTable';

  import { products } from '../../data';

  let images;
  let selected = [];
  let variants;

  $: {
    images = products.reduce((imgs, product) => {
      return { ...imgs, ...Object.fromEntries(product.images.map(img => [img.id, img.src])) };
    }, {});

    variants = products.reduce((list, product) => {
      const productVariants = product.variants.map(variant => (
        { ...variant, image_uri: images[variant.id] || product.image.src }
      ));
      return [...list, ...productVariants];
    }, []);
  }

  const settings = {
    title: 'Choose Products to Add to Cart Template',
    searchableFields: ['title', 'sku'],
  };
</script>

<DataTable settings={settings} data={variants}>
  <thead>
    <tr>
      <td>Variant Name</td>
      <td>SKU</td>
      <td>Quantity</td>
      <td class="text-center">Select</td>
    </tr>
  </thead>
  <tbody>
    {#each $rows as row}
      <tr>
        <td>{row.title}</td>
        <td>{row.sku}</td>
        <td>{row.inventory_quantity}</td>
        <td class="text-center">
          <Checkbox bind:group={selected} value={row.id}/>
        </td>
      </tr>
    {/each}
  </tbody>
</DataTable>

<style>
  :global(.s-checkbox) {
      display: block;
  }
</style>
