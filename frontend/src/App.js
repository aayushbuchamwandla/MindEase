import React, { useState } from "react";
import axios from "axios";

function App() {
  const [message, setMessage] = useState("");
  const [response, setResponse] = useState("");

  const sendMessage = async () => {
    try {
      const res = await axios.post("/chat", { message });
      setResponse(res.data.response);
    } catch (err) {
      console.error(err);
      setResponse("Error connecting to backend");
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>MindEase Chatbot</h1>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type your message"
      />
      <button onClick={sendMessage}>Send</button>
      <p>{response}</p>
    </div>
  );
}

export default App;
