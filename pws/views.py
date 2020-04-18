from django.shortcuts import render
from sfl.models import sflOrderLine
from sfl.Operations.operations import *


# Create your views here.

def pwsView(request):
    return render(request,'ProvWorkSpace.html')

def sflOrderDataView(request):
    salesOrderNo=request.GET['salesOrderNo']

    Data=sflOrderLine.objects.filter(salesOrderNo=salesOrderNo)

    return render(request,'sflOrderData.html',{'salesOrderNo':Data[0].salesOrderNo,'offer':Data[0].offerName,'subRefId':Data[0].subRefId,'qty':Data[0].quantity})



def provisioningView(request):
    salesOrderNo=request.GET['salesOrderNo']
    Da=sflOrderLine.objects.all()
    for i in range(len(Da)):
        if salesOrderNo == Da[i].salesOrderNo:
            sflOrderLine.objects.filter(salesOrderNo=salesOrderNo).update(sflProvStatus='PROVISIONED')
            try:
                Sol_callback(GetSolCallBackRequest(salesOrderNo))
                return render(request, 'provision.html', {'salesOrderNo': salesOrderNo})
            except Exception as e:
                return e

    return render(request,'provision.html',{'salesOrderNo':'INVALID ORDER'})