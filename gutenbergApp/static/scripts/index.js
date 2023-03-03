const bookList = document.querySelector(".list-books");
const personList = document.querySelector(".list-persons");
const topicList = document.querySelector(".list-topics");

let bookItems;
let personItems;
let topicItems;

const resetBtn = document.querySelector(".reset-btn");
const BOOK_API = "http://localhost:8000/api/collection/";
const COLL_API = "http://localhost:8000/api/book/";
const CHAR_API = "http://localhost:8000/api/character/";

let obj;

async function getData(url) {
  console.log(url);
  const response = await fetch(url);
  console.log(response);
  return response.json();
}

getData(COLL_API)
  .then((data) => {
    obj = data.data;
    console.log(obj);
  })
  .then(() => {
    obj.forEach((item) => {
      bookList.innerHTML +=
        "<li class='list-group-item d-flex justify-content-between align-items-center'>" +
        item.name +
        "<span class='badge text-bg-info rounded-pill'>14</span></li>";
    });
    obj.forEach((item) => {
      personList.innerHTML +=
        "<li class='list-group-item d-flex justify-content-between align-items-center'>" +
        item.name +
        "<span class='badge text-bg-info rounded-pill'>14</span></li>";
    });
    obj.forEach((item) => {
      topicList.innerHTML +=
        "<li class='list-group-item d-flex justify-content-between align-items-center'>" +
        item.name +
        "<span class='badge text-bg-info rounded-pill'>14</span></li>";
    });
    bookItems = bookList.querySelectorAll("ul > li");
    personItems = personList.querySelectorAll("ul > li");
    topicItems = topicList.querySelectorAll("ul > li");
    addAllListeners();
  });

// function sleep(ms) {
//   return new Promise((resolve) => setTimeout(resolve, ms));
// }

let selectedBook = "";
let selectedPerson = "";

function addListeners(listeningItems, affectedItems, selectedListener) {
  for (let item of listeningItems) {
    item.addEventListener("click", (e) => {
      for (let listeningItem of listeningItems) {
        listeningItem.style.opacity = "0.5";
      }

      if (selectedListener !== e.target.innerText.match(/^[a-zA-Z]+\d{1}/)[0]) {
        selectedListener = e.target.innerText.match(/^[a-zA-Z]+\d{1}/)[0];
        e.target.style.opacity = "1";
      } else {
        e.target.style.opacity = "1";
      }
      console.clear();
      for (let affectedItem of affectedItems) {
        console.log(affectedItems);
        console.log(
          "affected: ",
          affectedItem.innerText.match(/^[a-zA-Z]+\d{1}/)[0]
        );
        console.log("selected: ", selectedListener);

        if (
          affectedItem.innerText.match(/^[a-zA-Z]+\d{1}/)[0] !==
          selectedListener
        ) {
          affectedItem.classList.remove("d-flex");
          affectedItem.classList.add("d-none");
        } else {
          affectedItem.classList.add("d-flex");
          affectedItem.classList.remove("d-none");
          affectedItem.style.opacity = "1";
        }
      }
    });
  }
}

function addAllListeners() {
  addListeners(bookItems, personItems, selectedBook);
  addListeners(personItems, topicItems, selectedPerson);
  resetBtn.addEventListener("click", (e) => {
    for (let bookItem of bookItems) {
      bookItem.classList.remove("d-none");
      bookItem.classList.add("d-flex");
      bookItem.style.opacity = "1";
    }
    for (let personItem of personItems) {
      personItem.classList.remove("d-none");
      personItem.classList.add("d-flex");
      personItem.style.opacity = "1";
    }
    for (let topicItem of topicItems) {
      topicItem.classList.remove("d-none");
      topicItem.classList.add("d-flex");
      topicItem.style.opacity = "1";
    }
  });
}

// window.addEventListener("load", function () {
//   Object.keys(obj).forEach((item) => {
//     bookList.innerHTML +=
//       "<li class='list-group-item d-flex justify-content-between align-items-center'>" +
//       item +
//       "<span class='badge text-bg-info rounded-pill'>14</span></li>";
//   });
//   Object.keys(obj).forEach((item) => {
//     personList.innerHTML +=
//       "<li class='list-group-item d-flex justify-content-between align-items-center'>" +
//       item +
//       "<span class='badge text-bg-info rounded-pill'>14</span></li>";
//   });
//   Object.keys(obj).forEach((item) => {
//     topicList.innerHTML +=
//       "<li class='list-group-item d-flex justify-content-between align-items-center'>" +
//       item +
//       "<span class='badge text-bg-info rounded-pill'>14</span></li>";
//   });
//   bookItems = bookList.querySelectorAll("ul > li");
//   personItems = personList.querySelectorAll("ul > li");
//   topicItems = topicList.querySelectorAll("ul > li");
//   addAllListeners();
// });
