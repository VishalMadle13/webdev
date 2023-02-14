function Style1()
{
    if(document.getElementById('LotusText').style.fontSize!='20px')
    {
        document.getElementById('LotusText').style.fontSize="20px";
        document.getElementById('LotusText').style.fontFamily="'Cambria',sans-serif";
        document.getElementById('LotusText').style.fontWeight="bold";
        document.getElementById('LotusText').style.color="red";
    }
    else
    {
         document.getElementById('LotusText').style.fontSize="15px";
         document.getElementById('LotusText').style.fontFamily="'Courier New',sans-serif";
         document.getElementById('LotusText').style.fontWeight="100";
         document.getElementById('LotusText').style.color="black";

    }
    
}

