import React, { Component } from 'react';
// import ExampleSlide from './ExampleSlide.js';
import UserInput from './UserInput.js';
import './App.css';
// also using Bootstrap CSS

import $ from 'jquery';


class App extends Component {
  // if subclass has consturcotr,
    // it must first call super() before using "this"
    constructor(props){
      // superclass "React.Component" constructor 
      super(props);

      // class constructor 
      this.state = {
        showInfo : false,
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
    const newInput = { showInfo : true, runtime : rt, director : dir, 
      genre1 : gnr1,genre2 : gnr2,genre3 : gnr3, poster_url : url };
    this.setState( newInput );
  }

  render() {

    const showInfo = this.state.showInfo;
    let predictDisply = null;

    if (showInfo) {
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

      var myData = predictData.responseText
      console.log("JSON Response:")
      console.log(myData)

      predictDisply = <div><h2>Predicted rating: </h2> {myData}</div>;    
    }

    return (
      <div className="page-display">
        <h1>Movie Rating Prediction</h1>
        {/* <ExampleSlide/> */}
        <UserInput onSubmit={this.handleSubmit}/>
        <br/><br/>
        {predictDisply}  
        {/* <OutputPrediction/> */}
      </div>
    );
  }
}

export default App;
