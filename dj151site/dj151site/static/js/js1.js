//document.write("Hello JavaScript");
$(document).ready(function() {
    //alert("abcdefg");
    /*
    $("body").click(function() {
        $(".error").hide();
    });
    */
    $("ul.error").click(function() {
        //$(this).hide(600);
        $(this).remove();
    });
    $('tr:nth-child(even)').addClass('form_odd');  //OK
    //$('tr:even').addClass('form_odd');
    $('table.content tr:nth-child(even)').addClass('form_odd');
    /*  == $('tr:nth-child(even)').addClass('form_odd');
    odd= {"background":"#EDA", "color":"#3f5"};
    even= {"background":"#2DA", "color":"#875"};
    odd_even("#table1", odd, even);
    odd_even("#table_test", odd, even);
    */
    $('table#content').find('tr').each(function() {
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
    //表格中的TR元素按下时，将该行对应的复选框在选中或者空切换，尚未实现
    $('table#content').find('tr').click(function() {
        $(this).bind("mousedown", function() {
			$(this).toggleClass('choiced');
            /*$(this).find('td:first').attr('value', 0);*/
			/*alert($(this).find('td:first').find('input').val());
			*/
        });
    });
    $().everyTime("2s", 'timeA', js_test, 2);
});

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
