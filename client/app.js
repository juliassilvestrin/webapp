console.log("connected");

let movieReviewWrapper = document.querySelector("#reviewList");

function addMovieReview(record) {
    let reviewContainer = document.createElement("div");
    reviewContainer.className = "reviewContainer";

    let titleElement = document.createElement("strong");
    titleElement.innerHTML = `Name: ${record.name}`;
    reviewContainer.appendChild(titleElement);

    let reviewElement = document.createElement("p");
    reviewElement.innerHTML = `Review: ${record.review}`;
    reviewContainer.appendChild(reviewElement);

    let ratingElement = document.createElement("p");
    ratingElement.innerHTML = `Rating: ${record.rating}`;
    reviewContainer.appendChild(ratingElement);

    let genreElement = document.createElement("p");
    genreElement.innerHTML = `Genre: ${record.genre}`;
    reviewContainer.appendChild(genreElement);

    let releaseYearElement = document.createElement("p");
    releaseYearElement.innerHTML = `Release Year: ${record.release_year}`;
    reviewContainer.appendChild(releaseYearElement);

    let editButton = document.createElement("button");
    editButton.innerHTML = "Edit";
    editButton.onclick = function () {
        loadMovieDetails(record);
    };
    reviewContainer.appendChild(editButton);

    let deleteButton = document.createElement("button");
    deleteButton.innerHTML = "Delete";
    deleteButton.onclick = function () {
        if (confirm("Are you sure you want to delete this movie?")) {
            deleteMovie(record.id);
        }
    };
    reviewContainer.appendChild(deleteButton);

    movieReviewWrapper.appendChild(reviewContainer);
}

let nameInput = document.querySelector("#edit-coaster-name");
let reviewInput = document.querySelector("#edit-coaster-review");
let ratingInput = document.querySelector("#edit-coaster-rating");
let genreInput = document.querySelector("#edit-coaster-genre");
let releaseYearInput = document.querySelector("#edit-coaster-release-year");

let addReviewButton = document.querySelector("#add-review-button");
let saveReviewButton = document.querySelector("#save-review-button");

let isEditing = false;
let editingId = null;


addReviewButton.onclick = function () {
    if (isEditing) return;

    let data = `name=${encodeURIComponent(nameInput.value)}&review=${encodeURIComponent(reviewInput.value)}&rating=${encodeURIComponent(ratingInput.value)}&genre=${encodeURIComponent(genreInput.value)}&release_year=${encodeURIComponent(releaseYearInput.value)}`;

    createMovie(data);

    clearInputFields();
};


saveReviewButton.onclick = function () {
    if (!isEditing) return;

    let data = `name=${encodeURIComponent(nameInput.value)}&review=${encodeURIComponent(reviewInput.value)}&rating=${encodeURIComponent(ratingInput.value)}&genre=${encodeURIComponent(genreInput.value)}&release_year=${encodeURIComponent(releaseYearInput.value)}`;

    editMovie(editingId, data);

    clearInputFields();
    isEditing = false;
    editingId = null;
};

function loadMovieDetails(record) {
    nameInput.value = record.name;
    reviewInput.value = record.review;
    ratingInput.value = record.rating;
    genreInput.value = record.genre;
    releaseYearInput.value = record.release_year;

    isEditing = true;
    editingId = record.id;
}

function clearInputFields() {
    nameInput.value = "";
    reviewInput.value = "";
    ratingInput.value = "";
    genreInput.value = "";
    releaseYearInput.value = "";
}

function loadMoviesFromServer() {
    movieReviewWrapper.innerHTML = "";

    fetch("http://localhost:8080/movies")
        .then(response => response.json())
        .then(data => {
            data.forEach(addMovieReview);
        });
}

function createMovie(data) {
    fetch("http://localhost:8080/movies", {
        method: "POST",
        body: data,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    }).then(() => {
        loadMoviesFromServer();
    });
}

//function editMovie(id, data) {
//fetch(`http://localhost:8080/movies/${id}`, {
// method: "PUT",
//body: data,
//headers: {
//"Content-Type": "application/x-www-form-urlencoded"
//   }
// }).then(() => {
//   loadMoviesFromServer();
// });
//}

function deleteMovie(id) {
    fetch(`http://localhost:8080/movies/${id}`, {
        method: "DELETE"
    }).then(() => {
        loadMoviesFromServer();
    });
}


loadMoviesFromServer();
