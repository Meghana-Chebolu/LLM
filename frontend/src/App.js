import React, { useState } from 'react';

function App() {
  const [inputText, setInputText] = useState('');
  const [apiKey, setApiKey] = useState('');
  const [response, setResponse] = useState('');

  const handleChatGPTCompletion = async () => {
    try {
      const result = await fetch('https://8000-meghanachebolu-llm-7bg3igl9sz1.ws-us107.gitpod.io/get_chatGPT_completion', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          api_key: apiKey,
          prompt: inputText,
        }),
      });

      const data = await result.json();
      setResponse(data.response);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <h1>React App</h1>
      <div>
        <input
          type="password"
          placeholder="Enter OpenAI API Key"
          value={apiKey}
          onChange={(e) => setApiKey(e.target.value)}
        />
        <br />
        <input
          type="text"
          placeholder="Enter chat prompt"
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
        />
        <br />
        <button onClick={handleChatGPTCompletion}>ChatGPT Completion</button>
      </div>
      <div>
        <p>Response: {response}</p>
      </div>
    </div>
  );
}

export default App;
