import logo from './logo.svg';
import './App.css';
import Typical from "react-typical"
import WebcamCapture from "./WebcamCapture"

document.body.style = 'background: #e1f7e7;';

function App() {
  
  return (
    <div className="App">
      <div className="Into">
        {/* <Typical
          loop={1}
          wrapper="b"
          steps={
            [ 'Hello there!', 1000,
              'My name is arnob!', 2000
            ]
          }
          >

        </Typical> */}

        <WebcamCapture>

        </WebcamCapture>
        
      </div>
      
    </div>
  );
}

export default App;
