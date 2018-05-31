access
    .controller('AccessController', function ($scope, $http) {

    $scope.data = {
        name: "default",
        area "default",
        time: "default"
    };
    $scope.submitForm = function() {
        console.log("posting data....");
        $http.post('http://localhost:8000/customers/', JSON.stringify(data)).success(function(){/*success callback*/});
    };
});
