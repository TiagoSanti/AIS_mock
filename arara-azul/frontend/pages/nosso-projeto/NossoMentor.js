import Image from 'next/image'
import { TiagoRomao } from '@/data/text/members'
import NossoMentorText from '@/data/text/nossoProjeto/NossoMentorText';

const NossoMentor = () => {
    return (
        <section className={'relative w-full h-full bg-primary'}>
            <div className={'relative z-10'}>
                <div className={'flex flex-wrap justify-around items-center p-16'}>
                    <div className={'flex flex-col justify-end items-center'}>
                        <span className={'text-secondary text-6xl font-bold mt-14'}>{NossoMentorText.title}</span>
                        <Image className={'filter'} src={TiagoRomao.image} alt={'Tiago Romão'} width={500} height={500} />
                    </div>
                    <div className={'flex-1 max-w-5xl bg-white h-full p-10 rounded-3xl pb-36'}>
                        <div className={'text-p-bold text-4xl font-bold mb-4 text-center'}>{TiagoRomao.name}</div>
                        <div className={'text-light text-2xl mb-8 text-center'}>{TiagoRomao.current_position}</div>
                        <div className={'text-primary text-2xl text-justify'}>{TiagoRomao.description}</div>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default NossoMentor;
