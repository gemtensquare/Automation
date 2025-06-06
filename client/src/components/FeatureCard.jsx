
// FeatureCard Component
function FeatureCard({ title, description, imageSrc }) {
    return (
        <div className="relative overflow-hidden rounded-3xl bg-gray-900 text-white h-[300px]">
            <div className="p-8 h-full flex flex-col justify-between z-10 relative">
                <div>
                    <h3 className="text-2xl md:text-3xl font-bold mb-4">{title}</h3>
                    <p className="text-gray-300">{description}</p>
                </div>
            </div>
            <div className="absolute inset-0 w-full h-full">
                <img src={imageSrc || "/placeholder.jpg"} alt={title} className="w-full h-full object-cover opacity-80" />
            </div>
        </div>
    )
}

export default FeatureCard;