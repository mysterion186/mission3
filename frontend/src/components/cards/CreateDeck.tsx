/**
 * View for creating a Deck
 */

import { ChangeEvent, FormEvent, useEffect, useState } from "react";
import { useRequireAuth } from "../../hooks/authentication";
import { useNavigate } from "react-router-dom";
import CardsApi from "../../services/CardsApi";
import AuthStorage from "../../services/AuthStorage";

function CreateDeck(){
    const [formData, setFormData] = useState({
        owner: -1, 
        theme: 1,
        name: ""
    });
    const [token, setToken] = useState("");

    // make sure the user is logged in 
    useRequireAuth();
    useEffect(() => {
        const localToken: string = AuthStorage.getJWTToken() as string;
        setToken(localToken);
        const userId: string = AuthStorage.getUserId() as string;
        setFormData((prevData) => ({
            ...prevData,
            ["owner"]: Number(userId),
        }))
    }, [])
    const navigate = useNavigate();

    const handleSubmit = async (e:FormEvent) => {
        e.preventDefault();
        const res = await CardsApi.createDeck(formData, token);
        console.log(token, formData);
        if (res.status === 201){
            console.log("Everythin went well ", res.data);
            navigate("/cards/flashcard/" + String(res.data.id));
        }
    };

    const handleInputchange = (e: ChangeEvent<HTMLInputElement>) => {
        const {name, value} = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };

    return (
        <>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="name">name:</label>
                    <input
                    type="text"
                    id="name"
                    name="name"
                    value={formData.name}
                    onChange={handleInputchange}
                    required
                    placeholder="Deck name"
                    />
                </div>
                <button type="submit">Create Deck</button>
            </form>
        </>
    )
}

export default CreateDeck;