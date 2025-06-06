

import axios from "axios"
import { toast } from "react-toastify";
import { useState, useEffect } from "react"
import { ChevronDown, ChevronUp, X } from "lucide-react"

import API from "../services/API"
import Constants from "../helper/Constants"

import Helper from "../helper/Helper"
const helper = new Helper()

const FilterComponent = ({ fetchFilteredNews, categoriNewsCount }) => {
    const [isDropdownOpen, setIsDropdownOpen] = useState(false)
    const [selectedCategories, setSelectedCategories] = useState([])
    const [activeFilters, setActiveFilters] = useState([])



    const toggleCategory = (category) => {
        setSelectedCategories((prev) =>
            prev.includes(category)
                ? prev.filter((c) => c !== category)
                : [...prev, category]
        )
    }
    const handleConfirm = () => {
        setIsDropdownOpen(false)
        setActiveFilters(selectedCategories)
    }

    const removeActiveFilter = async (filter) => {
        setActiveFilters((prev) => prev.filter((f) => f !== filter))
        setSelectedCategories((prev) => prev.filter((c) => c !== filter))
    }

    const openDropdown = () => {
        setSelectedCategories(activeFilters)
        setIsDropdownOpen(true)
    }

    useEffect(() => {
        setActiveFilters(selectedCategories);
        fetchFilteredNews(selectedCategories);
    }, [selectedCategories]);

    return (
        <div className="w-full max-w-4xl mx-auto p-6">
            <div className="bg-white border border-gray-200 shadow-lg rounded-xl p-6 space-y-3">
                {!isDropdownOpen ? (
                    <>
                        <div>
                            <button onClick={openDropdown} className="bg-gray-200 text-gray-800 cursor-pointer hover:bg-gray-300 px-4 py-2 rounded-md flex items-center gap-2">
                                Select Category
                                <ChevronDown className="w-4 h-4" />
                            </button>
                        </div>

                        {activeFilters.length > 0 && (
                            <div>
                                <p className="text-sm text-gray-500 mb-2">Active filters:</p>
                                <div className="flex flex-wrap gap-2">
                                    {activeFilters.map((filter) => (
                                        <span
                                            key={filter}
                                            className="bg-gray-100 cursor-pointer text-gray-800 px-3 py-1 rounded-full text-sm flex items-center gap-1"
                                        >
                                            <span className="underline">{filter} ({categoriNewsCount[filter] || 0})</span>
                                            <button
                                                onClick={() => removeActiveFilter(filter)}
                                                className="hover:text-red-600"
                                            >
                                                <X className="cursor-pointer h-3 w-3" />
                                            </button>
                                        </span>
                                    ))}
                                </div>
                            </div>
                        )}
                    </>
                ) : (
                    <>
                        <div className="flex items-center justify-between">
                            <button
                                onClick={() => setIsDropdownOpen(false)}
                                className="flex items-center gap-2 text-gray-700 font-medium cursor-pointer"
                            >
                                Select category
                                <ChevronUp className="w-4 h-4" />
                            </button>

                            <button
                                onClick={handleConfirm}
                                className="bg-blue-600 cursor-pointer text-white hover:bg-blue-700 px-5 py-2 rounded-md"
                            >
                                Confirm
                            </button>
                        </div>

                        <div className="flex flex-wrap gap-3">
                            {Constants.allNewsCategories.map((category) => {
                                const isSelected = selectedCategories.includes(category)
                                return (
                                    <button
                                        key={category}
                                        onClick={() => toggleCategory(category)}
                                        className={`flex cursor-pointer items-center gap-2 text-sm font-medium px-4 py-2 rounded-full border transition-colors ${isSelected
                                            ? "bg-green-100 text-green-800 border-green-300"
                                            : "bg-white text-gray-700 border-gray-300 hover:bg-gray-50"
                                            }`}
                                    >
                                        <span className="underline">{category} ({categoriNewsCount[category] || 0})</span>
                                        {isSelected && (
                                            <X
                                                onClick={(e) => {
                                                    e.stopPropagation()
                                                    toggleCategory(category)
                                                }}
                                                className="h-3 w-3 hover:text-red-600"
                                            />
                                        )}
                                    </button>
                                )
                            })}
                        </div>
                    </>
                )}
            </div>
        </div>
    )
}

export default FilterComponent;