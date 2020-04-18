from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from .serializers import InvokeProvSerializer
from .models import sflOrderLine

# Create your views here.

class InvokeProvisioning(APIView):
    def post(self,request):
        serializer=InvokeProvSerializer(data=request.data)
        if serializer.is_valid():
            ser = serializer.data
            sflOrderLine.objects.create(salesOrderNo=ser['salesOrderNo'],
                                        offerName=ser['offerName'],
                                        quantity=ser['quantity'],
                                        subRefId=ser['subRefId'],
                                        subscriptionId=ser['subscriptionId'],
                                        prov_email=ser['prov_email'],
                                        deliveryMethod=ser['deliveryMethod'],
                                        sflProvStatus='PROVISIONING'
                                        )


            resp={"status":"SUCCESS","salesOrderNo":ser['salesOrderNo'],"subRefId":ser['subRefId']}

            return Response(resp,status=200)
        else:
            return Response(serializer.errors,status=400)











