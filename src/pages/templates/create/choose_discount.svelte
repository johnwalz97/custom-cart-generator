<script>
  import { Checkbox } from 'svelte-materialify';

  import { DataTable, rows } from '../../../components/DataTable';

  import { discounts } from '../../../stores/discounts';

  let selected = [];

  const settings = {
    createButton: 'Next Step',
    searchableFields: ['title'],
    title: 'Choose Discount to Add to Cart Template',
  };
</script>

<DataTable settings={settings} data={$discounts}>
  <thead>
    <tr>
      <td>Discount Code</td>
      <td>Value</td>
      <td>Created</td>
      <td>Expires</td>
      <td class="text-center">Select</td>
    </tr>
  </thead>
  <tbody>
    {#each $rows as row}
      <tr>
        <td>{row.title}</td>
        <td>{row.title}</td>
        <td>{row.title}</td>
        <td>{row.title}</td>
        <td class="text-center">
          <Checkbox bind:group={selected} value={row.title}/>
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
