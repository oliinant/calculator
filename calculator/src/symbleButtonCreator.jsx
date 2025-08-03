import { Button } from './Button.jsx';
import { sendCalculation } from "./sendCalculation.jsx";
import { resultHandler } from './calculationResult.jsx';

export const SymbolHashmap = () => {
    const line = "absolute w-[25px] h-[8px] bg-[white] rounded-[10px]";
    const centerLine = "top-[40%] right-[20%]";
    const dot = "absolute w-[10px] h-[10px] bg-[white] rounded-[50px]";
    const centerDot = "top-[40%] right-[38%]";

    const symbols = {
        ".": <div className={`${dot} ${centerDot}`}></div>,

        "+": <>
            <div className={`${line} ${centerLine}`}></div>
            <div className={`${line} ${centerLine} rotate-90`}></div>
        </>,

        "-": <div className={`${line} ${centerLine}`}></div>,

        "*": <>
            <div className={`${line} ${centerLine} rotate-45`}></div>
            <div className={`${line} ${centerLine} rotate-135`}></div>
        </>,

        "/": <>
            <div className={`${dot} right-[38%] top-[65%]`}></div>
            <div className={`${line} ${centerLine}`}></div>
            <div className={`${dot} right-[38%] bottom-[65%]`}></div>
        </>,

        "=": <>
            <div className={`${line} right-[20%] bottom-[55%]`}></div>
            <div className={`${line} right-[20%] top-[55%]`}></div>
        </>
    };

    return symbols
}

export const symbolButtonsCreator = (setCalculation, calculation, setResult) => {
    const symbols = SymbolHashmap()

    let symbolButtons = Object.entries(symbols).map(([symbol, display]) => {
        return <Button
            key={symbol}
            buttonValue={symbol}
            height={"h-[50px]"}
            buttonDisplay={display}
            onClick={symbol !== "=" 
                ? () => setCalculation(prev => prev + symbol) 
                : async () => {const result = await sendCalculation(calculation)
                  resultHandler(result, setCalculation, setResult)  
                }
            }
        />
    });

    return symbolButtons;
};
