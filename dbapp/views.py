from django.db import connections
from django.db.models import Count, F
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
import json
from django.template import loader, Context

from dbapp.models import *

def graph(request):
	return render(request, '../template/webpage.html')
	
def cluster_interact_fge(request):
	return render(request, '../template/cluster_interact_fge.html')
	
def cluster_interact_dwe(request):
	return render(request, '../template/cluster_interact_dwe.html')
	
def cluster_interact_cwe(request):
	return render(request, '../template/cluster_interact_cwe.html')
	
def cluster_interact_hour_fge(request):
	return render(request, '../template/cluster_interact_hour_fge.html')
	
def cluster_interact_hour_dwe(request):
	return render(request, '../template/cluster_interact_hour_dwe.html')
	
def cluster_interact_hour_cwe(request):
	return render(request, '../template/cluster_interact_hour_cwe.html')
	
def cluster_interact_day_fge(request):
	return render(request, '../template/cluster_interact_day_fge.html')
	
def cluster_interact_day_dwe(request):
	return render(request, '../template/cluster_interact_day_dwe.html')
	
def cluster_interact_day_cwe(request):
	return render(request, '../template/cluster_interact_day_cwe.html')
	
def cluster_interact_month_fge(request):
	return render(request, '../template/cluster_interact_month_fge.html')
	
def cluster_interact_month_dwe(request):
	return render(request, '../template/cluster_interact_month_dwe.html')
	
def cluster_interact_month_cwe(request):
	return render(request, '../template/cluster_interact_month_cwe.html')
	
def cluster_fge_data(request):
    data = ClusterElectricityFge.objects.values('p','q','meaning')
    return JsonResponse(list(data), safe=False)
	
def cluster_dwe_data(request):
    data = ClusterElectricityDwe.objects.values('p','q','meaning')
    return JsonResponse(list(data), safe=False)
	
def cluster_cwe_data(request):
    data = ClusterElectricityCwe.objects.values('p','q','meaning')
    return JsonResponse(list(data), safe=False)
	
def cluster_fge_hour_data(request):
    data = ClusterPreHourElectricityFge.objects.values('p','q','meaning')
    return JsonResponse(list(data), safe=False)
	
def cluster_dwe_hour_data(request):
    data = ClusterPreHourElectricityDwe.objects.values('p','q','meaning')
    return JsonResponse(list(data), safe=False)
	
def cluster_cwe_hour_data(request):
    data = ClusterPreHourElectricityCwe.objects.values('p','q','meaning')
    return JsonResponse(list(data), safe=False)

def cluster_fge_day_data(request):
    data = ClusterPreDayElectricityFge.objects.values('p','q','meaning')
    return JsonResponse(list(data), safe=False)

def cluster_dwe_day_data(request):
    data = ClusterPreDayElectricityDwe.objects.values('p','q','meaning')
    return JsonResponse(list(data), safe=False)
	
def cluster_cwe_day_data(request):
    data = ClusterPreDayElectricityCwe.objects.values('p','q','meaning')
    return JsonResponse(list(data), safe=False)
	
def cluster_fge_month_data(request):
    data = ClusterPreMonthElectricityFge.objects.values('p','q','meaning')
    return JsonResponse(list(data), safe=False)
	
def cluster_dwe_month_data(request):
    data = ClusterPreMonthElectricityDwe.objects.values('p','q','meaning')
    return JsonResponse(list(data), safe=False)
	
def cluster_cwe_month_data(request):
    data = ClusterPreMonthElectricityCwe.objects.values('p','q','meaning')
    return JsonResponse(list(data), safe=False)
	
def passing_pq(request):
    data = ElectricityFge.objects.filter(p__gt=0).values('p','q')
    return JsonResponse(list(data), safe=False)

def elec_scatter(request):
    return render(request, '../template/scatter.html')
	
def passing_pt(request):
	data = PreDayElectricityFge.objects.values('date_day','p', 'q')
	return JsonResponse(list(data), safe=False)

#############################################################################
##################################hour#########################################
def passing_pq_hour_fge(request):
	data = PreHourElectricityFge.objects.values('p', 'q', 'datetime_hour')
	return JsonResponse(list(data), safe=False)

def passing_pq_hour_dwe(request):
	data = PreHourElectricityDwe.objects.values('p', 'q', 'datetime_hour')
	return JsonResponse(list(data), safe=False)
	
def passing_pq_hour_cwe(request):
	data = PreHourElectricityCwe.objects.values('p', 'q', 'datetime_hour')
	return JsonResponse(list(data), safe=False)
	
	
