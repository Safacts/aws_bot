'use client';

import React, { useState, useEffect, useRef } from 'react';
import { marked } from 'marked';
import DOMPurify from 'dompurify';
import { 
    BookOpen, 
    Search, 
    ChevronRight, 
    ListCircle, 
    ArrowUp,
    Hash,
    Menu,
    X,
    Layout,
    Clock
} from 'lucide-react';

interface Guide {
    id: string;
    title: string;
    content: string;
}

export default function StudyView({ initialGuides }: { initialGuides: Guide[] }) {
    const [activeGuide, setActiveGuide] = useState<Guide>(initialGuides[0]);
    const [toc, setToc] = useState<{ id: string; text: string; level: number }[]>([]);
    const [isSidebarOpen, setIsSidebarOpen] = useState(false);
    const [activeSection, setActiveSection] = useState('');
    const contentRef = useRef<HTMLDivElement>(null);

    // Generate Table of Contents from content
    useEffect(() => {
        const tokens = marked.lexer(activeGuide.content);
        const headers = tokens.filter(t => t.type === 'heading') as any[];
        
        const tocItems = headers.map(h => ({
            id: h.text.toLowerCase().replace(/[^\w]+/g, '-'),
            text: h.text,
            level: h.depth
        }));
        
        setToc(tocItems);
        
        // Custom renderer for ID generation
        const renderer = new marked.Renderer();
        renderer.heading = ({ text, depth }) => {
            const id = text.toLowerCase().replace(/[^\w]+/g, '-');
            return `<h${depth} id="${id}" class="section-heading">${text}</h${depth}>`;
        };
        
        const rawHtml = marked(activeGuide.content, { renderer }) as string;
        if (contentRef.current) {
            contentRef.current.innerHTML = DOMPurify.sanitize(rawHtml);
        }
    }, [activeGuide]);

    // Active Section Tracking
    useEffect(() => {
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        setActiveSection(entry.target.id);
                    }
                });
            },
            { rootMargin: '-10% 0px -80% 0px' }
        );

        const headings = document.querySelectorAll('.section-heading');
        headings.forEach((h) => observer.observe(h));

        return () => observer.disconnect();
    }, [activeGuide]);

    const scrollToSection = (id: string) => {
        const element = document.getElementById(id);
        if (element) {
            const offset = 100;
            const elementPosition = element.getBoundingClientRect().top;
            const offsetPosition = elementPosition + window.pageYOffset - offset;

            window.scrollTo({
                top: offsetPosition,
                behavior: 'smooth'
            });
            setActiveSection(id);
        }
    };

    return (
        <div className="wide-wrap px-4 sm:px-6">
            <div className="flex flex-col lg:flex-row gap-8 relative">
                
                {/* Mobile Toggle */}
                <button 
                    onClick={() => setIsSidebarOpen(!isSidebarOpen)}
                    className="lg:hidden fixed bottom-6 right-6 z-50 bg-[var(--accent)] text-white p-4 rounded-full shadow-lg"
                >
                    {isSidebarOpen ? <X /> : <Layout />}
                </button>

                {/* Sidebar - Guide Selection */}
                <aside className={`
                    fixed lg:sticky top-24 z-40 lg:z-auto h-[80vh] w-[280px]
                    transition-transform duration-300 transform 
                    ${isSidebarOpen ? 'translate-x-0' : '-translate-x-[110%] lg:translate-x-0'}
                    bg-[var(--surface-light)] backdrop-blur-xl border border-[var(--border)] rounded-2xl p-6
                    flex flex-col gap-6
                `}>
                    <div className="flex items-center gap-3 text-[var(--accent)] font-semibold border-b border-[var(--border)] pb-4">
                        <BookOpen size={20} />
                        <span>Library Index</span>
                    </div>
                    
                    <div className="flex flex-col gap-2 overflow-y-auto custom-scrollbar">
                        {initialGuides.map(guide => (
                            <button
                                key={guide.id}
                                onClick={() => {
                                    setActiveGuide(guide);
                                    setIsSidebarOpen(false);
                                    window.scrollTo({ top: 0, behavior: 'smooth' });
                                }}
                                className={`
                                    text-left px-4 py-3 rounded-xl transition-all flex items-center justify-between group
                                    ${activeGuide.id === guide.id 
                                        ? 'bg-[var(--accent)] text-white' 
                                        : 'hover:bg-[var(--surface-hover)] text-[var(--text-dim)]'}
                                `}
                            >
                                <span className="truncate text-sm font-medium">{guide.title}</span>
                                <ChevronRight size={16} className={`transition-transform ${activeGuide.id === guide.id ? 'translate-x-1' : 'group-hover:translate-x-1'}`} />
                            </button>
                        ))}
                    </div>

                    <div className="mt-auto pt-4 border-t border-[var(--border)]">
                        <div className="bg-[var(--surface-hover)] rounded-xl p-4 flex items-center gap-3">
                            <Clock size={16} className="text-[var(--accent)]" />
                            <div className="text-xs">
                                <p className="text-[var(--text-dim)]">Last Study</p>
                                <p className="font-medium text-[var(--text-main)]">Today, 2:45 PM</p>
                            </div>
                        </div>
                    </div>
                </aside>

                {/* Content Area */}
                <div className="flex-1 min-w-0">
                    <div className="mb-8 bg-gradient-to-r from-[var(--surface)] to-transparent p-8 rounded-3xl border border-[var(--border)]">
                        <div className="flex items-center gap-2 text-[var(--accent)] text-sm mb-4">
                            <BookOpen size={14} />
                            <span className="uppercase tracking-widest font-mono">AWS Digital Library</span>
                            <ChevronRight size={14} />
                            <span>{activeGuide.title}</span>
                        </div>
                        <h1 className="text-4xl md:text-5xl font-bold text-white mb-4 line-height-tight">
                            {activeGuide.title}
                        </h1>
                        <p className="text-[var(--text-dim)] max-w-2xl">
                            Master the core concepts of AWS with curated, exam-aligned documentation. 
                            Use the sidebar to navigate topics or the index to jump sections.
                        </p>
                    </div>

                    <div 
                        ref={contentRef}
                        className="prose-deep-space markdown-content mb-24"
                    />
                </div>

                {/* Table of Contents - Right Sidebar */}
                <aside className="hidden xl:block sticky top-24 h-fit w-[240px] shrink-0">
                    <div className="flex items-center gap-2 text-[var(--text-dim)] text-xs font-mono mb-4 uppercase tracking-widest px-4">
                        <Hash size={12} />
                        <span>In this guide</span>
                    </div>
                    <nav className="flex flex-col gap-1">
                        {toc.map((item, idx) => (
                            <button
                                key={idx}
                                onClick={() => scrollToSection(item.id)}
                                className={`
                                    text-left px-4 py-2 rounded-lg text-sm transition-all border-l-2
                                    ${activeSection === item.id 
                                        ? 'border-[var(--accent)] text-[var(--accent)] bg-[var(--accent-dim)]' 
                                        : 'border-transparent text-[var(--text-dim)] hover:text-white hover:bg-[var(--surface-hover)]'}
                                    ${item.level > 2 ? 'ml-4' : ''}
                                `}
                            >
                                {item.text}
                            </button>
                        ))}
                    </nav>

                    <button 
                        onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
                        className="mt-8 mx-auto w-full flex items-center justify-center gap-2 py-3 rounded-xl border border-[var(--border)] text-[var(--text-dim)] hover:text-white hover:border-[var(--accent)] transition-all group"
                    >
                        <ArrowUp size={16} className="group-hover:-translate-y-1 transition-transform" />
                        <span className="text-xs font-mono uppercase">Back to Top</span>
                    </button>
                </aside>
            </div>
        </div>
    );
}
