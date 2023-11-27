import { createBrowserRouter } from "react-router-dom";
import App from './App.tsx'
import Login from "./components/authentication/Login.tsx";
import Registration from "./components/authentication/Registration.tsx";
import User from "./components/authentication/User.tsx";
import UpdatePassword from "./components/authentication/UpdatePassword.tsx";
import PasswordResetLink from "./components/authentication/PasswordResetLink.tsx";
import PasswordReset from "./components/authentication/PasswordReset.tsx";
import AuthPage from "./pages/AuthPage.tsx";
import CardsPage from "./pages/CardsPage.tsx";
import Decks from "./components/cards/Decks.tsx";
import Quiz from "./components/cards/Quiz.tsx";

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />
    },
    {
        path: "/auth",
        element: <AuthPage />,
        children: [
            {
                path: "login",
                element: <Login />
            },
            {
                path: "register",
                element: <Registration />
            },
            {
                path: "user",
                element: <User />
            },
            {
                path: "update-password",
                element: <UpdatePassword />
            },
            {
                path: "password-reset-link",
                element: <PasswordResetLink />
            },
            {
                path: "password/reset/:uidb64/:token",
                element: <PasswordReset />
            }
        ]
    },
    {
        path: "/cards",
        element: <CardsPage />,
        children: [
            {
                path: "",
                element: <Decks />
            },
            {
                path: ":id",
                element: <Quiz />
            }
        ]
    }
])

export default router;