const API_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&apikey='
const apiKey = 'J2XCAJ3FZB9VJ54M'
// `https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey=${apiKey}`;

/**
 * Filtra dados JSON com base em um intervalo de datas.
 *
 * @param {Object} jsonData - Dados JSON originais para filtrar.
 * @param {string} startDate - A data inicial do intervalo de datas no formato YYYY-MM-DD.
 * @param {string} endDate - A data final do intervalo de datas no formato YYYY-MM-DD.
 *
 * @return {Object} filteredData - Um objeto contendo os dados JSON filtrados que estão dentro do intervalo de datas especificado.
 */
function filterDataByDateRange(jsonData, startDate, endDate) {
    const filteredData = {};
    for (const date in jsonData) {
        if (date >= startDate && date <= endDate) {
            filteredData[date] = jsonData[date];
        }
    }
    return filteredData;
}

/**
 * Obtenha uma série temporal de um ativo específico dentro de um intervalo de datas.
 *
 * @param {string} inputSymbol - O símbolo do ativo para o qual recuperar a série temporal.
 * @param {string} startDate - A data inicial do intervalo de datas no formato YYYY-MM-DD.
 * @param {string} endDate - A data final do intervalo de datas no formato YYYY-MM-DD.
 *
 * @return {Promise<Object>} - Retorna uma Promise que resolve para um objeto que contém a série temporal para o ativo especificado.
 *
 * @throws {Error} - Lança um erro se a API atingir o limite de uso por minuto ou se houver algum problema ao buscar os dados.
 */
export async function getSymbolTimeSeries(inputSymbol, startDate, endDate) {
    startDate = formatDate(startDate)
    endDate = formatDate(endDate)
    try {
        console.log(startDate, endDate, 'asdsad')
        let url = `${API_URL}${apiKey}&symbol=${inputSymbol}`;
        const response = await fetch(url, {
            method: 'GET',
            
        })

        const json = await response.json()
        console.log(json)
        if (json.detail) {
            throw new Error(json.detail)
        } else {
            if (json.hasOwnProperty('Meta Data')) {
                json['Time Series (Daily)'] = filterDataByDateRange(json['Time Series (Daily)'], startDate, endDate)
                return json
            } else { throw new Error(json['Error Message'])}
        }
    } catch (error) {
        console.error(error)
        throw new Error('Erro ao buscar os dados do código de identificação')
    }
}

function formatDate(date) {
    const [day, month, year] = date?.split('/')
    return `${year}-${month}-${day}`
}