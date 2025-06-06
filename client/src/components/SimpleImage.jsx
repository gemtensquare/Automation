import React from 'react';

const SimpleImage = () => {
    return (
        <div className="flex justify-center items-center">
            <div className="max-w-sm rounded-lg shadow-lg overflow-hidden bg-white">
                <div className="relative">
                    <img src="http://127.0.0.1:8000/Media/news_images/Picsart_25-04-11_21-17-59-091.jpg" alt="Simple Image" className="w-full h-64 object-cover" />
                    <div className="absolute bottom-2 left-2 bg-black bg-opacity-50 text-white text-sm py-1 px-3 rounded-full">
                        Recent Post
                    </div>
                </div>
                <div className="p-4">
                    <h3 className="text-xl font-semibold text-gray-800">
                        Simpl dededededededededed haha iij ijfirfj e Image for meee hello bangladesh
                    </h3>
                    <div className="flex mt-2 gap-2">
                        <a target="_blank" href="http://127.0.0.1:8000/Media/news_images/Picsart_25-04-11_21-17-59-091.jpg" rel="noopener noreferrer" className="flex-1 py-2 px-4 bg-gray-200 rounded-lg font-medium text-center">
                            View News
                        </a>
                        <a target="_blank" href="http://127.0.0.1:8000/Media/news_images/Picsart_25-04-11_21-17-59-091.jpg" rel="noopener noreferrer" className="flex-1 py-2 px-4 bg-orange-500 text-white rounded-lg font-medium text-center">
                            View Images
                        </a>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default SimpleImage;