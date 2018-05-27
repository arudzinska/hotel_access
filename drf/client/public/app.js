'use strict';

var access = angular.module("access", []);

angular
    .module('SampleApplication', [
        'appRoutes',
        'access',
        'ngResource'
    ]);
