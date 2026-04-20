"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const navLinks = [
  { name: "Overview", href: "/" },
  { name: "Study Center", href: "/study" },
  { name: "Practice Quiz", href: "/quiz" },
  { name: "Micro-Notes", href: "/notes" },
  { name: "Mission Strategy", href: "/strategy" },
  { name: "NPTEL Ethics", href: "/ethics" },
];

export default function Navbar() {
  const pathname = usePathname();

  return (
    <nav className="sticky top-0 z-50 bg-[rgba(10,10,15,0.92)] backdrop-blur-xl border-b border-[var(--border)] px-6 flex items-center h-16">
      <div className="nav-logo text-[13px] font-semibold text-[var(--text2)] tracking-widest uppercase mr-8 shrink-0">
        AWS <span>HUB</span>
      </div>

      <div className="flex gap-1 flex-1 overflow-x-auto no-scrollbar mask-fade-right scroll-smooth">
        {navLinks.map((link) => {
          const isActive = pathname === link.href;
          const isEthics = link.name.includes("NPTEL");

          return (
            <Link
              key={link.href}
              href={link.href}
              className={`
                flex items-center gap-2 px-5 py-4 text-[13px] font-medium transition-all whitespace-nowrap border-b-2
                ${isActive 
                  ? (isEthics ? "text-[var(--text)] border-[var(--nptel)]" : "text-[var(--text)] border-[var(--aws)]")
                  : "text-[var(--text3)] border-transparent hover:text-[var(--text2)]"}
              `}
            >
              {isActive && (
                <span className={`w-1.5 h-1.5 rounded-full ${isEthics ? "bg-[var(--nptel)]" : "bg-[var(--aws)]"} opacity-60`} />
              )}
              {link.name}
            </Link>
          );
        })}
      </div>
    </nav>
  );
}
