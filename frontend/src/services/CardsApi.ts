import axios from "axios";
import { type_headers } from "../types/api.types";
const instance = axios.create({
    baseURL: import.meta.env.VITE_BACKEND_URL
});

export default {
    async call(method: string, ressources: string, data:object | null = null, token: string | null = null ){
        const headers: type_headers = {
            "Content-type": "application/json"
        };

        if (token !== null){
            headers.authorization = "Bearer " + token;
        }
        return instance({
            method,
            headers: headers,
            url: ressources,
            data
        }).then((res) => {
            return {status: res.status, data: res.data};
        }).catch((err) => {
            return {status: err.response.status, data: err.response.data};
        })
    },

    // returns all the decks that are in the app
    async getAllDecks(){
        return this.call("get", "/cards/deck/list");
    },

    // returns all flashcard for a specific Deck
    async getQuiz(id: string){
        return this.call("get", `/cards/deck/${id}`)
    },

    // create a Deck
    async createDeck(data: {owner: number, theme: number, name: string}, token: string){
        return this.call("post", "/cards/deck/create", data, token);
    },

    async createFlashcard(
        data: {deck: number, question: string, answer: string, position: number} | 
            {deck: number, question: string, answer: string, position: number} [],
        token: string
    ){
       return this.call("post", "/cards/flashcard/create", data, token);
    }
}