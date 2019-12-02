from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from sort_dataframeby_monthorweek import *
import pandas as pd

from django.http import JsonResponse

#lets take this out of the code
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


df = pd.read_csv('Corporate_Banking.csv')
pd.options.display.float_format = 'GHS {:,.2f}'.format
df['last_update'] = pd.to_datetime(df['last_update'])
df['monthname'] = df['last_update'].dt.month_name()
df['weekday'] = df['last_update'].dt.weekday_name
df['day'] = df['last_update'].dt.day
df['hour'] = df['last_update'].dt.hour
df['month'] = df['last_update'].dt.month


def service_value_counts(request):
    service_value_counts = df.groupby('provider_name')[['amount']].count().reset_index()
    service_value_counts = service_value_counts.to_dict('record')
    json_data = JsonResponse(service_value_counts, safe=False)
    return json_data


def service_revenue(request):
    service_revenue = df.groupby('provider_name')[['amount']].sum().reset_index()
    service_revenue = service_revenue.to_dict('r')
    json_data = JsonResponse(service_revenue, safe=False)
    return json_data


def service(request):
    service = pd.pivot_table(df, values=['amount', 'recipient_bank_name'], index=['provider_name'],
                             aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'service_revenue', 'recipient_bank_name': 'service_count'})
    service = service.to_dict('r')
    json_data = JsonResponse(service, safe=False)
    return json_data


def all_monthly_service(request):
    all_monthly_service = pd.pivot_table(df, values=['amount', 'recipient_bank_name'], index=['monthname', 'provider_name'],
                                     aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'monthly_service_revenue', 'recipient_bank_name': 'monthly_service_count'})
    all_monthly_service = Sort_Dataframeby_Month(df=all_monthly_service, monthcolumnname='monthname')
    all_monthly_service = all_monthly_service.to_dict('r')
    json_data = JsonResponse(all_monthly_service, safe=False)
    return json_data


def all_weekday_service(request):
    all_weekday_service = pd.pivot_table(df, values=['amount', 'recipient_bank_name'], index=['weekday', 'provider_name'],
                                     aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'weekday_service_revenue', 'recipient_bank_name': 'weekday_service_count'})
    all_weekday_service = Sort_Dataframeby_Weekday(df=all_weekday_service, Weekdaycolumnname='weekday')
    all_weekday_service = all_weekday_service.to_dict('r')
    json_data = JsonResponse(all_weekday_service, safe=False)
    return json_data


def all_daily_service(request):
    all_daily_service = pd.pivot_table(df, values=['amount', 'recipient_bank_name'], index=['day', 'provider_name'],
                                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'daily_service_revenue', 'recipient_bank_name': 'daily_service_count'})
    all_daily_service = all_daily_service.to_dict('r')
    json_data = JsonResponse(all_daily_service, safe=False)
    return json_data


def all_hourly_service(request):
    all_hourly_service = pd.pivot_table(df, values=['amount', 'recipient_bank_name'], index=['hour', 'provider_name'],
                                    aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'hourly_service_revenue', 'recipient_bank_name': 'hourly_service_count'})
    all_hourly_service = all_hourly_service.to_dict('r')
    json_data = JsonResponse(all_hourly_service, safe=False)
    return json_data


def all_june_weekday_service(request):
    all_june_weekday_service = pd.pivot_table(df[df['monthname'] == 'June'], values=['amount', 'recipient_bank_name'],
                                        index=['provider_name', 'weekday'],
                                        aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'june_service_revenue', 'recipient_bank_name': 'june_service_count'})
    all_june_weekday_service = all_june_weekday_service.to_dict('r')
    json_data = JsonResponse(all_june_weekday_service, safe=False)
    return json_data


def all_june_daily_service(request):
    all_june_daily_service = pd.pivot_table(df[df['monthname'] == 'June'], values=['amount', 'recipient_bank_name'],
                                        index=['provider_name', 'day'],
                                        aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'june_service_revenue', 'recipient_bank_name': 'june_service_count'})
    all_june_daily_service = all_june_daily_service.to_dict('r')
    json_data = JsonResponse(all_june_daily_service, safe=False)
    return json_data


def all_june_hourly_service(request):
    all_june_weekday_service = pd.pivot_table(df[df['monthname'] == 'June'], values=['amount', 'recipient_bank_name'],
                                        index=['provider_name', 'hour'],
                                        aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'june_service_revenue', 'recipient_bank_name': 'june_service_count'})
    all_june_weekday_service = all_june_weekday_service.to_dict('r')
    json_data = JsonResponse(all_june_weekday_service, safe=False)
    return json_data


def all_july_weekday_service(request):
    all_july_weekday_service = pd.pivot_table(df[df['monthname'] == 'July'], values=['amount', 'recipient_bank_name'],
                                        index=['provider_name', 'weekday'],
                                        aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'july_service_revenue', 'recipient_bank_name': 'july_service_count'})
    all_july_weekday_service = all_july_weekday_service.to_dict('r')
    json_data = JsonResponse(all_july_weekday_service, safe=False)
    return json_data


def all_july_daily_service(request):
    all_july_daily_service = pd.pivot_table(df[df['monthname'] == 'July'], values=['amount', 'recipient_bank_name'],
                                        index=['provider_name', 'day'],
                                        aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'july_service_revenue', 'recipient_bank_name': 'july_service_count'})
    all_july_daily_service = all_july_daily_service.to_dict('r')
    json_data = JsonResponse(all_july_daily_service, safe=False)
    return json_data


