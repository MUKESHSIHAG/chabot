import React, { useState } from "react";
import { FaPaperPlane } from 'react-icons/fa';

export default function Input({ onSend }) {
  const [text, setText] = useState("");

  const handleInputChange = e => {
    setText(e.target.value);
  };

  const handleSend = e => {
    e.preventDefault();
    onSend(text);
    setText("");
  };

  return (
    <div className="input">
      <form onSubmit={handleSend} style={{ display: 'flex', alignItems: 'center' }}>
        <input
          type="text"
          onChange={handleInputChange}
          value={text}
          placeholder="Enter your message here"
        />
        <button type="submit" style={{ background: 'none', border: 'none', cursor: 'pointer' }}>
          <FaPaperPlane size={20} />
        </button>
      </form>
    </div>
  );
}
