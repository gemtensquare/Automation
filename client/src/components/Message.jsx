import axios from 'axios';
import { toast } from 'react-toastify';
import React, { useEffect, useState } from 'react';


import MessageBox from './MessageBox';
import API from '../services/API';


function Message() {
    const [message, setMessage] = useState('');

    useEffect(() => {
        // window.scroll({ top: 500, left: 0, behavior: 'smooth' });
        const fetchMessage = async () => {
            try {
                toast.info("Faching new news, Please wait...");
                const response = await axios.get(API.testApi);
                setMessage(response.data.message);
                toast.success(response.data.message);
            } catch (error) {
                toast.error(error.message || "An error occurred");
                console.error("Error fetching the message:", error);
                setMessage("Something went wrong. Please try again.");
            }
        };
        fetchMessage();
    }, []);

    return (
        <MessageBox message={message} />
    );
}

export default Message;