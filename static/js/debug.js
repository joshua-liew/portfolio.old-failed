htmx.defineExtension('debug', {
    onEvent: function (name, evt) {
        if (console.debug) {
            console.debug(name, evt);
        } else if (console) {
            console.log("DEBUG:", name, evt);
        } else {
            throw "NO CONSOLE SUPPORTED"
        }
    }
});

htmx.on("htmx:beforeHistorySave", function(evt){
    console.log("Saving history : ", evt.detail);
    console.log("History Cache Before:", JSON.parse(localStorage.getItem("htmx-history-cache")))
    setTimeout(function () {
        console.log("History Cache After:", JSON.parse(localStorage.getItem("htmx-history-cache")))
    }, 10);
})