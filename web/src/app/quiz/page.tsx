import QuizEngine from '@/components/QuizEngine';

export default function QuizPage() {
    return (
        <main className="min-h-screen pt-24 pb-12">
            <div className="wide-wrap px-4 mb-12">
                <h1 className="text-4xl md:text-5xl font-bold text-white mb-4 font-sora">AWS Practice Exam</h1>
                <p className="text-[var(--text-dim)] max-w-2xl">
                    Test your knowledge with 188 exam-accurate questions. 
                    Target 700+ to ensure readiness for the CLF-C02 certification.
                </p>
            </div>
            <QuizEngine />
        </main>
    );
}
