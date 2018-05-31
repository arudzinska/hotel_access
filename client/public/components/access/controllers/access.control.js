access
    .controller('AccessController', function($scope, Customer) {
        Customer.query().$promise.then(function(data) {
            $scope.customers = data;
        });
});
