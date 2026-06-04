import React, { useState, useRef, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {

  const [question, setQuestion] = useState("");
  const [chat, setChat] = useState([
    {
      sender: "bot",
      text: "Hello! 🧪 I am your Chemistry Lab Assistant.",
    }
  ]);
  const [loading, setLoading] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false);
  const [darkMode, setDarkMode] = useState(true);

  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [chat]);

  const categorizedQuestions = {
    Definitions: [
      "What is beaker",
      "What is pH",
      "What is molarity"
    ],
    Experiments: [
      "Explain acid base titration procedure",
      "Explain flame test procedure"
    ],
    Safety: [
      "Lab safety rules",
      "What to do in acid spill"
    ],
    Formulas: [
      "Titration formula",
      "Dilution formula"
    ]
  };

  const suggestions = [
    "What is beaker",
    "Explain acid base titration procedure",
    "Lab safety rules"
  ];

  const askQuestion = async (customQuestion = null) => {

    const q = customQuestion || question;
    if (!q.trim()) return;

    setChat(prev => [...prev, { sender: "user", text: q }]);
    setLoading(true);

    try {
      const res = await axios.post("http://localhost:5000/ask", {
        question: q
      });

      setChat(prev => [...prev, {
        sender: "bot",
        text: res.data.answer
      }]);

    } catch {
      setChat(prev => [...prev, {
        sender: "bot",
        text: "⚠️ Server error."
      }]);
    }

    setLoading(false);
    setQuestion("");
  };

  const clearChat = () => {
    setChat([
      {
        sender: "bot",
        text: "Chat cleared. Ask me anything! 🧪"
      }
    ]);
  };

  const startVoice = () => {

    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
      alert("Voice recognition not supported.");
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.start();

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      setQuestion(transcript);
    };
  };

  return (
    <div className={`app ${darkMode ? "dark" : "light"}`}>

      {/* MENU BUTTON */}
      <div className="menu-button" onClick={() => setMenuOpen(!menuOpen)}>
        ☰
      </div>

      {/* SIDEBAR */}
      <div className={`sidebar ${menuOpen ? "open" : ""}`}>
        <h3>Categories</h3>

        {Object.keys(categorizedQuestions).map((category, index) => (
          <details key={index}>
            <summary>{category}</summary>

            {categorizedQuestions[category].map((q, i) => (
              <div
                key={i}
                className="question-item"
                onClick={() => {
                  askQuestion(q);
                  setMenuOpen(false);
                }}
              >
                {q}
              </div>
            ))}

          </details>
        ))}

      </div>

      {/* CHAT AREA */}
      <div className="chat-container">

        <div className="header">
          🧪 Chemistry Lab Assistant

          <div className="header-buttons">
            <button onClick={() => setDarkMode(!darkMode)}>
              {darkMode ? "☀️" : "🌙"}
            </button>
            <button onClick={clearChat}>🧹</button>
          </div>
        </div>

        <div className="chat-box">

          {chat.map((msg, index) => (
            <div key={index} className={`message-row ${msg.sender}`}>
              <div className="message-bubble">
                {Array.isArray(msg.text) ? (
                  <ol>
                    {msg.text.map((item, i) => (
                      <li key={i}>{item}</li>
                    ))}
                  </ol>
                ) : (
                  msg.text
                )}
              </div>
            </div>
          ))}

          {loading && <div className="typing">Typing...</div>}

          <div ref={chatEndRef}></div>

        </div>

        {/* Suggestions */}
        <div className="suggestions">
          {suggestions.map((s, i) => (
            <button key={i} onClick={() => askQuestion(s)}>
              {s}
            </button>
          ))}
        </div>

        {/* Input Area */}
        <div className="input-area">
          <input
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask your question..."
          />
          <button onClick={() => askQuestion()}>➤</button>
          <button onClick={startVoice}>🎤</button>
        </div>

      </div>

    </div>
  );
}

export default App;