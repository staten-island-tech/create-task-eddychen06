<script lang="ts">
    import { Button } from "$lib/components/ui/button";
    import * as Card from "$lib/components/ui/card";
    import { Input } from "$lib/components/ui/input";
    import { Label } from "$lib/components/ui/label";
    import * as Alert from "$lib/components/ui/alert";
    import { update, state } from "../store";

    let username: String
    let password: String

    function handleLogIn() {
        let user = $state.users.filter((user) => user.username === username)

        if(user.length > 0) {
            if (user[0].password === password) {
                update(state => {
                    state.loggedIn = true
                    state.user = user
                    return state
                })
            }
        }
    }

    function handleSwitchForm() {
        update(state => {
            state.logInForm = false
            return state
        })
    }

    let errorMessage = ""

  </script>
  <div class="flex flex-col">
  
  <Card.Root class="w-[350px]">
    <Card.Header class="space-y-1">
		<Card.Title class="text-2xl">Welcome back!</Card.Title>
		<Card.Description>Enter your credentials below to log in your account</Card.Description>
	</Card.Header>
    <Card.Content>
      <form>
        <div class="grid w-full items-center gap-4">
          <div class="flex flex-col space-y-1.5">
            <Label for="username">Username</Label>
            <Input id="username" bind:value={username}/>
          </div>
          <div class="flex flex-col space-y-1.5">
            <Label for="password">Password</Label>
            <Input id="password" type="password" bind:value={password}/>
          </div>
        </div>
      </form>
    </Card.Content>
    <Card.Footer class="flex flex-col gap-y-4">
		<Button class="w-full" on:click={handleLogIn}>Log In</Button>
        <Label>Don't have an account? <button class="underline" on:click={handleSwitchForm}>Sign Up</button></Label>
	</Card.Footer>
  </Card.Root>

</div>