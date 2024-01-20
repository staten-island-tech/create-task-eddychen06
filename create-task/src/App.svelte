<script lang="ts">
  import SignUp from "./components/SignUp.svelte";
  import LogIn from "./components/LogIn.svelte";
  import Button from "$lib/components/ui/button/button.svelte";
  import * as Table from "$lib/components/ui/table";
  import * as Tabs from "$lib/components/ui/tabs";
  import * as Dialog from "$lib/components/ui/dialog";
  import { Input } from "$lib/components/ui/input";
  import { Label } from "$lib/components/ui/label";
  import * as Avatar from "$lib/components/ui/avatar";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu";
  import { update, state } from "./store";
  import { LogOut, RefreshCcw  } from "lucide-svelte";
  import { Badge } from "$lib/components/ui/badge";
  import * as Select from "$lib/components/ui/select";
  import { parse } from "svelte/compiler";

  let symbol: String;
  let stockData;
  let isStockData = false;
  let numShares = 0;
  let promise;

  function handleLogOut() {
    let userIndex = $state.users.findIndex((x) => x.id == $state.user[0].id);

    update((state) => {
      state.loggedIn = false;
      state.user = [];
      return state;
    });
  }

  async function getStockData() {
    const response = await fetch(`https://financialmodelingprep.com/api/v3/quote/${symbol}?apikey=m8Q38IpoxVAOZBP9ddg9AtNQNeVvmXeI`);
    let data = await response.json();
    return stockData = data[0]
  }

  function calculateMaxShares() {
    let cash = $state.user[0].portfolio.cash;

    return Math.floor(cash / stockData.price);
  }

  function handleBuy() {
    if (numShares > calculateMaxShares()) {
      return;
    }

    update((state) => {

      if (state.user[0].portfolio.stocks.find(stock => stock.symbol === stockData.symbol)) {
        
        state.user[0].portfolio.stocks.map(stock => {
          if (stock.symbol === stockData.symbol) {
            return { ...stock, shares: stock.shares += parseInt(numShares) };
          }
        });
      } else {
        state.user[0].portfolio.stocks.push( {
          "symbol": stockData.symbol,
          "name": stockData.name,
          "shares": parseInt(numShares),
          "price": stockData.price,
        });
      }

      state.user[0].transactions.push( {
          "symbol": stockData.symbol,
          "name": stockData.name,
          "shares": parseInt(numShares),
          "price": stockData.price,
          "total": (stockData.price * numShares).toFixed(2),
          "date": new Date().toLocaleString(),
          "order": "BUY"
        });

        state.user[0].portfolio.cash -= parseInt((stockData.price * numShares).toFixed(2))

      
      return state;
    });

   
    
  }

  function handleSell() {
    if (numShares > $state.user[0].portfolio.stocks.find(stock => stock.symbol === stockData.symbol).shares) {
      return console.log("you don't have that many shares")
    } else if (!$state.user[0].portfolio.stocks.find(stock => stock.symbol === stockData.symbol)) {
      return console.log("you don't have those stocks")
    }

    

    update((state) => {

      if (state.user[0].portfolio.stocks.find(stock => stock.symbol === stockData.symbol).shares - parseInt(numShares) === 0) {
        state.user[0].portfolio.stocks.splice(state.user[0].portfolio.stocks.findIndex(x => x.symbol === stockData.symbol), 1)
      } else {
        state.user[0].portfolio.stocks.map(stock => {
        if (stock.symbol === stockData.symbol) {
          return { ...stock, shares: stock.shares -= parseInt(numShares) };
        }
      });
      }

      state.user[0].transactions.push( {
          "symbol": stockData.symbol,
          "name": stockData.name,
          "shares": parseInt(numShares),
          "price": stockData.price,
          "total": (stockData.price * numShares).toFixed(2),
          "date": new Date().toLocaleString(),
          "order": "SELL"
        });

        state.user[0].portfolio.cash += parseInt((stockData.price * numShares).toFixed(2))


      return state;
      });
    
  }

  function calculateTotal() {
    let cash = $state.user[0].portfolio.cash
    let stocksValue = 0

    $state.user[0].portfolio.stocks.forEach(x => stocksValue += (x.shares * x.price))
    
    return stocksValue + cash
  }
</script>

