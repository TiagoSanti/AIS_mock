import Head from'next/head'
import ClassificadorNoticias from '@/pages/classificador/ClassificadorNoticias';
import Definicao from '@/pages/classificador/Definicao';
import Aplicacao from '@/pages/classificador/Aplicacao';
import Multilingual from '@/pages/classificador/Multilingual';
import PolaridadeEmocional from "./PolaridadeEmocional";

const Classificador = () => {
    return (
        <>
            <Head>
                <title>Tuiaia - Classificador</title>
                <meta name="description" content="A melhor IA para classificar sentimento de notícias" />
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <link rel="icon" href="/logo-tuiuiu.ico" />
            </Head>
            <main className={'overflow-x-hidden pt-[104px]'}>
                <ClassificadorNoticias />
                <Definicao />
                <PolaridadeEmocional />
                <Multilingual />
                <Aplicacao />
            </main>
        </>
    )
}

export default Classificador;
