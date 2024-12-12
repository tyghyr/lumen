const b1 = document.getElementById("lgn-btn");
b1.addEventListener("mousedown", function(){
    b1.style.backgroundColor = "aliceblue";
    b1.style.color = "blue";
})

b1.addEventListener("mouseup", function(){
    b1.style.backgroundColor = "";
    b1.style.color = "";
})