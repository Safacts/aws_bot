import type { Metadata } from "next";
import { Sora, JetBrains_Mono } from "next/font/google";
import "./globals.css";

const sora = Sora({
  variable: "--font-sora",
  subsets: ["latin"],
});

const jetbrainsMono = JetBrains_Mono({
  variable: "--font-jetbrains-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "AWS Hub - Jeevitha's Study Center",
  description: "A professional, adaptive study platform for AWS Cloud Practitioner certification.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${sora.variable} ${jetbrainsMono.variable} antialiased`}>
      <body className="bg-[var(--bg)] text-[var(--text)] font-sans min-h-screen">
        <div className="noise-overlay" />
        {children}
      </body>
    </html>
  );
}
