import Image from 'next/image'
import FeedDeNoticiaText from "@/data/text/feed/FeedDeNoticiaText";

const Introducao = () => {
    return (
        <section className={'w-full overflow-hidden'}>
            <div className={'relative h-[600px]'}>
                <Image className={'absolute -right-20 top-0 -z-10 '} src={'arara_vermelha_feed.svg'} alt={''} width={500} height={500}/>
                <Image className={'absolute -left-28 -bottom-28 -z-10'} src="arara_azul_feed.svg" alt={''} width={500} height={500} />
                <div className={'flex p-10 px-40 flex-col justify-center items-center text-center max-w-[70%] m-auto'}>
                    <div className={'flex-1 h-full p-10 rounded-3xl pb-31'}>
                        <div className={'text-p-bold text-6xl font-bold mb-10'}>{FeedDeNoticiaText.title}</div>
                        <div className={'feed-title text-secondary text-4xl font-bold max-w-none'}>{FeedDeNoticiaText.description}</div>
                        <div className={'text-white text-2xl text-center justify-center items-center flex'}>
                            <div className={'grid grid-cols-3 gap-10'}>
                                <div className={'text-p-bold font-bold mb-10'}>
                                    <div className={'mb-10'}>
                                        <Image className={'ml-2'} src={'/calendario_feed.svg'} alt={''} width={350} height={350}/>
                                    </div>
                                    <div className={'feed-icons'}>
                                        {FeedDeNoticiaText.advantage1}
                                    </div>
                                </div>
                                <div className={'text-p-bold font-bold mb-10'}>
                                    <div className={'text-3xl mb-10'}>
                                        <Image className={'ml-2'} src={'/livro_feed.svg'} alt={''} width={350} height={350}/>
                                    </div>
                                    <div className={'feed-icons'}>
                                        {FeedDeNoticiaText.advantage2}
                                    </div>
                                </div>
                                <div className={'text-p-bold font-bold mb-10'}>
                                    <div className={'mb-10'}>
                                        <Image className={'ml-2'} src={'dinheiro_feed.svg'} alt={''} width={350} height={350}/>
                                    </div>
                                    <div className={'feed-icons'}>
                                        {FeedDeNoticiaText.advantage3}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default Introducao;
