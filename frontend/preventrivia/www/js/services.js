angular.module('app.services', [])

.factory('Question', ['ApiUrl', '$resource', function(ApiUrl, $resource){
  return $resource(ApiUrl + '/api/question/:id');
}])

.service('BlankService', [function(){

}]);
