// app/page.tsx
export default function Home() {
  return (
    <div className="min-h-screen bg-blue-50">
      <div className="container mx-auto px-4 py-12">
        <div className="max-w-4xl mx-auto text-center">
          <h1 className="text-4xl md:text-6xl font-bold mb-8 bg-gradient-to-r from-blue-600 to-blue-800 bg-clip-text text-transparent pb-4">
            Phishing Detection Platform
          </h1>

          <p className="text-lg md:text-xl text-gray-700 mb-12">
            Protect yourself from malicious content with our advanced detection
            system. Quickly verify whether emails or SMS messages are legitimate
            or potential threats.
          </p>

          <div className="grid md:grid-cols-2 gap-8 mb-16">
            <div className="bg-white p-8 rounded-xl shadow-lg border border-blue-100">
              <h2 className="text-2xl font-bold text-blue-800 mb-4">
                Email Detection
              </h2>
              <p className="text-gray-600 mb-4">
                Analyze email content for phishing attempts, suspicious links,
                and malicious attachments using advanced AI algorithms.
              </p>
              <ul className="text-left list-disc list-inside text-gray-600 space-y-2">
                <li>Detect spoofed sender addresses</li>
                <li>Identify malicious links</li>
                <li>Analyze content patterns</li>
              </ul>
            </div>

            <div className="bg-white p-8 rounded-xl shadow-lg border border-blue-100">
              <h2 className="text-2xl font-bold text-blue-800 mb-4">
                SMS Detection
              </h2>
              <p className="text-gray-600 mb-4">
                Verify SMS messages for scam attempts, fake promotions, and
                suspicious content with real-time analysis.
              </p>
              <ul className="text-left list-disc list-inside text-gray-600 space-y-2">
                <li>Detect fake verification codes</li>
                <li>Identify phishing attempts</li>
                <li>Analyze URL safety</li>
              </ul>
            </div>
          </div>

          <div className="bg-white p-8 rounded-xl shadow-lg border border-blue-100 max-w-2xl mx-auto">
            <h3 className="text-xl font-semibold text-blue-800 mb-4">
              How It Works
            </h3>
            <div className="flex flex-col md:flex-row justify-between items-center gap-6">
              <div className="flex-1">
                <p className="text-gray-600">
                  1. Paste your email/SMS content
                  <br />
                  2. Our AI analyzes the text
                  <br />
                  3. Get instant security assessment
                </p>
              </div>
              <a
                href="/email-detection"
                className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 rounded-lg transition-colors duration-200"
              >
                Try Now
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
