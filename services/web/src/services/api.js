import axios from "axios";

const api = axios.create({ baseURL: process.env.REACT_APP_USERS_SERVICE_URL });

export default api;