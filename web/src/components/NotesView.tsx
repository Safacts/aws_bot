'use client';

import React, { useState } from 'react';
import { 
    Cloud, 
    ShieldCheck, 
    Cpu, 
    Banknote, 
    ArrowLeftRight,
    Search,
    AlertCircle,
    Info,
    CheckCircle2
} from 'lucide-react';

const CATEGORIES = [
    { id: 'cloud', label: 'Cloud Concepts', icon: Cloud },
    { id: 'sec', label: 'Security', icon: ShieldCheck },
    { id: 'tech', label: 'Technology', icon: Cpu },
    { id: 'billing', label: 'Billing', icon: Banknote },
    { id: 'compare', label: 'Comparisons', icon: ArrowLeftRight },
];

export default function NotesView() {
    const [activeTab, setActiveTab] = useState('cloud');

    return (
        <div className="wide-wrap px-4 pb-20">
            {/* Tab Navigation */}
            <div className="flex flex-wrap gap-2 mb-12 bg-[var(--surface-light)] p-2 rounded-[24px] border border-[var(--border)] sticky top-24 z-30 backdrop-blur-xl">
                {CATEGORIES.map(cat => (
                    <button
                        key={cat.id}
                        onClick={() => setActiveTab(cat.id)}
                        className={`
                            flex items-center gap-2 px-6 py-3 rounded-xl transition-all font-medium text-sm
                            ${activeTab === cat.id 
                                ? 'bg-[var(--accent)] text-white shadow-lg shadow-[var(--accent-dim)]' 
                                : 'text-[var(--text-dim)] hover:text-white hover:bg-[var(--surface-hover)]'}
                        `}
                    >
                        <cat.icon size={18} />
                        {cat.label}
                    </button>
                ))}
            </div>

            {/* Content Panels */}
            <div className="space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-500">
                
                {activeTab === 'cloud' && (
                    <>
                        <NoteBlock title="6 Advantages of Cloud Computing" tag="Memorize">
                            <ul className="space-y-4">
                                <NoteItem label="Trade CapEx for OpEx" desc="No upfront server purchases, pay monthly" />
                                <NoteItem label="Economies of Scale" desc="AWS buys in bulk, prices dropped 75+ times" />
                                <NoteItem label="Stop Guessing Capacity" desc="Auto Scaling handles demand spikes" />
                                <NoteItem label="Increase Speed & Agility" desc="Deploy in minutes instead of weeks" />
                                <NoteItem label="Stop Spending on Data Centers" desc="Focus on business, not hardware" />
                                <NoteItem label="Go Global in Minutes" desc="Deploy in any Region worldwide instantly" />
                            </ul>
                        </NoteBlock>

                        <div className="grid md:grid-cols-2 gap-8">
                            <NoteBlock title="Cloud Deployment Models">
                                <ul className="space-y-4">
                                    <NoteItem label="Public Cloud" desc="Everything on AWS. (Startups, most companies)" />
                                    <NoteItem label="Private Cloud" desc="Your own data center. (Gov, Banks)" />
                                    <NoteItem label="Hybrid Cloud" desc="Mix of AWS + On-premises. MOST COMMON exam scenario" />
                                </ul>
                            </NoteBlock>
                            <NoteBlock title="Service Models" tag="Common Trap">
                                <ul className="space-y-4">
                                    <NoteItem label="IaaS" desc="You manage OS, apps. AWS manages hardware. (EC2)" />
                                    <NoteItem label="PaaS" desc="You manage app only. (Elastic Beanstalk, RDS)" />
                                    <NoteItem label="SaaS" desc="You manage nothing. (Gmail, Salesforce)" />
                                </ul>
                            </NoteBlock>
                        </div>

                        <NoteBlock title="Well-Architected Framework — 6 Pillars">
                            <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6 mt-4">
                                <PillarCard name="Operational Excellence" desc="Automate, improve processes" />
                                <PillarCard name="Security" desc="IAM, encryption, controls" />
                                <PillarCard name="Reliability" desc="Fault tolerance, recovery" />
                                <PillarCard name="Performance Efficiency" desc="Right resource types" />
                                <PillarCard name="Cost Optimization" desc="Avoid waste, track spend" />
                                <PillarCard name="Sustainability" desc="Environmental impact" />
                            </div>
                        </NoteBlock>
                    </>
                )}

                {activeTab === 'sec' && (
                    <>
                        <NoteBlock title="Shared Responsibility Model" tag="10+ Qs">
                            <div className="grid md:grid-cols-2 gap-6 mt-4">
                                <div className="p-6 rounded-2xl bg-[var(--surface-hover)] border border-[var(--border)]">
                                    <h4 className="text-[var(--accent)] font-bold text-sm uppercase tracking-widest mb-4">AWS Responsibilities</h4>
                                    <ul className="text-sm space-y-2 text-[var(--text-dim)]">
                                        <li>• Physical security of data centers</li>
                                        <li>• Hardware and global network</li>
                                        <li>• Managed services (RD patching)</li>
                                        <li>• The Hypervisor software</li>
                                    </ul>
                                </div>
                                <div className="p-6 rounded-2xl bg-[var(--surface-hover)] border border-[var(--border)]">
                                    <h4 className="text-white font-bold text-sm uppercase tracking-widest mb-4">Your Responsibilities</h4>
                                    <ul className="text-sm space-y-2 text-[var(--text-dim)]">
                                        <li>• Encrypting your own data</li>
                                        <li>• IAM users and permissions</li>
                                        <li>• OS patches on EC2 instances</li>
                                        <li>• Network firewall configuration</li>
                                    </ul>
                                </div>
                            </div>
                        </NoteBlock>

                        <NoteBlock title="IAM Reference">
                            <div className="grid sm:grid-cols-2 gap-4">
                                <QuickNote label="Users" desc="Permanent individuals (access keys)" />
                                <QuickNote label="Groups" desc="Collections for ease of management" />
                                <QuickNote label="Roles" desc="Temporary (EC2 access to S3)" />
                                <QuickNote label="Policies" desc="JSON documents (Allow/Deny)" />
                            </div>
                        </NoteBlock>

                        <NoteBlock title="Security Core Services">
                            <div className="overflow-x-auto">
                                <table className="w-full text-left text-sm">
                                    <thead className="bg-[var(--surface-hover)] text-white">
                                        <tr>
                                            <th className="p-4 rounded-tl-xl border-b border-[var(--border)]">Service</th>
                                            <th className="p-4 border-b border-[var(--border)]">What it does</th>
                                        </tr>
                                    </thead>
                                    <tbody className="text-[var(--text-dim)] divide-y divide-[var(--border)]">
                                        <TableRow l="Shield Standard" r="Free, automatic Layer 3/4 DDoS protection" />
                                        <TableRow l="WAF" r="Blocks SQLi, XSS (Layer 7 HTTP attacks)" />
                                        <TableRow l="GuardDuty" r="ML-based threat detection (Logs analysis)" />
                                        <TableRow l="Macie" r="Finds PII/Sensitive data in S3 buckets" />
                                        <TableRow l="Inspector" r="Vulnerability scans for EC2/Containers" />
                                        <TableRow l="CloudTrail" r="Audit logs - who did what, when, where" />
                                    </tbody>
                                </table>
                            </div>
                        </NoteBlock>
                    </>
                )}

                {activeTab === 'tech' && (
                    <>
                        <NoteBlock title="EC2 Pricing Strategies" tag="Exam Favorite">
                            <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
                                <PriceCard type="On-Demand" usage="Unknown / Spiky" cost="Highest" />
                                <PriceCard type="Reserved" usage="Steady State (1-3 yr)" cost="72% Low" />
                                <PriceCard type="Spot" usage="Batch / Insensitive" cost="90% Low" />
                                <PriceCard type="Dedicated" usage="Compliance / BYOL" cost="Premium" />
                            </div>
                        </NoteBlock>

                        <NoteBlock title="S3 Storage Tiering">
                            <ul className="space-y-4">
                                <NoteItem label="Standard" desc="Frequent access, high performance" />
                                <NoteItem label="Standard-IA" desc="Infrequent access, cheaper storage, retrieval fee" />
                                <NoteItem label="Intelligent" desc="Automatic tiering based on usage" />
                                <NoteItem label="Glacier" desc="Low cost archive, long retrieval (mins/hrs)" />
                                <NoteItem label="Deep Archive" desc="Lowest cost, 12hr+ retrieval" />
                            </ul>
                        </NoteBlock>
                    </>
                )}

                {activeTab === 'billing' && (
                    <div className="grid lg:grid-cols-2 gap-8">
                        <NoteBlock title="Support Plans">
                            <div className="space-y-4">
                                <div className="flex justify-between items-center p-4 rounded-xl bg-[var(--surface-hover)] border-l-4 border-gray-500">
                                    <div><p className="font-bold">Basic / Developer</p><p className="text-xs text-[var(--text-dim)]">Trial / Dev use</p></div>
                                    <p className="text-xs font-mono">Email only</p>
                                </div>
                                <div className="flex justify-between items-center p-4 rounded-xl bg-[var(--surface-hover)] border-l-4 border-[var(--accent)]">
                                    <div><p className="font-bold">Business</p><p className="text-xs text-[var(--text-dim)]">24/7 Phone/Chat</p></div>
                                    <p className="text-xs font-mono text-[var(--accent)]">&lt; 1 hr</p>
                                </div>
                                <div className="flex justify-between items-center p-4 rounded-xl bg-[var(--surface-hover)] border-l-4 border-white">
                                    <div><p className="font-bold">Enterprise</p><p className="text-xs text-[var(--text-dim)]">TAM Assigned</p></div>
                                    <p className="text-xs font-mono text-white">&lt; 15 min</p>
                                </div>
                            </div>
                        </NoteBlock>

                        <NoteBlock title="Billing Tools Toolkit">
                            <div className="grid grid-cols-2 gap-4">
                                <QuickNote label="Calculator" desc="Predict FUTURE costs" />
                                <QuickNote label="Cost Explorer" desc="Analyze PAST spending" />
                                <QuickNote label="Budgets" desc="ALERTS when thresholds hit" />
                                <QuickNote label="CUR" desc="Granular line-item DETAIL" />
                            </div>
                        </NoteBlock>
                    </div>
                )}

                {activeTab === 'compare' && (
                    <NoteBlock title="Commonly Confused Services">
                        <div className="overflow-x-auto">
                            <table className="w-full text-left text-sm">
                                <thead className="bg-[var(--surface-hover)] text-white">
                                    <tr>
                                        <th className="p-4 rounded-tl-xl border-b border-[var(--border)]">Service A</th>
                                        <th className="p-4 border-b border-[var(--border)]">Service B</th>
                                        <th className="p-4 rounded-tr-xl border-b border-[var(--border)]">The Key Difference</th>
                                    </tr>
                                </thead>
                                <tbody className="text-[var(--text-dim)] divide-y divide-[var(--border)]">
                                    <CompareRow a="CloudWatch" b="CloudTrail" d="Metrics (Performance) vs Audit (API Logs)" />
                                    <CompareRow a="SG (Firewall)" b="NACL" d="Stateful (Instance) vs Stateless (Subnet)" />
                                    <CompareRow a="S3" b="EBS" d="Object Storage vs Block Storage (Drive)" />
                                    <CompareRow a="SNS" b="SQS" d="Pub/Sub (Push) vs Queue (Pull)" />
                                    <CompareRow a="Direct Connect" b="VPN" d="Physical Line vs Encrypted Tunnel (Public)" />
                                </tbody>
                            </table>
                        </div>
                    </NoteBlock>
                )}

            </div>
        </div>
    );
}

