import { useState } from "react";
import styles from "./EntryPage.module.css";
import { RegisterForm } from "./components/RegisterForm";
import { LoginForm } from "./components/LoginForm";

export const EntryPage = () => {
  const [form, changeForm] = useState<"R" | "L">("R");

  return (
    <div className={styles.container}>
      <h1>Student Enrollment System</h1>
      <div className={styles.formWrapper}>
        <div className={styles.selectionHeader}>
          <button
            className={`${styles.registerBtn} ${
              form == "R" ? styles.activeBtn : styles.nonActiveBtn
            }`}
            onClick={() => changeForm("R")}
          >
            Register
          </button>
          <button
            className={`${styles.loginBtn} ${
              form == "L" ? styles.activeBtn : styles.nonActiveBtn
            }`}
            onClick={() => changeForm("L")}
          >
            Login
          </button>
        </div>
        {form == "R" ? <RegisterForm /> : <LoginForm />}
      </div>
    </div>
  );
};
