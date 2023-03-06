const bookList = document.querySelector(".list-books");
const personList = document.querySelector(".list-persons");
const topicList = document.querySelector(".list-topics");
const personHeader = document.querySelector("#person");
const bookHeader = document.querySelector("#book");

const topicHeader = document.querySelector("#topics");

let bookItems = [];
let personItems = [];
let topicItems = [];

let books;
let persons = [];
let topics = [];

const resetBtn = document.querySelector(".reset-btn");
const COLL_API = "http://localhost:8000/api/collection/";
const BOOK_API = "http://localhost:8000/api/book/";
const CHAR_API = "http://localhost:8000/api/character/";
const TOPIC_API = "http://localhost:8000/api/bookTopic/";

// TODO: Anpassung der Listeneinträge für jede Column
function createBookEntry(item, ...column) {
  if (column[0] == "topic") {
    return `<li class="list-group-item d-flex justify-content-between align-items-center" data-dbid='${
      item.pk
    }'>${item.fields.bookName.toUpperCase()}<span class="badge text-bg-warning rounded-pill">14</span></li>`;
  }
  return `<li class="list-group-item d-flex justify-content-between align-items-center" data-dbid='${
    item.pk
  }'>${item.fields.bookName.toUpperCase()}</li>`;
}
function createTopicEntry(item, ...column) {
  return `<li class="list-group-item d-flex justify-content-between align-items-center" data-dbid=''>${item.TopicName}<span class="badge text-bg-warning rounded-pill">${item.Count}</span></li>`;
}

function createPersonEntry(item, ...column) {
  return `<li class="list-group-item d-flex justify-content-between align-items-center" data-dbid='${
    item.pk
  }'>${item.fields.Name.toUpperCase()}</li>`;
}

function fillUpColumns(books, persons, topics) {
  books.forEach((item) => {
    console.log(item.fields);
    bookList.innerHTML += createBookEntry(item);
  });
  //persons.forEach((item) => {
  //  personList.innerHTML += createListEntry(item);
  //});
  //topics.forEach((item) => {
  //  topicList.innerHTML += createListEntry(item, "topic");
  //});
  bookHeader.innerHTML = "Books  ";
  bookHeader.innerHTML += `<span class='badge text-bg-warning rounded-pill'>${books.length}</span>`;
}

async function getData(url) {
  const response = await fetch(url);

  return response.json();
}

getAllData().then(() => {
  fillUpColumns(books, persons, topics);
  bookItems = bookList.querySelectorAll("ul > li");
  topicItems = topicList.querySelectorAll("ul > li");
  addAllListeners();
});

async function getAllData() {
  await getData(COLL_API).then((data) => {
    books = JSON.parse(data);
    console.log(books);
  });
}

// function sleep(ms) {
//   return new Promise((resolve) => setTimeout(resolve, ms));
// }

let selectedBook = "";
let selectedPerson = "";

function addBookListeners(listeningItems, affectedItems, selectedListener) {
  for (let item of listeningItems) {
    item.addEventListener("click", async (e) => {
      console.clear();
      topicList.innerHTML = "";
      let id = e.target.dataset.dbid;
      console.log(id);
      for (let listeningItem of listeningItems) {
        listeningItem.style.opacity = "0.5";
      }

      if (selectedListener !== id) {
        selectedListener = id;
        e.target.style.opacity = "1";
      } else {
        e.target.style.opacity = "1";
      }

      persons = await getData(BOOK_API + id).then((data) => {
        json = JSON.parse(data);
        return json;
      });
      console.log(persons);

      if (personList.innerHTML !== "") {
        personList.innerHTML = "";
      }

      persons.map((item) => {
        if (item.fields["Name"].match(/.*-+.*/)) {
          console.log(item);
        }
      });

      topicsJSON = await getData(TOPIC_API + id).then((data) => {
        json = JSON.parse(data);
        console.log();
        return json;
      });

      personHeader.innerHTML = "Persons  ";
      personHeader.innerHTML += `<span class='badge text-bg-warning rounded-pill'>${persons.length}</span>`;

      // topicHeader.innerHTML = "Topics  ";
      // topicHeader.innerHTML += `<span class='badge text-bg-warning rounded-pill'>${topicsJSON.length}</span>`;

      persons.forEach((item) => {
        personList.innerHTML += createPersonEntry(item);
      });
      personItems = personList.querySelectorAll("ul > li");
      addPersonListeners(personItems, topicItems, selectedPerson);
    });
  }
}

