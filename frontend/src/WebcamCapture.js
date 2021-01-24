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
    const [age, setAge] = useState('')
    const [gender, setGender] = useState('')
    const [race, setRace] = useState('')
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

    const addData = (event) => {
      event.preventDefault()
      const newData = {
        a: age,
        g: gender,
        r: race
      }
      axios.post('http://127.0.0.1:5000/predictManuel', newData)
    }

    const handleAgeChange = (event) => {
      setAge(event.target.value)
    }
    const handleGenderChange = (event) => {
      setGender(event.target.value)
    }
    const handleRaceChange = (event) => {
      setRace(event.target.value)
    }
    if (display) {
      return (
        <div>
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
          <form onSubmit={addData} className='button2'>
              Age: <input value={age} onChange={handleAgeChange} className="formElement"/>
              Gender: <input value={gender} onChange={handleGenderChange} className="formElement"/>
              Race: <input value={race} onChange={handleRaceChange} className="formElement"/>
              <button type="submit">save</button>
            </form> 
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