import { CheckCircle, Loader2 } from 'lucide-react'; // Install via `npm install lucide-react`

const MessageBox = ({ message }) => {
  return (
    <div className="my-10 flex items-center justify-center">
      <div
        className={`flex items-center gap-3 px-6 py-4 rounded-xl shadow-md transition-all duration-300
        ${message ? "bg-green-100 text-green-700" : "bg-yellow-100 text-yellow-700 animate-pulse"}`}
      >
        {message ? (
          <CheckCircle className="w-6 h-6 text-green-600" />
        ) : (
          <Loader2 className="w-6 h-6 animate-spin text-yellow-600" />
        )}
        <span className="text-lg font-semibold">
          {message || "Loading..."}
        </span>
      </div>
    </div>
  );
};

export default MessageBox;
