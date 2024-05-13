let url = 'http://35.199.123.76/feed'

export default async function findAllNews(start_date, end_date) {
    try{
        
        if (start_date && end_date) {
            url = `${url}?startdate=${start_date}&enddate=${end_date}`
        }

        const timeout = 30000
        const controller = new AbortController();
        const idTimer = setTimeout(() => controller.abort(), timeout);

        const response = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            signal: controller.signal
        })
        
        clearTimeout(idTimer);
        const json = await response.json()
        
        if (json.detail) {
            throw new Error(json.detail)
        } else {
            return json
        }
    } catch (error) {
        if (error.name === 'AbortError') {
            alert('Ocorreu um erro ao tentar buscar as notícias')
            return []
        } else {
            
        }
    }
}
