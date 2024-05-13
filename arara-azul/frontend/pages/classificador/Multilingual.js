import { MultilingualText } from '@/data/text/classificador';
import Image from "next/image";

const Multilingual = () => {
    return (
        <section className={'bg-[url("/multilingual-classificador.svg")] px-48 py-32 relative bg-right-center bg-no-repeat bg-cover w-full flex items-center'}>
            <Image className={'absolute -left-60'} src="arara-multilingual-classificador.svg" alt="Araras multilingual" width={800} height={800} />
            <div className={'relative z-10'}>
                <div className={'flex m-auto flex-col justify-center items-center max-w-[60%]'}>
                    <div className="text-secondary text-6xl font-bold mb-10 text-center">{MultilingualText.title}</div>
                    <div className="text-white text-3xl text-justify">
                        {MultilingualText.paragraph_one}<br /><br />
                        {MultilingualText.paragraph_two}
                    </div>
                </div>
            </div>
            <Image className={'absolute -right-48'} src="/bandeiras-multilingual-classificador.svg" alt="Bandeiras multilingual" width={800} height={600} />
        </section>
    )
}

export default Multilingual;
