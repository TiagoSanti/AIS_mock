import { useEffect, useState } from 'react';
import { Chart } from 'react-google-charts';

const PieCharts = ({ news }) => {
    const [emotionData, setEmotionData] = useState([['Tipo', 'Cassificação'], ['Negativos', 0], ['Neutros', 0], ['Positivos', 0]])
    const [impactData, setImpactData] = useState([['Tipo', 'Cassificação'], ['Curto prazo', 0], ['Indeterminado', 0], ['Longo prazo', 0]])
    const [magnitudeData, setMagnitudeData] = useState([['Tipo', 'Cassificação'], ['Pequeno impacto', 0], ['Indeterminado', 0], ['Grande impacto', 0]])
    const [newsLength, setNewsLength] = useState(0)


    useEffect(() => {
        if (news?.length > 0) {
            const newsSliced = news.slice(newsLength,)
            newsSliced?.map((data) => {
                emotionData[data.classification.sentiment+1][1]++
                impactData[data.classification.term+1][1]++
                magnitudeData[data.classification.intensity+1][1]++
            })
            setNewsLength(news.length)
        }
    }, [news])

    return <section className={'flex justify-center items-center w-[100%] m-auto gap-4 text-4xl text-secondary font-bold'}>
        <div className={'flex flex-col justify-center items-center flex-1'}>
            <div>
                Polaridade Emocional
            </div>
            <Chart
                chartType={'PieChart'}
                data={emotionData}
                options={{colors: ['#EB615C', '#c0bfbb', '#48B091']}}
                width={'100%'}
                height={'500px'}
                className={'flex-1'}
            />
        </div>
        <div className={'flex flex-col justify-center items-center flex-1'}>
            <div>
                Impacto Temporal
            </div>
            <Chart
                chartType={'PieChart'}
                data={impactData}
                options={{colors: ['#EB615C', '#c0bfbb', '#48B091']}}
                width={'100%'}
                height={'500px'}
                className={'flex-1'}
            />
        </div>
        <div className={'flex flex-col justify-center items-center flex-1'}>
            <div>
                Magnitude
            </div>
            <Chart
                chartType={'PieChart'}
                data={magnitudeData}
                options={{colors: ['#EB615C', '#c0bfbb', '#48B091']}}
                width={'100%'}
                height={'500px'}
                className={'flex-1'}
            />
        </div>
    </section>
}

export default PieCharts