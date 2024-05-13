import { ImpactoTemporalText } from '@/data/text/classificador';
import { PolaridadeEmocionalText } from '@/data/text/classificador';
import { MagnitudeText } from '@/data/text/classificador';
import Image from 'next/image'

const PolaridadeEmocional = () => {
    return (
        <section className={'p-8 flex-col h-full rounded-3xl mt-8'}>
                <div className={'flex-1'}>
                    <div className={'text-secondary text-6xl font-bold mb-8 ml-12'}>{PolaridadeEmocionalText.title}</div>
                    <div className={'text-white text-3xl text-center justify-center items-center flex'}>
                        <div className={'grid grid-cols-3 gap-10'}>
                            <div className={'text-p-bold text-2xl font-bold mb-10'}>
                                <div className={'text-3xl'}>
                                    <Image className={'inline-block ml-2 positive-icon'} src={'/positive_icon.svg'} alt={''} width={300} height={300}/>
                                </div>
                                <div className={'mt-6 mb-6 text-third text-5xl'}>
                                    {PolaridadeEmocionalText.positive_title}<br/>
                                </div>
                                <div className={'max-w-[90%] mx-auto text-justify'}>
                                    {PolaridadeEmocionalText.positive_description}
                                </div>
                            </div>
                            <div className={'text-p-bold text-2xl font-bold mb-10'}>
                                <div className={'text-3xl'}>
                                    <Image className={'inline-block ml-2 neutral-icon'} src={'/neutral_icon.svg'} alt={''} width={300} height={300}/>
                                </div>
                                <div className={'mt-6 mb-6 text-classify-neutral text-5xl'}>
                                    {PolaridadeEmocionalText.neutral_title}<br/>
                                </div>
                                <div className={'max-w-[90%] mx-auto text-justify'}>
                                    {PolaridadeEmocionalText.neutral_description}
                                </div>
                            </div>
                            <div className={'text-p-bold text-2xl font-bold mb-10'}>
                                <div className={'text-3xl'}>
                                    <Image className={'inline-block ml-2 negative-icon'} src={'/negative_icon.svg'} alt={''} width={300} height={300}/>
                                </div>
                                <div className={'mt-6 mb-6 text-classify-negative text-5xl'}>
                                    {PolaridadeEmocionalText.negative_title}<br/>
                                </div>
                                <div className={'max-w-[90%] mx-auto text-justify'}>
                                    {PolaridadeEmocionalText.negative_description}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className={'text-secondary text-6xl font-bold mt-12 -mb-20 ml-12'}>{ImpactoTemporalText.title}</div>
                    <div className={'text-white text-3xl text-center justify-center items-center flex'}>
                        <div className={'grid grid-cols-2 gap-10'}>
                            <div className={'text-p-bold text-2xl font-bold mb-8'}>
                                <div>
                                    <Image className={'inline-block -ml-36'} src={'/curto_prazo.svg'} alt={''} width={600} height={600}/>
                                </div>
                                <div className={'-mt-24 mb-8 text-5xl'}>
                                    {ImpactoTemporalText.short_term_title}<br/>
                                </div>
                                <div className={'mt-35 mb-8 max-w-[70%] mx-auto'}>
                                    {ImpactoTemporalText.short_term_description}
                                </div>
                            </div>
                            <div className={'text-p-bold text-2xl font-bold mb-10'}>
                                <div>
                                    <Image className={'inline-block ml-2'} src={'/longo_prazo.svg'} alt={''} width={600} height={600}/>
                                </div>
                                <div className={'-mt-24 mb-8 text-5xl'}>
                                    {ImpactoTemporalText.long_term_title}<br/>
                                </div>
                                <div className={'mt-35 mb-8 max-w-[70%] mx-auto'}>
                                    {ImpactoTemporalText.long_term_description}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className={'text-secondary text-6xl font-bold mt-8 -mb-8 ml-12'}>{MagnitudeText.title}</div>
                    <div className={'text-3xl text-center flex'}>
                        <div className={'grid grid-cols-2 gap-10'}>
                            <div className={'text-p-bold text-2xl font-bold mb-8'}>
                                <div>
                                    <Image className={'inline-block ml-2'} src={'/flor_de_ipe.svg'} alt={''} width={450} height={450}/>
                                </div>
                                <div className={'mb-8 text-5xl'}>
                                    {MagnitudeText.low_impact_title}<br/>
                                </div>
                                <div className={'mt-35 mb-8 max-w-[70%] mx-auto'}>
                                    {MagnitudeText.low_impact_description}
                                </div>
                            </div>
                            <div className={'text-p-bold text-2xl font-bold mb-10'}>
                                <div className={'text-3xl'}>
                                    <Image className={'inline-block ml-2'} src={'/arvore_de_ipe.svg'} alt={''} width={450} height={450}/>
                                </div>
                                <div className={'mb-8 text-5xl'}>
                                    {MagnitudeText.high_impact_title}<br/>
                                </div>
                                <div className={'mt-35 mb-8 max-w-[72%] mx-auto'}>
                                    {MagnitudeText.high_impact_description}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
        </section>
    )
}

export default PolaridadeEmocional;
