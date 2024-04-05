import "./App.css";
import Header from "./components/Header";
import NotesListPage from "./pages/NotesListPage";
import NotePage from "./pages/NotePage";
import { Routes, Route } from "react-router-dom";

export default function App() {
    return (
        <div className="container dark">
            <div className="app">
            <Header />
            <Routes>
                <Route path="/" exact element={<NotesListPage />} />
                <Route path="/note/:noteId" element={<NotePage />} />
            </Routes>
            </div>
        </div>
    );
}
