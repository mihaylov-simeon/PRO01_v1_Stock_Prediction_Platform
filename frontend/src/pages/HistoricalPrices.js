import React, { useEffect, useState } from 'react';
import "../styles/HistoricalPrices.css"
import api from '../api';

const StockPrices = () => {
    // Variables to hold stock data and toggle state
    const [history, setHistory] = useState([])
    const [isExpanded, setIsExpanded] = useState(false);
    const [searchQuery, setSearchQuery] = useState("");
    const [startDate, setStartDate] = useState("")
    const [endDate, setEndDate] = useState("")

    // use the hook to fetch the data when the component loads
    useEffect(() => {
        const getStockHistoryPrices = async () => {
            try {
                // fetch the data from the API
                const response_history = await api.get("api/history_prices");
                // store the data in the stocks state
                setHistory(response_history.data);
            } catch (error) {
                console.error("Error fetching stock data!", error);
            }
        };
        // call the function to fetch the data
        getStockHistoryPrices();
    }, []);

    function toggleTable() {
        setIsExpanded(prevState => !prevState);
    }

    function stockSearchQuery(e) {
        var upperCase = e.target.value.toUpperCase();
        setSearchQuery(upperCase)
    }

    // Filter history data based on search query and date range
    const filteredStocksHistory = history.filter(stock => {
        const stockDate = new Date(stock.date).toISOString().split('T')[0];
        const withinDateRange =
            (!startDate || stockDate >= startDate) &&
            (!endDate || stockDate <= endDate);

        return (
            stock.ticker.toUpperCase().includes(searchQuery) &&
            withinDateRange
        );
    });

    return (
        <div>
            <h1>History Prices</h1>
            <div className='input__container'>
                <input onChange={stockSearchQuery} id="stock__search" placeholder='Search stocks'></input>
            </div>
            <div className='input__container__date'>
                <input 
                    type="date"
                    value={startDate}
                    onChange={(e) => setStartDate(e.target.value)}
                />
                <input 
                    type="date"
                    value={endDate}
                    onChange={(e) => setEndDate(e.target.value)}
                />
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
                            {filteredStocksHistory.map((stock) => (
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
