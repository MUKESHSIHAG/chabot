import React, { useState, useEffect } from "react";
import ReactDOM from "react-dom";
import { v4 as uuidv4 } from 'uuid';

import BotMessage from "./components/BotMessage";
import UserMessage from "./components/UserMessage";
import Messages from "./components/Messages";
import Input from "./components/Input";

import API from "./api/ChatbotAPI";

import "./styles.css";
import Header from "./components/Header";

function Chatbot() {
  const [messages, setMessages] = useState([]);
  const session_id = uuidv4();

  useEffect(() => {
    async function loadWelcomeMessage() {
      const welcomeMessage = await API.GetChatbotResponse("hi", session_id);
      if (welcomeMessage) {
        setMessages([
          {
            id: welcomeMessage.id,
            type: 'bot',
            content: <BotMessage fetchMessage={() => welcomeMessage.response} />
          }
        ]);
      }
    }
    loadWelcomeMessage();
  }, []);

  const send = async text => {
    const userMessage = await API.GetChatbotResponse(text, session_id);

    if (userMessage) {
      const botMessage = {
        id: uuidv4(),
        type: 'bot',
        content: <BotMessage fetchMessage={() => userMessage.response} />
      };

      setMessages([
        ...messages,
        {
          id: userMessage.id,
          type: 'user',
          content: (
            <UserMessage
              id={userMessage.id}
              text={userMessage.message}
              onUpdate={handleUpdateMessage}
              onDelete={() => handleDeleteMessage(userMessage.id, botMessage.id)}
            />
          ),
        },
        botMessage
      ]);
    }
  };

  const handleUpdateMessage = (id, newText) => {
    setMessages(prevMessages =>
      prevMessages.map(msg =>
        msg.id === id ? { ...msg, content: <UserMessage id={id} text={newText} onUpdate={handleUpdateMessage} onDelete={() => handleDeleteMessage(id, uuidv4())} /> } : msg
      )
    );
  };

  const handleDeleteMessage = (userId, botId) => {
    setMessages(prevMessages =>
      prevMessages.filter(msg => msg.id !== userId && msg.id !== botId)
    );
  };

  return (
    <div className="chatbot">
      <Header />
      <Messages messages={messages.map(msg => msg.content)} />
      <Input onSend={send} />
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<Chatbot />, rootElement);