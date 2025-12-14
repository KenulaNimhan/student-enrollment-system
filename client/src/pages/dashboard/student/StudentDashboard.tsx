import { MyCourses } from "./courses/MyCourses";
import { OtherCourses } from "./courses/OtherCourses";
import styles from "./StudentDashboard.module.css";
import { useNavigate } from "react-router-dom";

type Props = {
  page: "myCourses" | "otherCourses" | "myAccount";
};

export const StudentDashboard = ({ page }: Props) => {
  const navigate = useNavigate();
  const studentId = localStorage.getItem("studentId");

  if (studentId == null) {
    navigate("/");
    return;
  }

  console.log(studentId);

  return (
    <div className={styles.dashboardContainer}>
      <header>
        <h2>Student Dashboard</h2>
        <div>
          <button
            className={
              page == "myCourses" ? styles.activeBtn : styles.nonActiveBtn
            }
            onClick={() => navigate("/student-dashboard/my-courses")}
          >
            My Courses
          </button>
          <button
            className={
              page == "otherCourses" ? styles.activeBtn : styles.nonActiveBtn
            }
            onClick={() => navigate("/student-dashboard/other-courses")}
          >
            Other Courses
          </button>
          <button
            className={styles.signOutBtn}
            onClick={() => {
              localStorage.removeItem("studentId");
              navigate("/");
            }}
          >
            SignOut
          </button>
        </div>
      </header>
      {page == "myCourses" ? <MyCourses studentId={studentId!} /> : ""}
      {page == "otherCourses" ? <OtherCourses studentId={studentId!} /> : ""}
    </div>
  );
};
