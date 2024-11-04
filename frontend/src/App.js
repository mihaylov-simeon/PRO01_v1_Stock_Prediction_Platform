import './App.css';
import React from 'react'
import StockPrices from './components/StockPrices/StockPrices'
import NavBar from './components/NavBar/NavBar'

const App = () => {
  return (
    <div>
      <StockPrices />
      <NavBar />
    </div>
  )
}

export default App;
