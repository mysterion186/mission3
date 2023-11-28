/**
 * View for creating flashcards
 */
import { FormEvent, useEffect, useState } from "react";
import { useRequireAuth } from "../../hooks/authentication";
import { useNavigate, useParams } from "react-router-dom";
import CardsApi from "../../services/CardsApi";
import AuthStorage from "../../services/AuthStorage";


function CreateFlashcard() {
    useRequireAuth();

    const { id } = useParams();
    const [position, setPosition] = useState(1);
    const [forms, setForms] = useState([
        { deck: Number(id) as number, question: '', answer: '', position: position },
    ]);
    const [token, setToken] = useState("");

    const handleAddForm = () => {
        setForms([...forms, { deck: Number(id), question: '', answer: '', position: position + 1 }]);
    };

    const handleChange = (index: number, field: string, value: string) => {
        const updatedForms = [...forms];
        updatedForms[index][field] = value;
        setForms(updatedForms);
    };
    const navigate = useNavigate();

    const handleSubmit = async (e:FormEvent) => {
        e.preventDefault();
        const res = await CardsApi.createFlashcard(forms, token);
        if (res.status === 201){
            console.log(res.data);
            navigate("/cards");
        }
        else{
            console.log(res);
        }
    };

    useEffect(() => {
        const localToken:string = AuthStorage.getJWTToken() as string;
        setToken(localToken);
    }, [])

    return (
        <div>
            {forms.map((form, index) => (
                <div key={index}>
                    <label>
                        Question:
                        <input
                        type="text"
                        value={form.question}
                        onChange={(e) => handleChange(index, 'question', e.target.value)}
                        />
                    </label>
                    <label>
                        Answer:
                        <input
                        type="text"
                        value={form.answer}
                        onChange={(e) => handleChange(index, 'answer', e.target.value)}
                        />
                    </label>
                </div>
            ))}
            <button onClick={handleAddForm}>Add More Fields</button>
            <button onClick={handleSubmit}>Submit</button>
        </div>
    );
}

export default CreateFlashcard;