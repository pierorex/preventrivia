angular.module('app.controllers', [])
  
.controller('pollCtrl', function($scope, Question, Answer) {
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
  });

  $scope.showNextQuestion = function() {
    if ($scope.actual_question.index == $scope.questions.length -1)
      $scope.actual_question = $scope.questions[0];
    else
      $scope.actual_question = $scope.questions[$scope.actual_question.index+1];
    $scope.data = {
     availableOptions: $scope.actual_question.choice_set,
     selectedOption: $scope.actual_question.choice_set[0] //This sets the default value of the select in the ui
    };
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
  };

  $scope.saveAnswer = function(){
    console.log($scope.actual_question);
    today = new Date();

    $scope.answer = new Answer;
    $scope.answer.date_time = today;
    $scope.answer.question = $scope.actual_question.id;
    $scope.answer.choice = $scope.data.selectedOption.id;
    $scope.answer.user = 1;
    console.log($scope.answer);

    $scope.answer.$save(function(){
      console.log("succes");
    }, function(response){
      console.log(response);
    });
  };

})
   
.controller('recommendationsCtrl', function($scope) {

})
   
.controller('formationCtrl', function($scope, Tip) {
  $scope.tips = Tip.query(function() {
    console.log($scope.tips);
  });
})
    