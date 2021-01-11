function getBotResponse() {
  var rawText = $("#textInput").val();
  var userHtml = '<p class="text userText"><span>' + rawText + "</span></p>";
  $("#textInput").val("");
  $("#chatbox").append(userHtml);
  document
    .getElementById("userInput")
    .scrollIntoView({
      block: "start",
      behavior: "smooth"
    });
  $.get("/get", {
    msg: rawText
  }).done(function (data) {
    var botHtml = '<p class="text botText"><span>' + data + "</span></p>";
    $("#chatbox").append(botHtml);
    document
      .getElementById("userInput")
      .scrollIntoView({
        block: "start",
        behavior: "smooth"
      });
  });
}
$(document).ready(function () {
  $("#textInput").keypress(function (e) {
    if (e.which == 13) {
      getBotResponse();
    }
  });
  $("#clearBtn").click(function () {
    $("#textInput").val("");
    document.getElementById('chatbox').innerHTML = "<p class=\"text botText\"><span>Hi! I'm Candice your personal ChatBot!</span></p>";
  });
});