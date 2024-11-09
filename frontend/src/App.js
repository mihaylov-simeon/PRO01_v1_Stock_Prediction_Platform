import './App.css';
import React from 'react'
import StockPrices from './pages/StockPrices'
import NavBar from './components/NavBar'

const App = () => {
  return (
    <div>
      <StockPrices />
      <NavBar />
    </div>
  )
}

export default App;
