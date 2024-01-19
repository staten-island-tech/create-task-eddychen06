<script lang="ts">
  import user from "./assets/users.json";
  import SignUp from "./components/SignUp.svelte";
  import LogIn from "./components/LogIn.svelte";
  import Button from "$lib/components/ui/button/button.svelte";
  import * as Table from "$lib/components/ui/table";
  import * as Tabs from "$lib/components/ui/tabs";
  import * as Dialog from "$lib/components/ui/dialog";
  import { Input } from "$lib/components/ui/input";
  import { Label } from "$lib/components/ui/label";
  import { update, state } from "./store";


  let apiKey = "YSX6UP5EWPIW6I14"
  let symbol: String
  let stockData = []
  let isStockData = false

  function handleLogOut() {
    update((state) => {
      state.loggedIn = false;
      state.user = []
      return state;
    });
  }


async function getStockData() {
  const response = await fetch(`https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${symbol}&apikey=${apiKey}`);
  let data = await response.json();
  return stockData.push(data["Global Quote"])
}

function test() {
  console.log(stockData)
}

</script>

<main class="h-screen w-screen flex items-center justify-center">
  

  {#if $state.loggedIn === true}
  <div class="w-6/12">
    <div class="flex justify-between mb-4 items-center">
      <h2 class="scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0"> Welcome {$state.user[0].username}! </h2>
      <Button on:click={handleLogOut}>Log Out</Button>
    </div>

    <Tabs.Root value="portfolio">
      <div class="flex justify-between">
      <Tabs.List>
        <Tabs.Trigger value="portfolio">Portfolio</Tabs.Trigger>
        <Tabs.Trigger value="transactions">Transaction History</Tabs.Trigger>
      </Tabs.List>
      <Dialog.Root>
        <Dialog.Trigger>Trade</Dialog.Trigger>
        <Dialog.Content class="sm:max-w-[425px]">
          <Dialog.Header>
            <Dialog.Title>Trade</Dialog.Title>
          </Dialog.Header>
          <div>
            <div class="flex gap-x-2">
              <Input id="symbol" bind:value={symbol} placeholder="Enter Symbol" class="outline-none"/>
              <Button on:click={getStockData}>Search</Button>
            </div>
            {#if stockData.length > 0}
              <div>it works</div>
            {/if}
          </div>
          {#if stockData}
          <Dialog.Footer>
            <Button on:click={test}>Submit Trade</Button>
          </Dialog.Footer>
          {/if}
        </Dialog.Content>
      </Dialog.Root>
    </div>
      <Tabs.Content value="portfolio">
        <Table.Root>
          <Table.Caption>A list of your portfolio.</Table.Caption>
          <Table.Header>
            <Table.Row>
              <Table.Head class="w-[100px]">Symbol</Table.Head>
              <Table.Head>Name</Table.Head>
              <Table.Head>Shares</Table.Head>
              <Table.Head>Price</Table.Head>
              <Table.Head class="text-right">Total</Table.Head>
            </Table.Row>
          </Table.Header>
          <Table.Body>
            <Table.Row>
              <Table.Cell class="font-medium">NFLX</Table.Cell>
              <Table.Cell>Netflix Inc.</Table.Cell>
              <Table.Cell>1</Table.Cell>
              <Table.Cell>$260.79</Table.Cell>
              <Table.Cell class="text-right">$260.79</Table.Cell>
            </Table.Row>
          </Table.Body>
        </Table.Root>
      </Tabs.Content>
      <Tabs.Content value="transactions">
        <Table.Root>
          <Table.Caption>A list of your recent transactions.</Table.Caption>
          <Table.Header>
            <Table.Row>
              <Table.Head class="w-[100px]">Symbol</Table.Head>
              <Table.Head>Name</Table.Head>
              <Table.Head>Shares</Table.Head>
              <Table.Head>Price</Table.Head>
              <Table.Head class="text-right">Total</Table.Head>
            </Table.Row>
          </Table.Header>
          <Table.Body>
            <Table.Row>
              <Table.Cell class="font-medium">INV001</Table.Cell>
              <Table.Cell>Paid</Table.Cell>
              <Table.Cell>Credit Card</Table.Cell>
              <Table.Cell class="text-right">$250.00</Table.Cell>
            </Table.Row>
          </Table.Body>
        </Table.Root>
      </Tabs.Content>
    </Tabs.Root>


    

    

  </div>
  {:else}
  {#if $state.logInForm === true}
  <LogIn />
  {:else} 
  <SignUp />
  {/if}
  {/if}
</main>

<style>
</style>
