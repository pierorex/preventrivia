angular.module('app.controllers', [])
  
.controller('pollCtrl', function($scope, Question) {
  var questions = Question.query(function() {
    console.log(questions);
  });
})
   
.controller('recommendationsCtrl', function($scope) {

})
   
.controller('formationCtrl', function($scope) {

})
    