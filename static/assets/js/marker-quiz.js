 //initialize video.js

  var video = videojs('my_video');

 //import jsonData from django view
  var questions = JSON.parse(document.querySelector('#jsonData').getAttribute('data-json'));
  console.log("questions:",questions);

  //create a question_list for loading quiz list
  var question_list = document.getElementsByClassName('question-list-item');

  //Click handler for the question_list_item
  for(var i = 0; i < question_list.length; i++){
    $('.question-list-item').eq(i).on('click',function(e){
      console.log("Question box is clicking.")
      //Create a modal      
    })
  }

  var questionCounter = 0; //Tracks question number
  var selections = []; //Array containing user choices
  var quiz = $('#quiz'); //Quiz div object
  
  //initialize markers 
  var markers = []

  for (var i = 0; i < questions.length; i++){
    var marker = {
      time:questions[i].time,
      text:questions[i].question
    }
    markers.push(marker)
  }
  console.log("markers:",markers)
  console.log("marker-quiz.js is loading");

 //load the marker plugin
 video.markers({
   //When reach the markers, load the quiz page
   onMarkerReached: function(marker) {
     $('#quiz-box').css('visibility', 'visible');
     video.pause()
     //Display questions
     displayNext();
     let quiz = marker.text
    //  alert(quiz['question'])
   },
   markers: this.markers
 });

  //click handler for the 'submit' button
  $('#submit').on('click', function (e) {
    e.preventDefault();
    
    // Suspend click listener during fade animation
    if(quiz.is(':animated')) {        
      return false;
    }
    choose();
    
    // If no user selection, progress is stopped
    if (isNaN(selections[questionCounter])) {
        alert('Please make a selection!');
    } 
    else {
        var index = selections[questionCounter]
        console.log("User choice:",questions[questionCounter].choices[index])
        console.log("Correct Answer:",questions[questionCounter]['correctAnswer'])
        if(questions[questionCounter].choices[index] === questions[questionCounter].correctAnswer){
            alert("Your answer is correct.")
        }
        else{
            alert(`Your answer is wrong. The correct Answer is ${questions[questionCounter].correctAnswer}`)
        }
        //Display the button
        $('.question-list-item').eq(questionCounter).attr('disabled', false);
        questionCounter++;
        video.play()

      //After finishing a question, hide the quesition box
      $('#quiz-box').css('visibility', 'hidden');

    }
  });
  
  // //Click handler for the 'prev' button
  // $('#prev').on('click', function (e) {
  //   e.preventDefault();
    
  //   if(quiz.is(':animated')) {
  //     return false;
  //   }
  //   choose();
  //   questionCounter--;
  //   displayNext();
  // });
  
  // //Click handler for the 'Start Over' button
  // $('#start').on('click', function (e) {
  //   e.preventDefault();
    
  //   if(quiz.is(':animated')) {
  //     return false;
  //   }
  //   questionCounter = 0;
  //   selections = [];
  //   displayNext();
  //   $('#start').hide();
  // });
  

  // Animates buttons on hover
  $('.button').on('mouseenter', function () {
    $(this).addClass('active');
  });
  $('.button').on('mouseleave', function () {
    $(this).removeClass('active');
  });
  
  //Creates and returns the div that contains the questions and 
  //the answer selections
  function createQuestionElement(index) {
    var qElement = $('<div>', {
      id: 'question'
    });
    
    var header = $('<h2>Question ' + (index + 1) + ':</h2>');
    qElement.append(header);
    
    var question = $('<p>').append(questions[index].question);
    qElement.append(question);
    
    var radioButtons = createRadios(index);
    qElement.append(radioButtons);
    
    return qElement;
  }
  
  //Creates a list of the answer choices as radio inputs
  function createRadios(index) {
    var radioList = $('<ul>');
    var item;
    var input = '';
    for (var i = 0; i < questions[index].choices.length; i++) {
      item = $('<li>');
      input = '<input type="radio" name="answer" value=' + i + ' />';
      input += questions[index].choices[i];
      item.append(input);
      radioList.append(item);
    }
    return radioList;
  }
  
  //Reads the user selection and pushes the value to an array
  function choose() {
    selections[questionCounter] = +$('input[name="answer"]:checked').val();
  }
  
  //Displays next requested element
  function displayNext() {
    quiz.fadeOut(function() {
      $('#question').remove();
      
      if(questionCounter < questions.length){
        var nextQuestion = createQuestionElement(questionCounter);
        quiz.append(nextQuestion).fadeIn();
        if (!(isNaN(selections[questionCounter]))) {
          $('input[value='+selections[questionCounter]+']').prop('checked', true);
        }
        
        // Controls display of 'prev' button
        if(questionCounter === 1){
          $('#prev').show();
        } else if(questionCounter === 0){
          
          $('#prev').hide();
          $('#submit').show();
        }
      }else {
        var scoreElem = displayScore();
        quiz.append(scoreElem).fadeIn();
        $('#submit').hide();
        $('#prev').hide();
        $('#start').show();
      }
    });
  }
  
  //Computes score and returns a paragraph element to be displayed
  function displayScore() {
    var score = $('<p>',{id: 'question'});
    
    var numCorrect = 0;
    for (var i = 0; i < selections.length; i++) {
      if (selections[i] === questions[i].correctAnswer) {
        numCorrect++;
      }
    }
    
    score.append('You got ' + numCorrect + ' questions out of ' +
                 questions.length + ' right!!!');
    return score;
  }



  