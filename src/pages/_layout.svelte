<script>
  import { url } from '@roxi/routify';
  import { AppBar, Avatar, Button, Menu } from 'svelte-materialify';
</script>

<AppBar>
  <span slot='title'>1-Click</span>
  <div style='flex-grow:1'></div>
  <a class='text-decoration-none nav-link' href={$url('./templates')}>Cart Templates</a>
  <Menu closeOnClick={false} right>
    <div slot='activator'>
      <Button fab depressed>
        <Avatar size='36px' class='primary-color'>JW</Avatar>
      </Button>
    </div>
  </Menu>
</AppBar>
<slot/>

<style>
    .nav-link {
        padding-right: 10px;
    }
</style>