// Sub-components for clean structure

function NoteBlock({ title, tag, children }: { title: string, tag?: string, children: React.ReactNode }) {
    return (
        <section className="bg-[var(--surface)] border border-[var(--border)] rounded-[32px] p-8 md:p-10 shadow-xl">
            <div className="flex items-center justify-between mb-8">
                <h3 className="text-xl md:text-2xl font-bold text-white font-sora">{title}</h3>
                {tag && (
                    <span className="bg-[var(--accent-dim)] text-[var(--accent)] text-[10px] uppercase tracking-widest font-bold px-3 py-1 rounded-full border border-[var(--accent-dim)]">
                        {tag}
                    </span>
                )}
            </div>
            {children}
        </section>
    );
}

function NoteItem({ label, desc }: { label: string, desc: string }) {
    return (
        <li className="flex gap-4 group">
            <div className="mt-1.5 shrink-0"><CheckCircle2 size={16} className="text-[var(--accent)]" /></div>
            <div>
                <span className="font-bold text-white mr-2">{label}</span>
                <span className="text-[var(--text-dim)]">— {desc}</span>
            </div>
        </li>
    );
}

function PillarCard({ name, desc }: { name: string, desc: string }) {
    return (
        <div className="p-5 rounded-2xl bg-[var(--surface-light)] border border-[var(--border)] hover:border-[var(--accent)] transition-all">
            <p className="text-white font-bold mb-1 text-sm">{name}</p>
            <p className="text-xs text-[var(--text-dim)] leading-relaxed">{desc}</p>
        </div>
    );
}

