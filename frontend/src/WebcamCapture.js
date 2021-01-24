import React from "react"
import {useState} from "react"
import Webcam from "react-webcam"
import "./Camera.css"
import axios from 'axios'
import {ImagePicker} from "react-file-picker"

const Camera = () => {
    var webcamRef = React.useRef(null);
    const [imgSrc, setImgSrc] = React.useState(null);
    const [display, setDisplay] = useState(true);
    const capture = React.useCallback(() => {
      const imageSrc = webcamRef.current.getScreenshot();
      console.log(imageSrc)
      setImgSrc(imageSrc);
      setDisplay(false)
      
    }, [webcamRef, setImgSrc]);


    
    
    

    const retake = () => {
      setDisplay(true)
    }

    const proc = () => {
      const imgObject = {
        img: imgSrc
      }
      axios.post('http://127.0.0.1:5000/predict', imgObject)
    }

    if (display) {
      return (
        <div className="body">
            <div className="cam">
              <Webcam
                audio={false}
                ref={webcamRef}
                screenshotFormat="image/jpeg"
                forceScreenshotSourceSize="true"
              />
            </div>
        
          <button onClick={capture}>Capture photo</button>
          <ImagePicker
            extensions={['jpg', 'jpeg']}
            dims={{minWidth: 100, maxWidth: 3800, minHeight: 100, maxHeight: 3800}}
            onChange={base64 => {
              console.log(base64)
              setImgSrc(base64)
              setDisplay(false)
            }}
            onError={base64 => console.log(base64)}
          >
            <button>
              Click to upload image
            </button>
          </ImagePicker>
                </div>
      );
    }
    else {
      return (
        <div className="body">
          {imgSrc && (
            <img className="displayImage"
              src={imgSrc}
            />
          )}
          <div className="buttonBlock">
          <button onClick={retake}>Retake</button>
          <button onClick={proc}>Proceed</button>

          </div>

        </div>
      )
    }
  };

export default Camera