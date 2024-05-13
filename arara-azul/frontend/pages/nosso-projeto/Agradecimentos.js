import AgradecimentosText from '@/data/text/nossoProjeto/AgradecimentosText';
import Image from 'next/image';

const Agradecimentos = () => {
    return (
        <section className={'relative px-20 pt-32 pb-56 flex flex-col justify-center items-center overflow-hidden'}>
            <Image className={'absolute top-0 left-0 -z-10'} src={'linhas_cima_agradecimentos.svg'} alt={''} width={400} height={400} />
            <div className={'font-bold text-6xl text-secondary mb-12'}>{AgradecimentosText.title}</div>
            <div className={'text-2xl max-w-screen-2xl text-primary text-justify'}>
                <span>{AgradecimentosText.paragraph_one}<br/><br/></span>
                <span>
                    {AgradecimentosText.paragraph_two}
                    <a href={'https://github.com'} className={'underline'} target={'_blank'}>GitHub</a>
                    {AgradecimentosText.paragraph_two_continuation}<br/><br/>
                </span>
                <span>{AgradecimentosText.paragraph_three}<br/></span>
                <span>{AgradecimentosText.paragraph_four}</span>
                <Image className={'absolute bottom-12 right-0 -z-10'} src={'linhas_direita_agradecimentos.svg'} alt={''} width={400} height={400} />
            </div>
            <Image className={'absolute -bottom-60 left-0 -z-10'} src={'linhas_baixo_agradecimentos.svg'} alt={''} width={400} height={400} />
            <Image className={'absolute -bottom-44 left-1/2 -z-10'} src={'tamandua.svg'} alt={''} width={550} height={550} />
        </section>
    )
}

export default Agradecimentos
