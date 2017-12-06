import React, { Component } from 'react';
// import ExampleSlide from './ExampleSlide.js';
import UserInput from './UserInput.js';
import './App.css';

import $ from 'jquery';


class App extends Component {
  // if subclass has consturcotr,
    // it must first call super() before using "this"
    constructor(props){
      // superclass "React.Component" constructor 
      super(props);

      // class constructor 
      this.state = {
        runtime : "194", 
        director : "James Cameron",
        genre1 : 'Romance',
        genre2 : 'Drama',
        genre3 : '(no genres listed)',
        poster_url : 'http://img.moviepostershop.com/titanic-movie-poster-1997-1020339699.jpg'
      };

      this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit( rt, dir, gnr1,gnr2,gnr3, url ){
    const newInput = { runtime : rt, director : dir, 
      genre1 : gnr1,genre2 : gnr2,genre3 : gnr3, poster_url : url };
    this.setState( newInput );
  }

  render() {

    var predictData = $.ajax({
      type: "GET",
      url: "http://localhost:7777/predict?runtime=" + this.state.runtime 
        + "&director=" + this.state.director 
        + "&genre1=" + this.state.genre1 
        + "&genre2=" + this.state.genre2
        + "&genre3=" + this.state.genre3         
        + "&image_url=" + this.state.poster_url,
      async: false
    })
    console.log("Prediction Data:")
    console.log(predictData)

    // Parse data from here

    var myData = predictData.responseText
    console.log("JSON Response:")
    console.log(myData)

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
