import { DefinicaoText } from '@/data/text/classificador';

const Definicao = () => {
    return (
        <section
            className={'bg-[url("/cachoeira-definicao-classificador.svg")] overflow-hidden w-full bg-no-repeat bg-cover pb-601 flex items-center justify-end'}>
            <div className={'flex justify-end items-center p-20'}>
                <div className={'flex-1 max-w-5xl bg-p-bold h-full p-10 rounded-3xl pb-31'}>
                    <div className={'text-secondary text-5xl font-bold mb-10'}>{DefinicaoText.title}</div>
                    <div className={'text-white text-3xl text-justify'}>
                        {DefinicaoText.paragraph_one}<br/><br/>
                        {DefinicaoText.description}<br/><br/>
                        {DefinicaoText.paragraph_two}<br/><br/>
                        {DefinicaoText.paragraph_three}
                    </div>
                </div>
            </div>
        </section>
    )
}

export default Definicao