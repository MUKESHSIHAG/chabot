// src/components/UserMessage.js
import React, { useState } from 'react';
import { FaEdit, FaTrash } from 'react-icons/fa';
import API from '../api/ChatbotAPI';

export default function UserMessage({ id, text, onUpdate, onDelete }) {
  const [isEditing, setIsEditing] = useState(false);
  const [newText, setNewText] = useState(text);

  const handleEdit = async () => {
    if (isEditing) {
      const updatedMessage = await API.EditUserMessage(id, newText);
      if (updatedMessage) {
        onUpdate(id, newText);
      }
    }
    setIsEditing(!isEditing);
  };

  const handleDelete = async () => {
    const deletedMessage = await API.DeleteUserMessage(id);
    if (deletedMessage) {
      onDelete(id);
    }
  };

  return (
    <div className="message-container">
      {isEditing ? (
        <input
          type="text"
          value={newText}
          onChange={(e) => setNewText(e.target.value)}
          className='edit'
          onBlur={handleEdit}
          autoFocus
        />
      ) : (
        <div className="user-message">{text} <FaEdit onClick={handleEdit} style={{ cursor: 'pointer' }} /> <FaTrash onClick={handleDelete} style={{ cursor: 'pointer' }} /></div>
      )}
    </div>
  );
}
