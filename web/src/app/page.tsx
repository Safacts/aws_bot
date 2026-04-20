import Link from "next/link";
import Navbar from "@/components/Navbar";
import { createClient } from "@/utils/supabase/server";
import { cookies } from "next/headers";

export default async function Home() {
  const cookieStore = await cookies();
  const supabase = createClient(cookieStore);
  
  // Try to get latest quiz attempt for accuracy
  const { data: latestAttempt } = await supabase
    .from('quiz_progress')
    .select('accuracy')
    .order('completed_at', { ascending: false })
    .limit(1)
    .maybeSingle();

  const stats = [
    { label: "Total Questions", value: "188", sub: "Full bot question bank" },
    { label: "Study Material", value: "5", sub: "Detailed AWS Guides" },
    { label: "Avg Accuracy", value: latestAttempt ? `${latestAttempt.accuracy}%` : "0%", sub: latestAttempt ? "Based on latest check" : "Take a quiz to start" },
    { label: "Exam Readiness", value: latestAttempt && latestAttempt.accuracy >= 70 ? "Ready" : "Studying", sub: "Goal: 70% Accuracy" },
  ];

const domains = [
  { name: "Cloud Concepts", pct: "24%", desc: "6 advantages, deployment models, Well-Architected Framework", accent: "#ff9900" },
  { name: "Security & Compliance", pct: "30%", desc: "Shared Responsibility, IAM, Shield, WAF, GuardDuty", accent: "#3b82f6" },
  { name: "Technology & Services", pct: "34%", desc: "EC2, S3, RDS, Lambda, CloudFront, VPC and more", accent: "#22c55e" },
  { name: "Billing & Support", pct: "12%", desc: "Free Tier, Cost Explorer, Support Plans, TCO", accent: "#a855f7" },
];

const keywordCards = [
  {
    title: "Cost & Pricing keywords",
    icon: "$",
    tags: ["cost-effective", "save money", "lowest cost", "reserved", "spot", "glacier", "CapEx → OpEx"],
    color: "cost",
  },
  {
    title: "Security keywords",
    icon: "🔒",
    tags: ["DDoS", "web attacks", "threat detection", "sensitive data", "encryption keys", "audit trail", "compliance"],
    color: "secure",
  },
  {
    title: "Serverless keywords",
    icon: "λ",
    tags: ["no server management", "least overhead", "event-driven", "auto scale", "pay per use", "containers no EC2"],
    color: "server",
  },
];

  return (
    <main className="min-h-screen">
      <Navbar />
      
      {/* HERO SECTION */}
      <section className="px-6 py-16 md:py-24 max-w-[900px] mx-auto text-left relative z-10">
        <div className="text-[11px] font-semibold tracking-[0.15em] uppercase text-[var(--aws)] mb-4">
          Personal Study Hub
        </div>
        <h1 className="text-4xl md:text-6xl font-light leading-[1.15] text-[var(--text)] mb-4">
          Empowering <strong className="font-semibold text-[var(--text)]">Jeevitha</strong><br />
          for AWS Certification
        </h1>
        <p className="text-base text-[var(--text2)] max-w-[560px] mb-9 leading-relaxed">
          Your comprehensive mission control for AWS Cloud Practitioner (CLF-C02). 
          Read, practice, and conquer.
        </p>
        <div className="inline-flex items-center gap-2.5 bg-[var(--card)] border border-[var(--border2)] rounded-full px-4.5 py-2.5 text-[13px] text-[var(--text2)]">
          <div className="w-2 h-2 rounded-full bg-[var(--correct)] shadow-[0_0_0_3px_rgba(34,197,94,0.15)]" />
          CLF-C02 · 188 Practice Questions · 5 Study Guides
        </div>
      </section>

      {/* STAT GRID */}
      <section className="grid grid-cols-2 md:grid-cols-4 gap-3 max-w-[900px] mx-auto px-6 mb-12 relative z-10">
        {stats.map((stat) => (
          <div key={stat.label} className="premium-card p-5">
            <div className="text-[11px] font-semibold uppercase tracking-wider text-[var(--text3)] mb-2">
              {stat.label}
            </div>
            <div className="text-[26px] font-semibold text-[var(--text)] font-mono">
              {stat.value}
            </div>
            <div className="text-[12px] text-[var(--text3)] mt-1">
              {stat.sub}
            </div>
          </div>
        ))}
      </section>

      {/* DOMAINS SECTION */}
      <section className="max-w-[900px] mx-auto px-6 mb-12 relative z-10">
        <div className="text-[12px] font-semibold tracking-widest uppercase text-[var(--text3)] mb-4">
          Domains at a glance
        </div>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
          {domains.map((domain) => (
            <Link 
              key={domain.name} 
              href="/quiz"
              className="premium-card p-5 group relative overflow-hidden block no-underline"
              style={{ "--accent": domain.accent } as any}
            >
              <div className="absolute top-0 inset-x-0 h-[3px] transition-transform duration-200 origin-left scale-x-0 group-hover:scale-x-100 bg-[var(--accent)]" />
              <div className="inline-block px-2 py-0.5 rounded-full text-[11px] font-mono font-medium mb-3 bg-[color-mix(in_srgb,var(--accent)_12%,transparent)] text-[var(--accent)]">
                {domain.pct}
              </div>
              <div className="font-medium text-[var(--text)] text-[14px] mb-1.5">
                {domain.name}
              </div>
              <div className="text-[12px] text-[var(--text3)] leading-relaxed">
                {domain.desc}
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* KEYWORDS SECTION */}
      <section className="max-w-[900px] mx-auto px-6 mb-16 relative z-10">
        <div className="text-[12px] font-semibold tracking-widest uppercase text-[var(--text3)] mb-4">
          Critical keywords — what words in the question tell you the answer
        </div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
          {keywordCards.map((card) => (
            <div key={card.title} className="premium-card p-5">
              <h4 className="text-[13px] font-semibold text-[var(--text)] mb-3.5 flex items-center gap-2">
                <div className="w-5 h-5 rounded-md flex items-center justify-center text-[11px] font-bold bg-[color-mix(in_srgb,var(--aws)_15%,transparent)] text-[var(--aws)]">
                  {card.icon}
                </div>
                {card.title}
              </h4>
              <div className="flex flex-wrap gap-1">
                {card.tags.map((tag) => (
                  <span key={tag} className={`kw-tag ${card.color}`}>
                    {tag}
                  </span>
                ))}
              </div>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
}
