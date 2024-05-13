import FlipNumbers from 'react-flip-numbers';
import { FormControl, InputLabel, Select, MenuItem } from '@mui/material'

const Introducao = ({ news }) => {

    return <section className={'bg-white text-primary flex flex-col items-center w-full p-10'}>
        <div className={'text-7xl font-bold'}>
            Dashboard
        </div>
        <div className={'text-5xl flex items-center justify-center flex-col'}>
            <div className={'my-10'}>Notícias classificadas</div>
            <div id={'flipBox'} className={'mb-10'}>
                <FlipNumbers height={70} width={70} color='white' background='#043475' numberStyle={{ fontSize: 40 }} play numbers={(news? news.length : 0) + ''} />
            </div>
        </div>
    </section>
}

export default Introducao