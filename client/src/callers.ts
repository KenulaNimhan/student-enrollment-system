import type { EnrollReq, Course } from "./types";


// calls the api to enroll a student in a course
export const enroll = async (courseId: number, studentId: string) => {
  const request: EnrollReq = {
    course_id: courseId,
    student_id: Number(studentId),
  };

  console.log(request);

  const url = "http://localhost:8000/enroll";
  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(request),
    });
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const result = await response.json();
    console.log(result);
  } catch (error: any) {
    console.error(error.message);
  }
};

// calls the api to remove a student from the course
export const disenroll = async (courseId: number, studentId: string) => {
  const request: EnrollReq = {
    course_id: courseId,
    student_id: Number(studentId),
  };

  console.log(request);

  const url = "http://localhost:8000/disenroll";
  try {
    const response = await fetch(url, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(request),
    });
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const result = await response.json();
    console.log(result);
  } catch (error: any) {
    console.error(error.message);
  }
};

// calls the api to fetch list of students enrolled in a course
export const fetchStudentList = async (id: number, setter: React.Dispatch<React.SetStateAction<string[]>>) => {
  const url = `http://localhost:8000/course-students?course_id=${id}`;
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const result = await response.json();
    setter(result);
    console.log(result);
  } catch (error: any) {
    console.error(error.message);
  }
};

// calls the api to fetch a list of all courses
export const fetchCourses = async (setter: React.Dispatch<React.SetStateAction<Course[]>>) => {
    const url = "http://localhost:8000/all-courses";
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        const result: Course[] = await response.json();
        console.log(result);
        setter(result);
    } catch (error: any) {
        console.error(error.message);
    }
};

// calls the api to fetch list of enrolled courses of a student
export const fetchMyCourses = async (id: string, setter: React.Dispatch<React.SetStateAction<Course[]>>) => {
      const url = `http://localhost:8000/enrolled-courses?student_id=${id}`;
      try {
        const response = await fetch(url);

        if (!response.ok) {
          throw new Error(`Response status: ${response.status}`);
        }
        const result = await response.json();
        console.log(result);
        setter(result);
      } catch (error: any) {
        console.error(error.message);
      }
    };

// calls the api to fetch all unenrolled courses of a student
export const fetchOtherCourses = async (id: string, setter: React.Dispatch<React.SetStateAction<Course[]>>) => {
    const url = `http://localhost:8000/unenrolled-courses?student_id=${id}`;
    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        const result = await response.json();
        console.log(result);
        setter(result);
    } catch (error: any) {
        console.error(error.message);
    }
};