function QuickNote({ label, desc }: { label: string, desc: string }) {
    return (
        <div className="p-4 rounded-xl bg-[var(--surface-hover)] border border-[var(--border)]">
            <p className="text-[var(--accent)] font-bold text-xs uppercase mb-1">{label}</p>
            <p className="text-sm text-white">{desc}</p>
        </div>
    );
}

function PriceCard({ type, usage, cost }: { type: string, usage: string, cost: string }) {
    return (
        <div className="p-5 rounded-2xl bg-[var(--surface-hover)] border border-[var(--border)] text-center">
            <p className="text-white font-bold mb-1">{type}</p>
            <p className="text-xs text-[var(--text-dim)] mb-3">{usage}</p>
            <p className="text-[10px] font-mono text-[var(--accent)] uppercase">{cost}</p>
        </div>
    );
}

function TableRow({ l, r }: { l: string, r: string }) {
    return (
        <tr>
            <td className="p-4 font-bold text-white">{l}</td>
            <td className="p-4">{r}</td>
        </tr>
    );
}

function CompareRow({ a, b, d }: { a: string, b: string, d: string }) {
    return (
        <tr className="hover:bg-[var(--surface-hover)] transition-colors">
            <td className="p-4 font-bold text-white">{a}</td>
            <td className="p-4 font-bold text-[var(--accent)]">{b}</td>
            <td className="p-4 italic">{d}</td>
        </tr>
    );
}