###################################day##########################################
def passing_pq_day_fge(request):
	data = PreDayElectricityFge.objects.values('date_day','p', 'q')
	return JsonResponse(list(data), safe=False)

def passing_pq_day_dwe(request):
	data = PreDayElectricityDwe.objects.values('date_day','p', 'q')
	return JsonResponse(list(data), safe=False)
	
def passing_pq_day_cwe(request):
	data = PreDayElectricityCwe.objects.values('date_day','p', 'q')
	return JsonResponse(list(data), safe=False)

###################################month##########################################
def passing_pq_month_fge(request):
	data = PreMonthElectricityFge.objects.values('p', 'q', 'date_month')
	return JsonResponse(list(data), safe=False)

def passing_pq_month_dwe(request):
	data = PreMonthElectricityDwe.objects.values('p', 'q', 'date_month')
	return JsonResponse(list(data), safe=False)
	
def passing_pq_month_cwe(request):
	data = PreMonthElectricityCwe.objects.values('p', 'q', 'date_month')
	return JsonResponse(list(data), safe=False)

###################################year##########################################
def passing_pq_year_fge(request):
	data = PreYearElectricityFge.objects.values('p', 'q', 'date_year')
	return JsonResponse(list(data), safe=False)

def passing_pq_year_dwe(request):
	data = PreYearElectricityDwe.objects.values('p', 'q', 'date_year')
	return JsonResponse(list(data), safe=False)
	
def passing_pq_year_cwe(request):
	data = PreYearElectricityCwe.objects.values('p', 'q', 'date_year')
	return JsonResponse(list(data), safe=False)

#############################################################################	
#############################################################################	

#############################################################################
##################################hour#######################################
def elec_linegraph_passing_pq_hour_fge(request):
    return render(request, '../template/linegraph_hour_fge.html')

def elec_linegraph_passing_pq_hour_dwe(request):
    return render(request, '../template/linegraph_hour_dwe.html')
	
def elec_linegraph_passing_pq_hour_cwe(request):
    return render(request, '../template/linegraph_hour_cwe.html')
	
def elec_scatter_passing_pq_hour_fge(request):
    return render(request, '../template/scatterplot_hour_fge.html')
	
def elec_scatter_passing_pq_hour_dwe(request):
    return render(request, '../template/scatterplot_hour_dwe.html')
	
def elec_scatter_passing_pq_hour_cwe(request):
    return render(request, '../template/scatterplot_hour_cwe.html')
	
##################################day#######################################
def elec_linegraph_passing_pq_day_fge(request):
    return render(request, '../template/linegraph_day_fge.html')

def elec_linegraph_passing_pq_day_dwe(request):
    return render(request, '../template/linegraph_day_dwe.html')
	
def elec_linegraph_passing_pq_day_cwe(request):
    return render(request, '../template/linegraph_day_cwe.html')
	
def elec_scatter_passing_pq_day_fge(request):
    return render(request, '../template/scatterplot_day_fge.html')
	
def elec_scatter_passing_pq_day_dwe(request):
    return render(request, '../template/scatterplot_day_dwe.html')
	
def elec_scatter_passing_pq_day_cwe(request):
    return render(request, '../template/scatterplot_day_cwe.html')
	
##################################month#######################################
def elec_linegraph_passing_pq_month_fge(request):
    return render(request, '../template/linegraph_month_fge.html')

def elec_linegraph_passing_pq_month_dwe(request):
    return render(request, '../template/linegraph_month_dwe.html')
	
def elec_linegraph_passing_pq_month_cwe(request):
    return render(request, '../template/linegraph_month_cwe.html')
	
def elec_scatter_passing_pq_month_fge(request):
    return render(request, '../template/scatterplot_month_fge.html')
	
def elec_scatter_passing_pq_month_dwe(request):
    return render(request, '../template/scatterplot_month_dwe.html')
	
def elec_scatter_passing_pq_month_cwe(request):
    return render(request, '../template/scatterplot_month_cwe.html')
	
##################################year#######################################
def elec_linegraph_passing_pq_year_fge(request):
    return render(request, '../template/linegraph_year_fge.html')

def elec_linegraph_passing_pq_year_dwe(request):
    return render(request, '../template/linegraph_year_dwe.html')
	
def elec_linegraph_passing_pq_year_cwe(request):
    return render(request, '../template/linegraph_year_cwe.html')
	
