// App.js
import React, { useState } from 'react';
import { environment } from "./environment";
import './App.css';

function App() {
  const env = environment;
  const [selectedOption, setSelectedOption] = useState('ChatGPT');
  const [apiKey, setApiKey] = useState('');
  const [inputText, setInputText] = useState('');
  const [response, setResponse] = useState('');
  const [error, setError] = useState('');

  const handleChatGPTCompletion = async () => {
    try {
      const formData = new FormData();
      formData.append('api_key', apiKey);
      formData.append('prompt', inputText);

      const result = await fetch(env.fastAPIUrl, {
        method: 'POST',
        cache: 'no-cache',
        credentials: 'same-origin',
        redirect: 'follow',
        referrerPolicy: 'no-referrer',
        body: formData,
      });
      if (!result.ok) {
        throw new Error(`HTTP error! Status: ${result.status}`);
      }
      const data = await result.json();
      console.log("API Response:", data);
      setResponse(data.response);
      setError('');
    } catch (error) {
      setResponse('');
      setError('Error occurred. Please check your input and try again.');
      console.error('Error:', error);
    }
  };

  const renderOptionFields = () => {
    let apiKeyPlaceholder = '';
    let inputTextPlaceholder = '';

    switch (selectedOption) {
      case 'ChatGPT':
        apiKeyPlaceholder = 'Enter ChatGPT API Key';
        inputTextPlaceholder = 'Enter prompt';
        break;
      case 'LLaMA-7B':
        apiKeyPlaceholder = 'Enter LLaMA-7B API Key';
        inputTextPlaceholder = 'Enter prompt';
        break;
      case 'Gemini':
        apiKeyPlaceholder = 'Enter Gemini API Key';
        inputTextPlaceholder = 'Enter prompt';
        break;
      default:
        break;
    }

    return (
      <div className="input-container">
        <input
          className="input-box"
          type="password"
          placeholder={apiKeyPlaceholder}
          value={apiKey}
          onChange={(e) => setApiKey(e.target.value)}
        />
        <br />
        <input
          className="input-box"
          type="text"
          placeholder={inputTextPlaceholder}
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
        />
      </div>
    );
  };

  return (
    <div className="app-container">
      <h1>LLM App</h1>
      <div className="form-container">
        <label className="label">Select the Model:</label>
        <select
          className="select-option"
          value={selectedOption}
          onChange={(e) => setSelectedOption(e.target.value)}
        >
          <option value="ChatGPT">ChatGPT</option>
          <option value="LLaMA-7B">LLaMA-7B</option>
          <option value="Gemini">Gemini</option>
        </select>
        {renderOptionFields()}
        <button className="blue-button" onClick={handleChatGPTCompletion}>
          Get Response
        </button>
      </div>
      <div style={{ marginTop: '20px' }}>
        <p style={{ color: 'red' }}>{error}</p>
        {response && (
          <div style={{ marginTop: '10px', border: '1px solid #ccc', padding: '10px', borderRadius: '5px' }}>
            <p style={{ color: 'green', marginBottom: '5px' }}>Response:</p>
            <pre style={{ whiteSpace: 'pre-wrap', wordWrap: 'break-word' }}>{response}</pre>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
