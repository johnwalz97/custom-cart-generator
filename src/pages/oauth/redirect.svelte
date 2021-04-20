<script>
  import { goto } from '@roxi/routify';
  import { finishAuth } from '../../stores/auth';

  finishAuth().then(() => $goto('/'));
</script>
