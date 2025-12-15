import { useEffect, useState } from "react";
import { CourseCard } from "../../components/CourseCard";
import styles from "./CourseContainer.module.css";
import type { Course } from "../../../../types";
import { enroll, fetchOtherCourses } from "../../../../callers";

type Props = {
  studentId: string;
};

export const OtherCourses = ({ studentId }: Props) => {
  const [otherCourses, setOtherCourses] = useState<Course[]>([]);

  useEffect(() => {
    fetchOtherCourses(studentId, setOtherCourses);
  }, [otherCourses.length]);

  return (
    <div className={styles.courseContainer}>
      {otherCourses.map((item) => {
        return (
          <CourseCard
            key={item.courseId}
            subject={item.subject}
            tutor={item.tutor}
            btnName="Enroll"
            btnFn={() => {
              enroll(item.courseId, studentId);
              fetchOtherCourses(studentId, setOtherCourses);
            }}
          />
        );
      })}
    </div>
  );
};
