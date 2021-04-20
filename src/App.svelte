<script>
  import { Router } from '@roxi/routify';
  import { routes } from '../.routify/routes';

  import { MaterialApp } from 'svelte-materialify';
</script>

<style global>
    @import "../assets/global.css";
</style>

<MaterialApp>
  <Router {routes}/>
</MaterialApp>
