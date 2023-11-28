/**
 * This file contains all the stuff related to localStorage.
 * I'll save the token here for the moment, and find a better way later.
 */

export default{
    saveJWTToken(token: string):void{
        window.localStorage.setItem("token", token);
    },
    getJWTToken():string | null{
        return window.localStorage.getItem("token");
    },
    saveUserId(id: string):void {
        window.localStorage.setItem("id", id);
    },
    getUserId(): string | null{
        return window.localStorage.getItem("id");
    }
}