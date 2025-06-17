import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import theme from './theme/theme';
import DashboardLayout from './components/layout/DashboardLayout';
import Dashboard from './pages/Dashboard';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <DashboardLayout>
          <Routes>
            <Route path="/" element={<Dashboard />} />
            {/* Diğer sayfalar için route'lar buraya eklenecek */}
          </Routes>
        </DashboardLayout>
      </Router>
    </ThemeProvider>
  );
}

export default App; 