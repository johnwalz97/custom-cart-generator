<script>
  import { Icon, TextField } from 'svelte-materialify';
  import { mdiCartPlus } from '@mdi/js';

  import { DataTable, rows } from '../../../components/DataTable';

  import { products } from '../../../stores/products';

  let images;
  let selected = [];
  let variants;
  let cartQuantities = [];

  const settings = {
    title: 'Choose Products to Add to Cart Template',
    searchableFields: ['title', 'sku'],
  };
</script>

<DataTable settings={settings} data={$products}>
  <thead>
    <tr>
      <td>SKU</td>
      <td>Product Name</td>
      <td>Inventory Qty.</td>
      <td class="text-center">Add to Template</td>
    </tr>
  </thead>
  <tbody>
    {#each $rows as row, idx}
      <tr>
        <td>{row.sku}</td>
        <td>{row.title}</td>
        <td>{row.inventory_quantity}</td>
        <td class="text-center">
          <TextField style="width: 100px" type="number" bind:value={cartQuantities[idx]}>
            <div slot="append-outer">
              <Icon path={mdiCartPlus}/>
            </div>
          </TextField>
          <!--          <Checkbox bind:group={selected} value={row.id}/>-->
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
