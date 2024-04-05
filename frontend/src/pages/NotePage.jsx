import { useParams, useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import { FaChevronLeft } from "react-icons/fa6";



export default function NotePage() {
    let { noteId } = useParams();
    let [note, setNote] = useState(null);
    const navigate = useNavigate();
    const getNote = async () => {
        if (noteId === "new") return;
        let response = await fetch(`http://localhost:8000/api/${noteId}`);
        let data = await response.json();
        setNote(data);
    };
    useEffect(() => {
        getNote();
    }, [noteId]);

    const updateNote = async () => {
        await fetch(`/api/notes/${noteId}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(note),
        });
    };

    const deleteNote = async () => {
        await fetch(`/api/notes/${noteId}`, {
            method: "DELETE",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(note),
        });
        navigate("/");
    };
    const createNote = async () => {
        await fetch(`/api/notes`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(note),
        });
        navigate("/");
    };

    let handleChange = (value) => {
        setNote((note)=> ({...note, "body": value}));
    };

    let handleSubmit = () => {
        console.log(note);
        if (noteId !== "new" && note.body === "") {
            deleteNote();
        } else if (noteId !== "new") {
            updateNote();
        } else if (noteId === "new" && note.body !== null) {
            createNote();
        }
        navigate("/");
    };

    return (
        <div className="note">
            <div className="note-header">
                <h3>
                    <FaChevronLeft onClick={handleSubmit} />
                </h3>
                {noteId !== "new" ? (
                    <button onClick={deleteNote}>Delete</button>
                ) : (
                    <button onClick={createNote}>Done</button>
                )}
            </div>

            <textarea
                onChange={(e) => handleChange(e.target.value)}
                value={note?.body}
            ></textarea>
        </div>
    );
}