def elec_scatter_passing_pq_year_fge(request):
    return render(request, '../template/scatterplot_year_fge.html')
	
def elec_scatter_passing_pq_year_dwe(request):
    return render(request, '../template/scatterplot_year_dwe.html')
	
def elec_scatter_passing_pq_year_cwe(request):
    return render(request, '../template/scatterplot_year_cwe.html')
#############################################################################		
#############################################################################		

# def date_select(request):
	# recieve_data = json.loads(request.GET.get('chanal'))
	# print(recieve_data['start_date'])
	# return JsonResponse({'server_startdate': recieve_data['start_date']})
	
def passing_pt_fge(request):
	#recieve_data = json.loads(request.GET.get('chanal'))
	data = ElectricityFge.objects.values('unix_ts','p', 'q')
	
	time_str = list(data)
	only_val = list()
	only_str = ""
	for i in range(0, len(time_str)):
		dt = datetime.datetime.fromtimestamp(time_str[i]["unix_ts"]).strftime('%Y-%b-%d %H:%M:%S')
		only_val.append({'unix_ts': dt, 'p' : int(time_str[i]["p"]), 'q' : int(time_str[i]["q"])})
	for j in range(0, len(only_val)):
		only_str = only_str + str(only_val[j]) + ','
		print(j)
		
	#return JsonResponse(only_val, safe=False)
	#print(recieve_data['start_date'])
	#return JsonResponse({'server_data': recieve_data['start_date']})
	only_str = only_str[:len(only_str)-1]
	print (only_str)
	return render(request,'linegraph.html', {'server_data': json.dumps(only_str)})
	
	
def elec_linegraph(request):
    return render(request, '../template/linegraph.html')

def piechart_show_total(request):
	fge = ElectricityFge.objects.values('s','p', 'q')
	dwe = ElectricityDwe.objects.values('s','p', 'q')
	cwe = ElectricityCwe.objects.values('s','p', 'q')
	
	fge_list = list(fge)
	dwe_list = list(dwe)
	cwe_list = list(cwe)

	data_list = list()
	
	fge_s = int(sum(item['s'] for item in fge_list)/1000)
	fge_p = int(sum(item['p'] for item in fge_list)/1000)
	fge_q = int(sum(item['q'] for item in fge_list)/1000)
	
	dwe_s = int(sum(item['s'] for item in dwe_list)/1000)
	dwe_p = int(sum(item['p'] for item in dwe_list)/1000)
	dwe_q = int(sum(item['q'] for item in dwe_list)/1000)
	
	cwe_s = int(sum(item['s'] for item in cwe_list)/1000)
	cwe_p = int(sum(item['p'] for item in cwe_list)/1000)
	cwe_q = int(sum(item['q'] for item in cwe_list)/1000)
	
	data_list.append(([fge_s, dwe_s, cwe_s], [fge_p, dwe_p, cwe_p], [fge_q, dwe_q, cwe_q]))
	
	return render(request,'piechart_total.html', {'value_rev': json.dumps(data_list[0])})
	
def on_percen(request):
	fge = ClusterElectricityFge.objects.values('time_ts').filter(meaning = 'ON\r')
	dwe = ClusterElectricityDwe.objects.values('time_ts').filter(meaning = 'ON\r')
	cwe = ClusterElectricityCwe.objects.values('time_ts').filter(meaning = 'ON\r')
	fge_c = ClusterElectricityFge.objects.all().count()
	dwe_c = ClusterElectricityDwe.objects.all().count()
	cwe_c = ClusterElectricityCwe.objects.all().count()

	fge_list = list(fge)
	dwe_list = list(dwe)
	cwe_list = list(cwe)

	data_1 = list()
	data_2 = list()
	data_3 = list()

	fge_r = (float(len(fge_list))/float(fge_c))*100.0
	dwe_r = (float(len(dwe_list))/float(dwe_c))*100.0
	cwe_r = (float(len(cwe_list))/float(cwe_c))*100.0
	
	for i in range(0, len(fge_list)):
		data_1.append([fge_list[i]["time_ts"], fge_r])
		
	for i in range(0, len(dwe_list)):
		data_2.append([dwe_list[i]["time_ts"], dwe_r])
	
	for i in range(0, len(cwe_list)):
		data_3.append([cwe_list[i]["time_ts"], cwe_r])

	
	return render(request,'percen_on.html', {'d1': json.dumps(data_1), 'd2': json.dumps(data_2), 'd3': json.dumps(data_3)})	
	