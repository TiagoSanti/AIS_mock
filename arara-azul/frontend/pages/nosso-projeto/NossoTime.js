import Image from 'next/image'
import { Hallyson, Lourdes, Rodrigo, TiagoSanti } from '@/data/text/members'
import NossoTimeText from '@/data/text/nossoProjeto/NossoTimeText';

const members = [Hallyson, Rodrigo, Lourdes, TiagoSanti]

const NossoTime = () => {
    return (
        <section className={'relative w-full pb-72 overflow-hidden'} >
            <Image className={'absolute -top-0 -left-20 -z-10'} src={'geometrico_cima.svg'} alt={''} width={600} height={600} />
            <Image className={'absolute -top-0 -right-20 -z-10'} src={'araras_nosso_time.svg'} alt={''} width={400} height={400} />
            <div className={'flex flex-col justify-center items-center pt-16 max-w-3xl m-auto'}>
                <span className={'text-6xl font-bold text-secondary mb-12'}>{NossoTimeText.title}</span>
                <span className={'text-p-bold text-center text-4xl'}>
                    {NossoTimeText.subtitle_first}<br/>
                    {NossoTimeText.subtitle_second}
                </span>
            </div>
            <Image className={'absolute top-1/3 right-0 -z-10'} src={'tucano.svg'} alt={''} width={300} height={300} />
            {members?.map((member, index) => {
                return (
                    <div className={'flex justify-center pt-8 gap-6 flex-wrap mt-14'} key={index}>
                        {index % 2 === 0 && <Image src={member.image} alt={`Foto do ${member.name}`} width={300} height={300} />}
                            <div className={'flex flex-col gap-4 max-w-2xl p-4'}>
                                <span className={'text-third font-bold text-4xl'}>{member.name}</span>
                                <span className={'font-semibold text-3xl text-secondary'}>{member.graduation}</span>
                                <span className={'break-words text-2xl text-primary text-justify'}>{member.description}</span>
                            </div>
                        {index % 2 !== 0 && <Image src={member.image} alt={`Foto do ${member.name}`} width={300} height={300} />}
                    </div>
                )
            })}
            <Image className={'absolute -bottom-32 -left-14 -z-10'} src={'jacare.svg'} alt={''} width={500} height={500} />
            <Image className={'absolute -bottom-32 -right-40 -z-10'} src={'geometrico_baixo.svg'} alt={''} width={800} height={800} />
        </section>
    )
}

export default NossoTime
