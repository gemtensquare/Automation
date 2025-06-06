import NavBar from '../components/NavBar';
import threeDring from '../assets/3d-ring.png';


const HeroSection = () => {
    return (
        <div className="bg-gradient-to-r from-orange-500 to-amber-400 rounded-4xl overflow-hidden">
            <div className="container mx-auto px-4 sm:px-6 lg:px-8">
                <NavBar />
                <div className="flex flex-col md:flex-row items-center">
                    <div className="md:w-1/2 z-10 mb-10 md:mb-0">
                        <h1 className="text-4xl md:text-5xl lg:text-6xl font-bold text-white mb-4">Gemten Ai</h1>
                        <h2 className="text-2xl md:text-3xl lg:text-4xl font-medium text-white">
                            Blend Concept With Technology
                        </h2>
                    </div>
                    <div className="md:w-1/2 flex justify-center md:justify-end">
                        <div className="relative w-64 h-64 md:w-80 md:h-80 lg:w-96 lg:h-96">
                            <img src={threeDring} alt="3D Ring" className="w-full h-full object-contain" />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
};

export default HeroSection;