import axios from 'axios';
import { toast } from 'react-toastify';
import { HiPlus } from 'react-icons/hi';
import React, { useState, useEffect } from 'react';
import { FaFacebook, FaTrashAlt } from 'react-icons/fa';
import { motion, AnimatePresence } from 'framer-motion';


import API from "../services/API";
import Constant from "../helper/Constants";
import TemplateShowingModal from '../components/TemplateShowingModal';


const Customization = () => {
    const [pages, setPages] = useState([]);
    const [pageId, setPageId] = useState('');
    const [pageName, setPageName] = useState('');
    const [templates, setTemplates] = useState([]);
    const [showModal, setShowModal] = useState(false);
    const [accessToken, setAccessToken] = useState('');
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [editingIndex, setEditingIndex] = useState(null);
    const [selectedTemplate, setselectedTemplate] = useState(null);
    const [selectedCategories, setSelectedCategories] = useState([]);


    const fetchTemplates = async () => {
        try {
            const response = await axios.get(API.getTemplate);
            setTemplates(response.data?.data);
        } catch (error) {
            toast.error("Failed to fetch templates.");
            console.error("Template fetch error:", error);
        }
    };

    useEffect(() => {
        setIsModalOpen(true);
        try {
            const storedPages = JSON.parse(localStorage.getItem('pages')) || [];
            if (Array.isArray(storedPages)) setPages(storedPages);
        } catch (error) {
            console.error('Error reading pages from localStorage:', error);
        }
        fetchTemplates();
    }, []);

    const resetForm = () => {
        setPageName('');
        setPageId('');
        setAccessToken('');
        setSelectedCategories([]);
        setEditingIndex(null);
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        if (!pageName.trim() || !pageId.trim() || !accessToken.trim()) {
            toast.error('All fields are required!');
            return;
        }

        if (selectedCategories.length === 0) {
            toast.error('Select at least one category.');
            return;
        }

        const newPage = { pageName, pageId, accessToken, categories: selectedCategories };

        let updatedPages = [...pages];

        if (editingIndex !== null) {
            updatedPages[editingIndex] = newPage;
            toast.success('Page updated successfully');
        } else {
            if (pages.some((p) => p.pageId === pageId)) {
                toast.error('This Page ID already exists.');
                return;
            }
            updatedPages.push(newPage);
            toast.success('Page added successfully');
        }

        setPages(updatedPages);
        localStorage.setItem('pages', JSON.stringify(updatedPages));
        resetForm();
        setShowModal(false);
    };

    const handleDelete = (index) => {
        const updatedPages = pages.filter((_, i) => i !== index);
        setPages(updatedPages);
        localStorage.setItem('pages', JSON.stringify(updatedPages));
        toast.success('Page deleted');
    };

    const closeModal = () => {
        setIsModalOpen(false);
    };

    const handleEdit = (index) => {
        const page = pages[index];
        if (!page) return;

        setPageName(page.pageName || '');
        setPageId(page.pageId || '');
        setAccessToken(page.accessToken || '');
        setSelectedCategories(Array.isArray(page.categories) ? page.categories : []);
        setEditingIndex(index);
        setShowModal(true);
    };

    const pageAccessLink = 'https://developers.facebook.com/tools/explorer/?method=GET&path=me%2Faccounts%3Faccess_token%3DLONG_LIVED_USER_TOKEN&version=v22.0';

    const handleCategoryChange = (category) => {
        setSelectedCategories((prev) =>
            prev.includes(category) ? prev.filter((c) => c !== category) : [...prev, category]
        );
    };

    const toggleImageSelection = (template_id) => {
        setselectedTemplate(template_id);
    };

    const submitPostHandler = () => {

    }

    return (
        <section className="pt-12 px-4 bg-gradient-to-br">
            <div className="max-w-7xl mx-auto bg-white rounded-3xl shadow-2xl p-8 relative">
                <h2 className="text-3xl md:text-4xl font-extrabold text-orange-600 mb-8 flex items-center gap-3">
                    <a href={pageAccessLink} target="_blank" rel="noopener noreferrer">
                        <FaFacebook className="text-blue-600 text-4xl" />
                    </a>
                    Facebook Page Manager
                </h2>

                <div className="space-y-4">
                    {pages.length === 0 ? (
                        <p className="text-gray-500 italic">No pages added yet.</p>
                    ) : (
                        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                            {pages.map((page, index) => (
                                <div key={index} className="bg-gradient-to-br from-orange-100 via-white to-amber-100 p-5 rounded-xl border border-orange-200 shadow-sm hover:shadow-lg transition">
                                    <div className="mb-2 flex items-center gap-2">
                                        <p className="text-lg font-semibold text-gray-700">Page Name:</p>
                                        <a href={`https://www.facebook.com/${page.pageId}`} target="_blank" className="text-lg text-gray-900 font-bold truncate">
                                            {page.pageName}
                                        </a>
                                    </div>
                                    <div className="mb-2 flex items-center gap-2">
                                        <p className="text-lg text-gray-700 font-semibold">Page ID:</p>
                                        <p className="text-lg text-gray-900 truncate">{page.pageId}</p>
                                    </div>
                                    {/* <div className="mb-2 flex items-center gap-2">
                                        <p className="text-lg text-gray-700 font-semibold">Selected Template:</p>
                                        <p className="text-lg text-gray-900 truncate">{selectedTemplate || 'None'}</p>
                                    </div> */}
                                    <div className="mb-2 flex">
                                        {/* <p className="text-lg text-gray-700 font-semibold">Categories:</p> */}
                                        <p className="text-sm font-normal text-gray-800">{page.categories?.join(', ') || 'None'}</p>
                                    </div>
                                    <div className="flex justify-between mt-4">
                                        <button onClick={() => handleEdit(index)} className="cursor-pointer inline-flex items-center text-blue-500 hover:text-blue-700 font-medium">
                                            ✏️ Edit
                                        </button>
                                        <button onClick={() => handleDelete(index)} className="cursor-pointer inline-flex items-center text-red-500 hover:text-red-700 font-medium">
                                            <FaTrashAlt className="mr-2" /> Remove
                                        </button>
                                    </div>
                                </div>
                            ))}
                        </div>
                    )}
                </div>

                <button onClick={() => { resetForm(); setShowModal(true); }} className="cursor-pointer mt-10 px-6 py-3 bg-orange-500 hover:bg-orange-600 text-white font-semibold rounded-full flex items-center gap-2 shadow-md">
                    <HiPlus className="text-xl" /> Add New Page
                </button>
            </div>

            <AnimatePresence>
                {showModal && (
                    <motion.div
                        className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50"
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        transition={{ duration: 0.3 }}
                    >
                        <motion.div
                            className="bg-white rounded-2xl w-full max-w-3xl p-8 relative shadow-xl"
                            initial={{ opacity: 0, scale: 0.8, y: -50 }}
                            animate={{ opacity: 1, scale: 1, y: 0 }}
                            exit={{ opacity: 0, scale: 0.8, y: -50 }}
                            transition={{ duration: 0.4, ease: "easeOut" }}
                        >
                            <button onClick={() => setShowModal(false)} className="absolute top-4 right-4 text-gray-500 text-2xl hover:text-gray-700 cursor-pointer ">&times;</button>
                            <h3 className="text-xl font-bold text-orange-600 mb-6">{editingIndex !== null ? 'Edit Facebook Page' : 'Add Facebook Page'}</h3>
                            <form onSubmit={handleSubmit} className="space-y-4">
                                <div>
                                    <label className="block text-sm font-medium text-gray-700">Page Name</label>
                                    <input value={pageName} onChange={(e) => setPageName(e.target.value)} placeholder="Enter Page Name" className="w-full px-4 py-2 border rounded-lg" />
                                </div>
                                <div>
                                    <label className="block text-sm font-medium text-gray-700">Page ID</label>
                                    <input value={pageId} onChange={(e) => setPageId(e.target.value)} placeholder="Enter Facebook Page ID" className="w-full px-4 py-2 border rounded-lg" />
                                </div>
                                <div>
                                    <label className="block text-sm font-medium text-gray-700">Access Token</label>
                                    <input value={accessToken} onChange={(e) => setAccessToken(e.target.value)} placeholder="Enter Access Token" className="w-full px-4 py-2 border rounded-lg" />
                                </div>
                                <div>
                                    <label className="block text-sm font-medium text-gray-700">Select News Categories</label>
                                    <div className="flex flex-wrap gap-2">
                                        {Constant.allNewsCategories.map((category, index) => (
                                            <label key={index} className="flex items-center gap-2 bg-orange-100 px-3 py-1 rounded-lg text-sm cursor-pointer">
                                                <input type="checkbox" checked={selectedCategories.includes(category)} onChange={() => handleCategoryChange(category)} />
                                                {category}
                                            </label>
                                        ))}
                                    </div>
                                </div>
                                <button type="submit" className="w-full py-3 cursor-pointer  bg-orange-500 hover:bg-orange-600 text-white font-bold rounded-lg shadow-md">
                                    {editingIndex !== null ? 'Update Page' : 'Save Page'}
                                </button>
                            </form>
                        </motion.div>
                    </motion.div>
                )}
            </AnimatePresence>
            {/* <AnimatePresence>
                {isModalOpen && <TemplateShowingModal templates={templates} closeModal={closeModal} submitPostHandler={submitPostHandler} selectedTemplate={[]} toggleImageSelection={toggleImageSelection} />}
            </AnimatePresence> */}
        </section>
    );
};

export default Customization;
