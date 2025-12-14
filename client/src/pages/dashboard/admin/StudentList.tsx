import styles from "./StudentList.module.css";
import type { Course } from "../../../types";
import { useEffect, useState } from "react";
import { fetchStudentList } from "../../../callers";

type Props = {
  course: Course;
  courseSetter: React.Dispatch<React.SetStateAction<Course | null>>;
};

export const StudentList = ({ course, courseSetter }: Props) => {
  const [students, setStudents] = useState<string[]>([]);

  useEffect(() => {
    fetchStudentList(course.courseId, setStudents);
  }, []);

  return (
    <div className={styles.studentListContainer}>
      <div className={styles.listWrapper}>
        <div className={styles.header}>
          <img
            src="./src/assets/backIcon.png"
            alt=""
            onClick={() => courseSetter(null)}
          />
        </div>
        <h2>
          Students - {course.subject} {`[${course.tutor}]`}
        </h2>
        {students.map((item, index) => {
          return <p key={index}>{item}</p>;
        })}
      </div>
    </div>
  );
};
