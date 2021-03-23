<script>
  import {
    Button,
    Card,
    CardImg,
    CardImgOverlay,
    CardBody,
    Col,
    Container,
    Input,
    Modal,
    ModalBody,
    ModalFooter,
    ModalHeader,
    Row,
    Table,
  } from 'sveltestrap';
  import { discounts, products } from '../data';

  let cartUrl;
  let images = {};
  let itemCheckboxes;
  let open = false;
  let selectedDiscount;
  let step = 'choose_items';
  let variants = [];

  $: itemCheckboxes = products.reduce((object, product) => ({ ...object, [product.id]: false }), {});
  $: variants = products.reduce((list, product) => {
    const productVariants = product.variants.map(variant => ({ ...variant, product_image: product.image.src }));
    return [...list, ...productVariants];
  }, []);
  $: products.forEach(product => product.images.forEach(img => images[img.id] = img.src));

  const discountVal = discount => {
    if (discount.value_type === 'percentage') {
      return (discount.value * -1) + '%';
    } else if (discount.value_type === 'fixed_amount') {
      return '$' + (discount.value * -1);
    }
  };

  const generateCart = () => {
    'https://www.freeiconspng.com/uploads/no-image-icon-15.png';
    const variantIds = Object.fromEntries(Object.entries(itemCheckboxes).filter(([_, value]) => !!value));

    cartUrl = 'https://awesome-test-fake-store.myshopify.com/cart/';
    cartUrl += Object.keys(variantIds).join(':1,') + ':1';
    if (selectedDiscount) {
      cartUrl += `?discount=${selectedDiscount}`;
    }

    open = true;
  };

  const getItemImage = (variant) => {
    if (variant.id in images) {
      return images[variant.id];
    } else if (variant.product_image) {
      return variant.product_image;
    }
    return 'https://www.freeiconspng.com/uploads/no-image-icon-15.png';
  };

  const reset = () => {
    open = false;
    cartUrl = '';
    selectedDiscount = false;
    Object.keys(itemCheckboxes).forEach(itemId => itemCheckboxes[itemId] = false);
    step = 'choose_items';
  };
  const toggle = () => open = !open;
</script>

<Row style="margin-bottom: 25px">
  <Col lg={{ offset: 4 }}>
    {#if step === 'choose_items'}
      <h3>Choose Products for Cart</h3>
    {:else}
      <h3>Choose Discount for Cart</h3>
    {/if}
  </Col>
  <Col lg={{ offset: 2 }}>
    {#if step === 'choose_items'}
      <a href="#" on:click={() => step = 'choose_discount'}>Next</a>
    {:else}
      <a href="#" on:click={() => step = 'choose_items'}>Back</a>
      &nbsp;
      &nbsp;
      <a href="#" on:click={generateCart}>Generate Cart</a>
    {/if}
  </Col>
</Row>


{#if (step === 'choose_items')}
  <div class="items">
    {#each variants as variant}
      <Card on:click={() => itemCheckboxes[variant.id] = !itemCheckboxes[variant.id]}>
        <CardImgOverlay>
          <Input checked={itemCheckboxes[variant.id]} type="checkbox" style="margin-left: -5px"/>
        </CardImgOverlay>
        <CardImg src={getItemImage(variant)}/>
        <CardBody>
          <h5>{variant.title}</h5>
          <p>Qty. {variant.inventory_quantity}</p>
        </CardBody>
      </Card>
    {/each}
  </div>

{:else}

  <Container fluid>
    <Table bordered hover striped>
      <thead>
        <tr>
          <th>ID</th>
          <th>Code</th>
          <th>Discount</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        {#each discounts as discount}
          <tr>
            <th>{discount.id}</th>
            <th>{discount.title}</th>
            <td>{discountVal(discount)}</td>
            <td
              style="text-align: center; cursor: pointer"
              on:click={() => selectedDiscount = discount.title}
            >
              <Input checked={selectedDiscount === discount.title} style="margin: 0" type="checkbox"/>
            </td>
          </tr>
        {/each}
      </tbody>
    </Table>
  </Container>

{/if}

<Modal isOpen={open} {toggle}>
  <ModalHeader {toggle}>Custom Cart Link</ModalHeader>
  <ModalBody>
    <a href={cartUrl} target="_blank">Generated Cart (Click to test)</a>
    <br/>
    <pre>
      {cartUrl}
    </pre>
  </ModalBody>
  <ModalFooter>
    <Button color="secondary" on:click={reset}>Close and Reset</Button>
  </ModalFooter>
</Modal>

<style>
    .items {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        grid-gap: 10px;
    }

    .items > :global(.card) {
        cursor: pointer;
    }

    .items > :global(.card) :global(img) {
        height: 160px;
        width: auto;
    }
</style>
