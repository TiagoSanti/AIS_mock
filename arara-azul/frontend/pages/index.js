import Head from 'next/head'
import Classificador from '@/pages/classificador'

export default function Home() {

  return (
      <>
        <Head>
          <title>Tuiaia - Classificador</title>
          <meta name="description" content="A melhor IA para classificar sentimento de notícias" />
          <meta name="viewport" content="width=device-width, initial-scale=1" />
          <link rel="icon" href="/logo-tuiuiu.ico" />
          <link rel="preconnect" href="https://fonts.googleapis.com" />
          <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin />
        </Head>
        <main>
          <Classificador />
        </main>
      </>
  )
}
