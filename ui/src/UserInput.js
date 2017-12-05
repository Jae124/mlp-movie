import React from 'react';
import TextInput from './TextInput.js';

// import {Typeahead} from 'react-bootstrap-typeahead';

// Runtime- int
// Director- string
// Genre (pick 3)- ???
// poster image- url

class UserInput extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            runtime : '',
            director : '',
            genre : '',
            poster_url : ''
         }

        // ** methods not bound by default in JS -> without bound, 'undefined'
        // ** if method referred without (), need to bind that method
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleRuntimeChange = this.handleRuntimeChange.bind(this);
        this.handleDirectorChange = this.handleDirectorChange.bind(this);
        this.handleGenreChange = this.handleGenreChange.bind(this);
        this.handlePosterChange = this.handlePosterChange.bind(this);
        
    }

    // ** e is synthetic event
    handleSubmit( e ){
        // ** cannot return false like HTML- use preventDefault()
        e.preventDefault(); 
        console.log(this.state);
        this.props.onSubmit( this.state.runtime, this.state.director, this.state.genre, this.state.poster_url );
    }

    // => try to handle both events in one method with event.target
    // => see React doc- Forms
    handleRuntimeChange( val ){
        // ** don't modity state directly
        // ** constructor only place where you can assign "this.state" 
        // ** use setState() instead
        this.setState( { runtime : val  } );
        // ** there's another form - setState( function(prevState, props) )
    }

    handleDirectorChange( val ){
        this.setState( { director : val } );
    }

    handleGenreChange( val ){
        this.setState( { genre : val } );
    }

    handlePosterChange( val ){
        this.setState( { poster_url : val } );
    }
    
    render(){
        return(
            <div>
                <form className='card-form'>
                    <h2> Input parameters to predict rating </h2>
                    {
                    //** in JSX, pass ftn as event handlers, rather than string in HTML
                    }
                    <TextInput name="runtime" label="Runtime"
                        value={this.state.runtime}
                        onChange={this.handleRuntimeChange}/>  
                    <TextInput name="director" label="Director"
                        value={this.state.director}
                        onChange={this.handleDirectorChange}/>
                    <TextInput name="genre" label="Genre"
                        value={this.state.genre}
                        onChange={this.handleGenreChange}/>
                    <TextInput name="poster_url" label="Poster URL"
                        value={this.state.poster_url}
                        onChange={this.handlePosterChange}/>
                    <button className="btn btn-primary"
                        onClick={this.handleSubmit}>Submit</button>

                    {/* Name:
                    <input type="name"></input><br/>
                    Message:
                    <input type="message"></input> */}
                </form>
            </div>
        );
    }
}

export default UserInput;