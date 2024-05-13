const API_URL = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&apikey='
const apiKey = 'J2XCAJ3FZB9VJ54M'
// `https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=tesco&apikey=demo`;

export async function getEmlpoyeeOptions(employee) {
    try {
        console.log(employee)
        let url = `${API_URL}${apiKey}&keywords=${employee}`;
        const response = await fetch(url, {
            method: 'GET',
        })
        const json = await response.json()
        console.log(json)
        if (!json.hasOwnProperty('Error Message')) {
            return json
        } else {
            throw new Error(json['Error Message'])
        }
    } catch (error) {
        console.error(error)
        throw new Error('Erro ao buscar os dados do código de identificação')
    }
}
