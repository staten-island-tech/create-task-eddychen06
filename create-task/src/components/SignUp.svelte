<script lang="ts">
  import { Button } from "$lib/components/ui/button";
  import * as Card from "$lib/components/ui/card";
  import { Input } from "$lib/components/ui/input";
  import { Label } from "$lib/components/ui/label";
  import { update, state } from "../store";


  let username: String;
  let password: String;


    function addUser() {
        let users = $state.users
        if (users.filter((user) => user.username === username).length > 0){
            console.log("exists")
        } else {
            update(state => {
            state.users.unshift({
                id: state.users.length + 1,
                username: username,
                password: password,
                portfolio: {
                  "cash": 10000,
                  "stocks": []
                },
                transactions: [],
            })
            return state

        })
        }
    }

    function handleSwitchForm() {
        update(state => {
            state.logInForm = true
            return state
        })
        
    }
  
</script>

<Card.Root class="w-[350px]">
  <Card.Header class="space-y-1">
    <Card.Title class="text-2xl">Create an account</Card.Title>
    <Card.Description
      >Enter your email below to create your account</Card.Description
    >
  </Card.Header>
  <Card.Content>
    <form>
      <div class="grid w-full items-center gap-4">
        <div class="flex flex-col space-y-1.5">
            <Label for="username">Username</Label>
            <Input id="username" bind:value={username} />
          </div>
        <div class="flex flex-col space-y-1.5">
          <Label for="password">Password</Label>
          <Input id="password" type="password" bind:value={password} />
        </div>
      </div>
    </form>
  </Card.Content>
  <Card.Footer class="flex flex-col gap-y-4">
    <Button class="w-full" on:click={addUser} >Create account</Button>
    <Label
      >Have an account? <button class="underline" on:click={handleSwitchForm}
        >Log In</button
      ></Label
    >
  </Card.Footer>
</Card.Root>
