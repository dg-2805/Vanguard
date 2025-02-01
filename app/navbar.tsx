// components/Navbar.tsx
"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const Navbar = () => {
  const pathname = usePathname();

  return (
    <nav className="w-full bg-gradient-to-r from-blue-400 via-blue-600 to-blue-800 px-4 py-4 shadow-lg">
      <div className="mx-auto flex max-w-6xl items-center justify-center">
        {" "}
        {/* Changed justify-between to justify-center */}
        <div className="flex space-x-4">
          <Link
            href="/"
            className={`rounded-md px-4 py-2 text-base font-medium text-white transition-colors duration-200 hover:text-blue-200 ${
              pathname === "/" ? "text-blue-300" : ""
            }`}
          >
            Home
          </Link>
          <Link
            href="/email-detection"
            className={`rounded-md px-4 py-2 text-base font-medium text-white transition-colors duration-200 hover:text-blue-200 ${
              pathname === "/email-detection" ? "text-blue-300" : ""
            }`}
          >
            Email Detection
          </Link>
          <Link
            href="/sms-detection"
            className={`rounded-md px-4 py-2 text-base font-medium text-white transition-colors duration-200 hover:text-blue-200 ${
              pathname === "/sms-detection" ? "text-blue-300" : ""
            }`}
          >
            SMS Detection
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
