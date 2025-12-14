import { useState } from "react";
import styles from "./Form.module.css";
import { useNavigate } from "react-router-dom";

export const LoginForm = () => {
  const navigate = useNavigate();
  const [validCreds, setValidCreds] = useState<boolean>(true);

  const login = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const formData = new FormData(e.currentTarget);
    const data = Object.fromEntries(formData.entries());

    console.log(data);

    const url = "http://localhost:8000/login";
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        setValidCreds(false);
        return;
      }

      setValidCreds(true);
      const studentId = await response.json();
      localStorage.setItem("studentId", studentId.toString());
      console.log(studentId);
      navigate("/student-dashboard/my-courses");
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <>
      <div className={styles.formContainer}>
        <form onSubmit={login}>
          <input name="email" type="email" placeholder="Email" required />
          <input
            name="password"
            type="password"
            placeholder="Password"
            required
          />
          <span className={validCreds ? styles.nonVisible : styles.visible}>
            invalid email or password
          </span>
          <button type="submit">Login</button>
        </form>
      </div>
    </>
  );
};
