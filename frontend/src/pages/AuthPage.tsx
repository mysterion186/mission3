/**
 * Default layout for every page related to the authentication
 */
import { Outlet } from "react-router-dom";
function AuthPage(){

    return(
        <>
        <h1>Base Page for authentication</h1>
        <Outlet />
        </>
    )
}

export default AuthPage;