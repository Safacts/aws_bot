'use client';

import React, { useState, useEffect } from 'react';
import { 
    CheckCircle2, 
    XCircle, 
    ArrowRight, 
    RotateCcw, 
    Trophy,
    Target,
    Zap,
    Brain,
    HelpCircle,
    Layers,
    Filter
} from 'lucide-react';
import nptelData from '@/data/nptel_questions.json';

interface Question {
    cat: string;
    q: string;
    opts: string[];
    a: number;
    exp: string;
}

export default function EthicsQuiz() {
    const [batchIndex, setBatchIndex] = useState(0);
    const [questions, setQuestions] = useState<Question[]>([]);
    const [currentIndex, setCurrentIndex] = useState(0);
    const [selectedOption, setSelectedOption] = useState<number | null>(null);
    const [isAnswered, setIsAnswered] = useState(false);
    const [score, setScore] = useState(0);
    const [showResults, setShowResults] = useState(false);

    useEffect(() => {
        setQuestions(nptelData[batchIndex]);
        // Reset state when batch changes
        setCurrentIndex(0);
        setSelectedOption(null);
        setIsAnswered(false);
        setScore(0);
        setShowResults(false);
    }, [batchIndex]);

    const handleOptionSelect = (idx: number) => {
        if (isAnswered) return;
        setSelectedOption(idx);
    };

    const handleSubmit = () => {
        if (selectedOption === null) return;
        if (selectedOption === questions[currentIndex].a) setScore(prev => prev + 1);
        setIsAnswered(true);
    };

    const handleNext = () => {
        if (currentIndex < questions.length - 1) {
            setCurrentIndex(prev => prev + 1);
            setSelectedOption(null);
            setIsAnswered(false);
        } else {
            setShowResults(true);
        }
    };

    if (questions.length === 0) return <div className="p-20 text-center">Loading Ethics Module...</div>;

    if (showResults) {
        return (
            <div className="wide-wrap px-4 py-20 flex flex-col items-center">
                <div className="bg-[var(--surface)] border border-[var(--border)] rounded-[40px] p-12 max-w-2xl w-full text-center relative overflow-hidden backdrop-blur-2xl shadow-2xl">
                    <div className="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-transparent via-[var(--nptel)] to-transparent opacity-50" />
                    
                    <div className="w-24 h-24 bg-[var(--nptel2)]/20 rounded-full flex items-center justify-center mx-auto mb-8 animate-pulse">
                        <Trophy size={48} className="text-[var(--nptel)]" />
                    </div>

                    <h2 className="text-4xl font-bold text-white mb-2 font-sora">Ethics Assessment Clear!</h2>
                    <p className="text-[var(--text-dim)] mb-12">Solid understanding of Data Analytics foundations.</p>

                    <div className="grid grid-cols-2 gap-6 mb-12">
                        <div className="bg-[var(--surface-light)] p-6 rounded-3xl border border-[var(--border)]">
                            <p className="text-3xl font-bold text-[var(--nptel)]">{score}/{questions.length}</p>
                            <p className="text-xs text-[var(--text-dim)] uppercase tracking-wider mt-1">Score</p>
                        </div>
                        <div className="bg-[var(--surface-light)] p-6 rounded-3xl border border-[var(--border)]">
                            <p className="text-3xl font-bold text-white">{Math.round((score/questions.length)*100)}%</p>
                            <p className="text-xs text-[var(--text-dim)] uppercase tracking-wider mt-1">Accuracy</p>
                        </div>
                    </div>

                    <button 
                        onClick={() => {
                            setBatchIndex(0);
                            setShowResults(false);
                        }}
                        className="flex items-center justify-center gap-2 w-full bg-[var(--nptel)] text-white py-4 rounded-2xl font-semibold hover:brightness-110 transition-all shadow-lg shadow-[var(--nptel2)]/20"
                    >
                        <RotateCcw size={20} />
                        Retry This Module
                    </button>
                </div>
            </div>
        );
    }

    const q = questions[currentIndex];
    const progress = ((currentIndex + 1) / questions.length) * 100;

    return (
        <div className="wide-wrap px-4 py-12 lg:py-24">
            
            {/* Batch Selector */}
            <div className="flex flex-wrap items-center gap-3 mb-12 bg-[var(--surface-light)] p-2 rounded-2xl w-fit border border-[var(--border)]">
                <div className="px-4 py-2 text-xs font-bold text-[var(--text-dim)] uppercase tracking-widest flex items-center gap-2 border-r border-[var(--border)] mr-2">
                    <Filter size={14} />
                    Module
                </div>
                {nptelData.map((_, idx) => (
                    <button
                        key={idx}
                        onClick={() => setBatchIndex(idx)}
                        className={`
                            px-6 py-2 rounded-xl text-sm font-medium transition-all
                            ${batchIndex === idx 
                                ? 'bg-[var(--nptel)] text-white shadow-lg shadow-[var(--nptel2)]/20' 
                                : 'text-[var(--text-dim)] hover:text-white hover:bg-[var(--surface-hover)]'}
                        `}
                    >
                        Batch {idx + 1}
                    </button>
                ))}
            </div>

            <div className="grid lg:grid-cols-12 gap-12">
                {/* Left: Progress */}
                <div className="lg:col-span-4 flex flex-col gap-6">
                    <div className="bg-[var(--surface-light)] border border-[var(--border)] rounded-3xl p-8 backdrop-blur-xl">
                        <div className="flex items-center gap-4 mb-8">
                            <div className="w-12 h-12 bg-[var(--nptel2)]/20 rounded-2xl flex items-center justify-center text-[var(--nptel)]">
                                <Layers size={24} />
                            </div>
                            <div>
                                <p className="text-xs text-[var(--text-dim)] uppercase tracking-widest">NPTEL Course</p>
                                <p className="font-bold text-white font-sora">Data Analytics</p>
                            </div>
                        </div>

                        <div className="space-y-6">
                            <div>
                                <div className="flex justify-between items-end mb-2">
                                    <span className="text-xs text-[var(--text-dim)] uppercase font-mono">Progress</span>
                                    <span className="font-mono text-[var(--nptel)]">{currentIndex + 1} / {questions.length}</span>
                                </div>
                                <div className="h-2 bg-[var(--surface)] rounded-full border border-[var(--border)] overflow-hidden p-[2px]">
                                    <div 
                                        className="h-full bg-[var(--nptel)] rounded-full transition-all duration-500 ease-out"
                                        style={{ width: `${progress}%` }}
                                    />
                                </div>
                            </div>

                            <div className="grid grid-cols-2 gap-4">
                                <div className="bg-[var(--surface)] p-4 rounded-2xl border border-[var(--border)]">
                                    <p className="text-2xl font-bold text-white">{score}</p>
                                    <p className="text-[10px] text-[var(--text-dim)] uppercase tracking-widest font-mono">Solved</p>
                                </div>
                                <div className="bg-[var(--surface)] p-4 rounded-2xl border border-[var(--border)]">
                                    <p className="text-2xl font-bold text-white">{currentIndex + 1}</p>
                                    <p className="text-[10px] text-[var(--text-dim)] uppercase tracking-widest font-mono">Current</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                {/* Right: Question Card */}
                <div className="lg:col-span-8">
                    <div className="bg-[var(--surface)] border border-[var(--border)] rounded-[40px] p-8 md:p-12 shadow-2xl relative overflow-hidden">
                        <div className="absolute top-0 right-0 p-8 opacity-5">
                             <Layers size={120} />
                        </div>

                        <div className="flex items-center gap-2 text-[var(--nptel)] text-xs font-mono mb-6 uppercase tracking-widest relative z-10">
                            <Target size={14} />
                            <span>{q.cat}</span>
                        </div>

                        <h3 className="text-2xl md:text-3xl font-bold text-white mb-10 leading-tight font-sora relative z-10">
                            {q.q}
                        </h3>

                        <div className="space-y-4 mb-12 relative z-10">
                            {q.opts.map((opt, idx) => (
                                <button
                                    key={idx}
                                    onClick={() => handleOptionSelect(idx)}
                                    disabled={isAnswered}
                                    className={`
                                        w-full text-left p-6 rounded-2xl border transition-all flex items-center justify-between group
                                        ${isAnswered 
                                            ? idx === q.a 
                                                ? 'bg-green-500/10 border-green-500/50 text-green-400' 
                                                : idx === selectedOption 
                                                    ? 'bg-red-500/10 border-red-500/50 text-red-400' 
                                                    : 'bg-transparent border-[var(--border)] opacity-50'
                                            : selectedOption === idx 
                                                ? 'bg-[var(--nptel)] border-[var(--nptel)] text-white shadow-[0_0_20px_var(--nptel2)]/20' 
                                                : 'bg-[var(--surface-light)] border-[var(--border)] text-[var(--text-dim)] hover:border-[var(--nptel)]'
                                        }
                                    `}
                                >
                                    <span className="flex-1 font-medium">{opt}</span>
                                    <div className={`
                                        w-6 h-6 rounded-full border-2 flex items-center justify-center shrink-0
                                        ${selectedOption === idx ? 'bg-white border-white text-[var(--nptel)]' : 'border-[var(--border-strong)]'}
                                        ${isAnswered && idx === q.a ? 'bg-green-500 border-green-500 text-white' : ''}
                                    `}>
                                        {isAnswered && idx === q.a ? <CheckCircle2 size={16} /> : 
                                         isAnswered && idx === selectedOption && idx !== q.a ? <XCircle size={16} /> :
                                         <div className={`w-2 h-2 rounded-full ${selectedOption === idx ? 'bg-current' : 'bg-transparent'}`} />}
                                    </div>
                                </button>
                            ))}
                        </div>

                        {isAnswered && (
                            <div className="mb-12 animate-in fade-in slide-in-from-bottom-4 duration-500 relative z-10">
                                <div className="p-6 rounded-2xl border border-[var(--nptel)]/20 bg-[var(--nptel2)]/5">
                                    <p className="text-xs text-[var(--nptel)] uppercase tracking-widest font-bold mb-2 flex items-center gap-2">
                                        <HelpCircle size={14} />
                                        Sensei's Logic
                                    </p>
                                    <p className="text-[var(--text-dim)] italic leading-relaxed">
                                        {q.exp}
                                    </p>
                                </div>
                            </div>
                        )}

                        <div className="flex justify-end relative z-10">
                            {!isAnswered ? (
                                <button
                                    onClick={handleSubmit}
                                    disabled={selectedOption === null}
                                    className="px-10 py-5 bg-[var(--nptel)] text-white rounded-2xl font-bold text-lg disabled:opacity-50 disabled:grayscale transition-all hover:scale-[1.02] shadow-xl shadow-[var(--nptel2)]/20"
                                >
                                    Verify Knowledge
                                </button>
                            ) : (
                                <button
                                    onClick={handleNext}
                                    className="px-10 py-5 bg-white text-black rounded-2xl font-bold text-lg flex items-center gap-3 transition-all hover:scale-[1.02] shadow-xl"
                                >
                                    {currentIndex < questions.length - 1 ? 'Next' : 'Results'}
                                    <ArrowRight size={20} />
                                </button>
                            )}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}
