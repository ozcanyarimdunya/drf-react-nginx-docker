import React, {Component} from 'react';

class CountryItem extends Component {
    render() {
        return (
            <li>{this.props.text}</li>
        );
    }
}

export default CountryItem;