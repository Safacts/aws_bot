import NotesView from '@/components/NotesView';
import { Target } from 'lucide-react';

export default function NotesPage() {
    return (
        <main className="min-h-screen pt-24 pb-12">
            <div className="wide-wrap px-4 mb-12">
                <div className="flex items-center gap-2 text-[var(--accent)] text-sm mb-4">
                    <Target size={14} />
                    <span className="uppercase tracking-widest font-mono">Reference Vault</span>
                </div>
                <h1 className="text-4xl md:text-5xl font-bold text-white mb-4 font-sora">AWS Micro-Notes</h1>
                <p className="text-[var(--text-dim)] max-w-2xl text-lg">
                    Distilled summaries of core AWS concepts. Use these for quick revision 
                    and to clarify commonly confused services before the exam.
                </p>
            </div>
            <NotesView />
        </main>
    );
}
