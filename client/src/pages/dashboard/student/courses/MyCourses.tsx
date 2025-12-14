import { useEffect, useState } from "react";
import { CourseCard } from "../../components/CourseCard";
import styles from "./CourseContainer.module.css";
import type { Course } from "../../../../types";
import { disenroll, fetchMyCourses } from "../../../../callers";

type Props = {
  studentId: string;
};

export const MyCourses = ({ studentId }: Props) => {
  const [myCourses, setMyCourses] = useState<Course[]>([]);

  useEffect(() => {
    fetchMyCourses(studentId, setMyCourses);
  }, []);

  return (
    <div className={styles.courseContainer}>
      {myCourses.map((item, index) => {
        return (
          <CourseCard
            key={index}
            subject={item.subject}
            tutor={item.tutor}
            btnName="Remove"
            btnFn={() => {
              disenroll(item.courseId, studentId);
              fetchMyCourses(studentId, setMyCourses);
            }}
          />
        );
      })}
    </div>
  );
};
