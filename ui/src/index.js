import React from 'react';
import ReactDOM from 'react-dom';
import './stylesheet.css';
import App from './App';
// import ExampleSlide from './ExampleSlide';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(
    // <ExampleSlide/>,
    <App />, 
    document.getElementById('root')
);
registerServiceWorker();
