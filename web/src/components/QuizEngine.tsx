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
    HelpCircle
} from 'lucide-react';
import questionsData from '@/data/questions.json';
import { createClient } from '@/utils/supabase/client';

interface Question {
    domain: string;
    q: string;
    opts: string[];
    a: number;
    exp: string;
}

export default function QuizEngine() {
    const [questions, setQuestions] = useState<Question[]>([]);
    const [currentIndex, setCurrentIndex] = useState(0);
    const [selectedOption, setSelectedOption] = useState<number | null>(null);
    const [isAnswered, setIsAnswered] = useState(false);
    const [score, setScore] = useState(0);
    const [showResults, setShowResults] = useState(false);
    const [history, setHistory] = useState<{question: number, correct: boolean}[]>([]);
    const [syncing, setSyncing] = useState(false);

    const supabase = createClient();

    useEffect(() => {
        // Shuffle questions or just load
        setQuestions(questionsData.slice(0, 50)); // Start with first 50
    }, []);

    const handleOptionSelect = (idx: number) => {
        if (isAnswered) return;
        setSelectedOption(idx);
    };

    const handleSubmit = () => {
        if (selectedOption === null) return;
        
        const isCorrect = selectedOption === questions[currentIndex].a;
        if (isCorrect) setScore(prev => prev + 1);
        
        setHistory(prev => [...prev, { question: currentIndex, correct: isCorrect }]);
        setIsAnswered(true);
    };

    const handleNext = async () => {
        if (currentIndex < questions.length - 1) {
            setCurrentIndex(prev => prev + 1);
            setSelectedOption(null);
            setIsAnswered(false);
        } else {
            setShowResults(true);
            await saveProgress();
        }
    };

    const saveProgress = async () => {
        setSyncing(true);
        try {
            const { error } = await supabase
                .from('quiz_progress')
                .insert([
                    { 
                        score: score, 
                        total: questions.length, 
                        accuracy: Math.round((score/questions.length)*100),
                        completed_at: new Date().toISOString()
                    }
                ]);
            if (error) console.error('Sync Error:', error);
        } catch (e) {
            console.error('Connection failed:', e);
        } finally {
            setSyncing(false);
        }
    };

    const restart = () => {
        setCurrentIndex(0);
        setSelectedOption(null);
        setIsAnswered(false);
        setScore(0);
        setShowResults(false);
        setHistory([]);
    };

    if (questions.length === 0) return <div className="p-20 text-center">Initializing Knowledge Base...</div>;

    if (showResults) {
        return (
            <div className="wide-wrap px-4 py-20 flex flex-col items-center">
                <div className="bg-[var(--surface)] border border-[var(--border)] rounded-[40px] p-12 max-w-2xl w-full text-center relative overflow-hidden backdrop-blur-2xl">
                    <div className="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-transparent via-[var(--accent)] to-transparent opacity-50" />
                    
                    <div className="w-24 h-24 bg-[var(--accent-dim)] rounded-full flex items-center justify-center mx-auto mb-8 animate-bounce">
                        <Trophy size={48} className="text-[var(--accent)]" />
                    </div>

                    <h2 className="text-4xl font-bold text-white mb-2 font-sora">Quiz Completed!</h2>
                    <p className="text-[var(--text-dim)] mb-12">Great job, Jeevitha. Here's how you performed:</p>

                    <div className="grid grid-cols-2 gap-6 mb-12">
                        <div className="bg-[var(--surface-light)] p-6 rounded-3xl border border-[var(--border)]">
                            <p className="text-3xl font-bold text-[var(--accent)]">{score}/{questions.length}</p>
                            <p className="text-xs text-[var(--text-dim)] uppercase tracking-wider mt-1">Final Score</p>
                        </div>
                        <div className="bg-[var(--surface-light)] p-6 rounded-3xl border border-[var(--border)]">
                            <p className="text-3xl font-bold text-white">{Math.round((score/questions.length)*100)}%</p>
                            <p className="text-xs text-[var(--text-dim)] uppercase tracking-wider mt-1">Accuracy</p>
                        </div>
                    </div>

                    <button 
                        onClick={restart}
                        className="flex items-center justify-center gap-2 w-full bg-[var(--accent)] text-white py-4 rounded-2xl font-semibold hover:brightness-110 transition-all shadow-lg shadow-[var(--accent-dim)]"
                    >
                        <RotateCcw size={20} />
                        Retry Knowledge Check
                    </button>
                </div>
            </div>
        );
    }

    const q = questions[currentIndex];
    const progress = ((currentIndex + 1) / questions.length) * 100;

    return (
        <div className="wide-wrap px-4 py-12 lg:py-24 grid lg:grid-cols-12 gap-12">
            
            {/* Left: Progress & Stats */}
            <div className="lg:col-span-4 flex flex-col gap-6">
                <div className="bg-[var(--surface-light)] border border-[var(--border)] rounded-3xl p-8 backdrop-blur-xl">
                    <div className="flex items-center gap-4 mb-8">
                        <div className="w-12 h-12 bg-[var(--accent-dim)] rounded-2xl flex items-center justify-center text-[var(--accent)]">
                            <Brain size={24} />
                        </div>
                        <div>
                            <p className="text-xs text-[var(--text-dim)] uppercase tracking-widest">Active Session</p>
                            <p className="font-bold text-white font-sora">AWS Cloud Practitioner</p>
                        </div>
                    </div>

                    <div className="space-y-6">
                        <div>
                            <div className="flex justify-between items-end mb-2">
                                <span className="text-xs text-[var(--text-dim)] uppercase font-mono">Progress</span>
                                <span className="font-mono text-[var(--accent)]">{currentIndex + 1} / {questions.length}</span>
                            </div>
                            <div className="h-2 bg-[var(--surface)] rounded-full border border-[var(--border)] overflow-hidden p-[2px]">
                                <div 
                                    className="h-full bg-[var(--accent)] rounded-full transition-all duration-500 ease-out shadow-[0_0_10px_var(--accent)]"
                                    style={{ width: `${progress}%` }}
                                />
                            </div>
                        </div>

                        <div className="grid grid-cols-2 gap-4">
                            <div className="bg-[var(--surface)] p-4 rounded-2xl border border-[var(--border)]">
                                <p className="text-2xl font-bold text-white">{score}</p>
                                <p className="text-[10px] text-[var(--text-dim)] uppercase tracking-widest font-mono">Correct</p>
                            </div>
                            <div className="bg-[var(--surface)] p-4 rounded-2xl border border-[var(--border)]">
                                <p className="text-2xl font-bold text-white">{currentIndex - score + (isAnswered && selectedOption !== q.a ? 1 : 0)}</p>
                                <p className="text-[10px] text-[var(--text-dim)] uppercase tracking-widest font-mono">Missed</p>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="bg-gradient-to-br from-[var(--accent-dim)] to-transparent border border-[var(--accent-dim)] rounded-3xl p-8">
                    <h4 className="text-white font-semibold mb-2 flex items-center gap-2">
                        <Zap size={16} className="text-[var(--accent)]" />
                        Quick Hint
                    </h4>
                    <p className="text-sm text-[var(--text-dim)] leading-relaxed italic">
                        "Focus on the 'Shared Responsibility Model'. It's usually the most tested domain. You've got this, Jeevitha!" — AWS Sensei
                    </p>
                </div>
            </div>

            {/* Right: Question Card */}
            <div className="lg:col-span-8">
                <div className="bg-[var(--surface)] border border-[var(--border)] rounded-[40px] p-8 md:p-12 shadow-2xl relative">
                    <div className="flex items-center gap-2 text-[var(--accent)] text-xs font-mono mb-6 uppercase tracking-widest">
                        <Target size={14} />
                        <span>{q.domain}</span>
                    </div>

                    <h3 className="text-2xl md:text-3xl font-bold text-white mb-10 leading-tight font-sora">
                        {q.q}
                    </h3>

                    <div className="space-y-4 mb-12">
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
                                            ? 'bg-[var(--accent)] border-[var(--accent)] text-white shadow-[0_0_20px_var(--accent-dim)]' 
                                            : 'bg-[var(--surface-light)] border-[var(--border)] text-[var(--text-dim)] hover:border-[var(--accent)]'
                                    }
                                `}
                            >
                                <span className="flex-1 font-medium">{opt}</span>
                                <div className={`
                                    w-6 h-6 rounded-full border-2 flex items-center justify-center shrink-0
                                    ${selectedOption === idx ? 'bg-white border-white text-[var(--accent)]' : 'border-[var(--border-strong)]'}
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
                        <div className="mb-12 animate-in fade-in slide-in-from-bottom-4 duration-500">
                            <div className={`p-6 rounded-2xl border ${selectedOption === q.a ? 'bg-green-500/5 border-green-500/20' : 'bg-blue-500/5 border-blue-500/20'}`}>
                                <p className="text-xs uppercase tracking-widest font-bold mb-2 flex items-center gap-2">
                                    <HelpCircle size={14} />
                                    Explanation
                                </p>
                                <p className="text-[var(--text-dim)] italic leading-relaxed">
                                    {q.exp}
                                </p>
                            </div>
                        </div>
                    )}

                    <div className="flex justify-end">
                        {!isAnswered ? (
                            <button
                                onClick={handleSubmit}
                                disabled={selectedOption === null}
                                className="px-10 py-5 bg-[var(--accent)] text-white rounded-2xl font-bold text-lg disabled:opacity-50 disabled:grayscale transition-all hover:scale-[1.02] shadow-xl shadow-[var(--accent-dim)]"
                            >
                                Submit Answer
                            </button>
                        ) : (
                            <button
                                onClick={handleNext}
                                className="px-10 py-5 bg-white text-black rounded-2xl font-bold text-lg flex items-center gap-3 transition-all hover:scale-[1.02] shadow-xl"
                            >
                                {currentIndex < questions.length - 1 ? 'Next Question' : 'View Results'}
                                <ArrowRight size={20} />
                            </button>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}
