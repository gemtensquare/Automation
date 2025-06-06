import React, { useState } from "react"
import { Link } from "react-router-dom"


const NavBar = () => {
  const [activeTab, setActiveTab] = useState("overview")
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

  const navItems = [
    { name: "Overview", id: "overview", path: "/" },
    { name: "News", id: "news", path: "/news/" },
    // { name: "Check Api", id: "message", path: "/message/" },
    { name: "Customization", id: "customization", path: "/customization/" },
    { name: "Contact Us", id: "contactus", path: "/contact/us/" },
    // { name: "Show Pic", id: "showpic", path: "/show/pic/" },
  ]

  return (
    <nav className="py-6">
      <div className="flex items-center justify-between">
        <div className="md:hidden">
          <button className="text-white bg-transparent border-none cursor-pointer"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path
                d="M3 12H21M3 6H21M3 18H21"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
              />
            </svg>
          </button>
        </div>

        <div className="hidden mx-auto md:flex items-center bg-white rounded-full p-1 shadow-lg">
          {navItems.map((item) => (
            <Link to={item.path} key={item.id} className={`px-6 py-2 rounded-full text-sm font-medium transition-colors ${activeTab === item.id ? "bg-orange-500 text-white" : "text-gray-600 hover:text-gray-900"
              }`} onClick={() => setActiveTab(item.id)}> {item.name} </Link>
          ))}
        </div>

        {/* <button className="bg-orange-500 hover:bg-orange-600 text-white rounded-full px-6 py-2 font-medium transition-colors">
          Contact Us
        </button> */}
      </div>

      {/* Mobile menu */}
      {mobileMenuOpen && (
        <div className="md:hidden mt-4 bg-white rounded-lg p-2 shadow-lg">
          {navItems.map((item) => (
            <Link to={item.path} key={item.id}
              className={`block w-full text-left px-4 py-2 rounded-md text-sm font-medium ${activeTab === item.id ? "bg-orange-500 text-white" : "text-gray-600 hover:bg-gray-100"
                }`}
              onClick={() => {
                setActiveTab(item.id)
                setMobileMenuOpen(false)
              }}>
              {item.name}
            </Link>
          ))}
        </div>
      )}
    </nav>
  )
}
export default NavBar;