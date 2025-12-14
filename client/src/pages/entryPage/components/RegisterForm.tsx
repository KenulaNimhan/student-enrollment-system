import { useState } from "react";
import styles from "./Form.module.css";

export const RegisterForm = () => {
  const [responseMsg, setResponseMsg] = useState<string>("");

  const register = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const formData = new FormData(e.currentTarget);
    const data = Object.fromEntries(formData.entries());

    console.log(data);

    const url = "http://localhost:8000/register-student";
    try {
      const response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (response.status == 400) {
        setResponseMsg("invalid data. please try again");
      } else if (response.status == 500) {
        setResponseMsg("registration unsuccessful. try again");
      }

      if (response.ok) {
        setResponseMsg("registration successful. please login.");
      }

      console.log(await response.json());
    } catch (e) {
      console.error(e);
    }
  };

  return (
    <div className={styles.formContainer}>
      <form onSubmit={register}>
        <input name="name" type="text" placeholder="Name" required />
        <input name="age" type="number" placeholder="Age" />
        <input name="email" type="email" placeholder="Email" required />
        <input
          name="password"
          type="password"
          placeholder="Password"
          required
        />
        <span>{responseMsg}</span>
        <button type="submit">Register</button>
      </form>
    </div>
  );
};
