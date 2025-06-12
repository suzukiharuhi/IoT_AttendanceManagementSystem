import { useEffect, useState } from "react";
import { getAttendance, Attendance } from "../api/attendance";

export function useGetAttendance() {
  /*
  状態管理フック
  */
 
  // Stateの初期設定
  const [data, setData] = useState<Attendance[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    getAttendance()
      .then((res) => {
        setData(res);
        setLoading(false);
      })
      .catch((err) => {
        setError(err);
        setLoading(false);
      });
  }, []);

  return { data, loading, error };
}
