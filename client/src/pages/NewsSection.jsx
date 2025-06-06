import axios from 'axios';
import React, { useState, useEffect } from 'react';
import { motion } from "framer-motion";

import { toast } from 'react-toastify';

import NewsCard from '../components/NewsCard';
import ToggleSwitch from '../components/ToggleSwitch';
import useFetch from '../hooks/useFetch'
import MessageBox from '../components/MessageBox';
import FilterComponent from '../components/Filtering';

import API from "../services/API"
import Helper from '../helper/Helper';


// Main App Component
const NewsSection = () => {
  const [message, setMessage] = useState('');
  const [newsData, setNewsData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [autoPost, setAutoPost] = useState(true);
  const [newsToShow, setNewsToShow] = useState([]);
  const [filteredNews, setFilteredNews] = useState([]);

  const { templateResponse, templateLoading = true, templateError } = useFetch(API.getTemplate);
  const templates = templateResponse?.data || [];

  const helper = new Helper();

  const [categoriNewsCount, setCategoriNewsCount] = useState(null);

  const fetchFilteredNews = async (selectedCategories) => {
    // toast.info("Fetching filtered news, Please wait...");
    try {
      // const response = await axios.post(API.getNews,
      //   {
      //     categories: selectedCategories
      //   }
      // );
      // toast.success(response.data.message);
      // setFilteredNews(response.data.data);
      const news = helper.FilterNews(newsData, selectedCategories);
      if (news.length > 0) {
        setNewsToShow(news);
        setFilteredNews(news);
      }
      else if (newsData.length > 0) {
        setNewsToShow(newsData);
      }
    }
    catch (error) {
      toast.error(error.message || "An error occurred");
      console.log(error)
    }
  }

  useEffect(() => {
    window.scroll({ top: 490, left: 0, behavior: 'smooth' });
    const fetchNews = async () => {
      try {
        // toast.info("Faching new news, Please wait...");
        const response = await axios.get(API.getNews);
        setNewsData(response.data.data);
        setNewsToShow(response.data.data);
        const count = helper.getCategoriesNewsCount(response.data.data);
        setCategoriNewsCount(count);
        setLoading(false);
        // toast.success(response.data.message);
      } catch (error) {
        toast.error(error.message || "An error occurred");
        console.error("Error fetching the news:", error);
      }
    }
    fetchNews();


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
    // fetchMessage();
  }, []);


  return (
    <div className="container mx-auto p-4 max-w-7xl">
      {/* <MessageBox message={messages} /> */}
      <FilterComponent fetchFilteredNews={fetchFilteredNews} categoriNewsCount={categoriNewsCount}/>
      {/* <MessageBox message={messages} /> */}
      <header className="flex justify-between items-center mb-8 py-4">
        <h1 className="text-3xl font-bold">News ({newsToShow.length || "..."})</h1>
        <div className="flex items-center gap-3">
          <span className="text-xl">Auto Post</span>
          <ToggleSwitch isOn={autoPost} handleToggle={() => setAutoPost(!autoPost)} />
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {loading
          ? Array(8).fill().map((_, index) => (
            <motion.div key={index} className="bg-gray-200 h-64 rounded-lg shadow-md"
              initial={{ opacity: 0.3, scale: 0.9 }} animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.8, repeat: Infinity, repeatType: "reverse" }} />
          ))
          : newsToShow.map((card, index) => (
            <NewsCard news={card} key={index}/>
          ))}
      </div>
    </div>
  );
};


export default NewsSection;