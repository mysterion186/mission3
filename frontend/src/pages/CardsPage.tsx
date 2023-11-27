/**
 * Default layout for every page related to cards
 */
import { Outlet } from "react-router-dom";
function CardsPage(){

    return(
        <>
        <h1>Base Page for cards</h1>
        <Outlet />
        </>
    )
}

export default CardsPage;