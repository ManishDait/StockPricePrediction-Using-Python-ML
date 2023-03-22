isDark = false;
let root = document.querySelector(':root')
function closeMenu(){
    document.getElementById("menu_p").classList.toggle('active');
    document.getElementById("ham").classList.toggle('active')
    document.getElementById("drop_down").classList.toggle('active');
    document.getElementById("table_box").classList.toggle('active');
    document.getElementById("table_box4").classList.toggle('active');
    document.getElementById("menu_p2").classList.toggle('active');
    document.getElementById("drop_down2").classList.toggle('active');
    document.getElementById("btn").classList.toggle('active');
    document.getElementById("dash").classList.toggle('active');
}

function toggleDropDown(){
    document.getElementById("option").classList.toggle('active');
}

function toggleDropDown2(){
    document.getElementById("option2").classList.toggle('active');
}

function toggleDark(){
    if(!isDark){
        document.getElementById("dark").innerHTML="brightness_high";
        document.documentElement.style.setProperty('--body-background','rgb(19, 19, 19)')
        document.documentElement.style.setProperty('--text-color','rgb(255, 255, 255)');
        document.documentElement.style.setProperty('--ico-color','rgb(243, 243, 243');
        document.documentElement.style.setProperty('--nav-color','rgb(39, 39, 39)');
        document.documentElement.style.setProperty('--menu-color','rgb(82, 82, 82)');
        document.documentElement.style.setProperty('--hover-color','rgba(128, 128, 128, 0.938)');
        isDark = true;
    }
    else{
        document.getElementById("dark").innerHTML="brightness_2";
        document.documentElement.style.setProperty('--body-background','rgb(255, 255, 255)')
        document.documentElement.style.setProperty('--text-color','rgb(0, 0, 0)');
        document.documentElement.style.setProperty('--ico-color','rgb(128, 128, 128)');
        document.documentElement.style.setProperty('--nav-color','rgb(243, 243, 243)');
        document.documentElement.style.setProperty('--menu-color','rgb(255, 255, 255)');
        document.documentElement.style.setProperty('--hover-color','rgba(199, 199, 199, 0.938)');
        isDark = false;
    }
    
}

let isShow = false;

function toggleChart(){
    let btn = document.getElementById('btn');
    if(!isShow){
        btn.innerHTML = "Hide prediction Chart";
        isShow = true;
    }
    else{
        btn.innerHTML = "Show prediction Chart";
        isShow = false;
    }

    document.getElementById('predict').classList.toggle("active")
    document.getElementById('myChart').classList.toggle("active")
}