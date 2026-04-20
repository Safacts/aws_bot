import fs from 'fs';
import path from 'path';
import StudyView from '@/components/StudyView';

export default async function StudyPage() {
    const guidesDir = path.join(process.cwd(), 'src/content/guides');
    const files = fs.readdirSync(guidesDir);
    
    const guides = files
        .filter(file => file.endsWith('.md'))
        .sort((a, b) => {
            if (a === 'master_index.md') return -1;
            if (b === 'master_index.md') return 1;
            return a.localeCompare(b);
        })
        .map(file => ({
            id: file.replace('.md', ''),
            title: file.replace('.md', '').replace(/_/g, ' ').replace(/\b\w/g, l => l.toUpperCase()),
            content: fs.readFileSync(path.join(guidesDir, file), 'utf-8')
        }));

    return (
        <main className="min-h-screen pt-24 pb-12">
            <StudyView initialGuides={guides} />
        </main>
    );
}
