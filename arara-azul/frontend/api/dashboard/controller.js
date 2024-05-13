import { getSymbolTimeSeries } from './find-cotations-by-name-service'
import { getEmlpoyeeOptions } from './find-employee-options-service'

export async function findEmployeeOptions(employee) {
    return await getEmlpoyeeOptions(employee)
}

export async function findCotationsByName(name, start_date, end_date) {
    return await getSymbolTimeSeries(name, start_date, end_date)
}

