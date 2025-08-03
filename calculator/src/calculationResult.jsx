export async function resultHandler(result, setCalculation, setResult) {
    if (result.error) {
        setCalculation(result.message)
        setResult("")
    } else if (result.wasShortend) {
        setResult(
            <>
                {result.solution}*10<span className="relative -top-[8px]">{result.squaringNum}</span>
            </>
        );
    } else {
        setResult(result.solution)
    }
}