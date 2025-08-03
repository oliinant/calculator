export const buttonHashmapCreator = ( nameList, componentList ) => {
    let buttonHashmap = {};
    
    for (let i = 0; i < componentList.length; i++) {
        buttonHashmap[nameList[i]] = [componentList[i]];
    }

    return buttonHashmap
};