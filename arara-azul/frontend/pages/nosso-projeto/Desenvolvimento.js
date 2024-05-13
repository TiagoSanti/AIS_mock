import Image from 'next/image';
import { DesenvolvimentoText } from '@/data/text/nossoProjeto';

const Desenvolvimento = () => {
    return (
        <section className={'bg-[url("/background_desenvolvimento.svg")] overflow-hidden w-full bg-no-repeat bg-cover flex'}>
            <div className={'mt-20 ml-44 mr-12 p-4'}>
                <div className={'text-secondary text-6xl'}>
                    {DesenvolvimentoText.title}
                </div>
                <div className={'text-white text-2xl mt-8 mb-24'}>
                    {DesenvolvimentoText.paragraph_one}<br/><br/>
                    {DesenvolvimentoText.paragraph_two}<br/><br/>
                    {DesenvolvimentoText.paragraph_three}<br/><br/>
                    {DesenvolvimentoText.paragraph_four}
                </div>
            </div>
            <div className={'mr-28 mt-20 p-4'}>
                <Image src="onca_desenvolvimento_nosso_projeto.svg" alt={''} width={3500} height={3500}></Image>
            </div>
        </section>
    );
};

export default Desenvolvimento;