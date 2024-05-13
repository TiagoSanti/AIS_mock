const ClassificacaoCard = ({classification, identifier}) => {
    const titlesByClassification = ['Polaridade Emocional', 'Magnitude', 'Impacto Temporal']
    const textsByClassification = [
        [
            {text: 'Negativa', subText: ' negativa'},
            {text: 'Neutra', subText: ' neutra'},
            {text: 'Positiva', subText: ' positiva'},
        ],
        [
            {text: 'Baixo impacto', subText: ' de baixo impacto'},
            {text: 'Indefinida', subText: ' indefinida'},
            {text: 'Grande impacto', subText: ' de grande impacto'},
        ],
        [
            {text: 'Curto prazo', subText: ' de curto prazo'},
            {text: 'Indefinida', subText: ' indefinida'},
            {text: 'Longo prazo', subText: ' de longo prazo'},
        ]
    ]

    return (
        <>
            {classification && <>
                <div className={'flex-1 mt-8 bg-primary p-10 rounded-3xl font-bold text-white mb-10  overflow-hidden'}>
                    <div className={'text-3xl text-center text-secondary'}>{titlesByClassification[identifier]}</div>
                    <div className={'text-4xl font-bold text-center my-10'}>
                        {textsByClassification[identifier][parseInt(classification?.prediction_index)].text}
                    </div>
                    <div className={'text-xl mt-10'}>
                        <div className={'mb-5 text-third'}>
                            <span>Confiabilidade da classificação: 
                                <span className={'font-bold ml-2'}>{classification?.prediction_probatility}</span>
                            </span>
                        </div>
                        <div className={'my-4 pb-2'}>
                            <div className={'mb-4'}>
                                As palavras-chave que levaram o Tuiaia a classificar essa notícia como
                                <span className={'font-bold'}>
                                    {textsByClassification[identifier][parseInt(classification?.prediction_index)].subText}
                                </span> foram:
                            </div>
                            {classification?.influential_words.map((word, index) => (
                                <div key={index} className={'inline-block text-xl m-2 bg-white w-fit p-2 rounded-full'}>
                                    <span className={'font-bold text-black'}>{word}</span>
                                </div>
                            ))}
                        </div>
                    </div>
                </div>
            </>
            }
        </>
        
    )
}

export default ClassificacaoCard