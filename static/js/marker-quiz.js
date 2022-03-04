 // initialize video.js

 var video = videojs('my_video');

 var questions = [{
    question: "What is your major?",
    choices: ['Internet Technology','Computing Science','Data Science','Software Development'],
    correctAnswer: 'Internet Technology'
  }, {
    question: "What is your major?",
    choices: ['Internet Technology','Computing Science','Data Science','Software Development'],
    correctAnswer: 'Computing Science'
  }];
  
  var questionCounter = 0; //Tracks question number
  var selections = []; //Array containing user choices
  var quiz = $('#quiz'); //Quiz div object
  
 console.log("marker-quiz.js is loading");
 //quiz可以先通过html页面存放到cookie中
 //记得在跳出页面时消除cookie


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
   markers: [
       //重构一下

       {time: 100, text:questions[0]},
       {time: 150, text:questions[1]},
   ]
 });

  // Click handler for the 'next' button
  $('#next').on('click', function (e) {
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
        questionCounter++;
        video.play()
      //After finishing a question, hide the quesition box
      $('#quiz-box').css('visibility', 'hidden');
    }
  });
  
  // Click handler for the 'prev' button
  $('#prev').on('click', function (e) {
    e.preventDefault();
    
    if(quiz.is(':animated')) {
      return false;
    }
    choose();
    questionCounter--;
    displayNext();
  });
  
  // Click handler for the 'Start Over' button
  $('#start').on('click', function (e) {
    e.preventDefault();
    
    if(quiz.is(':animated')) {
      return false;
    }
    questionCounter = 0;
    selections = [];
    displayNext();
    $('#start').hide();
  });
  
  // Animates buttons on hover
  $('.button').on('mouseenter', function () {
    $(this).addClass('active');
  });
  $('.button').on('mouseleave', function () {
    $(this).removeClass('active');
  });
  
  // Creates and returns the div that contains the questions and 
  // the answer selections
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
  
  // Creates a list of the answer choices as radio inputs
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
  
  // Reads the user selection and pushes the value to an array
  function choose() {
    selections[questionCounter] = +$('input[name="answer"]:checked').val();
  }
  
  // Displays next requested element
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
          $('#next').show();
        }
      }else {
        var scoreElem = displayScore();
        quiz.append(scoreElem).fadeIn();
        $('#next').hide();
        $('#prev').hide();
        $('#start').show();
      }
    });
  }
  
  // Computes score and returns a paragraph element to be displayed
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
