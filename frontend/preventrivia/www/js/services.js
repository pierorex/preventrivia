angular.module('app.services', ['ngResource'])


.config(function($resourceProvider) {
  $resourceProvider.defaults.stripTrailingSlashes = false;
})

.factory('Question', ['ApiUrl', '$resource', function(ApiUrl, $resource){
  return $resource(ApiUrl + '/api/question/:id');
}])
    
.factory('Tip', ['ApiUrl', '$resource', function(ApiUrl, $resource){
  return $resource(ApiUrl + '/api/tip/:id');
}])

.factory('Recommendation', ['ApiUrl', '$resource', function(ApiUrl, $resource){
  return $resource(ApiUrl + '/api/recommendation/:id');
}])

.factory('Answer', ['ApiUrl', '$resource', function(ApiUrl, $resource){
  return $resource(ApiUrl + '/api/answer/', {}, {
    update: { method: 'PUT' }
  });
}])    
.service('BlankService', [function(){

}]);
