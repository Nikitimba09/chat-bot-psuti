let tg = window.Telegram.WebApp;
tg.expand();
tg.MainButton.textColor = "#FFFFFF";
tg.MainButton.color = "#2cab37";
let item = "";

let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");
let usercard = document.getElementById("usercard"); // Элемент usercard

btn1.addEventListener("click", function () {
    if (tg.MainButton.isVisible) {
        tg.MainButton.hide();
    } else {
        tg.MainButton.setText("Вывести информацию о популярных ароматах");
        item = "popular";
        tg.MainButton.show();
        showUserCard("Вот несколько популярных ароматов:\n1. Chanel No. 5\n2. Dior Sauvage\n3. Gucci Bloom");
    }
});

btn2.addEventListener("click", function () {
    if (tg.MainButton.isVisible) {
        tg.MainButton.hide();
    } else {
        tg.MainButton.setText("Вывести советы по выбору");
        item = "advice";
        tg.MainButton.show();
        showUserCard("Вот несколько советов по выбору аромата:\n- Учитывайте время года.\n- Пробуйте аромат на коже.\n- Не спешите с выбором.");
    }
});

function showUserCard(message) {
    usercard.style.display = "block"; // Показать карточку пользователя
    usercard.innerText = message; // Установить текст в карточке
}

Telegram.WebApp.onEvent("mainButtonClicked", function () {
    tg.sendData(item);
});
