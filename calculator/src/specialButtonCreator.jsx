import { Button } from "./Button"

export const specialButtonsCreator = (setCalculation, setResult) => {

    const specialButtonsHash = {
        "DEL": () => setCalculation(prev => prev.slice(0, -1)),
        "AC": () => (setCalculation(""), setResult(""))
    };

    let specialButtons = Object.entries(specialButtonsHash).map(([buttonName, functionality]) => {
        return <Button
            key={buttonName}
            buttonValue={buttonName}
            height={"h-[30px]"}
            onClick={functionality}
            buttonDisplay={
            <span className="absolute top-[45%] translate-y-[-50%] translate-x-[-50%] font-bold text-[18px] text-[white]">
                {buttonName}
            </span>
        }
        />
    });

    return specialButtons


}