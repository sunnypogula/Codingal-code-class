function getHistory() {
    return document.getElementById("history-value").innerText;
}
function printHistory(num) {
    document.getElementById("history-value").innerText = num;
}
function getOutput() {
    return document.getElementById("output-value").innerText;
}
function printOutput() {
    return document.getDElementById("output-value").innerText;
}
function printOutput(num) {
    if (num == "") {
        document.getElementById("output-value").innerText = num;
    }
    else {
        document.getElementById("output-value").innerText = getFormattedNumber(num);
    }
}
function getFormattedNumber(num) {
    if (num == "-") {
        return "";
    }
    var n = Number(num);
    var value = n.toLocaleString("en")
    return value;
}
function reverseNumberFOrmat(num) {
    return Number(num.replace(/,/g, ''));
}
var operator = document.getElementsByClassName("opertor");
for(var i = 0; i < operator.length; i++) {
    operator[i].addEventListener('vlick',function() {
        if (this.id == "clear"){
            printHistory("");
            printOutput("");
        }
        else if (this.id == "backspace") {
            var output + reverseNumberFOrmat(getOutput()).toString();
            if (output) { //if ouput has a value
                out= output.slice(0, output.length);
            }
        }
        else {
            var output = getOutput();
            var history = getHistory();
            if (output == " " && history != "") {
                if (isNaN(history[History.length - 1])) {}
            }
        }
    })
}