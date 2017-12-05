import React from 'react';
import ReactDOM from 'react-dom';
import Slider from 'react-slick';

import './ExampleSlide.css';



var ExampleSlide = React.createClass({
    render: function() {
        var settings = {
          dots: true
      }
      return (
          <div className='container'>
            <Slider {...settings}>
              <div><img src='http://placekitten.com/g/400/200' /></div>
            <div><img src='http://placekitten.com/g/400/200' /></div>
            <div><img src='http://placekitten.com/g/400/200' /></div>
            <div><img src='http://placekitten.com/g/400/200' /></div>
          </Slider>
        </div>
      );
    }
});

ReactDOM.render(
    <ExampleSlide/>,
    document.getElementById('root')
  );
  

// export default ExampleSlide;