def all_july_hourly_service(request):
    all_july_hourly_service = pd.pivot_table(df[df['monthname'] == 'July'], values=['amount', 'recipient_bank_name'],
                                        index=['provider_name', 'hour'],
                                        aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'july_service_revenue', 'recipient_bank_name': 'july_service_count'})
    all_july_hourly_service = all_july_hourly_service.to_dict('r')
    json_data = JsonResponse(all_july_hourly_service, safe=False)
    return json_data


def all_aug_weekday_service(request):
    all_aug_weekday_service = pd.pivot_table(df[df['monthname'] == 'August'], values=['amount', 'recipient_bank_name'],
                                       index=['provider_name', 'weekday'],
                                       aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'aug_service_revenue', 'recipient_bank_name': 'aug_service_count'})
    all_aug_weekday_service = all_aug_weekday_service.to_dict('r')
    json_data = JsonResponse(all_aug_weekday_service, safe=False)
    return json_data

def all_aug_daily_service(request):
    all_aug_daily_service = pd.pivot_table(df[df['monthname'] == 'August'], values=['amount', 'recipient_bank_name'],
                                       index=['provider_name', 'day'],
                                       aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'aug_service_revenue', 'recipient_bank_name': 'aug_service_count'})
    all_aug_daily_service = all_aug_daily_service.to_dict('r')
    json_data = JsonResponse(all_aug_daily_service, safe=False)
    return json_data


def all_aug_hourly_service(request):
    all_aug_hourly_service = pd.pivot_table(df[df['monthname'] == 'August'], values=['amount', 'recipient_bank_name'],
                                       index=['provider_name', 'hour'],
                                       aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'aug_service_revenue', 'recipient_bank_name': 'aug_service_count'})
    all_aug_hourly_service = all_aug_hourly_service.to_dict('r')
    json_data = JsonResponse(all_aug_hourly_service, safe=False)
    return json_data


def all_sep_weekday_service(request):
    all_sep_weekday_service = pd.pivot_table(df[df['monthname'] == 'September'], values=['amount', 'recipient_bank_name'],
                                       index=['provider_name', 'weekday'],
                                       aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'sep_service_revenue', 'recipient_bank_name': 'sep_service_count'})
    all_sep_weekday_service = all_sep_weekday_service.to_dict('r')
    json_data = JsonResponse(all_sep_weekday_service, safe=False)
    return json_data

def all_sep_daily_service(request):
    all_sep_daily_service = pd.pivot_table(df[df['monthname'] == 'September'], values=['amount', 'recipient_bank_name'],
                                       index=['provider_name', 'day'],
                                       aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'sep_service_revenue', 'recipient_bank_name': 'sep_service_count'})
    all_sep_daily_service = all_sep_daily_service.to_dict('r')
    json_data = JsonResponse(all_sep_daily_service, safe=False)
    return json_data


def all_sep_hourly_service(request):
    all_sep_hourly_service = pd.pivot_table(df[df['monthname'] == 'September'], values=['amount', 'recipient_bank_name'],
                                       index=['provider_name', 'hour'],
                                       aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'sep_service_revenue', 'recipient_bank_name': 'sep_service_count'})
    all_sep_hourly_service = all_sep_hourly_service.to_dict('r')
    json_data = JsonResponse(all_sep_hourly_service, safe=False)
    return json_data


def all_recipient_channel(request):
    all_recipient_channel = pd.pivot_table(df, values=['amount', 'provider_name'], index=['recipient_bank_name'],
                               aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'recipient_revenue', 'provider_name': 'recipient_count'})
    all_recipient_channel = all_recipient_channel.to_dict('r')
    json_data = JsonResponse(all_recipient_channel, safe=False)
    return json_data


def all_monthly_recipient_channel(request):
    all_monthly_recipient_channel = pd.pivot_table(df, values=['amount', 'provider_name'],
                                       index=['monthname', 'recipient_bank_name'],
                                       aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'monthly_recipient_revenue', 'provider_name': 'monthly_recipient_count'})
    all_monthly_recipient_channel = Sort_Dataframeby_Month(df=all_monthly_recipient_channel, monthcolumnname='monthname')
    all_monthly_recipient_channel = all_monthly_recipient_channel.to_dict('r')
    json_data = JsonResponse(all_monthly_recipient_channel, safe=False)
    return json_data


def all_weekday_recipient_channel(request):
    all_weekday_recipient_channel = pd.pivot_table(df, values=['amount', 'provider_name'], index=['weekday', 'recipient_bank_name'],
                                       aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'weekday_recipient_revenue', 'provider_name': 'weekday_recipient_count'})
    all_weekday_recipient_channel = Sort_Dataframeby_Weekday(df=all_weekday_recipient_channel, Weekdaycolumnname='weekday')
    all_weekday_recipient_channel = all_weekday_recipient_channel.to_dict('r')
    json_data = JsonResponse(all_weekday_recipient_channel, safe=False)
    return json_data


def all_daily_recipient_channel(request):
    all_daily_recipient_channel = pd.pivot_table(df, values=['amount', 'provider_name'], index=['day', 'recipient_bank_name'],
                                     aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'daily_recipient_revenue', 'provider_name': 'daily_recipient_count'})
    all_daily_recipient_channel = all_daily_recipient_channel.to_dict('r')
    json_data = JsonResponse(all_daily_recipient_channel, safe=False)
    return json_data


