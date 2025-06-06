const ToggleSwitch = ({ isOn, handleToggle }) => {
    return (
        <div onClick={handleToggle} className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500 ${isOn ? 'bg-green-500' : 'bg-gray-200'}`}>
            <span className={`inline-block h-5 w-5 transform rounded-full bg-white transition-transform ${isOn ? 'translate-x-6' : 'translate-x-1'}`} />
        </div>
    );
};

export default ToggleSwitch;