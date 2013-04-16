$(document).ready(function() {
    //$('tr:odd').addClass('form_odd');
    //$('tr:nth-child(even)').addClass('form_odd');
    $("#hide").click(function() {
        $("p").hide();
        $("#div4").fadeOut();
        $("#div5").fadeOut("slow");
        $("#div6").fadeOut(3000);
    });
    $("#show").click(function() {
        $("p").show();
        $("#div4").fadeIn();
        $("#div5").fadeIn("slow");
        $("#div6").fadeIn(3000);
    });

    $("#a3").click(function() {
        $("p").toggle();
        $("#div4").fadeToggle();
        $("#div5").fadeToggle("slow");
        $("#div6").fadeToggle(3000);
    });
    $("#a4").click(function() {
        $("p").toggle(10000);
    });
    $("#toggle").click(function() {
        $("p").toggle(1000);
    });

});

function alert1() {
    var temp = "Welcome";
    alert(temp);
};

function test2() {
    var b = document.getElementById("js1");
    var c = b.getElementsByTagName("p");
    //b.style.color = "green";
    //c.style.color = "red";
    alert(c[0].innerHTML);
};

function test3() {
    x = document.getElementById("js1");
    //$(x).css("background-color", "red");
    //x.style.color = "#ffff00";
    x.style.color = 'yellow';
    x.innerHTML = x.innerHTML.toUpperCase();
};

function test4() {
    document.write('<p>javaScript function test</p>');
};
var i = 0;

function test5(id) {
    if ((i % 2) == 0) {
        id.innerHTML = "Yes 1";
    } else {
        id.innerHTML = "No 2";
    };
    i += 1;
};

function add1() {
    i += 1;
    x = document.getElementById("add");
    x.innerHTML = "add 1:" + String(i)
};

function setName(obj) {
    obj.name = "Nicholas";
    //alert(obj.name);
    obj = new Object();
    obj.name = "Greg";
    //alert(obj.name);
    function swap(Name) {
        var temp = obj.name;
        obj.name = Name;
        alert(temp + "TEST");
    };
    swap("Hello, world");
};

function displayInfo(args) {
    var output = "";
    if (typeof args.name == "string") {
        output += "Name:" + args.name + "\n";
    }

    if (typeof args.age == "number") {
        output += "Age:" + args.age + "\n";
    }
    alert(output);
};

function testObject() {
    var person = new Object();
    setName(person);

    displayInfo({
        name: "Nicholas",
        age:29
    });
};
