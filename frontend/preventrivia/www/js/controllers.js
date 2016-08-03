angular.module('app.controllers', [])
  
.controller('pollCtrl', function($scope, Question) {
  $scope.questions = Question.query(function() {
    for (var i=0; i<$scope.questions.length; i++) {
      $scope.questions[i].index = i;
    }

    console.log($scope.questions);
    $scope.actual_question = $scope.questions[0];
  });

  $scope.showNextQuestion = function() {
    if ($scope.actual_question.index == $scope.questions.length -1)
      $scope.actual_question = $scope.questions[0];
    else
      $scope.actual_question = $scope.questions[$scope.actual_question.index+1];
  };

  $scope.showPreviousQuestion = function() {
    if ($scope.actual_question.index == 0)
      $scope.actual_question = $scope.questions[$scope.questions.length-1];
    else
      $scope.actual_question = $scope.questions[$scope.actual_question.index-1];
  };
})
   
.controller('recommendationsCtrl', function($scope) {

})
   
.controller('formationCtrl', function($scope, Tip) {
  $scope.tips = Tip.query(function() {
    console.log($scope.tips);
  });
})
    