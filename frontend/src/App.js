import React, {useEffect, useState} from 'react';
import axios from "axios";

const App = () => {
    const [cars, setCars] = useState([])
    useEffect(()=>{
        axios.get('/api/cars').then(value => value.data).then(value => setCars(value.data))
    }, [])
    return (
        <div>
            {cars.map(value => <div key={value.id}>{JSON.stringify(value)}</div>)}
        </div>
    )
};

export default App;