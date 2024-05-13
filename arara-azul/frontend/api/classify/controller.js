import classifyNews from './classify-news-service'

export async function getNewsClassification(notice){
    return await classifyNews(notice)
}
