<script lang="ts">
  import { userStore, isSignUp, isLoggedIn, userDetails } from "./store";
  import SignUp from "./components/SignUp.svelte";
  import LogIn from "./components/LogIn.svelte";
  import Button from "$lib/components/ui/button/button.svelte";
  import * as Avatar from "$lib/components/ui/avatar";

  function handleLogOut() {
    $isLoggedIn = false;
  }
</script>

<main class="h-screen w-screen flex items-center justify-center">


  {#if $isLoggedIn === true}
  <div class="flex flex-col">

    <h1>Welcome {$userDetails.email}</h1>
    <Button on:click={handleLogOut}>Log Out</Button>
    <Avatar.Root>
      <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
      <Avatar.Fallback>CN</Avatar.Fallback>
    </Avatar.Root>
    </div>  
  {:else if $isSignUp === false}
    <LogIn />
  {:else}
    <SignUp />
  {/if}
</main>

<style>
</style>
