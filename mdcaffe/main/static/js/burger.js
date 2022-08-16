const hamb = document.querySelector("#hamb");
const popup = document.querySelector("#popup");
const menu = document.querySelector("#menu__list").cloneNode(1);
const body = document.body;

var open_menu = false

hamb.addEventListener("click", hambHandler);

function hambHandler(e) {
    console.log(window.scrollY)
    
    if (window.scrollY > 200) {
        popup.style.top = "60px"
    } else {
        popup.style.top ="200px"
    }  
    
    if (open_menu == false) {
        e.preventDefault();
        popup.classList.toggle("open");
        hamb.classList.toggle("active");
        body.classList.toggle("noscroll");
        renderPopup();
        open_menu = true
    } else {
        e.preventDefault();
        popup.classList.toggle("open");
        hamb.classList.toggle("active");
        body.classList.toggle("noscroll");
        renderPopup();
        menu.remove()
        open_menu = false
    }
}

function renderPopup() {
  popup.appendChild(menu);
}

const links = Array.from(menu.children);

links.forEach((link) => {
  link.addEventListener("click", closeOnClick);
});

function closeOnClick() {
  popup.classList.remove("open");
  hamb.classList.remove("active");
  body.classList.remove("noscroll");
}