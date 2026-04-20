import { 
    Zap, 
    Divide, 
    Clock, 
    ArrowRight,
    Search,
    Brain,
    Target
} from 'lucide-react';

export default function StrategyPage() {
    return (
        <main className="min-h-screen pt-24 pb-24">
            <div className="wide-wrap px-4">
                <div className="mb-16">
                    <div className="flex items-center gap-2 text-[var(--accent)] text-sm mb-4">
                        <Zap size={14} />
                        <span className="uppercase tracking-widest font-mono">Mission Control</span>
                    </div>
                    <h1 className="text-4xl md:text-5xl font-bold text-white mb-4 font-sora">Exam Strategy</h1>
                    <p className="text-[var(--text-dim)] max-w-2xl text-lg">
                        The CLF-C02 is a test of pattern recognition. Master these mental buckets 
                        and elimination rules to guarantee a passing score.
                    </p>
                </div>

                <div className="grid lg:grid-cols-3 gap-8">
                    
                    {/* Bucket 1: Keywords */}
                    <StrategyCard 
                        icon={<Search className="text-[var(--accent)]" />}
                        title="Keyword Mapping" 
                        num="01"
                        desc="When you see these words, look for these answers."
                    >
                        <div className="space-y-3 mt-6">
                            <KeywordPair w="Cost-effective" a="Spot / S3-IA / Reserved" />
                            <KeywordPair w="Serverless" a="Lambda / Fargate / DynamoDB" />
                            <KeywordPair w="High Availability" a="Multi-AZ / Auto Scaling" />
                            <KeywordPair w="Real-time" a="Kinesis / Lambda" />
                            <KeywordPair w="DDoS protection" a="Shield Standard (FREE)" />
                            <KeywordPair w="Audit / Who did what" a="CloudTrail" />
                            <KeywordPair w="Least overhead" a="Managed / Serverless" />
                            <KeywordPair w="Petabyte move" a="Snowball / Snowmobile" />
                        </div>
                    </StrategyCard>

                    {/* Bucket 2: Elimination */}
                    <StrategyCard 
                        icon={<Divide className="text-[var(--info)]" />}
                        title="Elimination Rules" 
                        num="02"
                        desc="Instantly remove wrong choices with these rules."
                    >
                        <ul className="space-y-4 mt-6">
                            <RuleItem text="If 'No server management' → Eliminate EC2" />
                            <RuleItem text="If 'Relational DB' → Eliminate DynamoDB" />
                            <RuleItem text="If 'Physical move' → Eliminate DataSync" />
                            <RuleItem text="If '15-min response' → Pick Enterprise plan" />
                            <RuleItem text="If 'SQL / Transact' → It's RDS or Aurora" />
                            <RuleItem text="Watch for 'NOT' or 'EXCEPT' in bold" />
                        </ul>
                    </StrategyCard>

                    {/* Bucket 3: Time Management */}
                    <StrategyCard 
                        icon={<Clock className="text-[var(--correct)]" />}
                        title="Time Management" 
                        num="03"
                        desc="90 minutes, 65 questions. Pace yourself."
                    >
                        <div className="space-y-6 mt-6">
                            <div className="bg-[var(--surface-hover)] p-4 rounded-2xl border border-[var(--border)]">
                                <p className="text-2xl font-bold text-white font-mono">1.4 min</p>
                                <p className="text-[10px] text-[var(--text-dim)] uppercase tracking-widest">Per Question Target</p>
                            </div>
                            <ul className="space-y-3 text-sm text-[var(--text-dim)]">
                                <li className="flex gap-2"><span>•</span> Flag & Skip if unsure instantly</li>
                                <li className="flex gap-2"><span>•</span> 15 Qs are unscored — don't panic</li>
                                <li className="flex gap-2"><span>•</span> No penalty — ALWAYS GUESS</li>
                                <li className="flex gap-2"><span>•</span> Review flagged items at the end</li>
                            </ul>
                        </div>
                    </StrategyCard>

                </div>

                {/* Final Mentor Quote */}
                <div className="mt-20 p-12 rounded-[40px] bg-gradient-to-br from-[var(--bg2)] to-transparent border border-[var(--border)] text-center relative overflow-hidden">
                    <div className="absolute top-0 left-0 w-full h-full opacity-10 pointer-events-none">
                        <Brain size={400} className="absolute -bottom-20 -right-20 text-[var(--accent)]" />
                    </div>
                    <div className="relative z-10">
                        <p className="text-2xl md:text-3xl text-white font-medium mb-6 italic">
                            "You've trained for this, Jeevitha. Trust the pattern, trust your intuition."
                        </p>
                        <p className="text-[var(--accent)] font-bold tracking-widest uppercase text-sm">
                            — AWS Sensei
                        </p>
                    </div>
                </div>

            </div>
        </main>
    );
}

function StrategyCard({ icon, title, num, desc, children }: { icon: React.ReactNode, title: string, num: string, desc: string, children: React.ReactNode }) {
    return (
        <div className="bg-[var(--surface)] border border-[var(--border)] rounded-[32px] p-8 relative group hover:border-[var(--border2)] transition-all">
            <div className="absolute top-8 right-8 text-4xl font-black text-white/5 font-mono select-none">
                {num}
            </div>
            <div className="w-12 h-12 rounded-2xl bg-[var(--surface-light)] flex items-center justify-center mb-6 border border-[var(--border)] shadow-inner">
                {icon}
            </div>
            <h3 className="text-xl font-bold text-white mb-2 font-sora">{title}</h3>
            <p className="text-xs text-[var(--text-dim)] leading-relaxed mb-6">
                {desc}
            </p>
            <div className="border-t border-[var(--border)] pt-6">
                {children}
            </div>
        </div>
    );
}

function KeywordPair({ w, a }: { w: string, a: string }) {
    return (
        <div className="flex flex-col gap-1 p-3 rounded-xl bg-[var(--surface-light)] border border-[var(--border)]">
            <span className="text-[10px] uppercase tracking-widest font-bold text-[var(--text-dim)]">{w}</span>
            <div className="flex items-center gap-2">
                <ArrowRight size={12} className="text-[var(--accent)]" />
                <span className="text-sm font-medium text-white">{a}</span>
            </div>
        </div>
    );
}

function RuleItem({ text }: { text: string }) {
    return (
        <div className="flex items-start gap-3">
            <div className="mt-1 shrink-0"><Target size={14} className="text-[var(--info)]" /></div>
            <p className="text-sm text-[var(--text-dim)]">{text}</p>
        </div>
    );
}
