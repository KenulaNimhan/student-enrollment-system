import { Routes, Route } from "react-router-dom";
import { EntryPage } from "./pages/entryPage/EntryPage";
import { AdminDashboard } from "./pages/dashboard/admin/AdminDashboard";
import { StudentDashboard } from "./pages/dashboard/student/StudentDashboard";

function App() {
  return (
    <Routes>
      <Route path="/" element={<EntryPage />} />
      <Route
        path="/student-dashboard/my-courses"
        element={<StudentDashboard page="myCourses" />}
      />
      <Route
        path="/student-dashboard/other-courses"
        element={<StudentDashboard page="otherCourses" />}
      />
      <Route
        path="/student-dashboard/my-account"
        element={<StudentDashboard page="myAccount" />}
      />
      <Route path="/admin-dashboard" element={<AdminDashboard />} />
    </Routes>
  );
}

export default App;
