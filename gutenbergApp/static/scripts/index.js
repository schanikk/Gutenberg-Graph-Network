const bookList = document.querySelector(".list-books");
const personList = document.querySelector(".list-persons");
const topicList = document.querySelector(".list-topics");

const bookItems = bookList.querySelectorAll("ul > li");
const personItems = personList.querySelectorAll("ul > li");
const topicItems = topicList.querySelectorAll("ul > li");

const resetBtn = document.querySelector(".reset-btn");

console.log(bookItems);
console.log(personItems);

let selectedBook = "";
let selectedPerson = "";

function addListeners(listeningItems, affectedItems, selectedListener) {
  for (let item of listeningItems) {
    item.addEventListener("click", (e) => {
      for (let listeningItem of listeningItems) {
        listeningItem.style.opacity = "0.5";
      }

      if (selectedListener !== e.target.innerHTML) {
        selectedListener = e.target.innerHTML;
        e.target.style.opacity = "1";
      } else {
        e.target.style.opacity = "1";
      }
      console.clear();
      for (let affectedItem of affectedItems) {
        console.log(affectedItems);
        console.log("affected: ", affectedItem.innerHTML);
        console.log("selected: ", selectedListener);

        if (affectedItem.innerHTML !== selectedListener) {
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
