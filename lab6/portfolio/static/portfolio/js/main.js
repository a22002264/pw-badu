window.onscroll = function() {makeSticky()};

// Get the navbar
const navbar = document.getElementById("header-id");

// Get the offset position of the navbar


// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function makeSticky() {
  if (window.scrollY >= navbar.offsetTop) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}

function scrollToView(id){
  var top = document.getElementById(id).offsetTop - document.getElementById("nav-id").offsetHeight - 10;
  //show 10 pixels down the border
  window.scrollTo(0, top);
}

