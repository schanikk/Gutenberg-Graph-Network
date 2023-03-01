const bookList = document.querySelector(".list-books");
const personList = document.querySelector(".list-persons");
const topicList = document.querySelector(".list-topics");

const bookItems = bookList.querySelectorAll("ul > li");
const personItems = personList.querySelectorAll("ul > li");
const topicItems = topicList.querySelectorAll("ul > li");

console.log(bookItems);
console.log(personItems);

let selectedBook = undefined;
let selectedPerson = undefined;

// for (book of bookItems) {
//   book.addEventListener("click", (e) => {
//     if (selectedBook !== e.target.innerText) {
//       selectedBook = e.target.innerText;
//       for (person of personItems) {
//         if (person.innerText !== e.target.innerText) {
//           person.style.display = "none";
//         } else {
//           person.style.display = "block";
//         }
//       }
//     }
//   });
// }

function addListeners(listeningItems, affectedItems, selectedListener) {
  for (item of listeningItems) {
    item.addEventListener("click", (e) => {
      if (selectedListener !== e.target.innerText) {
        selectedListener = e.target.innerText;
        for (item of affectedItems) {
          if (item.innerText !== e.target.innerText) {
            item.style.display = "none";
          } else {
            item.style.display = "block";
          }
        }
      }
    });
  }
}
addListeners(bookItems, personItems, selectedBook);
addListeners(personItems, topicItems, selectedPerson);
