import { useGetAttendance } from "../../hooks/useGetAttendance";
import "./HomePage.css";

function HomePage() {
  const { data, loading, error } = useGetAttendance();

  const getStatusColumn = (status: string, target: string) =>
    status === target ? <span className="circle" /> : null;
  
  return (
    <div>
      <h3>出席一覧</h3>
      {loading && <p>読み込み中...</p>}
      {error && <p>エラー: {error.message}</p>}
      <table className="attendance-table">
        <thead>
          <tr>
            <th>名前</th>
            <th>在室</th>
            <th>一時不在</th>
            <th>退室</th>
            <th>更新時刻</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <tr key={item.id}>
              <td>{item.name}</td>
              <td>{getStatusColumn(item.status, "在室")}</td>
              <td>{getStatusColumn(item.status, "一時不在")}</td>
              <td>{getStatusColumn(item.status, "退室")}</td>
              <td>{item.datetime}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default HomePage;
