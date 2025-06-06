const Footer = () => {
    return (
        <footer className="bg-gray-900 text-gray-300 mt-10">
            <div className="max-w-6xl mx-auto px-4 py-10 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8">
                <div>
                    <h3 className="text-lg font-semibold mb-3">Company</h3>
                    <ul>
                        <li className="hover:text-white cursor-pointer">About Us</li>
                        <li className="hover:text-white cursor-pointer">Careers</li>
                        <li className="hover:text-white cursor-pointer">Press</li>
                    </ul>
                </div>

                <div>
                    <h3 className="text-lg font-semibold mb-3">Services</h3>
                    <ul>
                        <li className="hover:text-white cursor-pointer">Web Development</li>
                        <li className="hover:text-white cursor-pointer">Design</li>
                        <li className="hover:text-white cursor-pointer">Marketing</li>
                    </ul>
                </div>

                <div>
                    <h3 className="text-lg font-semibold mb-3">Support</h3>
                    <ul>
                        <li className="hover:text-white cursor-pointer">Help Center</li>
                        <li className="hover:text-white cursor-pointer">Privacy Policy</li>
                        <li className="hover:text-white cursor-pointer">Terms of Service</li>
                    </ul>
                </div>

                <div>
                    <h3 className="text-lg font-semibold mb-3">Stay Connected</h3>
                    <p className="text-sm mb-3">Subscribe to our newsletter</p>
                    <input
                        type="email"
                        placeholder="Enter your email"
                        className="w-full px-3 py-2 rounded bg-gray-800 text-white outline-none focus:ring-2 focus:ring-green-500"
                    />
                </div>
            </div>

            <div className="text-center text-sm text-gray-500 py-4 border-t border-gray-700">
                © {new Date().getFullYear()} Gemten Ai. All rights reserved.
            </div>
        </footer>
    );
};

export default Footer;