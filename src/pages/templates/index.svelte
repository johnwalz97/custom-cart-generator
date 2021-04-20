<script>
  import { Button } from 'svelte-materialify';
  import { DataTable, rows } from '../../components/DataTable';

  import { goto } from '@roxi/routify';

  import { templates } from '../../stores/templates';

  const settings = {
    createButton: {
      title: 'Create Cart Template',
      callback: () => $goto('./choose_products'),
    },
    title: 'Templates',
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
        <td>{row.products}</td>
        <td>{row.discount}</td>
        <td class="text-center">
          <Button>Cart Link</Button>
          <Button>Mass Cart Link</Button>
        </td>
      </tr>
    {/each}
  </tbody>
</DataTable>
