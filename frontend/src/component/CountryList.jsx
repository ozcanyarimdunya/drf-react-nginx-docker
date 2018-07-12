import React, {Component} from 'react';

import CountryItem from "./CountryItem";
import api from '../utils/api'


class CountryList extends Component {
    constructor(props) {
        super(props);
        this.state = {
            countries: []
        }
    }

    componentDidMount() {

        fetch(api.country, {})
            .then(resp => resp.json())
            .then(data => {
                this.setState({countries: data})
            })
            .catch(error => console.log(error));
    }

    render() {
        return (
            <ul>
                {
                    this.state.countries.map((item, index) => <CountryItem key={index} text={item.name}/>)
                }
            </ul>
        );
    }
}

export default CountryList;