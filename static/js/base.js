function getCookie(cname)
        {
          var name = cname + "=";
          var ca = document.cookie.split(';');
          for(var i=0; i<ca.length; i++)
          {
            var c = ca[i].trim();
            if (c.indexOf(name)==0) return c.substring(name.length,c.length);
          }
          return "";
        }
$(document).ready(function(){
    var is_login = getCookie("is_login")
    console.log(is_login)
    if(is_login == "True"){
        var logged = $('<a href="{% url '+ 'RecQuiz:logout' + ' %}" class="get-started-btn">Log Out</a>');
        $("#navbar").after(logged);
    }else{
        var passenger = $('<a href="{% url '+'RecQuiz:login'+' %}" class="get-started-btn">Get Started</a>');
        $("#navbar").after(passenger);
    }
})