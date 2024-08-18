import axios from 'axios';

const API = {
  GetChatbotResponse: async (message, session_id) => {
    try {
      const response = await axios.post('http://localhost:8000/chat/', {
        session_id: session_id,
        message: message,
      });
      console.log(response.data);
      return response.data;
    } catch (error) {
      console.error('Error fetching chatbot response:', error);
      return null;
    }
  },

  EditUserMessage: async (messageId, newMessage) => {
    try {
      const response = await axios.put(`http://localhost:8000/edit/${messageId}/`, {
        new_message: newMessage,
      });
      return response.data;
    } catch (error) {
      console.error('Error editing message:', error);
      return null;
    }
  },

  DeleteUserMessage: async (messageId) => {
    try {
      const response = await axios.delete(`http://localhost:8000/delete/${messageId}/`);
      return response.data;
    } catch (error) {
      console.error('Error deleting message:', error);
      return null;
    }
  },
};

export default API;
