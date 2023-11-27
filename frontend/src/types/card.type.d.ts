interface RawDeck{
    owner: number,
    theme: number,
    name: string
}
export interface Deck extends RawDeck{
    id: number,
    user_emai: string,
    
}

export interface Flashcard{
    deck: number,
    deck_name: string,
    question: string,
    answer: string, 
    position: number
}

export interface Quiz extends RawDeck{
    flashcards: Flashcard[]
}