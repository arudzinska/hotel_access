angular
    .module('appRoutes', ["ui.router"])
    .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {

    $stateProvider.state({
        name: 'access',
        url: '/',
        templateUrl: 'public/components/access/templates/access.template',
        controller: 'AccessController'
    });

    $urlRouterProvider.otherwise('/');
}])
