from rest_framework import viewsets
from access.models import Customer, Area, Rule, Logs
from access.serializers import CustomerSerializer, AreaSerializer, RuleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from datetime import date, time

class CustomerViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing Customer objects """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class AccessViewSet(APIView):
    """ ViewSet for checking if the customes has access to an area on a given timestamp. """

    def check_rule(self, rule, cst_name, balance, area, timestamp):
        """
        Helper function used in the POST HTTP processing method.

        :param rule: <class 'access.models.Rule'>
        :param cst_name: <class 'str'>
        :param balance: <class 'float'>
        :param area: <class 'str'>
        :param timestamp: <class 'datetime.datetime'>
        :return: <class 'tuple'>
        """

        date = timestamp.date()
        time = timestamp.time()

        if rule.visited_this_day:
            # there is a limitation - access denied if the customer had a visit in >>area<< on that day
            # pseudocode:
            # if Logs.objects.filter(cst_name && date && area):
            #   return (False, "Access denied: you have already been to >>area<< today.")

        if rule.from_time and rule.to_time:
            # checking whether current date fits into the interval
            start = rule.from_time
            end = rule.to_time
            if start <= end:    # not passing midnight
                if start <= time and end > time:
                    pass
                else:
                    # rule does not apply to this timestamp
                    return (None, None)
            else:   # passing midnight
                if start <= time or end > time:
                    pass
                else:
                    return (None, None)

        #   TODO: Handler for dates - similar to time

        if rule.free_per_stay:
            # pseudocode:
            # if Logs.objects.filter(cst_name && area) < rule.free_per_stay:
            #   price = 0
            if price == None:
                price = rule.price
            if price > balance:
                return (False, "You don't have enough funds on your account.")

        return (True, None)


    def post(self, cst_name, area, timestamp):
        """
        Returns content with two elements: (True/False, None/<str>)
        If access granted: (True, None)
        If access not granted: (False, explanation)

        :param cst_name: <class 'str'>
        :param area: <class 'str'>
        :param timestamp: <class 'datetime.datetime'>
        :return: <class 'rest_framework.response.Response'>
        """


        try:
            cst = Customer.objects.get(name=cst_name)
        except Customer.DoesNotExist:
            raise Http404

        # calculate the age of the person
        balance = cst.balance
        is_guest = cst.is_guest
        # exclude var is used later in exclusion filtering
        exclude = not is_guest


        # get the rules for area
        a_rules = Rule.objects.filter(area)
            if not a_rules:
                # No rules for this area - access forbidden!
                serializer = AccessSerializer(False, "Access to this area is forbidden.")
                return

        g_rules = a_rules.exclude(guest=exclude)
            if not g_rules and exclude = True:
                serializer = AccessSerializer(False, "This area is not accessible for non-guests.")
                return Response(serializer.data)
            elif not g_rules and exclude = False:
            serializer = AccessSerializer(False, "This area is not accessible for guests.")
                return Response(serializer.data)

        ad_rules = g_rules.exclude(adult=exclude)
            if not ad_rules and exclude = True:
                serializer = AccessSerializer(False, "This area is not accessible for adults.")
                return Response(serializer.data)
            elif not ad_rules and exclude = False:
                serializer = AccessSerializer(False, "This area is not accessible for underage.")
                return Response(serializer.data)

        w_rules = ad_rules.exclude(weekend=exclude)
            if not w_rules and exclude = True:
                serializer = AccessSerializer(False, "This area is not accessible on weekends.")
                return Response(serializer.data)
            elif not w_rules and exclude = False:
                serializer = AccessSerializer(False, "This area is not accessible on business days.")
                return Response(serializer.data)

        # w_rules is a QuerySet containing filtered rules based on is_guest, adult, weekend
        for rule in w_rules:
            access, description = check_rule(self, rule, cst_name, balance, area, timestamp)
            if access not None:
                serializer = AccessSerializer(access, description)
                return Response(serializer.data)
            # if access is None it means that the rule doesn't apply - continuing with the for loop