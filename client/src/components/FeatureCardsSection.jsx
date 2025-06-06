import FeatureCard from './FeatureCard';
import screenshot1 from '../assets/Screenshot1.png';
import screenshot2 from '../assets/Screenshot2.png';


const FeatureCardsSection = () => {
    return (
        // <div className="min-h-screen">
            // <div className="relative">
                <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-16">
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <FeatureCard title="CONNECT. SHARE. GROW. TOGETHER"
                            description="The new reality of communications"
                            imageSrc={screenshot2} />
                        <FeatureCard title="Explore the Future of Digital Design with Project After Cube."
                            description="Innovative solutions for tomorrow's challenges"
                            imageSrc={screenshot1} />
                    </div>
                </div>
            // </div>
        // </div>
    )
}

export default FeatureCardsSection;