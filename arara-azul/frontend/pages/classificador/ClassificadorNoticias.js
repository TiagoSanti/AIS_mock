import {useState} from 'react';
import Image from 'next/image';
import CapivaraLoading from '@/components/CapivaraLoading';
import { getNewsClassification } from '@/api/classify/controller'
import ClassificacaoCard from './ClassificacaoCard';

const ClassificadorNoticias = () => {
    const [text, setText] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [response, setResponse] = useState(null);

    const classify = async () => {
        setIsLoading(true);
        const classification = await getNewsClassification(text)
        if (classification) {
            setResponse(classification);    
        }
        setIsLoading(false);
    }

    return (
        <>
            <section className={'flex flex-col justify-center items-center max-w-4xl m-auto pt-10 text-primary min-h-[600px]'}>
                <h1 className={'text-7xl font-bold mb-8'}>Classificador de notícias</h1>
                <div className={'w-full relative'}>
                    <div className={'text-2xl'}>
                        Digite ou cole o texto da notícia sobre o mercado financeiro no campo abaixo:
                    </div>
                    <div className={'w-full bg-white relative mt-4 border-solid border-4 border-primary p-4 pb-0 rounded-3xl hover:outline-p-lighter'}>
                        <textarea
                            style={{overflowY: 'visible'}}
                            color={'primary'}
                            className={'w-full min-h-[200px] max-w-full max-h-[60vh] text-primary text-xl focus:outline-none'}
                            value={text}
                            onChange={(e) => setText(e.target.value)}
                            onFocus={(e) => e.target.parentElement.classList.add('border-p-lighter')}
                            onBlur={(e) => e.target.parentElement.classList.remove('border-p-lighter')}
                        />
                    </div>
                    <Image src={'folhas_direita.svg'} alt={''} width={250} height={250} className={'absolute  -right-28 top-2 -z-10'} ></Image>
                    <Image src={'folhas_esquerda.svg'} alt={''} width={200} height={200} className={'absolute  -left-32 top-12 -z-10'}></Image>
                </div>
                <div className={'w-full text-end text-2xl mt-2 mr-2'}>Caracteres: {text.length}</div>
                <div className={'w-full flex justify-center'}>
                    {!isLoading? (
                        <button
                            className={'bg-primary text-white font-bold rounded-full p-2 px-8 text-3xl hover:bg-p-bold hover:shadow-[0px_8px_15px_rgba(0,0,0,0.25)] hover:-translate-y-1 active:shadow-none active:translate-y-0'}
                            onClick={classify}
                        >
                            Classificar
                        </button>
                    ) : <div className={'mb-10'}>
                            <CapivaraLoading/>
                        </div>
                    }
                </div>
            </section>
            {response && (
                <div className={'flex w-[90vw] gap-5 m-auto'}>
                    {response.map((classification, index) => classification? 
                    <ClassificacaoCard classification={classification} key={index} identifier={index} /> : null
                    )}
                </div>
                )
            }
        </>
    )
}

export default ClassificadorNoticias
