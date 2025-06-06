import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Phone, Mail, MapPin } from 'lucide-react';
import { toast } from 'react-toastify'; // ✅ Import toast

const ContactUs = () => {
    const [formData, setFormData] = useState({
        name: '', email: '', message: '',
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        // Here you would send the form data to your server or email service...

        // ✅ Show toast on successful submission
        toast.success('Thank you for contacting us!');

        // Reset form
        setFormData({ name: '', email: '', message: '' });
    };

    useEffect(() => {
        window.scrollTo({ top: 420, left: 0, behavior: 'smooth' });
    }, []);

    return (
        <div className="px-6 py-12 flex flex-col items-center">
            <motion.div
                className="flex flex-col lg:flex-row gap-8 w-full max-w-6xl bg-white shadow-xl rounded-2xl p-8"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8 }}
            >
                {/* Left: Contact Info */}
                <div className="lg:w-1/2 space-y-6">
                    <h2 className="text-2xl font-semibold text-gray-800 mb-4">Get in Touch</h2>

                    <div className="flex items-start gap-4">
                        <Phone className="text-blue-600 mt-1" />
                        <div>
                            <h3 className="text-md font-medium text-gray-700">Phone</h3>
                            <p className="text-gray-600">+880 1317-129349</p>
                        </div>
                    </div>

                    <div className="flex items-start gap-4">
                        <Mail className="text-blue-600 mt-1" />
                        <div>
                            <h3 className="text-md font-medium text-gray-700">Email</h3>
                            <p className="text-gray-600">info@gemtenai.com</p>
                        </div>
                    </div>

                    <div className="flex items-start gap-4">
                        <MapPin className="text-blue-600 mt-1" />
                        <div>
                            <h3 className="text-md font-medium text-gray-700">Location</h3>
                            <p className="text-gray-600">123 Tech Park, Innovation City</p>
                        </div>
                    </div>
                </div>

                {/* Right: Contact Form */}
                <div className="lg:w-1/2">
                    <h2 className="text-xl font-semibold text-gray-800 mb-4">Contact Us</h2>
                    <form onSubmit={handleSubmit} className="space-y-5">
                        <div>
                            <label className="block text-gray-700 mb-1" htmlFor="name">Name</label>
                            <input
                                type="text"
                                name="name"
                                id="name"
                                value={formData.name}
                                onChange={handleChange}
                                required
                                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
                            />
                        </div>

                        <div>
                            <label className="block text-gray-700 mb-1" htmlFor="email">Email</label>
                            <input
                                type="email"
                                name="email"
                                id="email"
                                value={formData.email}
                                onChange={handleChange}
                                required
                                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
                            />
                        </div>

                        <div>
                            <label className="block text-gray-700 mb-1" htmlFor="message">Message</label>
                            <textarea
                                name="message"
                                id="message"
                                rows="5"
                                value={formData.message}
                                onChange={handleChange}
                                required
                                className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500"
                            />
                        </div>

                        <button
                            type="submit"
                            className="bg-blue-600 hover:bg-blue-700 text-white py-2 px-6 rounded-lg transition"
                        >
                            Send Message
                        </button>
                    </form>
                </div>
            </motion.div>
        </div>
    );
};

export default ContactUs;
