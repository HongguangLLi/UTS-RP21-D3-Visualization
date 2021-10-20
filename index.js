let fs = require("fs")

fs.readFile("./rank.json",(err,doc)=>{
    let arr = JSON.parse(doc.toString());
    let map = {};
    arr.forEach(d=>{
        map[d['title']] =  d.level;
        map[d['title-a']] = d.level;
    })
    console.log(map)
    fs.readFile("./data.json",(err1,doc1)=>{
        // inproceedings booktitle
        let data = JSON.parse(doc1.toString());
        let counter = 0;
        let rank = 0;
        data.forEach(d=>{
            delete d.ee;
            if(d.type === "inproceedings"){
                d.level = map[d.booktitle] || "undefined";
            }
        })
        fs.writeFile("./ndata.json",JSON.stringify(data),(err,doc)=>{})

    })
})