def all_hourly_recipient_channel(request):
    all_hourly_recipient_channel = pd.pivot_table(df, values=['amount', 'provider_name'], index=['hour', 'recipient_bank_name'],
                                      aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'hourly_recipient_revenue', 'provider_name': 'hourly_recipient_count'})
    all_hourly_recipient_channel = all_hourly_recipient_channel.to_dict('r')
    json_data = JsonResponse(all_hourly_recipient_channel, safe=False)
    return json_data


def all_june_weekday_recipient(request):
    all_june_weekday_recipient = pd.pivot_table(df[df['monthname'] == 'June'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'weekday'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'june_service_revenue', 'provider_name': 'june_service_count'})
    all_june_weekday_recipient = all_june_weekday_recipient.to_dict('r')
    json_data = JsonResponse(all_june_weekday_recipient, safe=False)
    return json_data


def all_june_daily_recipient(request):
    all_june_daily_recipient = pd.pivot_table(df[df['monthname'] == 'June'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'day'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'june_service_revenue', 'provider_name': 'june_service_count'})
    all_june_daily_recipient = all_june_daily_recipient.to_dict('r')
    json_data = JsonResponse(all_june_daily_recipient, safe=False)
    return json_data


def all_june_hourly_recipient(request):
    all_june_hour_recipient = pd.pivot_table(df[df['monthname'] == 'June'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'hour'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'june_service_revenue', 'provider_name': 'june_service_count'})
    all_june_hour_recipient = all_june_hour_recipient.to_dict('r')
    json_data = JsonResponse(all_june_hour_recipient, safe=False)
    return json_data


def all_july_weekday_recipient(request):
    all_july_weekday_recipient = pd.pivot_table(df[df['monthname'] == 'July'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'weekday'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'july_service_revenue', 'provider_name': 'july_service_count'})
    all_july_weekday_recipient = all_july_weekday_recipient.to_dict('r')
    json_data = JsonResponse(all_july_weekday_recipient, safe=False)
    return json_data


def all_july_daily_recipient(request):
    all_july_daily_recipient = pd.pivot_table(df[df['monthname'] == 'July'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'day'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'july_service_revenue', 'provider_name': 'july_service_count'})
    all_july_daily_recipient = all_july_daily_recipient.to_dict('r')
    json_data = JsonResponse(all_july_daily_recipient, safe=False)
    return json_data


def all_july_hourly_recipient(request):
    all_july_hourly_recipient = pd.pivot_table(df[df['monthname'] == 'July'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'hour'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'july_service_revenue', 'provider_name': 'july_service_count'})
    all_july_hourly_recipient = all_july_hourly_recipient.to_dict('r')
    json_data = JsonResponse(all_july_hourly_recipient, safe=False)
    return json_data


def all_aug_weekday_recipient(request):
    all_aug_weekday_recipient = pd.pivot_table(df[df['monthname'] == 'August'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'weekday'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'aug_service_revenue', 'provider_name': 'aug_service_count'})
    all_aug_weekday_recipient = all_aug_weekday_recipient.to_dict('r')
    json_data = JsonResponse(all_aug_weekday_recipient, safe=False)
    return json_data


def all_aug_daily_recipient(request):
    all_aug_daily_recipient = pd.pivot_table(df[df['monthname'] == 'August'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'day'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'aug_service_revenue', 'provider_name': 'aug_service_count'})
    all_aug_daily_recipient = all_aug_daily_recipient.to_dict('r')
    json_data = JsonResponse(all_aug_daily_recipient, safe=False)
    return json_data


def all_aug_hourly_recipient(request):
    all_aug_hourly_recipient = pd.pivot_table(df[df['monthname'] == 'August'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'hour'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'aug_service_revenue', 'provider_name': 'aug_service_count'})
    all_aug_hourly_recipient = all_aug_hourly_recipient.to_dict('r')
    json_data = JsonResponse(all_aug_hourly_recipient, safe=False)
    return json_data


def all_sep_weekday_recipient(request):
    all_sep_weekday_recipient = pd.pivot_table(df[df['monthname'] == 'September'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'weekday'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'sep_service_revenue', 'provider_name': 'sep_service_count'})
    all_sep_weekday_recipient = all_sep_weekday_recipient.to_dict('r')
    json_data = JsonResponse(all_sep_weekday_recipient, safe=False)
    return json_data


def all_sep_daily_recipient(request):
    all_sep_daily_recipient = pd.pivot_table(df[df['monthname'] == 'September'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'day'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'sep_service_revenue', 'provider_name': 'sep_service_count'})
    all_sep_daily_recipient = all_sep_daily_recipient.to_dict('r')
    json_data = JsonResponse(all_sep_daily_recipient, safe=False)
    return json_data


def all_sep_hourly_recipient(request):
    all_sep_hourly_recipient = pd.pivot_table(df[df['monthname'] == 'September'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'hour'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'sep_service_revenue', 'provider_name': 'sep_service_count'})
    all_sep_hourly_recipient = all_sep_hourly_recipient.to_dict('r')
    json_data = JsonResponse(all_sep_hourly_recipient, safe=False)
    return json_data


def all_uniq_batch(request):
    all_uniq_batch = pd.pivot_table(df, values=['amount', 'recipient_bank_name'], index=['batch_uuid'],
                           aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'batch_revenue', 'recipient_bank_name': 'batch_count'})
    all_uniq_batch = all_uniq_batch.to_dict('r')
    json_data = JsonResponse(all_uniq_batch, safe=False)
    return json_data


