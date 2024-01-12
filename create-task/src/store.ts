import { writable } from 'svelte/store'
import user from './assets/users.json' 

export let userStore = writable(user)