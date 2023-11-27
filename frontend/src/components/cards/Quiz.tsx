import { useState, useEffect } from "react";
import CardsApi from "../../services/CardsApi";
import { Quiz } from "../../types/card.type";
import { useParams } from "react-router-dom";

function Quiz(){
    const { id } = useParams();
    const [quiz, setQuiz] = useState<Quiz>();

    useEffect(()=>{
        async function fetchData(){
            const response = await CardsApi.getQuiz(id as string);
            if (response.status === 200){
                console.log(response.data);
                setQuiz(response.data);
            }
            else{
                console.log("I will redirect you if the quiz does not exist");
            }
        }
        fetchData();
    }, []);

    return(
        <>
        <h1>Quiz: {quiz?.name}</h1>
        <ul>
            {
                quiz?.flashcards.map((element, index) => (
                    <li key={index}>
                        question: {element.question} | {element.answer}
                    </li>
                ))
            }
        </ul>
        </>
    )
}

export default Quiz;