def transaction_status(request):
    transaction_status = df.groupby('transaction_status')[['batch_uuid']].count().reset_index()
    transaction_status = transaction_status.to_dict('r')
    json_data = JsonResponse(transaction_status, safe=False)
    return json_data


data = df[df['transaction_status'] == 'PAID']


def paid_service(request):
    paid_service = pd.pivot_table(data, values=['amount', 'recipient_bank_name'], index=['provider_name'],
                            aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'chanel_revenue', 'recipient_bank_name': 'chanel_count'})
    paid_service = paid_service.to_dict('r')
    json_data = JsonResponse(paid_service, safe=False)
    return json_data


def paid_service_count(request):
    paid_service_count = data.groupby('provider_name')[['amount']].count().reset_index()
    paid_service_count = paid_service_count.to_dict('record')
    json_data = JsonResponse(paid_service_count, safe=False)
    return json_data


def paid_service_revenue(request):
    paid_service_revenue = data.groupby('provider_name')[['amount']].sum().reset_index()
    paid_service_revenue = paid_service_revenue.to_dict('r')
    json_data = JsonResponse(paid_service_revenue, safe=False)
    return json_data


def paid_monthly_service(request):
    paid_monthly_service = pd.pivot_table(data, values=['amount', 'recipient_bank_name'], index=['monthname', 'provider_name'],
                                     aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'monthly_service_revenue', 'recipient_bank_name': 'monthly_service_count'})
    paid_monthly_service = Sort_Dataframeby_Month(df=paid_monthly_service, monthcolumnname='monthname')
    paid_monthly_service = paid_monthly_service.to_dict('r')
    json_data = JsonResponse(paid_monthly_service, safe=False)
    return json_data


def paid_weekday_service(request):
    paid_weekday_service = pd.pivot_table(data, values=['amount', 'recipient_bank_name'], index=['weekday', 'provider_name'],
                                     aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'weekday_service_revenue', 'recipient_bank_name': 'weekday_service_count'})
    paid_weekday_service = Sort_Dataframeby_Weekday(df=paid_weekday_service, Weekdaycolumnname='weekday')
    paid_weekday_service = paid_weekday_service.to_dict('r')
    json_data = JsonResponse(paid_weekday_service, safe=False)
    return json_data


def paid_daily_service(request):
    paid_daily_service = pd.pivot_table(data, values=['amount', 'recipient_bank_name'], index=['day', 'provider_name'],
                                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'daily_service_revenue', 'recipient_bank_name': 'daily_service_count'})
    paid_daily_service = paid_daily_service.to_dict('r')
    json_data = JsonResponse(paid_daily_service, safe=False)
    return json_data


def paid_hourly_service(request):
    paid_hourly_service = pd.pivot_table(data, values=['amount', 'recipient_bank_name'], index=['hour', 'provider_name'],
                                    aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'hourly_service_revenue', 'recipient_bank_name': 'hourly_service_count'})
    paid_hourly_service = paid_hourly_service.to_dict('r')
    json_data = JsonResponse(paid_hourly_service, safe=False)
    return json_data


def paid_june_weekday_service(request):
    paid_june_weekday_service = pd.pivot_table(data[data['monthname'] == 'June'], values=['amount', 'recipient_bank_name'],
                                        index=['provider_name', 'weekday'],
                                        aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'june_service_revenue', 'recipient_bank_name': 'june_service_count'})
    paid_june_weekday_service = paid_june_weekday_service.to_dict('r')
    json_data = JsonResponse(paid_june_weekday_service, safe=False)
    return json_data


def paid_june_daily_service(request):
    paid_june_daily_service = pd.pivot_table(data[data['monthname'] == 'June'], values=['amount', 'recipient_bank_name'],
                                        index=['provider_name', 'day'],
                                        aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'june_service_revenue', 'recipient_bank_name': 'june_service_count'})
    paid_june_daily_service = paid_june_daily_service.to_dict('r')
    json_data = JsonResponse(paid_june_daily_service, safe=False)
    return json_data


def paid_june_hourly_service(request):
    paid_june_hourly_service = pd.pivot_table(data[data['monthname'] == 'June'], values=['amount', 'recipient_bank_name'],
                                        index=['provider_name', 'hour'],
                                        aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'june_service_revenue', 'recipient_bank_name': 'june_service_count'})
    paid_june_hourly_service = paid_june_hourly_service.to_dict('r')
    json_data = JsonResponse(paid_june_hourly_service, safe=False)
    return json_data


def paid_july_weekday_service(request):
    paid_july_weekday_service = pd.pivot_table(data[data['monthname'] == 'July'], values=['amount', 'recipient_bank_name'],
                                        index=['provider_name', 'weekday'],
                                        aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'july_service_revenue', 'recipient_bank_name': 'july_service_count'})
    paid_july_weekday_service = paid_july_weekday_service.to_dict('r')
    json_data = JsonResponse(paid_july_weekday_service, safe=False)
    return json_data


def paid_july_daily_service(request):
    paid_july_daily_service = pd.pivot_table(data[data['monthname'] == 'July'], values=['amount', 'recipient_bank_name'],
                                        index=['provider_name', 'day'],
                                        aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'july_service_revenue', 'recipient_bank_name': 'july_service_count'})
    paid_july_daily_service = paid_july_daily_service.to_dict('r')
    json_data = JsonResponse(paid_july_daily_service, safe=False)
    return json_data


