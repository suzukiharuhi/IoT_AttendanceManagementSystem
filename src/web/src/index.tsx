import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App"; // アプリの土台（ルート）を読み込む
import "./index.css";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

