<<<<<<< HEAD
import React, { useState } from 'react'
import './App.css';
import Typical from "react-typical"


document.body.style = 'background: #e1f7e7;';


const typicalStyle = {
  color: 'grey',
  fontWeight: 'bold',
  fontSize: 30,
  paddingLeft: 50,
  paddingRight: 50,
  paddingTop: 50,
  paddingBottom: 200
}


const Welcome = () => {
  return (
    <div>
      <h1>Welcome to the "Insert App Name Here"</h1>
      <div style={typicalStyle}>
        <Typical
            loop={1}
            wrapper="b"
            steps={
              [ 'Click the Start button below to be redirected to our convinent camera UI where you will take a picture of yourself!\nOnce you take an image of yourself, our custom trained Convulational Neural Network will identify your race, gender, and ethnicity!\nThe page will rerender to display how much effect your vote has on the electoral college!', 500,]
            }>
        </Typical>
      </div>
      
    </div>
  )
}

const CustomButton = ({handleClick}) => {
  return (
    <button onClick={handleClick}>
      Start
    </button>
  )
}



const App = () => {
  const [ pageState, setPageState ] = useState(0)
  
  const startToNext = () => {
    setPageState(1)
  }
  return (
    <div className="App">
      <div className="Into">
        <Welcome/>
      </div>
      <div>
        <div className="Start">
          <CustomButton handleClick={startToNext} />
        </div>
      </div>


      
    </div>
  );
}

export default App;
