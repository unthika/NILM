"""dbalready URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.generic import TemplateView
from dbapp.views import *
 
urlpatterns = [
    # Examples:
    # url(r'^$', 'sample.views.home', name='home'),
    # url(r'^sample/', include('sample.foo.urls')),
 
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
 
    # Uncomment the next line to enable the admin:
	
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'hello/$',myfunction),
	url(r'^$',graph),
	url(r'^piechart_show_total', piechart_show_total, name='piechart_show_total'),
	url(r'^on_percen', on_percen, name='on_percen'),
	url(r'^cluster_fge_data', cluster_fge_data, name='cluster_fge_data'),
	url(r'^cluster_dwe_data', cluster_dwe_data, name='cluster_dwe_data'),
	url(r'^cluster_cwe_data', cluster_cwe_data, name='cluster_cwe_data'),
	url(r'^cluster_fge_hour_data', cluster_fge_hour_data, name='cluster_fge_hour_data'),
	url(r'^cluster_dwe_hour_data', cluster_dwe_hour_data, name='cluster_dwe_hour_data'),
	url(r'^cluster_cwe_hour_data', cluster_cwe_hour_data, name='cluster_cwe_hour_data'),
	url(r'^cluster_fge_day_data', cluster_fge_day_data, name='cluster_fge_day_data'),
	url(r'^cluster_dwe_day_data', cluster_dwe_day_data, name='cluster_dwe_day_data'),
	url(r'^cluster_cwe_day_data', cluster_cwe_day_data, name='cluster_cwe_day_data'),
	url(r'^cluster_fge_month_data', cluster_fge_month_data, name='cluster_fge_month_data'),
	url(r'^cluster_dwe_month_data', cluster_dwe_month_data, name='cluster_dwe_month_data'),
	url(r'^cluster_cwe_month_data', cluster_cwe_month_data, name='cluster_cwe_month_data'),
	url(r'^cluster/cluster_interact_fge', cluster_interact_fge, name='cluster_interact_fge'),
	url(r'^cluster/cluster_interact_dwe', cluster_interact_dwe, name='cluster_interact_dwe'),
	url(r'^cluster/cluster_interact_cwe', cluster_interact_cwe, name='cluster_interact_cwe'),
	url(r'^cluster/cluster_interact_hour_fge', cluster_interact_hour_fge, name='cluster_interact_hour_fge'),
	url(r'^cluster/cluster_interact_hour_dwe', cluster_interact_hour_dwe, name='cluster_interact_hour_dwe'),
	url(r'^cluster/cluster_interact_hour_cwe', cluster_interact_hour_cwe, name='cluster_interact_hour_cwe'),
	url(r'^cluster/cluster_interact_day_fge', cluster_interact_day_fge, name='cluster_interact_day_fge'),
	url(r'^cluster/cluster_interact_day_dwe', cluster_interact_day_dwe, name='cluster_interact_day_dwe'),
	url(r'^cluster/cluster_interact_day_cwe', cluster_interact_day_cwe, name='cluster_interact_day_cwe'),
	url(r'^cluster/cluster_interact_month_fge', cluster_interact_month_fge, name='cluster_interact_month_fge'),
	url(r'^cluster/cluster_interact_month_dwe', cluster_interact_month_dwe, name='cluster_interact_month_dwe'),
	url(r'^cluster/cluster_interact_month_cwe', cluster_interact_month_cwe, name='cluster_interact_month_cwe'),
    url(r'^api/passing_pq', passing_pq, name='passing_pq'),
	url(r'^elec_scatter', elec_scatter, name='elec_scatter'),
	url(r'^api/passing_pt_fge.json$', passing_pt_fge, name='passing_pt_fge'),
	url(r'^elec_linegraph', elec_linegraph, name='elec_linegraph'),
	url(r'^api/passing_pt', passing_pt, name='passing_pt'),
	url(r'^scatter/elec_scatter_passing_pq_hour_fge', elec_scatter_passing_pq_hour_fge, name='elec_scatter_passing_pq_hour_fge'),
	url(r'^scatter/elec_scatter_passing_pq_hour_dwe', elec_scatter_passing_pq_hour_dwe, name='elec_scatter_passing_pq_hour_dwe'),
	url(r'^scatter/elec_scatter_passing_pq_hour_cwe', elec_scatter_passing_pq_hour_cwe, name='elec_scatter_passing_pq_hour_cwe'),
	url(r'^scatter/elec_scatter_passing_pq_day_fge', elec_scatter_passing_pq_day_fge, name='elec_scatter_passing_pq_day_fge'),
	url(r'^scatter/elec_scatter_passing_pq_day_dwe', elec_scatter_passing_pq_day_dwe, name='elec_scatter_passing_pq_day_dwe'),
	url(r'^scatter/elec_scatter_passing_pq_day_cwe', elec_scatter_passing_pq_day_cwe, name='elec_scatter_passing_pq_day_cwe'),
	url(r'^scatter/elec_scatter_passing_pq_month_fge', elec_scatter_passing_pq_month_fge, name='elec_scatter_passing_pq_month_fge'),
	url(r'^scatter/elec_scatter_passing_pq_month_dwe', elec_scatter_passing_pq_month_dwe, name='elec_scatter_passing_pq_month_dwe'),
	url(r'^scatter/elec_scatter_passing_pq_month_cwe', elec_scatter_passing_pq_month_cwe, name='elec_scatter_passing_pq_month_cwe'),
	url(r'^scatter/elec_scatter_passing_pq_year_fge', elec_scatter_passing_pq_year_fge, name='elec_scatter_passing_pq_year_fge'),
	url(r'^scatter/elec_scatter_passing_pq_year_dwe', elec_scatter_passing_pq_year_dwe, name='elec_scatter_passing_pq_year_dwe'),
	url(r'^scatter/elec_scatter_passing_pq_year_cwe', elec_scatter_passing_pq_year_cwe, name='elec_scatter_passing_pq_year_cwe'),
	url(r'^passing_pq_hour_fge', passing_pq_hour_fge, name='passing_pq_hour_fge'),
	url(r'^passing_pq_hour_dwe', passing_pq_hour_dwe, name='passing_pq_hour_dwe'),
	url(r'^passing_pq_hour_cwe', passing_pq_hour_cwe, name='passing_pq_hour_cwe'),
	url(r'^passing_pq_day_fge', passing_pq_day_fge, name='passing_pq_day_fge'),
	url(r'^passing_pq_day_dwe', passing_pq_day_dwe, name='passing_pq_day_dwe'),
	url(r'^passing_pq_day_cwe', passing_pq_day_cwe, name='passing_pq_day_cwe'),
	url(r'^passing_pq_month_fge', passing_pq_month_fge, name='passing_pq_month_fge'),
	url(r'^passing_pq_month_dwe', passing_pq_month_dwe, name='passing_pq_month_dwe'),
	url(r'^passing_pq_month_cwe', passing_pq_month_cwe, name='passing_pq_month_cwe'),
	url(r'^passing_pq_year_fge', passing_pq_year_fge, name='passing_pq_year_fge'),
	url(r'^passing_pq_year_dwe', passing_pq_year_dwe, name='passing_pq_year_dwe'),
	url(r'^passing_pq_year_cwe', passing_pq_year_cwe, name='passing_pq_year_cwe'),
	url(r'^show/elec_linegraph_passing_pq_hour_fge', elec_linegraph_passing_pq_hour_fge, name='elec_linegraph_passing_pq_hour_fge'),
	url(r'^show/elec_linegraph_passing_pq_hour_dwe', elec_linegraph_passing_pq_hour_dwe, name='elec_linegraph_passing_pq_hour_dwe'),
	url(r'^show/elec_linegraph_passing_pq_hour_cwe', elec_linegraph_passing_pq_hour_cwe, name='elec_linegraph_passing_pq_hour_cwe'),
	url(r'^show/elec_linegraph_passing_pq_day_fge', elec_linegraph_passing_pq_day_fge, name='elec_linegraph_passing_pq_day_fge'),
	url(r'^show/elec_linegraph_passing_pq_day_dwe', elec_linegraph_passing_pq_day_dwe, name='elec_linegraph_passing_pq_day_dwe'),
	url(r'^show/elec_linegraph_passing_pq_day_cwe', elec_linegraph_passing_pq_day_cwe, name='elec_linegraph_passing_pq_day_cwe'),
	url(r'^show/elec_linegraph_passing_pq_month_fge', elec_linegraph_passing_pq_month_fge, name='elec_linegraph_passing_pq_month_fge'),
	url(r'^show/elec_linegraph_passing_pq_month_dwe', elec_linegraph_passing_pq_month_dwe, name='elec_linegraph_passing_pq_month_dwe'),
	url(r'^show/elec_linegraph_passing_pq_month_cwe', elec_linegraph_passing_pq_month_cwe, name='elec_linegraph_passing_pq_month_cwe'),
	url(r'^show/elec_linegraph_passing_pq_year_fge', elec_linegraph_passing_pq_year_fge, name='elec_linegraph_passing_pq_year_fge'),
	url(r'^show/elec_linegraph_passing_pq_year_dwe', elec_linegraph_passing_pq_year_dwe, name='elec_linegraph_passing_pq_year_dwe'),
	url(r'^show/elec_linegraph_passing_pq_year_cwe', elec_linegraph_passing_pq_year_cwe, name='elec_linegraph_passing_pq_year_cwe'),
	]