<script lang="ts">
  import { userStore } from "./store"
  import SignUp from './components/SignUp.svelte'
  import LogIn from './components/LogIn.svelte'

  let username: String;
  let password: String;
  let isUserLogin = false;

  let isSignUp = false;

</script>

<main class="h-screen w-screen flex items-center justify-center">
  <div>
    {#if isSignUp === false}
    <LogIn />
    {:else}
    <SignUp bind:isSignUp={isSignUp}/>
    {/if}
</div>

{#if isUserLogin === true} 
  <h1>Welcome {username}</h1>
{/if}

</main>

<style>
</style>
