import findAllNews from '@/api/feed/find-all-news'

export async function getAllNewsClassifieds(start_date, end_date){
    return await findAllNews(start_date, end_date)
}