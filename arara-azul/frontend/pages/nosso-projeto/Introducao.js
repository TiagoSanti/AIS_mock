import Image from 'next/image';
import { IntroducaoText } from '@/data/text/nossoProjeto';

const Introducao = () => {
    return (
        <section className={'bg-white overflow-hidden w-full flex h-[700px]'}>
            <div className={'flex flex-col text-center justify-center m-auto'}>
                <div className={'bg-[url("/tuiaia_background.svg")] bg-no-repeat bg-cover mb-5 w-[95vw]'}>
                    <Image className={'mx-auto -mt-20'} src={'tuiaia.svg'} alt={''} width={500} height={500} />
                    <div className={'text-primary text-3xl -mt-4'}>
                        {IntroducaoText.paragraph_one}<br/><br/>
                    </div>
                </div>
                <div className={'text-center'}>                    
                    <div className={'text-primary text-3xl my-2'}>
                        {IntroducaoText.paragraph_two}<br/><br/>
                    </div>
                    <div className={'text-third font-bold text-5xl my-2 mb-6'}>
                        {IntroducaoText.paragraph_three}
                        <span className={'text-secondary'}>
                            {IntroducaoText.paragraph_three_part_two}
                        </span>
                        {IntroducaoText.paragraph_three_part_three}
                    </div>
                </div>
            </div>
        </section>
    );
};

export default Introducao;