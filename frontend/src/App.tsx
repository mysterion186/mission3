import './App.css'
import { Link } from 'react-router-dom';

function App() {
  return (
      <div>
        <h2>React Google Login</h2>
        <p><Link to={"/auth/login"}>login</Link></p>
        <p><Link to={"/auth/register"}>register</Link></p>
        <p><Link to={"/auth/user"}>user</Link></p>
        <p><Link to={"/auth/update-password"}>update-password</Link></p>
        <p><Link to={"/auth/password-reset-link"}>password-reset-link</Link></p>
        <p>Click on the given link for actually change your password</p>
      </div>
  );
}

export default App;