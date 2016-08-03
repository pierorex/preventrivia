angular.module('app.services', [])

.factory('Question', ['ApiUrl', '$resource', function(ApiUrl, $resource){
  return $resource(ApiUrl + '/api/question/:id');
}])
    
.factory('Tip', ['ApiUrl', '$resource', function(ApiUrl, $resource){
  return $resource(ApiUrl + '/api/tip/:id');
}])
    
.service('BlankService', [function(){

}]);
