angular.module('app.controllers', [])
  
.controller('pollCtrl', function($scope, Question) {
  var questions = Question.query(function() {
    for (var i=0; i<questions.length; i++) {
      questions[i].index = i;
    }

    console.log(questions);
    $scope.actual_question = questions[0];
  });

  $scope.showNextQuestion = function() {
    if ($scope.actual_question.index == questions.length -1)
      $scope.actual_question = questions[0];
    else
      $scope.actual_question = questions[$scope.actual_question.index+1];
  };

  $scope.showPreviousQuestion = function() {
    if ($scope.actual_question.index == 0)
      $scope.actual_question = questions[questions.length-1];
    else
      $scope.actual_question = questions[$scope.actual_question.index-1];
  };
})
   
.controller('recommendationsCtrl', function($scope) {

})
   
.controller('formationCtrl', function($scope) {

})
    