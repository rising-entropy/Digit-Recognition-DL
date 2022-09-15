import React, {useState,useEffect, useRef} from 'react'
import axios from "axios"
import CanvasDraw from "react-canvas-draw";
import ProjectChart from './ProjectChart';

export default function ProjectCanvas() {

    const [imageBase64, setImageBase64] = useState("")
    const [prediction, setPrediction] = useState([])
    const [loading, setLoading] = useState(false)
    const canvasDraw = useRef(null);

    const eraseCanvas = () => {
        canvasDraw.current.eraseAll()
        setPrediction([])
    }

    const undoCanvas = () => {
        canvasDraw.current.undo()
        setPrediction([])
    }

    const submitCanvas = async() =>{
        setLoading(true);
        let base64 = canvasDraw.current.canvasContainer.childNodes[1].toDataURL();
        console.log(base64)
        if(base64 === "data:image/png;base64,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"){
            alert("Please draw a Digit Before Submit");
            setLoading(false)
            return;
        }

        console.log(base64.split("data:image/png;base64,")[1])

        setImageBase64(base64);
        axios.post("https://digit-recognition-backend.devangk.dev/recognize-digit",{
            image: base64.split("data:image/png;base64,")[1]
        }, {
            headers: {
                'Content-Type': 'application/json'
            }
        }).then((response)=>{
            let prediction = response.data.prediction
            setPrediction(prediction)
            console.log(prediction)
            setLoading(false)
        }).catch((err)=>{
            console.log(err);
            alert("Some Error Occurred!")
            setLoading(false)
        })
    }

    const getDigitFromPrediction = (pred) => {
        let maxIndex = -1;
        let maxNumber = -1;
        pred.forEach((element, ind) => {
            if(element>maxNumber){
                maxIndex = ind;
                maxNumber = element;
            }
        });
        return maxIndex
    }

  return (
    <div className='container container-fluid text-center'>
        <div className="row text-center" style={{margin: '1rem auto'}}>
            <div className="col-lg-4 col-md-3 col-sm-0">

            </div>
            <div className="col-lg-4 col-md-6 col-sm-12">
                <div className="container container-fluid">
                    <div className="row">
                        <CanvasDraw ref={canvasDraw} backgroundColor='white' brushColor='black' hideGrid={true} brushRadius={15} style={{boxShadow:"0 13px 27px -5px rgba(50, 50, 93, 0.25), 0 8px 16px -8px rgba(0, 0, 0, 0.3)"}} />
                    </div>
                    <div className="row text-center" style={{margin: '2rem auto'}}>
                        <div className="col-4 text-center">
                            <button disabled={loading} style={{padding: '0.6rem 2rem'}} className='btn btn-lg btn-danger' onClick={eraseCanvas}>Clear</button>
                        </div>
                        <div className="col-4 text-center">
                            <button disabled={loading} style={{padding: '0.6rem 2rem'}} className='btn btn-lg btn-warning' onClick={undoCanvas}>Undo</button>
                        </div>
                        <div className="col-4 text-center">
                            <button disabled={loading} style={{padding: '0.6rem 2rem'}}  className='btn btn-lg btn-success' onClick={submitCanvas}>Submit</button>
                        </div>
                    </div>
                    <div className="text-center row" style={{margin: '1rem auto'}}>
                        {prediction.length > 0 ? <p className='roboto' style={{fontSize: '1.5rem'}} >The drawn digit is probably: {getDigitFromPrediction(prediction)}</p>: <></>}
                    </div>
                </div>
            </div>
            <div className="col-lg-4 col-md-3 col-sm-0">
                
            </div>
        </div>
        <div className="row text-center">
            {prediction.length > 0 ? <ProjectChart data={prediction}  /> : <></>}
        </div>
    </div>
  )
}
