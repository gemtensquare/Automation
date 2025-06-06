import axios from 'axios';
import Swal from "sweetalert2";
import { useState } from 'react';
import { toast } from 'react-toastify';
import { motion, AnimatePresence } from "framer-motion";

import TimeAgo from './TimeAgo'
import API from "../services/API";
import useFetch from '../hooks/useFetch';
import TemplateShowingModal from './TemplateShowingModal';


const NewsCard = ({ news }) => {
    const staticImg = 'https://tds-images.thedailystar.net/sites/default/files/styles/big_202/public/images/2025/05/12/tds_-_2025-05-12t132510.257.png';

    const [templates, setTemplates] = useState([]);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [selectedTemplate, setselectedTemplate] = useState(null);


    const handlePost = async () => {
        try {
            const response = await axios.get(API.getTemplate);
            const data = response.data;

            setTemplates(data.data);

            toast.success("Please select a template image.");
            setIsModalOpen(true);
        } catch (error) {
            toast.error("Failed to fetch templates.");
            console.error("Template fetch error:", error);
        }
    };

    const closeModal = () => {
        setIsModalOpen(false);
        setselectedTemplate(null);
    };

    const toggleImageSelection = (template_id) => {
        setselectedTemplate(template_id);
    };

    const submitPostHandler = async () => {
        if (!selectedTemplate) {
            toast.error("Please select a template image.");
            return;
        }

        const storedPages = localStorage.getItem('pages');
        toast.info('Post queueing... Please wait...');

        try {
            closeModal();
            const response = await axios.post(API.PostNews, {
                id: news.id, storedPages, template_id: selectedTemplate
            });
            toast.success(response.data.message);
        } catch (error) {
            console.error("Post submission error:", error);
            toast.error("Failed to submit post.");
        }
    };

    return (
        <div className="flex justify-center items-center">
            {/* <h1> Fyyyfrfhurfhurfhrufh {templates} </h1> */}
            <div className="max-w-sm rounded-lg shadow-lg overflow-hidden bg-white">
                <div className="relative">
                    <img src={news.image_url || staticImg} alt={news.title} className="w-full h-64 object-cover" />

                    {/* Source - Top Left */}
                    <div className="absolute top-2 left-2 bg-black bg-opacity-50 text-white text-sm py-1 px-3 rounded-full">
                        {news.source}
                    </div>

                    {/* TimeAgo - Bottom Left */}
                    <div className="absolute bottom-2 left-2 bg-black bg-opacity-50 text-white text-sm py-1 px-3 rounded-full">
                        <TimeAgo isoDate={news.created_at} />
                    </div>

                    {/* Category - Bottom Right */}
                    <div className="absolute bottom-2 right-2 bg-black bg-opacity-50 text-white text-sm py-1 px-3 rounded-full">
                        {news.category}
                    </div>
                </div>

                <div className="p-4">
                    <h3 className="text-xl font-semibold text-gray-800">
                        {news.title.slice(0, 45)}...
                    </h3>
                    <div className="flex mt-2 gap-2">
                        <a target="_blank" href={news.url} rel="noopener noreferrer" className="flex-1 py-2 px-4 bg-gray-200 rounded-lg font-medium text-center">
                            View
                        </a>
                        <button onClick={handlePost} className="cursor-pointer flex-1 py-2 px-4 bg-orange-500 text-white rounded-lg font-medium text-center">
                            Post
                        </button>
                    </div>
                </div>
            </div>


            <AnimatePresence>
                {isModalOpen && <TemplateShowingModal templates={templates} closeModal={closeModal} submitPostHandler={submitPostHandler} selectedTemplate={selectedTemplate} toggleImageSelection={toggleImageSelection} />}
            </AnimatePresence>
        </div>
    );
};

export default NewsCard;