def paid_july_hourly_service(request):
    paid_july_hourly_service = pd.pivot_table(data[data['monthname'] == 'July'], values=['amount', 'recipient_bank_name'],
                                        index=['provider_name', 'hour'],
                                        aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'july_service_revenue', 'recipient_bank_name': 'july_service_count'})
    paid_july_hourly_service = paid_july_hourly_service.to_dict('r')
    json_data = JsonResponse(paid_july_hourly_service, safe=False)
    return json_data


def paid_aug_weekday_service(request):
    paid_aug_weekday_service = pd.pivot_table(data[data['monthname'] == 'August'], values=['amount', 'recipient_bank_name'],
                                       index=['provider_name', 'weekday'],
                                       aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'aug_service_revenue', 'recipient_bank_name': 'aug_service_count'})
    paid_aug_weekday_service = paid_aug_weekday_service.to_dict('r')
    json_data = JsonResponse(paid_aug_weekday_service, safe=False)
    return json_data

def paid_aug_daily_service(request):
    paid_aug_daily_service = pd.pivot_table(data[data['monthname'] == 'August'], values=['amount', 'recipient_bank_name'],
                                       index=['provider_name', 'day'],
                                       aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'aug_service_revenue', 'recipient_bank_name': 'aug_service_count'})
    paid_aug_daily_service = paid_aug_daily_service.to_dict('r')
    json_data = JsonResponse(paid_aug_daily_service, safe=False)
    return json_data


def paid_aug_hourly_service(request):
    paid_aug_hourly_service = pd.pivot_table(data[data['monthname'] == 'August'], values=['amount', 'recipient_bank_name'],
                                       index=['provider_name', 'hour'],
                                       aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'aug_service_revenue', 'recipient_bank_name': 'aug_service_count'})
    paid_aug_hourly_service = paid_aug_hourly_service.to_dict('r')
    json_data = JsonResponse(paid_aug_hourly_service, safe=False)
    return json_data


def paid_sep_weekday_service(request):
    paid_sep_weekday_service = pd.pivot_table(data[data['monthname'] == 'September'], values=['amount', 'recipient_bank_name'],
                                       index=['provider_name', 'weekday'],
                                       aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'sep_service_revenue', 'recipient_bank_name': 'sep_service_count'})
    paid_sep_weekday_service = paid_sep_weekday_service.to_dict('r')
    json_data = JsonResponse(paid_sep_weekday_service, safe=False)
    return json_data

def paid_sep_daily_service(request):
    paid_sep_daily_service = pd.pivot_table(data[data['monthname'] == 'September'], values=['amount', 'recipient_bank_name'],
                                       index=['provider_name', 'day'],
                                       aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'sep_service_revenue', 'recipient_bank_name': 'sep_service_count'})
    paid_sep_daily_service = paid_sep_daily_service.to_dict('r')
    json_data = JsonResponse(paid_sep_daily_service, safe=False)
    return json_data


def paid_sep_hourly_service(request):
    paid_sep_hourly_service = pd.pivot_table(data[data['monthname'] == 'September'], values=['amount', 'recipient_bank_name'],
                                       index=['provider_name', 'hour'],
                                       aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'sep_service_revenue', 'recipient_bank_name': 'sep_service_count'})
    paid_sep_hourly_service = paid_sep_hourly_service.to_dict('r')
    json_data = JsonResponse(paid_sep_hourly_service, safe=False)
    return json_data


def paid_recipient_channel(request):
    paid_recipient_channel = pd.pivot_table(data, values=['amount', 'provider_name'], index=['recipient_bank_name'],
                               aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'recipient_revenue', 'provider_name': 'recipient_count'})
    paid_recipient_channel = paid_recipient_channel.to_dict('r')
    json_data = JsonResponse(paid_recipient_channel, safe=False)
    return json_data


def paid_monthly_recipient_channel(request):
    paid_monthly_recipient_channel = pd.pivot_table(data, values=['amount', 'provider_name'],
                                       index=['monthname', 'recipient_bank_name'],
                                       aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'monthly_recipient_revenue', 'provider_name': 'monthly_recipient_count'})
    paid_monthly_recipient_channel = Sort_Dataframeby_Month(df=paid_monthly_recipient_channel, monthcolumnname='monthname')
    paid_monthly_recipient_channel = paid_monthly_recipient_channel.to_dict('r')
    json_data = JsonResponse(paid_monthly_recipient_channel, safe=False)
    return json_data


def paid_weekday_recipient_channel(request):
    paid_weekday_recipient_channel = pd.pivot_table(data, values=['amount', 'provider_name'], index=['weekday', 'recipient_bank_name'],
                                       aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'weekday_recipient_revenue', 'provider_name': 'weekday_recipient_count'})
    paid_weekday_recipient_channel = Sort_Dataframeby_Weekday(df=paid_weekday_recipient_channel, Weekdaycolumnname='weekday')
    paid_weekday_recipient_channel = paid_weekday_recipient_channel.to_dict('r')
    json_data = JsonResponse(paid_weekday_recipient_channel, safe=False)
    return json_data


def paid_daily_recipient_channel(request):
    paid_daily_recipient_channel = pd.pivot_table(data, values=['amount', 'provider_name'], index=['day', 'recipient_bank_name'],
                                     aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'daily_recipient_revenue', 'provider_name': 'daily_recipient_count'})
    paid_daily_recipient_channel = paid_daily_recipient_channel.to_dict('r')
    json_data = JsonResponse(paid_daily_recipient_channel, safe=False)
    return json_data