function addPersonListeners(listeningItems, affectedItems, selectedListener) {
  for (let item of listeningItems) {
    item.addEventListener("click", async (e) => {
      console.clear();
      let id = e.target.dataset.dbid;
      console.log(id);
      for (let listeningItem of listeningItems) {
        listeningItem.style.opacity = "0.5";
      }

      if (selectedListener !== id) {
        selectedListener = id;
        e.target.style.opacity = "1";
      } else {
        e.target.style.opacity = "1";
      }

      topicsJSON = await getData(CHAR_API + id).then((data) => {
        json = JSON.parse(data);
        console.log();
        return json;
      });
      console.log(topicsJSON);
      topics = [];

      Object.entries(topicsJSON).forEach((item) => {
        console.log(item[1]);
        tempTn = item[1]["TopicName:"].split(/_/g);
        console.log(tempTn);
        tempTn.shift();

        let tn = tempTn.join(" ").toUpperCase();

        item[1]["TopicName:"] = tn;

        topics.push({
          TopicName: item[1]["TopicName:"],
          Count: item[1]["Count"],
        });
        topics.sort((a, b) => (a.Count > b.Count ? -1 : 1));

        topicHeader.innerHTML = "Topics  ";
        topicHeader.innerHTML += `<span class='badge text-bg-warning rounded-pill'>${topics.length}</span>`;
      });

      // for (let i = 0; i < 1000; i++) {
      //   if (topicsJSON[i] == undefined) continue;
      //   console.log("Topic id", topicsJSON[i]);
      //   console.log("Topic Name", topicsJSON[i]["TopicName:"].split(/_/g));

      //   tempTn = topicsJSON[i]["TopicName:"].split(/_/g);
      //   console.log(tempTn);
      //   tempTn.shift();

      //   let tn = tempTn.join(" ").toUpperCase();

      //   topicsJSON[i]["TopicName:"] = tn;

      //   topics.push({
      //     TopicName: topicsJSON[i]["TopicName:"],
      //     Count: topicsJSON[i]["Count"],
      //   });
      // }

      console.log(topics);

      if (topicList.innerHTML !== "") {
        topicList.innerHTML = "";
      }

      // persons.map((item) => {
      //   if (item.fields["Name"].match(/.*-+.*/)) {
      //     console.log(item);
      //   }
      // });
      topics.forEach((item) => {
        topicList.innerHTML += createTopicEntry(item);
      });
    });
  }
}

function addAllListeners() {
  addBookListeners(bookItems, personItems, selectedBook);

  resetBtn.addEventListener("click", (e) => {
    for (let bookItem of bookItems) {
      // bookItem.classList.remove("d-none");
      // bookItem.classList.add("d-flex");
      bookItem.style.opacity = "1";
    }
    // for (let personItem of personItems) {
    //   personItem.classList.remove("d-none");
    //   personItem.classList.add("d-flex");
    //   personItem.style.opacity = "1";
    // }
    // for (let topicItem of topicItems) {
    //   topicItem.classList.remove("d-none");
    //   topicItem.classList.add("d-flex");
    //   topicItem.style.opacity = "1";
    // }
    topicList.innerHTML = "";
    personList.innerHTML = "";
    selectedBook = "";
    selectedPerson = "";
    topicHeader.innerHTML = "Topics";
    personHeader.innerHTML = "Persons";
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