<main class="h-screen w-screen flex items-center justify-center">
  {#if $state.loggedIn === true}
    <div class="w-4/12">
      <div class="flex justify-between mb-4 items-center">
        <h2
          class="scroll-m-20 border-b pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0"
        >
          Welcome {$state.user[0].username}!
        </h2>
        <DropdownMenu.Root>
          <DropdownMenu.Trigger
            ><Avatar.Root>
              <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
              <Avatar.Fallback>CN</Avatar.Fallback>
            </Avatar.Root></DropdownMenu.Trigger
          >
          <DropdownMenu.Content class="w-40">
            <DropdownMenu.Group>
              <DropdownMenu.Label>My Account</DropdownMenu.Label>
              <DropdownMenu.Separator />
              <DropdownMenu.Item on:click={handleLogOut}
                ><LogOut class="mr-2 h-4 w-4" />
                <span>Log out</span>
                <DropdownMenu.Shortcut>⇧⌘Q</DropdownMenu.Shortcut
                ></DropdownMenu.Item
              >
            </DropdownMenu.Group>
          </DropdownMenu.Content>
        </DropdownMenu.Root>
      </div>

      <div class="flex flex-col gap-y-2 mb-4">
        <Label for="symbol">Symbol Search / Trade</Label>
        <div class="flex gap-x-2">
          <Input id="symbol" placeholder="Enter Symbol" bind:value={symbol} />
          <Dialog.Root>
            <Dialog.Trigger
              ><Button on:click={getStockData}>Trade</Button></Dialog.Trigger
            >
            <Dialog.Content>
              <Dialog.Header>
                <Dialog.Title>Trade Order</Dialog.Title>
              </Dialog.Header>
              {#if stockData}
                <div>
                  <div class="flex gap-x-3 mb-2">
                    <h3
                      class="scroll-m-20 text-2xl font-semibold tracking-tight"
                    >
                      {stockData.name}
                    </h3>
                    <Badge>{stockData.symbol}</Badge>
                  </div>
                  <h1
                    class="scroll-m-20 text-5xl font-extrabold tracking-tight lg:text-5xl"
                  >
                    {stockData.price.toLocaleString("en-US", {
                      style: "currency",
                      currency: "USD",
                    })}
                  </h1>
                </div>
                <div>
                  <Label for="quantity">Quantity</Label>
                  <Input
                    id="quantity"
                    placeholder="Enter number of shares"
                    bind:value={numShares}
                  />
                  <p class="text-sm text-muted-foreground">
                    Maximum Amount: {calculateMaxShares()}
                  </p>
                </div>

                <div>
                  <h3 class="scroll-m-20 text-2xl font-semibold tracking-tight">
                    Order Summary
                  </h3>
                  <div class="flex justify-between">
                    <p class="font-bold">Price per share</p>
                    <p>
                      {stockData.price.toLocaleString("en-US", {
                        style: "currency",
                        currency: "USD",
                      })}
                    </p>
                  </div>
                  <div class="flex justify-between">
                    <p class="font-bold">Number of shares</p>
                    <p>{numShares}</p>
                  </div>
                  <div class="flex justify-between">
                    <p class="font-bold">Total</p>
                    <p>
                      {(numShares * stockData.price).toLocaleString("en-US", {
                        style: "currency",
                        currency: "USD",
                      })}
                    </p>
                  </div>
                </div>

                <div class="flex w-full justify-between gap-2">
                  <Button class="w-6/12" on:click={handleBuy}>Buy</Button>
                  <Button class="w-6/12" on:click={handleSell}>Sell</Button>
                </div>
              {/if}
            </Dialog.Content>
          </Dialog.Root>
        </div>
      </div>

      <Tabs.Root value="portfolio">
        <div class="flex justify-between">
          <Tabs.List>
            <Tabs.Trigger value="portfolio">Portfolio</Tabs.Trigger>
            <Tabs.Trigger value="transactions">Transaction History</Tabs.Trigger
            >
          </Tabs.List>
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
              {#each $state.user[0].portfolio.stocks as stock, i (i)}
                <Table.Row>
                  <Table.Cell class="font-medium">{stock.symbol}</Table.Cell>
                  <Table.Cell>{stock.name}</Table.Cell>
                  <Table.Cell>{stock.shares}</Table.Cell>
                  <Table.Cell>{stock.price.toLocaleString("en-US", {
                    style: "currency",
                    currency: "USD",
                  })}</Table.Cell>
                  <Table.Cell class="text-right"
                    >{(stock.price * stock.shares).toLocaleString("en-US", {
                      style: "currency",
                      currency: "USD",
                    })}</Table.Cell
                  >
                </Table.Row>
              {/each}
              <Table.Row class="w-full">
                <Table.Cell></Table.Cell>
                <Table.Cell></Table.Cell>
                <Table.Cell></Table.Cell>
                <Table.Cell class="font-bold">Cash</Table.Cell>
                <Table.Cell class="text-right"
                  >{$state.user[0].portfolio.cash.toLocaleString("en-US", {
                    style: "currency",
                    currency: "USD",
                  })}</Table.Cell
                >
              </Table.Row>
              <Table.Row class="w-full">
                <Table.Cell></Table.Cell>
                <Table.Cell></Table.Cell>
                <Table.Cell></Table.Cell>
                <Table.Cell class="font-bold">TOTAL</Table.Cell>
                <Table.Cell class="text-right">{calculateTotal().toLocaleString("en-US", {style: "currency", currency: "USD",})}</Table.Cell>
              </Table.Row>
            </Table.Body>
          </Table.Root>
        </Tabs.Content>
        <Tabs.Content value="transactions">
          <Table.Root>
            <Table.Caption>A list of your recent transactions.</Table.Caption>
            <Table.Header>
              <Table.Row>
                <Table.Head>Date</Table.Head>
                <Table.Head>Order Type</Table.Head>
                <Table.Head class="w-[100px]">Symbol</Table.Head>
                <Table.Head>Name</Table.Head>
                <Table.Head>Shares</Table.Head>
                <Table.Head>Price</Table.Head>
                <Table.Head class="text-right">Total</Table.Head>
              </Table.Row>
            </Table.Header>
            <Table.Body>
              {#each $state.user[0].transactions as transaction, i (i)}
                <Table.Row>
                  <Table.Cell>{transaction.date}</Table.Cell>
                  <Table.Cell>{transaction.order}</Table.Cell>
                  <Table.Cell>{transaction.symbol}</Table.Cell>
                  <Table.Cell>{transaction.name}</Table.Cell>
                  <Table.Cell>{transaction.shares}</Table.Cell>
                  <Table.Cell>{transaction.price.toLocaleString("en-US", {
                    style: "currency",
                    currency: "USD",
                  })}</Table.Cell>
                  <Table.Cell class="text-right"
                    >{(transaction.total).toLocaleString("en-US", {
                      style: "currency",
                      currency: "USD",
                    })}</Table.Cell
                  >
                </Table.Row>
              {/each}
            </Table.Body>
          </Table.Root>
        </Tabs.Content>
      </Tabs.Root>
    </div>
  {:else if $state.logInForm === true}
    <LogIn />
  {:else}
    <SignUp />
  {/if}
</main>

<style>
</style>
