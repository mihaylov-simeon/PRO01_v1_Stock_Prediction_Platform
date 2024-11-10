import './App.css';
import React from 'react'
import StockPrices from './pages/StockPrices'
import HistoricalPrices from "./pages/HistoricalPrices"
import NavBar from './components/NavBar'
import Form from './components/Form'
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

function logout() {
  localStorage.clear()
  return <Navigate to="/login"/>
}
function App() {
  return (
      <BrowserRouter>
          <NavBar />
          <Routes>
              <Route path="/stock_prices" element={<StockPrices />} />
              <Route path="/history_prices" element={<HistoricalPrices />} />
              <Route path="/login" element={<Form route="/api/token/" method="login" />} />
              <Route path="/register" element={<Form route="/api/register/" method="register" />} />
          </Routes>
      </BrowserRouter>
  );
}

export default App;



