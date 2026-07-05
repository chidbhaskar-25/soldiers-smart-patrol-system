document.addEventListener("DOMContentLoaded", function () {

    const buttons=document.querySelectorAll("button,.btn");

    buttons.forEach(btn=>{
        btn.addEventListener("mouseenter",()=>{
            btn.style.transform="scale(1.05)";
        });

        btn.addEventListener("mouseleave",()=>{
            btn.style.transform="scale(1)";
        });
    });

});