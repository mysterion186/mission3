/**
 * Components that will display all the Decks that are in the app
 */
import { useState, useEffect } from "react";
import CardsApi from "../../services/CardsApi";
import { Deck } from "../../types/card.type";

function Decks(){
    const [decks, setDecks] = useState<Deck[]>([]);

    useEffect(()=>{
        async function fetchData(){
            const response = await CardsApi.getAllDecks();
            if (response.status === 200){
                setDecks(response.data);
            }
            else{
                console.log("An error occured");
            }
        }
        fetchData();
    }, [])
    return(
        <>
        <h1>Resulat</h1>
        <ul>
            {
                decks.map((element, index) => (
                    <li key={index}>
                        name: {element.name} | theme: {element.theme}
                    </li>
                ))
            }
        </ul>
        </>
    )
}

export default Decks;