
const getFetch = async function() {
    try {
        const res = await fetch('http://0.0.0.0:8000/api/number/get/');
        const json = await res.json();
        const numberArr = [];

        for (const prop in json) {
            console.log(`obj.${prop} = ${json[prop].name}`);
            numberArr.push(json[prop].number)
        }
        
        console.log(numberArr)

        return numberArr;

    } catch (error) {
        return console.log(error)
    }
    
}

module.exports = {
    getFetch,

};

//getFetch()