def paid_hourly_recipient_channel(request):
    paid_hourly_recipient_channel = pd.pivot_table(data, values=['amount', 'provider_name'], index=['hour', 'recipient_bank_name'],
                                      aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'hourly_recipient_revenue', 'provider_name': 'hourly_recipient_count'})
    paid_hourly_recipient_channel = paid_hourly_recipient_channel.to_dict('r')
    json_data = JsonResponse(paid_hourly_recipient_channel, safe=False)
    return json_data


def paid_june_weekday_recipient(request):
    paid_june_weekday_recipient = pd.pivot_table(data[data['monthname'] == 'June'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'weekday'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'june_service_revenue', 'provider_name': 'june_service_count'})
    paid_june_weekday_recipient = paid_june_weekday_recipient.to_dict('r')
    json_data = JsonResponse(paid_june_weekday_recipient, safe=False)
    return json_data


def paid_june_daily_recipient(request):
    paid_june_daily_recipient = pd.pivot_table(data[data['monthname'] == 'June'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'day'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'june_service_revenue', 'provider_name': 'june_service_count'})
    paid_june_daily_recipient = paid_june_daily_recipient.to_dict('r')
    json_data = JsonResponse(paid_june_daily_recipient, safe=False)
    return json_data


def paid_june_hourly_recipient(request):
    paid_june_hourly_recipient = pd.pivot_table(data[data['monthname'] == 'June'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'hour'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'june_service_revenue', 'provider_name': 'june_service_count'})
    paid_june_hourly_recipient = paid_june_hourly_recipient.to_dict('r')
    json_data = JsonResponse(paid_june_hourly_recipient, safe=False)
    return json_data


def paid_july_weekday_recipient(request):
    paid_july_weekday_recipient = pd.pivot_table(data[data['monthname'] == 'July'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'weekday'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'july_service_revenue', 'provider_name': 'july_service_count'})
    paid_july_weekday_recipient = paid_july_weekday_recipient.to_dict('r')
    json_data = JsonResponse(paid_july_weekday_recipient, safe=False)
    return json_data


def paid_july_daily_recipient(request):
    paid_july_daily_recipient = pd.pivot_table(data[data['monthname'] == 'July'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'day'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'july_service_revenue', 'provider_name': 'july_service_count'})
    paid_july_daily_recipient = paid_july_daily_recipient.to_dict('r')
    json_data = JsonResponse(paid_july_daily_recipient, safe=False)
    return json_data


def paid_july_hourly_recipient(request):
    paid_july_hourly_recipient = pd.pivot_table(data[data['monthname'] == 'July'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'hour'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'july_service_revenue', 'provider_name': 'july_service_count'})
    paid_july_hourly_recipient = paid_july_hourly_recipient.to_dict('r')
    json_data = JsonResponse(paid_july_hourly_recipient, safe=False)
    return json_data


def paid_aug_weekday_recipient(request):
    paid_aug_weekday_recipient = pd.pivot_table(data[data['monthname'] == 'August'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'weekday'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'aug_service_revenue', 'provider_name': 'aug_service_count'})
    paid_aug_weekday_recipient = paid_aug_weekday_recipient.to_dict('r')
    json_data = JsonResponse(paid_aug_weekday_recipient, safe=False)
    return json_data


def paid_aug_daily_recipient(request):
    paid_aug_daily_recipient = pd.pivot_table(data[data['monthname'] == 'August'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'day'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'aug_service_revenue', 'provider_name': 'aug_service_count'})
    paid_aug_daily_recipient = paid_aug_daily_recipient.to_dict('r')
    json_data = JsonResponse(paid_aug_daily_recipient, safe=False)
    return json_data


def paid_aug_hourly_recipient(request):
    paid_aug_hourly_recipient = pd.pivot_table(data[data['monthname'] == 'August'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'hour'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'aug_service_revenue', 'provider_name': 'aug_service_count'})
    paid_aug_hourly_recipient = paid_aug_hourly_recipient.to_dict('r')
    json_data = JsonResponse(paid_aug_hourly_recipient, safe=False)
    return json_data


def paid_sep_weekday_recipient(request):
    paid_sep_weekday_recipient = pd.pivot_table(data[data['monthname'] == 'September'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'weekday'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'sep_service_revenue', 'provider_name': 'sep_service_count'})
    paid_sep_weekday_recipient = paid_sep_weekday_recipient.to_dict('r')
    json_data = JsonResponse(paid_sep_weekday_recipient, safe=False)
    return json_data


def paid_sep_daily_recipient(request):
    paid_sep_daily_recipient = pd.pivot_table(data[data['monthname'] == 'September'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'day'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'sep_service_revenue', 'provider_name': 'sep_service_count'})
    paid_sep_daily_recipient = paid_sep_daily_recipient.to_dict('r')
    json_data = JsonResponse(paid_sep_daily_recipient, safe=False)
    return json_data


def paid_sep_hourly_recipient(request):
    paid_sep_hourly_recipient = pd.pivot_table(data[data['monthname'] == 'September'], values=['amount', 'provider_name'],
                                        index=['recipient_bank_name', 'hour'],
                                        aggfunc={'amount': 'sum', 'provider_name': 'count'}).reset_index().rename(
        columns={'amount': 'sep_service_revenue', 'provider_name': 'sep_service_count'})
    paid_sep_hourly_recipient = paid_sep_hourly_recipient.to_dict('r')
    json_data = JsonResponse(paid_sep_hourly_recipient, safe=False)
    return json_data


