import { writable } from 'svelte/store'
import user from './assets/users.json' 

export let userStore = writable(user)

export const isSignUp = writable<boolean>(localStorage.isSignUp === 'true')

isSignUp.subscribe((value) => localStorage.isSignUp = JSON.stringify(value))

export const isLoggedIn = writable<boolean>(localStorage.isLoggedIn === 'false')

isLoggedIn.subscribe((value) => localStorage.isLoggedIn = JSON.stringify(value))

interface User {
    email: string
}

export const userDetails = writable<User>(JSON.parse(localStorage.getItem('user')))
  
userDetails.subscribe((value) => localStorage.user = JSON.stringify(value))