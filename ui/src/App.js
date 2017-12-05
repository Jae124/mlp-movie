import React, { Component } from 'react';
// import ExampleSlide from './ExampleSlide.js';
import UserInput from './UserInput.js';
import './App.css';

// import $ from 'jquery';


class App extends Component {
  // if subclass has consturcotr,
    // it must first call super() before using "this"
    constructor(props){
      // superclass "React.Component" constructor 
      super(props);

      // class constructor 
      this.state = {
          input: [
              {
                  runtime : "194", 
                  director : "James Cameron",
                  genre : 'Romance',
                  poster_url : 'http://img.moviepostershop.com/titanic-movie-poster-1997-1020339699.jpg'
              }
          ]
      };

      this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit( rt, dir, gnr, url ){
    const newInput = [{ runtime : rt, director : dir, genre : gnr, poster_url : url }];
    this.setState( { input: newInput} );
  }

  render() {

    // var predictData = $.ajax({
    //   type: "GET",
    //   url: "http://localhost:7777/predict?runtime=###&director=#######&genre=####&poster_url=####",
    //   async: false
    // })
    // console.log(predictData)

    // // Parse data from here

    // var myData = predictData.responseJSON
    // console.log(myData)

    return (
      <div>
        {/* <ExampleSlide/> */}
        <UserInput onSubmit={this.handleSubmit}/>
        {/* <OutputPrediction/> */}
      </div>
    );
  }
}

export default App;
