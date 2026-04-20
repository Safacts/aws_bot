import EthicsQuiz from '@/components/EthicsQuiz';
import { BookOpen } from 'lucide-react';

export default function EthicsPage() {
    return (
        <main className="min-h-screen pt-24 pb-12">
            <div className="wide-wrap px-4 mb-12">
                <div className="flex items-center gap-2 text-[var(--nptel)] text-sm mb-4">
                    <BookOpen size={14} />
                    <span className="uppercase tracking-widest font-mono">NPTEL Course Material</span>
                </div>
                <h1 className="text-4xl md:text-5xl font-bold text-white mb-4 font-sora">Data Analytics Foundations</h1>
                <p className="text-[var(--text-dim)] max-w-2xl text-lg">
                    Comprehensive practice for the NPTEL Data Analytics modules. 
                    Focus on statistical foundations and ethical data processing.
                </p>
            </div>
            <EthicsQuiz />
        </main>
    );
}
