const button = document.getElementById("menu_for_moblie");
const cover = document.getElementsByClassName("cover")[0];
const container = document.getElementsByClassName("container_menu_for_mobile")[0];

function click_on_menu_button(){
    cover.classList.toggle("show");
    cover.classList.toggle("hide");
    container.classList.toggle("flex");
    container.classList.toggle("hide");
}
button.addEventListener("click",click_on_menu_button);
cover.addEventListener("click",click_on_menu_button);