//-rename file
fs.rename(filePath,`${dirPath}/fruit.txt`,(err)=>
{
    if(!err)
    {
        console.log("file updated successfully!")
    }
})
