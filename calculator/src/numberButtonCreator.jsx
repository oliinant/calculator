import { Button } from './Button.jsx';


export const numberButtonsCreator = (setCalculation) => {
    const numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    let numberButtons = numbers.map((n) => {
        return <Button
            key={n}
            buttonValue={n}
            height={"h-[50px]"}
            onClick={() => setCalculation(prev => prev + n)}
            buttonDisplay={
                <span className="absolute top-[45%] translate-y-[-50%] translate-x-[-50%] font-bold text-[40px] text-[white]">
                    {n}
                </span>
            }
        />
    });
    return numberButtons;
};