import React, { Component } from 'react';
import ExampleSlide from './ExampleSlide.js';
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
        genres : [],
        actors : [],
        poster_url : 'http://img.moviepostershop.com/titanic-movie-poster-1997-1020339699.jpg'
      };

      this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit( rt, dir, gnr, actrs, url ){
    const newInput = { showInfo : true, runtime : rt, director : dir, 
      genres : gnr, actors : actrs, poster_url : url };
    this.setState( newInput );
  }

  render() {

    const showInfo = this.state.showInfo;
    let predictDisply = null;
    var posterDisplay = <ExampleSlide/>;

    if (showInfo) {
      var predictData = $.ajax({
        type: "GET",
        url: "http://localhost:7777/predict?runtime=" + this.state.runtime 
          + "&director=" + this.state.director 
          + "&genres=" + this.state.genres      
          + "&actors=" + this.state.actors                
          + "&image_url=" + this.state.poster_url,
        async: false
      })
      console.log("Prediction Data:")
      console.log(predictData)

      var myData = predictData.responseText
      console.log("JSON Response:")
      console.log(myData)

    
      // error check
      if(myData === " url "){
        predictDisply = <div><h2>Oops, please check poster URL input!</h2></div>;
      } else if (myData === " runtime "){
        predictDisply = <div><h2>Oops, please check your runtime input!</h2></div>;
      } else if (myData.charAt(0) === '<'){
        predictDisply = <div><h2>Sorry, our actors list is currently unstable!
          <br/>Please choose different actor(s).</h2></div>;
      } else{
        // format output
        var rating = myData.substring(1, myData.length - 1 )
        predictDisply = <div><h2>Predicted Rating: </h2> {rating}</div>;
      }
      posterDisplay = <div><img alt='poster' src={this.state.poster_url}/></div>;
    }

    return (
      <div className="page-display">
        <div className='left-half'>
          {posterDisplay}
        </div>
        <div className='right-half'>
          <h1>Movie Rating Prediction</h1>
          <UserInput onSubmit={this.handleSubmit}/>
          <br/>
          {predictDisply}  
        </div>
      </div>
    );
  }
}

export default App;
