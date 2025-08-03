import './App.css'
import { useState } from 'react'
import { numberButtonsCreator } from './numberButtonCreator'
import { symbolButtonsCreator } from './symbleButtonCreator'
import { buttonHashmapCreator } from './buttonHashmapCreator'
import { columnCreator } from './columnCreator'
import { Button } from './Button'
import { specialButtonsCreator } from './specialButtonCreator'
import { resultHandler }  from "./calculationResult"

function App() {
  const [calculation, setCalculation] = useState("")
  const [result, setResult] = useState({})
  console.log(result)

  const numberButtonList = numberButtonsCreator(setCalculation)
  const symbolButtonList = symbolButtonsCreator(setCalculation, calculation, setResult)
  const specialButtonsList = specialButtonsCreator(setCalculation, setResult)

  const numberButtonHashmap = buttonHashmapCreator(
    ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
    numberButtonList
  )
  const symbolButtonHashmap = buttonHashmapCreator(
    ["point", "addition", "subtraction", "multiplication", "division", "equals"],
    symbolButtonList
  )
  const specialButtonHashmap = buttonHashmapCreator(
    ["DEL", "AC"],
    specialButtonsList
  )

  const numberColumns = columnCreator( [["seven", "four", "one", "zero"], ["eight", "five", "two"], ["nine", "six", "three"]],
    numberButtonHashmap
  )
  const symbolColumn = columnCreator(
    [["addition", "subtraction", "multiplication", "division"]],
    symbolButtonHashmap
  )
  const specialColumn = columnCreator(
    [["DEL", "AC"]],
    specialButtonHashmap
  )


  return (
    <div className="flex justify-center items-center h-screen">

      <div className="bg-[#222222] py-[30px] px-[15px] rounded-[20px]">

        {/* Display */}
        <div className="w-[236px] h-[85px] mb-[30px] bg-[white] rounded-[15px]">
          <div className="overflow-x-auto whitespace-nowrap w-full p-[10px]">
            <p>{calculation}</p>
          </div>

          {/* Result */}
          <div className="flex justify-end p-[10px]">
            <p>{result}</p>
          </div>
        </div>

      
        {/* Special buttons */}
        <div className="flex space-x-[12px] justify-end">
          {specialColumn[0]}
        </div>

        {/*Main buttons*/}
        <div className="flex space-x-[12px]">
          <div>
            {numberColumns[0]}
          </div>

          <div>
            {numberColumns[1]}
            {symbolButtonHashmap.point}
          </div>

          <div>
            {numberColumns[2]}
            {symbolButtonHashmap.equals}
          </div>

          <div>
            {symbolColumn[0]}
          </div>
        </div>
      </div>

    </div>
  )
}

export default App
