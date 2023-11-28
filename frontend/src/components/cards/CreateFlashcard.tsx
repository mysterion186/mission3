/**
 * View for creating flashcards
 */
import { ChangeEvent, FormEvent, useEffect, useState } from "react";
import { useRequireAuth } from "../../hooks/authentication";
import { useNavigate } from "react-router-dom";
import CardsApi from "../../services/CardsApi";
import AuthStorage from "../../services/AuthStorage";


function CreateFlashcard() {

    const [formData, setFormData] = useState({
        deck: -1, 
        question: "",
        answer: "",
        position: 0
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
    }, []);
    const navigate = useNavigate();

    const handleSubmit = async (e:FormEvent) => {
        e.preventDefault();
        
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
                    <label htmlFor="question">question:</label>
                    <input
                    type="text"
                    id="question"
                    name="question"
                    value={formData.question}
                    onChange={handleInputchange}
                    required
                    placeholder="Question"
                    />
                </div>
                <div>
                    <label htmlFor="answer">answer:</label>
                    <input
                    type="text"
                    id="answer"
                    name="answer"
                    value={formData.answer}
                    onChange={handleInputchange}
                    required
                    placeholder="Answer"
                    />
                </div>
                <button type="submit">Create Flashcard</button>
            </form>
        </>
    )
}

export default CreateFlashcard;