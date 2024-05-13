import Head from 'next/head';
import Introducao from '@/pages/feed/Introducao';
import Noticias from '@/pages/feed/Noticias';

export default function Feed() {
    return (
        <>
            <Head>
                <title>Tuiaia - Feed</title>
                <meta name="description" content="A melhor IA para classificar sentimento de notícias" />
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <link rel="icon" href="/logo-tuiuiu.ico" />
            </Head>
            <main className={'overflow-hidden pt-[104px]'}>
                <Introducao />
                <Noticias />
            </main>
        </>
    )
}
