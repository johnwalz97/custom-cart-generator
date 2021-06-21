<script>
  import { Button, Card, CardActions, CardTitle, Icon, List, ListItem, Menu, TextField } from 'svelte-materialify';
  import { mdiArrowLeft, mdiArrowRight, mdiChevronDown } from '@mdi/js';

  import { rows } from './data';

  export let data = [];
  export let settings = {};

  let page, startRow, endRow, rowsPerPage, tableData, textFilter, totalRows;

  page = 1;
  rowsPerPage = 15;

  $: {
    tableData = textFilter ? data.filter(row => (
      Object.entries(row).filter(item => (
        settings.searchableFields.includes(item[0])
        &&
        String(item[1]).toLowerCase().includes(textFilter.toLowerCase())
      )).length
    )) : data;

    totalRows = tableData.length;
    startRow = (page * rowsPerPage) - rowsPerPage + 1;
    endRow = (totalRows < (page * rowsPerPage)) ? totalRows : page * rowsPerPage;

    rows.set(tableData.slice((page - 1) * rowsPerPage, page * rowsPerPage));
  }

  const pageBackward = () => {
    if (page > 1) {
      page -= 1;
    }
  };
  const pageForward = () => {
    if (endRow < totalRows) {
      page += 1;
    }
  };
</script>

<div class="container">
  <Card loading={!data.length}>
    <CardTitle style="justify-content: space-between">
      {settings.title}
      <div style="width: 300px; position: relative; top: 10px">
        <TextField clearable bind:value={textFilter}>Search</TextField>
      </div>
    </CardTitle>
    <div class="wrapper">
      <table>
        <slot/>
      </table>
    </div>
    <CardActions style="justify-content: space-between">
      {#if settings.createButton}
        <Button size="small" style="margin-left: 10px" on:click={settings.createButton.callback}>
          {settings.createButton.title}
        </Button>
      {:else }
        <span></span>
      {/if}
      <footer>
        {#if totalRows > 15}
          <span class="rows-selection">
            <span class="rows-selection-label">Rows per page:</span>
            <Menu hover>
              <div slot="activator">
                <span class="rows-selection-dropdown">
                  <Button size="small">
                    {rowsPerPage}
                    <Icon path={mdiChevronDown}/>
                  </Button>
                </span>
              </div>
              <List dense>
                <ListItem on:click={() => rowsPerPage = 15}>15</ListItem>
                <ListItem on:click={() => rowsPerPage = 30}>30</ListItem>
                <ListItem on:click={() => rowsPerPage = 50}>50</ListItem>
                <ListItem on:click={() => rowsPerPage = 100}>100</ListItem>
              </List>
            </Menu>
          </span>
        {/if}
        {#if totalRows > rowsPerPage}
          <span class="rows-amount">
            {startRow}-{endRow} of {totalRows}
          </span>
          <span class="pagination">
            <span class="pagination-button" on:click={pageBackward}>
              <Icon path={mdiArrowLeft}/>
            </span>
            <span class="pagination-button" on:click={pageForward}>
              <Icon path={mdiArrowRight}/>
            </span>
          </span>
        {/if}
      </footer>
    </CardActions>
  </Card>
</div>

<style>
    .container {
        width: auto;
        padding: 25px;
    }

    .wrapper {
        margin-top: 5px;
        display: block;
        max-width: 100%;
        overflow-x: auto;
    }

    table {
        border-collapse: collapse;
        border-spacing: 0;
        width: 100%;
    }

    table :global(tr) {
        height: 30px;
    }

    table :global(td) {
        padding-left: 25px;
    }

    table :global(tr) :global(td:last-of-type) {
        padding-right: 25px;
    }

    table :global(thead) :global(td) {
        font-size: 15px;
        font-weight: bold;
    }

    table:not(.dark) :global(tbody) :global(tr:nth-child(odd)) {
        background-color: #f2f2f2;
    }

    table.dark :global(tbody) :global(tr:nth-child(odd)) {
        background-color: #2F2F2F;
    }

    table:not(.dark) :global(tbody) :global(td) {
        border: 1px solid #dee2e6;
    }

    footer {
        font-size: 12px;
        text-align: right;
        padding-top: 22px;
        padding-bottom: 22px;
        padding-right: 30px;
    }

    footer span {
        vertical-align: middle;
    }

    .rows-selection {
        padding-right: 32px;
    }

    .rows-amount {
        padding-right: 32px;
    }

    .pagination {
        padding-right: 14px;
    }

    .pagination-button {
        cursor: pointer;
    }
</style>