def all_clients(request):
    all_clients = pd.pivot_table(data=df, index=['client_name'], values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    all_clients = all_clients.to_dict('r')
    json_data = JsonResponse(all_clients, safe=False)
    return json_data


def all_monthly_clients(request):
    all_monthly_clients = pd.pivot_table(data=df, index=['client_name', 'monthname'], values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    all_monthly_clients = all_monthly_clients.to_dict('r')
    json_data = JsonResponse(all_monthly_clients, safe=False)
    return json_data


def all_weekday_clients(request):
    all_weekday_clients = pd.pivot_table(data=df, index=['client_name', 'weekday'], values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    all_weekday_clients = all_weekday_clients.to_dict('r')
    json_data = JsonResponse(all_weekday_clients, safe=False)
    return json_data


def all_daily_clients(request):
    all_day_clients = pd.pivot_table(data=df, index=['client_name', 'day'], values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    all_day_clients = all_day_clients.to_dict('r')
    json_data = JsonResponse(all_day_clients, safe=False)
    return json_data


def all_hourly_clients(request):
    all_hour_clients = pd.pivot_table(data=df, index=['client_name', 'hour'], values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    all_hour_clients = all_hour_clients.to_dict('r')
    json_data = JsonResponse(all_hour_clients, safe=False)
    return json_data


def all_june_weekday_clients(request):
    all_june_weekday_clients = pd.pivot_table(data=df[df['monthname'] == 'June'], index=['client_name', 'weekday'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    all_june_weekday_clients = all_june_weekday_clients.to_dict('r')
    json_data = JsonResponse(all_june_weekday_clients, safe=False)
    return json_data


def all_june_daily_clients(request):
    all_june_daily_clients = pd.pivot_table(data=df[df['monthname'] == 'June'], index=['client_name', 'day'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    all_june_daily_clients = all_june_daily_clients.to_dict('r')
    json_data = JsonResponse(all_june_daily_clients, safe=False)
    return json_data


def all_june_hourly_clients(request):
    all_june_hourly_clients = pd.pivot_table(data=df[df['monthname'] == 'June'], index=['client_name', 'hour'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    all_june_hourly_clients = all_june_hourly_clients.to_dict('r')
    json_data = JsonResponse(all_june_hourly_clients, safe=False)
    return json_data


def all_july_weekday_clients(request):
    all_july_weekday_clients = pd.pivot_table(data=df[df['monthname'] == 'July'], index=['client_name', 'weekday'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    all_july_weekday_clients = all_july_weekday_clients.to_dict('r')
    json_data = JsonResponse(all_july_weekday_clients, safe=False)
    return json_data


def all_july_daily_clients(request):
    all_july_daily_clients = pd.pivot_table(data=df[df['monthname'] == 'July'], index=['client_name', 'day'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    all_july_daily_clients = all_july_daily_clients.to_dict('r')
    json_data = JsonResponse(all_july_daily_clients, safe=False)
    return json_data


def all_july_hourly_clients(request):
    all_july_hourly_clients = pd.pivot_table(data=df[df['monthname'] == 'July'], index=['client_name', 'hour'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    all_july_hourly_clients = all_july_hourly_clients.to_dict('r')
    json_data = JsonResponse(all_july_hourly_clients, safe=False)
    return json_data


def all_aug_weekday_clients(request):
    all_aug_weekday_clients = pd.pivot_table(data=df[df['monthname'] == 'August'], index=['client_name', 'weekday'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    all_aug_weekday_clients = all_aug_weekday_clients.to_dict('r')
    json_data = JsonResponse(all_aug_weekday_clients, safe=False)
    return json_data


def all_aug_daily_clients(request):
    all_aug_daily_clients = pd.pivot_table(data=df[df['monthname'] == 'August'], index=['client_name', 'day'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    all_aug_daily_clients = all_aug_daily_clients.to_dict('r')
    json_data = JsonResponse(all_aug_daily_clients, safe=False)
    return json_data


def all_aug_hourly_clients(request):
    all_aug_hourly_clients = pd.pivot_table(data=df[df['monthname'] == 'August'], index=['client_name', 'hour'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    all_aug_hourly_clients = all_aug_hourly_clients.to_dict('r')
    json_data = JsonResponse(all_aug_hourly_clients, safe=False)
    return json_data


def all_sep_weekday_clients(request):
    all_sep_weekday_clients = pd.pivot_table(data=df[df['monthname'] == 'September'], index=['client_name', 'weekday'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    all_sep_weekday_clients = all_sep_weekday_clients.to_dict('r')
    json_data = JsonResponse(all_sep_weekday_clients, safe=False)
    return json_data


def all_sep_daily_clients(request):
    all_sep_daily_clients = pd.pivot_table(data=df[df['monthname'] == 'September'], index=['client_name', 'day'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    all_sep_daily_clients = all_sep_daily_clients.to_dict('r')
    json_data = JsonResponse(all_sep_daily_clients, safe=False)
    return json_data


def all_sep_hourly_clients(request):
    all_sep_hourly_clients = pd.pivot_table(data=df[df['monthname'] == 'September'], index=['client_name', 'hour'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    all_sep_hourly_clients = all_sep_hourly_clients.to_dict('r')
    json_data = JsonResponse(all_sep_hourly_clients, safe=False)
    return json_data


def paid_clients(request):
    paid_clients = pd.pivot_table(data=data, index=['client_name'], values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    paid_clients = paid_clients.to_dict('r')
    json_data = JsonResponse(paid_clients, safe=False)
    return json_data



def paid_monthly_clients(request):
    paid_monthly_clients = pd.pivot_table(data=data, index=['client_name', 'monthname'], values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    paid_monthly_clients = paid_monthly_clients.to_dict('r')
    json_data = JsonResponse(paid_monthly_clients, safe=False)
    return json_data


def paid_weekday_clients(request):
    paid_weekday_clients = pd.pivot_table(data, index=['client_name', 'weekday'], values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    paid_weekday_clients = paid_weekday_clients.to_dict('r')
    json_data = JsonResponse(paid_weekday_clients, safe=False)
    return json_data


def paid_daily_clients(request):
    paid_daily_clients = pd.pivot_table(data, index=['client_name', 'day'], values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    paid_daily_clients = paid_daily_clients.to_dict('r')
    json_data = JsonResponse(paid_daily_clients, safe=False)
    return json_data


def paid_hourly_clients(request):
    paid_hourly_clients = pd.pivot_table(data, index=['client_name', 'hour'], values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    paid_hourly_clients = paid_hourly_clients.to_dict('r')
    json_data = JsonResponse(paid_hourly_clients, safe=False)
    return json_data


def paid_june_weekday_clients(request):
    paid_june_weekday_clients = pd.pivot_table(data=data[data['monthname'] == 'June'], index=['client_name', 'weekday'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    paid_june_weekday_clients = paid_june_weekday_clients.to_dict('r')
    json_data = JsonResponse(paid_june_weekday_clients, safe=False)
    return json_data


def paid_june_daily_clients(request):
    paid_june_daily_clients = pd.pivot_table(data=data[data['monthname'] == 'June'], index=['client_name', 'day'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    paid_june_daily_clients = paid_june_daily_clients.to_dict('r')
    json_data = JsonResponse(paid_june_daily_clients, safe=False)
    return json_data


def paid_june_hourly_clients(request):
    paid_june_hourly_clients = pd.pivot_table(data=data[data['monthname'] == 'June'], index=['client_name', 'hour'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    paid_june_hourly_clients = paid_june_hourly_clients.to_dict('r')
    json_data = JsonResponse(paid_june_hourly_clients, safe=False)
    return json_data


def paid_july_weekday_clients(request):
    paid_july_weekday_clients = pd.pivot_table(data=data[data['monthname'] == 'July'], index=['client_name', 'weekday'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    paid_july_weekday_clients = paid_july_weekday_clients.to_dict('r')
    json_data = JsonResponse(paid_july_weekday_clients, safe=False)
    return json_data


def paid_july_daily_clients(request):
    paid_july_daily_clients = pd.pivot_table(data=data[data['monthname'] == 'July'], index=['client_name', 'day'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    paid_july_daily_clients = paid_july_daily_clients.to_dict('r')
    json_data = JsonResponse(paid_july_daily_clients, safe=False)
    return json_data


def paid_july_hourly_clients(request):
    paid_july_hourly_clients = pd.pivot_table(data=data[data['monthname'] == 'July'], index=['client_name', 'hour'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    paid_july_hourly_clients = paid_july_hourly_clients.to_dict('r')
    json_data = JsonResponse(paid_july_hourly_clients, safe=False)
    return json_data


def paid_aug_weekday_clients(request):
    paid_aug_weekday_clients = pd.pivot_table(data=data[data['monthname'] == 'August'], index=['client_name', 'weekday'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    paid_aug_weekday_clients = paid_aug_weekday_clients.to_dict('r')
    json_data = JsonResponse(paid_aug_weekday_clients, safe=False)
    return json_data


def paid_aug_daily_clients(request):
    paid_aug_daily_clients = pd.pivot_table(data=data[data['monthname'] == 'August'], index=['client_name', 'day'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    paid_aug_daily_clients = paid_aug_daily_clients.to_dict('r')
    json_data = JsonResponse(paid_aug_daily_clients, safe=False)
    return json_data


def paid_aug_hourly_clients(request):
    paid_aug_hourly_clients = pd.pivot_table(data=data[data['monthname'] == 'August'], index=['client_name', 'hour'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    paid_aug_hourly_clients = paid_aug_hourly_clients.to_dict('r')
    json_data = JsonResponse(paid_aug_hourly_clients, safe=False)
    return json_data


def paid_sep_weekday_clients(request):
    paid_sep_weekday_clients = pd.pivot_table(data=data[data['monthname'] == 'September'], index=['client_name', 'weekday'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    paid_sep_weekday_clients = paid_sep_weekday_clients.to_dict('r')
    json_data = JsonResponse(paid_sep_weekday_clients, safe=False)
    return json_data


def paid_sep_daily_clients(request):
    paid_sep_daily_clients = pd.pivot_table(data=data[data['monthname'] == 'September'], index=['client_name', 'day'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    paid_sep_daily_clients = paid_sep_daily_clients.to_dict('r')
    json_data = JsonResponse(paid_sep_daily_clients, safe=False)
    return json_data


def paid_sep_hourly_clients(request):
    paid_sep_hourly_clients = pd.pivot_table(data=data[data['monthname'] == 'September'], index=['client_name', 'hour'],
                   values=['amount', 'recipient_bank_name'],
                   aggfunc={'amount': 'sum', 'recipient_bank_name': 'count'}).reset_index().rename(
        columns={'amount': 'revenue', 'recipient_bank_name': 'count'})
    paid_sep_hourly_clients = paid_sep_hourly_clients.to_dict('r')
    json_data = JsonResponse(paid_sep_hourly_clients, safe=False)
    return json_data

