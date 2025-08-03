export const sendCalculation = async (calculation) => {
    try {
        const response = await fetch("http://localhost:5000", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ "expression": calculation })
        });

        if (!response.ok) {
            let errorData;
            try {
                errorData = await response.json()
            }
            catch {
                return {error: true, message: "Something went wrong :("}
            }
            return errorData
        }
        const result = await response.json();
        return result;
    }
        catch(error) {
            return {error: true, message: error.message}
        }
    }