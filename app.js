let tg = window.Telegram.WebApp;
tg.expand();  // Разворачиваем Web App

// Настройки кнопки
tg.MainButton.textColor = "#FFFFFF";
tg.MainButton.color = "#2cab37";

// Переменная для хранения выбранного пункта
let item = "";

// Получаем элементы кнопок и карточку
let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");
let usercard = document.getElementById("usercard");

// Обработка клика по кнопке "Популярные ароматы"
btn1.addEventListener("click", function () {
    if (tg.MainButton.isVisible) {
        tg.MainButton.hide();
    } else {
        tg.MainButton.setText("Вывести информацию о популярных ароматах");
        item = "popular";  // Устанавливаем значение item
        tg.MainButton.show();  // Показываем кнопку
        showUserCard("Вот несколько популярных ароматов:\n1. Chanel No. 5\n2. Dior Sauvage");
    }
});

// Обработка клика по кнопке "Советы по выбору"
btn2.addEventListener("click", function () {
    if (tg.MainButton.isVisible) {
        tg.MainButton.hide();
    } else {
        tg.MainButton.setText("Вывести советы по выбору");
        item = "advice";  // Устанавливаем значение item
        tg.MainButton.show();  // Показываем кнопку
        showUserCard("Вот несколько советов по выбору аромата:\n- Учитывайте время года.\n- Пробуйте аромат на коже.\n- Не спешите с выбором.");
    }
});

// Функция для отображения карточки с информацией
function showUserCard(message) {
    usercard.style.display = "block";
    usercard.innerText = message;
}

// Отправка данных при нажатии на MainButton
Telegram.WebApp.onEvent("mainButtonClicked", function () {
    tg.sendData(item);  // Отправляем выбранный пункт в бота
});
