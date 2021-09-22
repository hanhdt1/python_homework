function changeColor(){
    document.getElementById("paragraph1").style.color="#059862";
    document.getElementById("paragraph2").style.color="yellow";
    document.getElementById("paragraph3").style.color="red";
}

function changeBgColor(color){
    document.getElementsByTagName("body")[0].style.backgroundColor = color
}

function copyContent(paragraph1, paragraph2){
    if(paragraph1 == paragraph2){
        alert("Bạn cần chọn 2 đoạn văn khác nhau để thấy sự thay đổi nhé!");
        return;
    }
    document.getElementsByTagName("p")[paragraph1].innerHTML = document.getElementsByTagName("p")[paragraph2].innerHTML
}

function changeFontSize(x){
    for(i=0; i<3; i++){
        document.getElementsByTagName("p")[i].style.fontSize = x+"px";
    }    
}

function increaseFontSize(paragraph){
    let fontSize = window.getComputedStyle(document.getElementsByTagName("p")[paragraph], null).getPropertyValue("font-size");
    fontSize = parseFloat(fontSize); 
    fontSize += 1;
    if(fontSize > 30){
        alert("Bạn không được tăng font size vượt quá 30px");
    }
    else{
        document.getElementsByTagName("p")[paragraph].style.fontSize = fontSize+"px";
    }
}

function decreaseFontSize(paragraph){
    let fontSize = window.getComputedStyle(document.getElementsByTagName("p")[paragraph], null).getPropertyValue("font-size");
    fontSize = parseFloat(fontSize); 
    fontSize -= 1;
    if(fontSize < 10){
        alert("Bạn không được giảm font size dưới 10px");
    }
    else{
        document.getElementsByTagName("p")[paragraph].style.fontSize = fontSize+"px";
    }
}
