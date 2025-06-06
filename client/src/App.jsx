import { useState } from 'react'
import 'react-toastify/dist/ReactToastify.css';
import { ToastContainer } from 'react-toastify';
import { Routes, Route } from 'react-router-dom';


import Message from './components/Message';
import HomePage from './pages/HomePage';
import HeroSection from './pages/HeroSection';
import Footer from './components/Footer';
import NewsSection from './pages/NewsSection';
import ContactUs from './components/ContactUs';
import SimpleImage from './components/SimpleImage';
import Customization from './pages/Customization';

function App() {
  return (
    <>
      <HeroSection />
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/message/" element={<Message />} />
        <Route path="/news/" element={<NewsSection />} />
        <Route path="/contact/us/" element={<ContactUs />} />
        <Route path="/show/pic/" element={<SimpleImage />} />
        <Route path="/customization/" element={<Customization />} />
      </Routes>
      <Footer />
      <ToastContainer />
    </>
  )
}

export default App;