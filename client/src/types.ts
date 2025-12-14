export type EnrollReq = {
  course_id: number;
  student_id: number;
};

export type Course = {
  courseId: number;
  subject: string;
  tutor: string;
};