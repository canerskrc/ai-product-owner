import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [requirements, setRequirements] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/requirements")
      .then(response => setRequirements(response.data))
      .catch(error => console.error("Error fetching data:", error));
  }, []);

  return (
    <div>
      <h1>AI Product Owner</h1>
      <ul>
        {requirements.map(req => (
          <li key={req.id}>{req.title} - Priority: {req.priority}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
