const answers = [
    "It  is certain",
    "Without a doubt",
    "It is decidedly so",
    "You may rely on it",
    "Yes definitely",
    "As I see it, yes.",
    "Cannot predict right now.",
    "Do not count on it.",
    "My sources say no.",
    "Ask again later.",
    "Signs point to yes.",
    "Outlook not so good."
]

document.getElementById("response").innerHTML=answers

function myFunction() {
    answers.sort(function(a,b){return 0.5 - Math.random()});
    document.getElementById("response").innerHTML=answers[0];
    document.getElementById("response").style.fontSize="40px";
}
