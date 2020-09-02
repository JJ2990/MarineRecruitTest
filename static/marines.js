var lastSearch

var gotonext = function(){
    id = id + 1
    window.location.href = "http://127.0.0.1:5000/view/" + id +""
}

var gotoprev = function(){
    id = id - 1
    console.log(id)
    window.location.href = "http://127.0.0.1:5000/view/" + id +""
}

var gotolearn = function(){
    window.location.href = "http://127.0.0.1:5000/learn"
}
var gotohome = function(){
    window.location.href = "http://127.0.0.1:5000"
}
var gotoquiz = function(){
    window.location.href = "http://127.0.0.1:5000/quiz"
}

var gotoQ = function(){
    window.location.href = "http://127.0.0.1:5000/question1"
}

var gotoQ2 = function(){
    window.location.href = "http://127.0.0.1:5000/question2"
}

var gotoQ3 = function(){
    window.location.href = "http://127.0.0.1:5000/question3"
}

var gotoQ4 = function(){
    window.location.href = "http://127.0.0.1:5000/question4"
}

var gotoQ5 = function(){
    window.location.href = "http://127.0.0.1:5000/question5"
}

$(document).ready(function(){

    $("#checkbtn1").click(function(){
        console.log("clicked")

        if(document.getElementById('question-1-answers-Right').checked) {
            var newRow = $("<div class='row rightA'>Correct</div>")
        } else {
            var newRow = $("<div class='row wrongA'>Incorrect</div>")
        }
        $("#Qresult").empty()
        $("#Qresult").append(newRow)
    })

    $("#next").click(function(){
        console.log("clicked")
        gotonext()
    })

    $("#prev").click(function(){
        console.log("clicked")
        gotoprev()
    })

    $("#learn").click(function(){
        console.log("clicked")
        gotolearn()
    })

    $("#quiz").click(function(){
        console.log("clicked")
        gotoquiz()
    })

    $("#home").click(function(){
        console.log("clicked")
        gotohome()
    })


    $("#startQ").click(function(){
        console.log("clicked")
        gotoQ()
    })

    $("#nextQ").click(function(){
        console.log("clicked")
        gotoQ2()
    })

    $("#Q3").click(function(){
        console.log("clicked")
        gotoQ3()
    })

    $("#Q4").click(function(){
        console.log("clicked")
        gotoQ4()
    })

    $("#Q5").click(function(){
        console.log("clicked")
        gotoQ5()
    })

    $(document).on("mouseover", ".both", function(e) {
        $(this).addClass("yellow curs")
    })
    $(document).on("mouseout", ".both", function(e) {
        $(this).removeClass("yellow")
    })

})