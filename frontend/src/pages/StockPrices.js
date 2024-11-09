import React, { useEffect, useState } from 'react';
import "../styles/StockPrices.css"
import api from '../api';

const StockPrices = () => {
    // Variables to hold stock data and toggle state
    const [stocks, setStocks] = useState([]);
    const [isExpanded, setIsExpanded] = useState(false);
    const [searchQuery, setSearchQuery] = useState("");

    // use the hook to fetch the data when the component loads
    useEffect(() => {
        const getStockPrices = async () => {
            try {
                // fetch the data from the api
                const data = await api();
                // store the data in the stocks state
                setStocks(data);
            } catch (error) {
                console.error("Error fetching stock data!");
            }
        };
        // call the function to fetch the data
        getStockPrices();
    }, []);

    function toggleTable() {
        setIsExpanded(prevState => !prevState);
    }

    function stockSearchQuery(e) {
        var upperCase = e.target.value.toUpperCase();
        setSearchQuery(upperCase)
    }

    const filteredStocks = stocks.filter(stock => (
            stock.ticker.toUpperCase().includes(searchQuery)));

    return (
        <div>
            <h1>Stock Prices</h1>
            <div className='input__container'>
                <input onChange={stockSearchQuery} id="stock__search" placeholder='Search stocks'></input>
            </div>
            <div className="table__container">
                <div className={`table__wrapper ${isExpanded ? "expanded" : ""}`}>
                    <table className="stock__info">
                        <thead>
                            <tr>
                                <th>Ticker:</th>
                                <th>Date:</th>
                                <th>Open:</th>
                                <th>High:</th>
                                <th>Low:</th>
                                <th>Close:</th>
                                <th>Volume:</th>
                                <th>Market Cap:</th>
                                <th>PE Ratio:</th>
                                <th>52-Week High:</th>
                                <th>52-Week Low:</th>
                            </tr>
                        </thead>
                        <tbody>
                            {filteredStocks.map((stock) => (
                                <tr id="single__stock" key={stock.id}>
                                    <th>{stock.ticker}</th>
                                    <th>{new Date(stock.date).toLocaleString()}</th>
                                    <th>{stock.open}</th>
                                    <th>{stock.high}</th>
                                    <th>{stock.low}</th>
                                    <th>{stock.close}</th>
                                    <th>{stock.volume}</th>
                                    <th>{stock.market_cap}</th>
                                    <th>{stock.pe_ratio}</th>
                                    <th>{stock.high_52_week}</th>
                                    <th>{stock.low_52_week}</th>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
                <button className="toggle__all__btn" onClick={toggleTable}>
                    {isExpanded ? "▲" : "▼"}
                </button>
        </div>
    );
};

export default StockPrices;
