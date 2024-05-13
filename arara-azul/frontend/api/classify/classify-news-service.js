const url = 'http://35.199.123.76/'

export default async function classifyNews(news) {
    try{
        const timeout = 60000
        const controller = new AbortController();
        const idTimer = setTimeout(() => controller.abort(), timeout);
        
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({news: news}),
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
        alert('Ocorreu um erro ao classificar a notícia')
    }
}
