let character = document.getElementById("character");
let police = document.getElementById("police");

function jump(){
    if(character.classList == "animate"){return}
    character.classList.add("animate");
    setTimeout(function(){
        character.classList.remove("animate");
    }, 300);

}

function startGame(){
    police.classList.add("startGame");
}

document.write("Double click game to start!");

let checkDead = setInterval(function() {
    let characterTop = parseInt(window.getComputedStyle(character).getPropertyValue("top"));
    let blockLeft = parseInt(window.getComputedStyle(police).getPropertyValue("left"));
    if(blockLeft<20 && blockLeft>-20 && characterTop>=130){
        police.style.animation = "none";
        alert("Game Over. score: "+Math.floor(counter/100));
        counter=0;
        police.style.animation = "block 1s infinite linear";
    }else{
        counter++;
        document.getElementById("scoreSpan").innerHTML = Math.floor(counter/100);
    }
}, 10);

