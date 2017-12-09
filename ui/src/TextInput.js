import React from 'react';

class TextInput extends React.Component{
    constructor(props){
        super(props);
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange( event ){
        const target = event.target;
        // console.log(target);     // basically the entire <input> tag with changed "value"
        this.props.onChange( target.value );
    }

    render() {
        return(
            <div className="form-group">
                <label className="control-label">{this.props.label}</label>
                <input type="text" className="form-control"
                    name={this.props.name} value={this.props.value}
                    placeholder={this.props.example}
                    onChange={this.handleChange}></input>
            </div>
        )
    }
}

export default TextInput;