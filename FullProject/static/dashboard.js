function savePlant() {
  const form = document.getElementById("myForm");
  const formData = new FormData(form);
  fetch('/save-plant', {
    method: 'POST',
    body: formData,
  })
  .then(response => response.json())
  .then(data => {
    console.log(data.message);
    // Handle the response data as needed
    window.location.href = "/";
  })
  .catch(error => console.log(error));
}

function savePost() {
  const form = document.getElementById("addPostForm");
  const formData = new FormData(form);
  fetch('/create-post', {
    method: 'POST',
    body: formData,
  })
  .then(response => response.json())
  .then(data => {
    console.log(data.message);
    // Handle the response data as needed
    window.location.href = "/feed";
  })
  .catch(error => console.log(error));
}

function update_moisture(){
 
  fetch('/updateDB', {
    method: 'POST',

  })
  .then(response => response.json())
  .then(data => {
    console.log(data.message);
    // Handle the response data as needed
    window.location.href = "/";
  })
  .catch(error => console.log(error));
}

// water drops
// Get the fill element
// const fillElement = document.getElementById("fill");
const allCards = document.querySelectorAll(".druppelCard");


// Function to update the fill percentage
const updateFill = (percentage, plantId) => {
  
  element = document.getElementById(plantId);
  fillElement = element.querySelector(".fill");
  console.log(fillElement);
  console.log(percentage);
  fillElement.style.height = `${percentage}%`;
}
allCards.forEach(card => {
  // haal de id perc op uit de card
  
  const percentage1 = parseInt(card.querySelector("#perc").innerText);
  parseInt(percentage1)
  
  updateFill(percentage1, card.id);
  
  setInterval(() => {
    const percentage = parseInt(card.querySelector("#perc").innerText);
    updateFill(percentage, card.id);
  }, 100);
});
// Example: Set the fill percentage to 70%
// updateFill(50);
