import { Link } from "react-router-dom";
import { IoAdd } from "react-icons/io5";

export default function AddButton() {
    return (
        <Link to={"/note/new"} className="floating-button">
            <IoAdd />
        </Link>
    );
}
