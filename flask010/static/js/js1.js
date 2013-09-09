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


});

function loadAjax()
{
    htmlobj = $.ajax({url:"/blog/now/", async:false});
    $("#myDiv").html(htmlobj.responseText);
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
