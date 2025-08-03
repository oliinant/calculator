export function Button({ buttonValue, buttonDisplay, height, onClick }) {


    return (
        <div>
            <button
                type="button"
                value={buttonValue}
                onClick={onClick}
                className={`relative mb-[4px] w-[50px] ${height} border-[4px] border-[white] rounded-[12px] bg-auto hover:bg-[#4A4A4A]`}
            >
                {buttonDisplay}
            </button>
        </div>
    );
};