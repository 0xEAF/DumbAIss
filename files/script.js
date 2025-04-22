function submitlearn(elem) {
    let question = $(elem).prev().prev().val();
    let response = $(elem).prev().val();

    $.getJSON("/api/learn", {"question": question, "response": response}, function (data) {
        if (data["status"] == "200") {
            $(elem).parent().remove();

            let element = $("<li></li>");
            element.attr("class", "bot");
            element.text(response);
            $("#chatbox").append(element);
        }
    });
}

(function () {
    // Quand on clique sur fermer
    $("#closebtn").on("click", function () {
        $.getJSON("/api/close");
    });

    // Quand on clique sur "envoyer"
    $("#submitbtn").on("click", function () {
        let question = $("#inputbox").val();
        $("#inputbox").val("");
        
        let element = $("<li></li>");
        element.attr("class", "user");
        element.text(question);
        $("#chatbox").append(element);

        $.getJSON("/api/ask", {"question": question}, function (data) {
            if (data["status"] == "404") {
                // Pas de réponse, demander la réponse
                let element = $(`<li class="learn">
                    Désolé, je ne connais pas la réponse. Que devrai-je répondre?
                    <input type="hidden" value="` + question + `">
                    <input type="text" placeholder="Entrez la réponse...">
                    <button type="button" class="learnbtn" onclick="submitlearn(this);">Envoyer</button>
                </li>`);
                $("#chatbox").append(element);
            } else {
                // On a une réponse, l'afficher
                let element = $("<li></li>");
                element.attr("class", "bot");
                element.text(data["response"]);
                $("#chatbox").append(element);
            }
        });
    });
})();