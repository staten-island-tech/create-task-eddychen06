<script lang="ts">
    import { Button } from "$lib/components/ui/button";
    import * as Card from "$lib/components/ui/card";
    import { Input } from "$lib/components/ui/input";
    import { Label } from "$lib/components/ui/label";
    import { userStore } from "../store";  

    let email: String 
    let password: String
    let status = false

    export let isUserLogin = status
    export let isSignUp = true

    function handleSignUp() {


        let id: Number = Math.floor(Math.random()*1000)
        $userStore[id] = {email, password}
        status = true
    }   

    function switchToLogIn() {
        isSignUp = false
    }

  </script>
  
  <Card.Root class="w-[350px]">
    <Card.Header class="space-y-1">
		<Card.Title class="text-2xl">Create an account</Card.Title>
		<Card.Description>Enter your email below to create your account</Card.Description>
	</Card.Header>
    <Card.Content>
      <form>
        <div class="grid w-full items-center gap-4">
          <div class="flex flex-col space-y-1.5">
            <Label for="email">Email</Label>
            <Input id="email" bind:value={email}/>
          </div>
          <div class="flex flex-col space-y-1.5">
            <Label for="password">Password</Label>
            <Input id="password" type="password" bind:value={password}/>
          </div>
        </div>
      </form>
    </Card.Content>
    <Card.Footer class="flex flex-col gap-y-2">
		<Button class="w-full" on:click={handleSignUp}>Create account</Button>
        <Label>Have an account? <button class="underline" on:click={switchToLogIn}>Log In</button></Label>
	</Card.Footer>
  </Card.Root>