angular.module('app.routes', [])

.config(function($stateProvider, $urlRouterProvider) {

  // Ionic uses AngularUI Router which uses the concept of states
  // Learn more here: https://github.com/angular-ui/ui-router
  // Set up the various states which the app can be in.
  // Each state's controller can be found in controllers.js
  $stateProvider
    
  

      .state('tabsController.poll', {
    url: '/poll',
    views: {
      'tab1': {
        templateUrl: 'templates/poll.html',
        controller: 'pollCtrl'
      }
    }
  })

  .state('tabsController.recommendations', {
    url: '/recommendations',
    views: {
      'tab2': {
        templateUrl: 'templates/recommendations.html',
        controller: 'recommendationsCtrl'
      }
    }
  })

  .state('tabsController.formation', {
    url: '/formation',
    views: {
      'tab3': {
        templateUrl: 'templates/formation.html',
        controller: 'formationCtrl'
      }
    }
  })

  .state('tabsController', {
    url: '/tabs',
    templateUrl: 'templates/tabsController.html',
    abstract:true
  })

$urlRouterProvider.otherwise('/tabs/poll')

  

});