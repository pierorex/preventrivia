angular.module('app.routes', [])

.config(function($stateProvider, $urlRouterProvider) {

  // Ionic uses AngularUI Router which uses the concept of states
  // Learn more here: https://github.com/angular-ui/ui-router
  // Set up the various states which the app can be in.
  // Each state's controller can be found in controllers.js
  $stateProvider
    
  

      .state('tabsController.encuesta', {
    url: '/poll',
    views: {
      'tab1': {
        templateUrl: 'templates/encuesta.html',
        controller: 'encuestaCtrl'
      }
    }
  })

  .state('tabsController.recomendaciones', {
    url: '/recommendations',
    views: {
      'tab2': {
        templateUrl: 'templates/recomendaciones.html',
        controller: 'recomendacionesCtrl'
      }
    }
  })

  .state('tabsController.formaciN', {
    url: '/formation',
    views: {
      'tab3': {
        templateUrl: 'templates/formaciN.html',
        controller: 'formaciNCtrl'
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