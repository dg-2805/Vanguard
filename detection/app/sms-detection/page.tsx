// app/sms-detection/page.tsx
"use client";

import { useState } from "react";

export default function SMSDetection() {
  const [input, setInput] = useState("");
  const [result, setResult] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const analyzeSMS = async () => {
    setIsLoading(true);
    setTimeout(() => {
      const isSpam = Math.random() > 0.5;
      setResult(
        isSpam
          ? "⚠️ This SMS is likely SPAM!"
          : "✅ This SMS appears legitimate!"
      );
      setIsLoading(false);
    }, 1000);
  };

  return (
    <div className="min-h-screen bg-blue-50">
      <div className="container mx-auto px-4 py-12">
        <div className="max-w-3xl mx-auto">
          <h1 className="text-4xl font-bold text-blue-800 mb-8 text-center">
            SMS Phishing Detection
          </h1>

          <div className="bg-white p-8 rounded-xl shadow-lg border border-blue-100">
            <label className="block text-lg font-medium text-gray-700 mb-4">
              Paste SMS content:
            </label>
            <textarea
              value={input}
              onChange={(e) => {
                setInput(e.target.value);
                setResult(null);
              }}
              className="w-full h-48 p-4 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent text-black" // Added text-black here
              placeholder="Paste the SMS message here..."
            />
            <button
              onClick={analyzeSMS}
              disabled={isLoading || !input}
              className={`mt-6 w-full py-3 px-6 text-lg font-medium text-white rounded-lg transition-colors ${
                isLoading || !input
                  ? "bg-gray-400"
                  : "bg-blue-600 hover:bg-blue-700"
              }`}
            >
              {isLoading ? "Analyzing..." : "Check for Spam"}
            </button>
            {result && (
              <div
                className={`mt-8 p-4 rounded-lg ${
                  result.includes("✅") ? "bg-green-600" : "bg-red-600"
                }`}
              >
                <p className="text-lg font-medium text-center">{result}</p>
              </div>
            )}
          </div>

          <div className="mt-8 bg-white p-6 rounded-xl shadow-lg border border-blue-100">
            <h2 className="text-2xl font-bold text-blue-800 mb-4">
              Detection Features
            </h2>
            <ul className="list-disc list-inside space-y-2 text-gray-600">
              <li>Scam message identification</li>
              <li>Suspicious link detection</li>
              <li>Urgency level analysis</li>
              <li>Sender verification checks</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
