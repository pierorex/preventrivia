angular.module('app.controllers', [])
  
.controller('pollCtrl', ['$scope', '$http', 'Question', 'Answer', function($scope, $http, Question, Answer) {
  $scope.questions = Question.query(function() {
    for (var i=0; i<$scope.questions.length; i++) {
      $scope.questions[i].index = i;
    }

    console.log($scope.questions);
    $scope.actual_question = $scope.questions[0];
    $scope.data = {
     availableOptions: $scope.actual_question.choice_set,
     selectedOption: $scope.actual_question.choice_set[0] //This sets the default value of the select in the ui
    };
    $scope.getAnswer();
  });

  $scope.getAnswer = function(){
    $http.post(
      'http://0.0.0.0:8000/api/answerUser',
      {
        'user': 1,
        'question': $scope.actual_question.id
      }, 
      {}
    ).then (
        function (response) {
          answerData = response.data;
          if(answerData.id != -1){
            for (elem in $scope.data.availableOptions){
              if($scope.data.availableOptions[elem].id == answerData.choice){
                $scope.data.selectedOption = $scope.data.availableOptions[elem];
              }
            }
          }
          $scope.answerId = answerData.id;
        },
        function (response) {
          console.log("Error");
          console.log(response);
        }
    );
  }

  $scope.showNextQuestion = function() {
    if ($scope.actual_question.index == $scope.questions.length -1)
      $scope.actual_question = $scope.questions[0];
    else
      $scope.actual_question = $scope.questions[$scope.actual_question.index+1];
    $scope.data = {
     availableOptions: $scope.actual_question.choice_set,
     selectedOption: $scope.actual_question.choice_set[0] //This sets the default value of the select in the ui
    };
    $scope.getAnswer();
  };

  $scope.showPreviousQuestion = function() {
    if ($scope.actual_question.index == 0)
      $scope.actual_question = $scope.questions[$scope.questions.length-1];
    else
      $scope.actual_question = $scope.questions[$scope.actual_question.index-1];
    $scope.data = {
     availableOptions: $scope.actual_question.choice_set,
     selectedOption: $scope.actual_question.choice_set[0] //This sets the default value of the select in the ui
    };
    $scope.getAnswer();
  };

  $scope.saveAnswer = function(){
    console.log($scope.answer);

    if($scope.answerId == -1){
      today = new Date();
      $scope.answer = new Answer;
      $scope.answer.date_time = today;
      $scope.answer.question = $scope.actual_question.id;
      $scope.answer.choice = $scope.data.selectedOption.id;
      $scope.answer.user = 1;

      $scope.answer.$save(function(){
        console.log("success Save");
      }, function(response){
        console.log(response);
      });
    } else {
      
      Answer.get({ id: $scope.answerId }, function(response) {
        console.log(response);
        response.choice = $scope.data.selectedOption.id;
  
        Answer.update({ id:$scope.answerId }, response);
        console.log("something")

      });
    }
  };

}])
   
.controller('recommendationsCtrl', function($scope) {

})
   
.controller('formationCtrl', function($scope, Tip) {
  $scope.tips = Tip.query(function() {
    console.log($scope.tips);
  });
})
    