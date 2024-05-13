import { DefinicaoText } from '@/data/text/nossoProjeto';

const Definicao = () => {
    return (
        <section
            className={'bg-[url("/capivara_definicao_nosso_projeto.svg")] overflow-hidden w-full bg-no-repeat bg-cover pb-601 flex items-center justify-end'}>
            <div className={'flex justify-end items-center p-20'}>
                <div className={'flex-1 max-w-5xl bg-white h-full p-10 rounded-3xl pb-31'}>
                    <div className={'text-secondary text-5xl font-bold mb-10'}>{DefinicaoText.title}</div>
                    <div className={'text-p-bold text-3xl text-justify'}>
                        {DefinicaoText.paragraph_one}<br/><br/>
                        {DefinicaoText.paragraph_two}<br/><br/>
                        {DefinicaoText.paragraph_three}<br/><br/>
                        {DefinicaoText.paragraph_four}<br/><br/>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default Definicao