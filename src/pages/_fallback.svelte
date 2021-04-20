<script>
  import { goto } from '@roxi/routify';
  import { Button, Col, Container } from 'svelte-materialify';
</script>

<Container>
  <Col style="text-align: center">
    <img alt="404" src="/404.svg" style="width: 400px"/>
    <h4>The page you're looking for does not exist.</h4>
    <br/>
    <Button on:click={$goto('/')}>Go Home</Button>
  </Col>
</Container>
