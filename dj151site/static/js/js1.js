$(document).ready(function() {
    $("ul.error").click(function() {
        //$(this).hide(600);
        $(this).remove();
    });
    $('tr:nth-child(even)').addClass('form_odd');  //OK
	$('table.content').click(function() {
		//$(this).find('tr:even').addClass('form_odd');
		//js_test();
	});

    //$('tr:even').addClass('form_odd');
    //$('table.content tr:nth-child(even)').addClass('form_odd');
    $('table.content').find('tr').each(function() {
        var tmp = $(this).css("background-color");
        $(this).bind("mouseenter", function() {
            //$(this).css("background-color", choice); //OK
			$(this).addClass('choice');
        });
        $(this).bind("mouseleave", function() {
            //$(this).css("background-color", tmp); //OK
			$(this).removeClass('choice');
        });
    });
    //当表格前的复选框选中后，该栏增加特殊颜色，取消选择后，颜色也取消
    $(":checkbox").click(function() {
        chkbox_attr = $(this).attr('checked');

        if (chkbox_attr == "checked") {
            $(this).parent().parent().addClass('choiced');
        } else {
            $(this).parent().parent().removeClass('choiced');
        };
        //alert(chkbox_attr);
        //alert($(this).parent().parent().html());
    });
    //将标题栏以上位置固定在当前页面中？？？？？？？？20130719-2300
    // $().everyTime("2s", 'timeA', js_test, 2);  //????????

    $("#id_validate").click(function() {
        //loadAjax();
        var s = Math.random()*10;
        $("#validate_img").attr("src", "");
        htmlobj = $.ajax({url:"/blog/validate/?md=" + s , async:false});
        $("#validate_img").attr("src", "/blog/validate/");
    });

    $('#id_pwd').click(function() {
        alert("hello");
    });
    /* var image1 = new Image();
    image1.src = "/static_blog/img/news1.gif"; */
    bannerNum = 1;
    noClock = window.setInterval("clock()", 100);

});

function rotateBanner() {
    if (++bannerNum > 4)
        bannerNum = 1;
    document.getElementById("news_gif").src = "/static_blog/img/news" + bannerNum + ".gif";
    window.setTimeout('rotateBanner();', 4000);
    //alert("Hello");

}

function clock() {
    var t = new Date();
    //document.getElementById("clock").value = t;  //for <input>
    document.getElementById("clock").innerHTML = t;
}

function loadAjax() {
    htmlobj = $.ajax({url:"/blog/now/", async:false});
    $("#myDiv").html(htmlobj.responseText);
}

function show_cookie() {
    alert(document.cookie);
}

function js_test() {
    alert("aaaa");
}

function hide_error() {
    //do something...
    $(".error").hide();
}

function odd_even(id, odd, even) {
    $(id).find('tr').each(function(index, element) {
        if (index % 2 == 1)
            $(this).addClass("form_even");
        else
            $(this).addClass("form_odd");
    });
}

function validate_login(form) {
	var returnValue = true;
	var username = form_login.username.value;
	var password = form_login.password.value;
	if (username.length < 4) {
		returnValue = false;
		alert("Your username must be at least \n4 characters long.\n Please try again.");
		form_login.username.focus();
		return returnValue;
	}
	if (password.length < 5) {
		returnValue = false;
		alert("Your password must be at least \n6 characters long.\n Please try again.");
		form_login.password.value = "";
		form_login.password.focus();
		return returnValue;
	}
	return returnValue;
}

function web_client() {
    //     < script  type ="text/javascript" >
    var Sys = {};
    var ua = navigator.userAgent.toLowerCase();
    var s;
    /*
    (s = ua.match(/ msie ([\d.] + ) /)) ? Sys.ie = s[ 1 ] :
        (s = ua.match(/ firefox\ / ([\d.] + ) /)) ? Sys.firefox = s[1] :
        (s = ua.match(/ chrome\ / ([\d.] + ) / )) ? Sys.chrome = s[1] :
        (s = ua.match(/ opera.([\d.] + ) / )) ? Sys.opera = s[ 1 ] :
        (s = ua.match(/ version\ / ([\d.] + ). * safari / )) ? Sys.safari = s[1] : 0;
        */
    /* 以下进行测试
       if (Sys.ie) document.write(' IE: ' + Sys.ie);
       if (Sys.firefox) document.write(' Firefox: ' + Sys.firefox);
       if (Sys.chrome) document.write(' Chrome: ' + Sys.chrome);
       if (Sys.opera) document.write(' Opera: ' + Sys.opera);
       if (Sys.safari) document.write(' Safari: ' + Sys.safari);
       </ script >
    */
    /*
    if (Sys.ie) alert(' IE: ' + Sys.ie);
    if (Sys.firefox) alert(' Firefox: ' +  Sys.firefox);
    if (Sys.chrome) alert(' Chrome: ' + Sys.chrome);
    if (Sys.opera) alert(' Opera: ' + Sys.opera);
    if (Sys.safari) alert(' Safari: ' + Sys.safari);
    */
    alert("bye");
}

/*
function displaymsg1()
{
	alert("Alert");
}

function displaymsg2()
{
	confirm("Confirm");
}


function displaymsg3()
{
	prompt("Name","chengl");
}

function for1()
{
	var i=0;
	for (; i<=10;i++)
	{
		document.write("The number is " + i);
		document.write("<br />");
	}
}

function js_try()
{
	var x=prompt("Enter a number between 0 and 10:","");
	try
	{
		if(x>10)
			throw "Err1";
		else if(x<0)
			throw "Err2";
	}
	catch(er)
	{
		if(er=="Err1")
			alert("Error! The value is too high");
		if(er == "Err2")
			alert("Error! The value is too low");
		return false;
	}
}
*/
