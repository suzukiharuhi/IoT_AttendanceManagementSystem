export type Attendance = {
  id: number;
  name: string;
  status: string;
  datetime: string;
};

export async function getAttendance() {
  // APIへHTTPリクエストを送る
  const res = await fetch(import.meta.env.VITE_API_URL + "/attendance");
  if (!res.ok) {
    throw new Error("Failed to fetch attendance data");
  }
  return await res.json();
}
