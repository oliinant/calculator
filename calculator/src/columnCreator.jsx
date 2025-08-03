export const columnCreator = ( columnNameList, hashmap ) => {
    let columnList = []

    for (const nameColumn of columnNameList) {
        const column = []

        for (const buttonName of nameColumn) {
            if (hashmap[buttonName]) {
                column.push(hashmap[buttonName])
            };
        };
        columnList.push(column);
    };

    return columnList
}