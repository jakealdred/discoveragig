$(document).ready(function () {
  var timer = null;
  var self = $("button");
  var clicked = false;
  $("button").on("click", function () {
    if (clicked === false){
      self.removeClass("filled");
      self.addClass("circle");
      self.html("");
      clicked = true;
      $("svg").css("display", "block");
      $(".circle_2").attr("class", "circle_2 fill_circle");

      timer = setInterval(
        function tick() {
        self.removeClass("circle");
        self.addClass("filled");
        // self.html("b");
        $(".wrap img").css("display", "block");
        $("svg").css("display", "none");
        clearInterval(timer);
      }, 2500);
      }
  });
});
