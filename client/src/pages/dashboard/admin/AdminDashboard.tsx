import styles from "./AdminDashboard.module.css";
import { CourseCard } from "../components/CourseCard";
import { useEffect, useState } from "react";
import type { Course } from "../../../types";
import { fetchCourses } from "../../../callers";
import { StudentList } from "./StudentList";
import { useNavigate } from "react-router-dom";

export const AdminDashboard = () => {
  const [courseInView, setCourseInView] = useState<Course | null>(null);
  const [courseData, setCourseData] = useState<Course[]>([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetchCourses(setCourseData);
  }, []);

  return (
    <div className={styles.dashboardContainer}>
      <header>
        <h2>Admin Dashboard</h2>
        <button onClick={() => navigate("/")}>Sign Out</button>
      </header>
      <h3>Course List</h3>
      <div className={styles.courseContainer}>
        {courseData.map((item, index) => {
          return (
            <CourseCard
              key={index}
              subject={item.subject}
              tutor={item.tutor}
              btnName="View Students"
              btnFn={() => setCourseInView(courseData[index])}
            />
          );
        })}
      </div>
      {courseInView ? (
        <StudentList course={courseInView} courseSetter={setCourseInView} />
      ) : (
        ""
      )}
    </div>
  );
};
