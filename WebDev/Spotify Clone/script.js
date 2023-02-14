console.log("welcome to Spotify");

//initialize the variable
let soundIndex=0;
let audioElement =  new Audio('songs/1.mp3');
let masterPlay = document.getElementById('masterPlay');
let myprogressBar = document.getElementById('myProgressBar');
let gif= document.getElementById('gif');
let masterSongName = document.getElementById('masterSongName');
let songItems= Array.from(document.getElementsByClassName('songItem'));
let songs=
[
{songName:"salam-e-Ishq",filePath:"songs/1.mp3",coverPath:"covers/1.jpg"},
{songName:"sa",filePath:"songs/2.mp3",coverPath:"covers/2.jpg"},
{songName:"salam-e-Ishq",filePath:"songs/3.mp3",coverPath:"covers/3.jpg"},
{songName:"salam-e-Ishq",filePath:"songs/4.mp3",coverPath:"covers/4.jpg"},
{songName:"salam-e-Ishq",filePath:"songs/5.mp3",coverPath:"covers/5.jpg"},
{songName:"salam-e-Ishq",filePath:"songs/6.mp3",coverPath:"covers/6.jpg"},
{songName:"salam-e-Ishq",filePath:"songs/7.mp3",coverPath:"covers/7.jpg"},
{songName:"salam-e-Ishq",filePath:"songs/8.mp3",coverPath:"covers/8.jpg"},
{songName:"salam-e-Ishq",filePath:"songs/9.mp3",coverPath:"covers/9.jpg"},
{songName:"salam-e-Ishq",filePath:"songs/10.mp3",coverPath:"covers/10.jpg"}
]

songItems.forEach((element, i)=>{
    // console.log(element,i);
    element.getElementsByTagName("img")[0].src=songs[i].coverPath;
    element.getElementsByClassName('songName')[0].innerText=songs[i].songName;

    
});
// audioElement.play();

//handle play/pause click
masterPlay.addEventListener('click',()=>{
    if(audioElement.paused||audioElement.currentTime<=0)
    {
        audioElement.play();
        masterPlay.classList.remove('fa-circle-play');
        masterPlay.classList.add('fa-circle-pause');
        gif.style.opacity=1;

    }
    else
    {
        audioElement.pause();
        masterPlay.classList.remove("fa-circle-pause");
        masterPlay.classList.add('fa-circle-play');
        gif.style.opacity=0;
    }
});

//listen to Events
   audioElement.addEventListener('timeupdate',()=>{
    console.log('timeupdate')
  //update Seeker
progress = parseInt((audioElement.currentTime/audioElement.duration)*100);
console.log(progress);
myprogressBar.value=progress;
});

//updating audio on seeking
myprogressBar.addEventListener('change',()=>{
    audioElement.currentTime=myprogressBar.value*audioElement.duration/100;
});

const makeAllPlays=()=>
{
    Array.from(document.getElementsByClassName('sPlay')).forEach((element)=>
    {
        element.classList.remove('fa-circle-pause');
        element.classList.add('fa-circle-play');
    });
}

//playing on clicking on play button in front of songs

Array.from(document.getElementsByClassName('sPlay')).forEach((element)=>
{
    element.addEventListener('click',(e)=>
    {
        makeAllPlays();
        songIndex = parseInt(e.target.id);
        e.target.classList.remove('fa-circle-play');
        e.target.classList.add('fa-circle-pause');
        audioElement.src=`songs/${songIndex+1}.mp3`;
        masterSongName.innerText=songs[songIndex].songName;
        audioElement.currentTime=0;
        audioElement.play();
        gif.style.opacity = 1;
        masterPlay.classList.remove('fa-circle-play');
        masterPlay.classList.add('fa-circle-pause');
    })
});

document.getElementById('next').addEventListener('click', ()=>{
    if(songIndex>=9){
        songIndex = 0
    }
    else{
        songIndex += 1;
    }
    audioElement.src = `songs/${songIndex+1}.mp3`;
    masterSongName.innerText = songs[songIndex].songName;
    audioElement.currentTime = 0;
    audioElement.play();
    masterPlay.classList.remove('fa-play-circle');
    masterPlay.classList.add('fa-pause-circle');

})

document.getElementById('previous').addEventListener('click',()=>
{
    if(songIndex<=0)
    {
        songIndex=0;
    }
    else
    {
        if(songIndex<=0)
        {
            songIndex = 0;
        }
        else
        {
            songIndex -= 1;
        }
        audioElement.src = `song/${songIndex+1}.mp3`;
        masterSongName.innerText = songs[songsIndex].songName;
        audioElement.play();
        masterPlay.classList.remove('fa-circle-play');
        masterPlay.classList.add('fa-circle-pause');

    }
})