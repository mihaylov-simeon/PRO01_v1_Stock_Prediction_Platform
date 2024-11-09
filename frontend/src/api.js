import axios from 'axios';

const API_URL = "http://127.0.0.1:8000/api/";

const api = async () => {
    try {
        const response = await axios.get(`${API_URL}stock_prices`);
        return response.data;
    } catch (error) {
        console.error("Error fetching stock prices:", error);
        throw error;
    }
};

export default api