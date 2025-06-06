import API from "../services/API";
import { motion, AnimatePresence } from "framer-motion";




const TemplateShowingModal = ({ templates, closeModal, submitPostHandler, selectedTemplate, toggleImageSelection }) => {
    return (
        <>
            <motion.div className="fixed inset-0 z-50 bg-gray bg-opacity-50 backdrop-blur-lg flex justify-center items-center"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}>
                <motion.div className="bg-white p-6 rounded-lg w-[90%] max-w-3xl relative"
                    initial={{ scale: 0.8, opacity: 0 }}
                    animate={{ scale: 1, opacity: 1 }}
                    exit={{ scale: 0.8, opacity: 0 }}
                    transition={{ duration: 0.3 }}>
                    <button onClick={closeModal} className="absolute top-2 right-2 text-gray-600 hover:text-black text-3xl cursor-pointer">
                        ✕
                    </button>

                    <h2 className="text-xl font-bold mb-4">Choose a Template for Post</h2>

                    <div className="h-120 overflow-y-auto pr-2">
                        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3">
                            {templates.map((template, index) => {
                                // const isSelected = img === selectedTemplate;
                                const isSelected = template.id === selectedTemplate;
                                return (
                                    <motion.div key={index} whileHover={{ scale: 1.05 }}
                                        whileTap={{ scale: 0.95 }} onClick={() => toggleImageSelection(template.id)}
                                        className="relative cursor-pointer group m-4">
                                        <img src={API.mediaBaseUrl + template.image} alt={`Preview ${template.name}`}
                                            className={`rounded-lg w-full object-cover transition-transform ${isSelected ? "ring-4 ring-orange-500 scale-105" : ""
                                                }`} />
                                        {isSelected && (
                                            <div className="absolute top-2 right-2 bg-white rounded-full p-1 shadow-md">
                                                <svg xmlns="http://www.w3.org/2000/svg" fill="orange" viewBox="0 0 24 24" stroke="white" strokeWidth="1.5" className="w-6 h-6">
                                                    <path strokeLinecap="round" strokeLinejoin="round" d="M4.5 12.75l6 6 9-13.5" />
                                                </svg>
                                            </div>
                                        )}
                                    </motion.div>
                                );
                            })}
                        </div>
                    </div>

                    <div className="mt-6 flex justify-between">
                        <button onClick={closeModal} className="bg-red-700 hover:bg-red-800 text-white cursor-pointer px-6 py-2 rounded-lg font-medium">
                            Cancel Post
                        </button>
                        <button onClick={submitPostHandler} className="bg-orange-500 hover:bg-orange-600 text-white cursor-pointer px-6 py-2 rounded-lg font-medium">
                            Confirm Post
                        </button>
                    </div>
                </motion.div>
            </motion.div>
        </>
    )
}

export default TemplateShowingModal;