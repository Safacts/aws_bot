import { createClient } from '@/utils/supabase/server'
import { cookies } from 'next/headers'

export default async function SupabaseTestPage() {
    const cookieStore = await cookies()
    const supabase = createClient(cookieStore)
    
    // Attempt to fetch some metadata or test query
    const { data, error } = await supabase.from('todos').select('*').limit(1);

    return (
        <main className="min-h-screen pt-24 pb-12 wide-wrap px-4">
            <h1 className="text-3xl font-bold text-white mb-8">Supabase Connection Test</h1>
            
            <div className="bg-[var(--surface)] border border-[var(--border)] rounded-2xl p-8">
                {error ? (
                    <div className="text-red-400">
                        <p className="font-bold">Error connecting to Supabase:</p>
                        <pre className="text-xs bg-black p-4 rounded mt-4 overflow-auto">
                            {JSON.stringify(error, null, 2)}
                        </pre>
                    </div>
                ) : (
                    <div className="text-green-400">
                        <p className="font-bold">Successfully connected to Supabase!</p>
                        <p className="text-[var(--text-dim)] mt-2">Data payload:</p>
                        <pre className="text-xs bg-black p-4 rounded mt-4 overflow-auto">
                            {JSON.stringify(data, null, 2)}
                        </pre>
                    </div>
                )}
            </div>
        </main>
    )
}
