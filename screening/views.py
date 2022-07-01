from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from fpdf import FPDF


# Create your views here.
@login_required
def home1(request):
    if request.method == 'POST':
        # request.session['investment_name'] = request.POST.get('investment_name')
        # request.session['prepare_by'] = request.POST.get('prepare_by')
        # request.session['date'] = request.POST.get('date')
        # request.session['firm_address'] = request.POST.get('firm_address')
        # request.session['brief_project'] = request.POST.get('brief_project')

        investment_name = request.POST.get('investment_name')
        prepare_by = request.POST.get('prepare_by')
        date = request.POST.get('date')
        firm_address = request.POST.get('firm_address')
        brief_project = request.POST.get('brief_project')

        input_data = {
            'investment_name': investment_name,
            'prepare_by': prepare_by,
            'date': date,
            'firm_address': firm_address,
            'brief_project': brief_project,
        }

        # db_data = Master(username=request.session.get('username'), investment_name=investment_name, prepare_by=prepare_by, date=date,
        #                  firm_address=firm_address, brief_project=brief_project)
        # db_data.save()
        # session_dict = get_session_data()
        # count = 1
        # context = {}
        #
        # print(db_data)

        context = {
            'input_data': input_data,
        }
        return render(request, 'self_assessment_1.html', context)
    # return HttpResponse('<h1> Screening home </h1>')
    return render(request, 'index_user.html')

#
# def get_session_data():
#     session_data = Master.objects.all()
#     dict_count = 1
#     session_dict = {}
#     for items in session_data:
#         session_dict['session_dict_{}'.format(dict_count)] = items.__dict__
#         session_dict.get('session_dict_{}'.format(dict_count))['_state'] = \
#             str(session_dict.get('session_dict_{}'.format(dict_count))['_state'])
#         session_dict.get('session_dict_{}'.format(dict_count))['date'] = \
#             session_dict.get('session_dict_{}'.format(dict_count))['date'].strftime("%Y-%m-%d")
#         dict_count+=1
#     return session_dict


@login_required
def home2(request):
    if request.method == 'POST':
        investment_name = request.POST.get('investment_name')
        # request.session['investment_name'] = investment_name
        prepare_by = request.POST.get('prepare_by')
        # request.session['prepare_by'] = request.POST.get('prepare_by')
        date = request.POST.get('date')
        # request.session['date'] = request.POST.get('date')
        firm_address = request.POST.get('firm_address')
        # request.session['firm_address'] = request.POST.get('firm_address')
        brief_project = request.POST.get('brief_project')
        # request.session['brief_project'] = request.POST.get('brief_project')
        client_name = request.POST.get('client_name')
        # request.session['client_name'] = request.POST.get('client_name')
        client_address = request.POST.get('client_address')
        # request.session['client_address'] = request.POST.get('client_address')
        client_contact_no = request.POST.get('client_contact_no')
        # request.session['client_contact_no'] = request.POST.get('client_contact_no')
        client_email = request.POST.get('client_email')
        # request.session['client_email'] = request.POST.get('client_email')
        company_name = request.POST.get('company_name')
        # request.session['company_name'] = request.POST.get('company_name')
        company_address = request.POST.get('company_address')
        # request.session['company_address'] = request.POST.get('company_address')
        industry_sector = request.POST.get('industry_sector')
        # request.session['industry_sector'] = request.POST.get('industry_sector')

        request.session['company_name'] = company_name

        input_data = {
            'investment_name': investment_name,
            'prepare_by': prepare_by,
            'date': date,
            'firm_address': firm_address,
            'brief_project': brief_project,
            'client_name': client_name,
            'client_address': client_address,
            'client_contact_no': client_contact_no,
            'client_email': client_email,
            'company_name': company_name,
            'company_address': company_address,
            'industry_sector': industry_sector,
        }

        # db_data1 = Master(investment_name=investment_name, prepare_by=prepare_by,
        #                   date=date, firm_address=firm_address, brief_project=brief_project,
        #                   client_name=client_name, client_address=client_address,
        #                   client_contact_no=client_contact_no, client_email=client_email, company_name=company_name,
        #                   company_address=company_address, industry_sector=industry_sector)
        #
        # db_data1.save()
        # print(db_data1)
        context = {
            'input_data': input_data,
        }
        return render(request, 'selection.html', context)
    # return HttpResponse('<h1> Screening home </h1>')
    return render(request, 'index_client.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['username'] = username
        user = authenticate(request, username=username, password=password)
        # client = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            authorized = True
            return render(request, 'index_user.html')
        else:
            messages.success(request, 'Invalid Username or Password')
            return render(request, 'login_user.html')
    if request.user.is_authenticated:
        return render(request, 'index_user.html')
    else:
        return render(request, 'login_user.html')


def login_client(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        client = authenticate(request, username=username, password=password)
        if client is not None:
            login(request, client)
            authorized = True
            return render(request, 'index_client.html')
        else:
            messages.success(request, 'Invalid Username or Password')
            return render(request, 'login_client.html')
    if request.user.is_authenticated:
        return render(request, 'index_client.html')
    else:
        return render(request, 'login_client.html')


def logout_user(request):
    logout(request)
    return render(request, 'logout.html')


# @login_required
# def self_assessment_1(request):
#     return render(request, 'self_assessment_1.html')


@login_required
def selection(request):
    return render(request, 'selection.html')


@login_required
def environment_selection(request):
    return render(request, 'environment_selection.html')

@login_required
def env_social_selection(request):
    return render(request, 'env_social_selection.html')

@login_required
def env_gov_selection(request):
    return render(request, 'env_gov_selection.html')


# if client select only social option:
@login_required
def social_1_scoring(request):
    if request.method == 'POST':
        f1_1 = request.POST.get("f1_1")
        comment1_1 = request.POST.get("comment1_1")
        exception1_1 = request.POST.get("exception1_1")
        f1_2 = request.POST.get("f1_2")
        comment1_2 = request.POST.get("comment1_2")
        exception1_2 = request.POST.get("exception1_2")
        f1_3 = request.POST.get("f1_3")
        comment1_3 = request.POST.get("comment1_3")
        exception1_3 = request.POST.get("exception1_3")
        f1_4 = request.POST.get("f1_4")
        comment1_4 = request.POST.get("comment1_4")
        exception1_4 = request.POST.get("exception1_4")
        f1_5 = request.POST.get("f1_5")
        comment1_5 = request.POST.get("comment1_5")
        exception1_5 = request.POST.get("exception1_5")
        f2_1 = request.POST.get("f2_1")
        comment2_1 = request.POST.get("comment2_1")
        exception2_1 = request.POST.get("exception2_1")
        f2_2 = request.POST.get("f2_2")
        comment2_2 = request.POST.get("comment2_2")
        exception2_2 = request.POST.get("exception2_2")
        f2_3 = request.POST.get("f2_3")
        comment2_3 = request.POST.get("comment2_3")
        exception2_3 = request.POST.get("exception2_3")
        f2_4 = request.POST.get("f2_4")
        comment2_4 = request.POST.get("comment2_4")
        exception2_4 = request.POST.get("exception2_4")
        f2_5 = request.POST.get("f2_5")
        comment2_5 = request.POST.get("comment2_5")
        exception2_5 = request.POST.get("exception2_5")
        f2_6 = request.POST.get("f2_6")
        comment2_6 = request.POST.get("comment2_6")
        exception2_6 = request.POST.get("exception2_6")
        f3_1 = request.POST.get("f3_1")
        comment3_1 = request.POST.get("comment3_1")
        exception3_1 = request.POST.get("exception3_1")
        f3_2 = request.POST.get("f3_2")
        comment3_2 = request.POST.get("comment3_2")
        exception3_2 = request.POST.get("exception3_2")
        f3_3 = request.POST.get("f3_3")
        comment3_3 = request.POST.get("comment3_3")
        exception3_3 = request.POST.get("exception3_3")
        f3_4 = request.POST.get("f3_4")
        comment3_4 = request.POST.get("comment3_4")
        exception3_4 = request.POST.get("exception3_4")
        f3_5 = request.POST.get("f3_5")
        comment3_5 = request.POST.get("comment3_5")
        exception3_5 = request.POST.get("exception3_5")
        f4_1 = request.POST.get("f4_1")
        comment4_1 = request.POST.get("comment4_1")
        exception4_1 = request.POST.get("exception4_1")
        f4_2 = request.POST.get("f4_2")
        comment4_2 = request.POST.get("comment4_2")
        exception4_2 = request.POST.get("exception4_2")
        f4_3 = request.POST.get("f4_3")
        comment4_3 = request.POST.get("comment4_3")
        exception4_3 = request.POST.get("exception4_3")
        f4_4 = request.POST.get("f4_4")
        comment4_4 = request.POST.get("comment4_4")
        exception4_4 = request.POST.get("exception4_4")
        f5_1 = request.POST.get("f5_1")
        comment5_1 = request.POST.get("comment5_1")
        exception5_1 = request.POST.get("exception5_1")
        f5_2 = request.POST.get("f5_2")
        comment5_2 = request.POST.get("comment5_2")
        exception5_2 = request.POST.get("exception5_2")
        f5_3 = request.POST.get("f5_3")
        comment5_3 = request.POST.get("comment5_3")
        exception5_3 = request.POST.get("exception5_3")
        f5_4 = request.POST.get("f5_4")
        comment5_4 = request.POST.get("comment5_4")
        exception5_4 = request.POST.get("exception5_4")
        f5_5 = request.POST.get("f5_5")
        comment5_5 = request.POST.get("comment5_5")
        exception5_5 = request.POST.get("exception5_5")
        f5_6 = request.POST.get("f5_6")
        comment5_6 = request.POST.get("comment5_6")
        exception5_6 = request.POST.get("exception5_6")
        f6_1 = request.POST.get("f6_1")
        comment6_1 = request.POST.get("comment6_1")
        exception6_1 = request.POST.get("exception6_1")
        f6_2 = request.POST.get("f6_2")
        comment6_2 = request.POST.get("comment6_2")
        exception6_2 = request.POST.get("exception6_2")
        f6_3 = request.POST.get("f6_3")
        comment6_3 = request.POST.get("comment6_3")
        exception6_3 = request.POST.get("exception6_3")
        f6_4 = request.POST.get("f6_4")
        comment6_4 = request.POST.get("comment6_4")
        exception6_4 = request.POST.get("exception6_4")
        f6_5 = request.POST.get("f6_5")
        comment6_5 = request.POST.get("comment6_5")
        exception6_5 = request.POST.get("exception6_5")
        f6_6 = request.POST.get("f6_6")
        comment6_6 = request.POST.get("comment6_6")
        exception6_6 = request.POST.get("exception6_6")
        f6_7 = request.POST.get("f6_7")
        comment6_7 = request.POST.get("comment6_7")
        exception6_7 = request.POST.get("exception6_7")
        f6_8 = request.POST.get("f6_8")
        comment6_8 = request.POST.get("comment6_8")
        exception6_8 = request.POST.get("exception6_8")
        f6_9 = request.POST.get("f6_9")
        comment6_9 = request.POST.get("comment6_9")
        exception6_9 = request.POST.get("exception6_9")
        f7_1 = request.POST.get("f7_1")
        comment7_1 = request.POST.get("comment7_1")
        exception7_1 = request.POST.get("exception7_1")
        f7_2 = request.POST.get("f7_2")
        comment7_2 = request.POST.get("comment7_2")
        exception7_2 = request.POST.get("exception7_2")
        f7_3 = request.POST.get("f7_3")
        comment7_3 = request.POST.get("comment7_3")
        exception7_3 = request.POST.get("exception7_3")
        f7_4 = request.POST.get("f7_4")
        comment7_4 = request.POST.get("comment7_4")
        exception7_4 = request.POST.get("exception7_4")
        f7_5 = request.POST.get("f7_5")
        comment7_5 = request.POST.get("comment7_5")
        exception7_5 = request.POST.get("exception7_5")
        f8_1 = request.POST.get("f8_1")
        comment8_1 = request.POST.get("comment8_1")
        exception8_1 = request.POST.get("exception8_1")
        f8_2 = request.POST.get("f8_2")
        comment8_2 = request.POST.get("comment8_1")
        exception8_2 = request.POST.get("exception8_2")
        f8_3 = request.POST.get("f8_3")
        comment8_3 = request.POST.get("comment8_3")
        exception8_3 = request.POST.get("exception8_3")
        f8_4 = request.POST.get("f8_4")
        comment8_4 = request.POST.get("comment8_4")
        exception8_4 = request.POST.get("exception8_4")
        f8_5 = request.POST.get("f8_5")
        comment8_5 = request.POST.get("comment8_5")
        exception8_5 = request.POST.get("exception8_5")
        f8_6 = request.POST.get("f8_6")
        comment8_6 = request.POST.get("comment8_6")
        exception8_6 = request.POST.get("exception8_6")
        f9_1 = request.POST.get("f9_1")
        comment9_1= request.POST.get("comment9_1")
        exception9_1 = request.POST.get("exception9_1")
        f9_2 = request.POST.get("f9_2")
        comment9_2 = request.POST.get("comment9_2")
        exception9_2 = request.POST.get("exception9_2")
        f9_3 = request.POST.get("f9_3")
        comment9_3 = request.POST.get("comment9_3")
        exception9_3 = request.POST.get("exception9_3")
        f9_4 = request.POST.get("f9_4")
        comment9_4 = request.POST.get("comment9_4")
        exception9_4 = request.POST.get("exception9_4")
        f9_5 = request.POST.get("f9_5")
        comment9_5 = request.POST.get("comment9_5")
        exception9_5 = request.POST.get("exception9_5")
        f9_6 = request.POST.get("f9_6")
        comment9_6= request.POST.get("comment9_6")
        exception9_6 = request.POST.get("exception9_6")
        f9_7 = request.POST.get("f9_7")
        comment9_7 = request.POST.get("comment9_7")
        exception9_7 = request.POST.get("exception9_7")
        f10_1 = request.POST.get("f10_1")
        comment10_1 = request.POST.get("comment10_1")
        exception10_1 = request.POST.get("exception10_1")
        f10_2 = request.POST.get("f10_2")
        comment10_2 = request.POST.get("comment10_2")
        exception10_2 = request.POST.get("exception10_2")
        f10_3 = request.POST.get("f10_3")
        comment10_3 = request.POST.get("comment10_3")
        exception10_3 = request.POST.get("exception10_3")

        input_data = {
            'f1_1': f1_1,
            'comment1_1': comment1_1,
            'exception1_1': exception1_1,
            'f1_2': f1_2,
            'comment1_2': comment1_2,
            'exception1_2': exception1_2,
            'f1_3': f1_3,
            'comment1_3': comment1_3,
            'exception1_3': exception1_3,
            'f1_4': f1_4,
            'comment1_4': comment1_4,
            'exception1_4': exception1_4,
            'f1_5': f1_5,
            'comment1_5': comment1_5,
            'exception1_5': exception1_5,
            'f2_1': f2_1,
            'comment2_1': comment2_1,
            'exception2_1': exception2_1,
            'f2_2': f2_2,
            'comment2_2': comment2_2,
            'exception2_2': exception2_2,
            'f2_3': f2_3,
            'comment2_3': comment2_3,
            'exception2_3': exception2_3,
            'f2_4': f2_4,
            'comment2_4': comment2_4,
            'exception2_4': exception2_4,
            'f2_5': f2_5,
            'comment2_5': comment2_5,
            'exception2_5': exception2_5,
            'f2_6': f2_6,
            'comment2_6': comment2_6,
            'exception2_6': exception2_6,
            'f3_1': f3_1,
            'comment3_1': comment3_1,
            'exception3_1': exception3_1,
            'f3_2': f3_2,
            'comment3_2': comment3_2,
            'exception3_2': exception3_2,
            'f3_3': f3_3,
            'comment3_3': comment3_3,
            'exception3_3': exception3_3,
            'f3_4': f3_4,
            'comment3_4': comment3_4,
            'exception3_4': exception3_4,
            'f3_5': f3_5,
            'comment3_5': comment3_5,
            'exception3_5': exception3_5,
            'f4_1': f4_1,
            'comment4_1': comment4_1,
            'exception4_1': exception4_1,
            'f4_2': f4_2,
            'comment4_2': comment4_2,
            'exception4_2': exception4_2,
            'f4_3': f4_3,
            'comment4_3': comment4_3,
            'exception4_3': exception4_3,
            'f4_4': f4_4,
            'comment4_4': comment4_4,
            'exception4_4': exception4_4,
            'f5_1': f5_1,
            'comment5_1': comment5_1,
            'exception5_1': exception5_1,
            'f5_2': f5_2,
            'comment5_2': comment5_2,
            'exception5_2': exception5_2,
            'f5_3': f5_3,
            'comment5_3': comment5_3,
            'exception5_3': exception5_3,
            'f5_4': f5_4,
            'comment5_4': comment5_4,
            'exception5_4': exception5_4,
            'f5_5': f5_5,
            'comment5_5': comment5_5,
            'exception5_5': exception5_5,
            'f5_6': f5_6,
            'comment5_6': comment5_6,
            'exception5_6': exception5_6,
            'f6_1': f6_1,
            'comment6_1': comment6_1,
            'exception6_1': exception6_1,
            'f6_2': f6_2,
            'comment6_2': comment6_2,
            'exception6_2': exception6_2,
            'f6_3': f6_3,
            'comment6_3': comment6_3,
            'exception6_3': exception6_3,
            'f6_4': f6_4,
            'comment6_4': comment6_4,
            'exception6_4': exception6_4,
            'f6_5': f6_5,
            'comment6_5': comment6_5,
            'exception6_5': exception6_5,
            'f6_6': f6_6,
            'comment6_6': comment6_6,
            'exception6_6': exception6_6,
            'f6_7': f6_7,
            'comment6_7': comment6_7,
            'exception6_7': exception6_7,
            'f6_8': f6_8,
            'comment6_8': comment6_8,
            'exception6_8': exception6_8,
            'f6_9': f6_9,
            'comment6_9': comment6_9,
            'exception6_9': exception6_9,
            'f7_1': f7_1,
            'comment7_1': comment7_1,
            'exception7_1': exception7_1,
            'f7_2': f7_2,
            'comment7_2': comment7_2,
            'exception7_2': exception7_2,
            'f7_3': f7_3,
            'comment7_3': comment7_3,
            'exception7_3': exception7_3,
            'f7_4': f7_4,
            'comment7_4': comment7_4,
            'exception7_4': exception7_4,
            'f7_5': f7_5,
            'comment7_5': comment7_5,
            'exception7_5': exception7_5,
            'f8_1': f8_1,
            'comment8_1': comment8_1,
            'exception8_1': exception8_1,
            'f8_2': f8_2,
            'comment8_2': comment8_2,
            'exception8_2': exception8_2,
            'f8_3': f8_3,
            'comment8_3': comment8_3,
            'exception8_3': exception8_3,
            'f8_4': f8_4,
            'comment8_4': comment8_4,
            'exception8_4': exception8_4,
            'f8_5': f8_5,
            'comment8_5': comment8_5,
            'exception8_5': exception8_5,
            'f8_6': f8_6,
            'comment8_6': comment8_6,
            'exception8_6': exception8_6,
            'f9_1':f9_1,
            'comment9_1': comment9_1,
            'exception9_1': exception9_1,
            'f9_2': f9_2,
            'comment9_2': comment9_2,
            'exception9_2': exception9_2,
            'f9_3': f9_3,
            'comment9_3': comment9_3,
            'exception9_3': exception9_3,
            'f9_4': f9_4,
            'comment9_4': comment9_4,
            'exception9_4': exception9_4,
            'f9_5': f9_5,
            'comment9_5': comment9_5,
            'exception9_5': exception9_5,
            'f9_6': f9_6,
            'comment9_6': comment9_6,
            'exception9_6': exception9_6,
            'f9_7': f9_7,
            'comment9_7': comment9_7,
            'exception9_7': exception9_7,
            'f10_1': f10_1,
            'comment10_1': comment10_1,
            'exception10_1': exception10_1,
            'f10_2': f10_2,
            'comment10_2': comment10_2,
            'exception10_2': exception10_2,
            'f10_3': f10_3,
            'comment10_3': comment10_3,
            'exception10_3': exception10_3,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'social_score.html', context)
    return render(request, 'social_1_scoring.html')




@login_required
def social_score(request):
    if request.method == 'POST':
        inequality = request.POST.get("inequality")
        s_comment1 = request.POST.get("s_comment1")
        exception1 = request.POST.get("exception1")
        social_cohesion = request.POST.get("social_cohesion")
        s_comment2 = request.POST.get("s_comment2")
        exception2 = request.POST.get("exception2")
        social_integration = request.POST.get("social_integration")
        s_comment3 = request.POST.get("s_comment3")
        exception3 = request.POST.get("exception3")
        labour_relations = request.POST.get("labour_relations")
        s_comment4 = request.POST.get("s_comment4")
        exception4 = request.POST.get("exception4")
        investment_human_capital = request.POST.get("investment_human_capital")
        s_comment5 = request.POST.get("s_comment5")
        exception5 = request.POST.get("exception5")
        economically_socially_communities = request.POST.get("economically_socially_communities")
        s_comment6 = request.POST.get("s_comment6")
        exception6 = request.POST.get("exception6")
        supply_chain_management_s = request.POST.get("supply_chain_management_s")
        s_comment7 = request.POST.get("s_comment7")
        exception7 = request.POST.get("exception7")

        input_data = {
            'inequality': inequality,
            's_comment1': s_comment1,
            'exception1': exception1,
            'social_cohesion': social_cohesion,
            's_comment2': s_comment2,
            'exception2': exception2,
            'social_integration': social_integration,
            's_comment3': s_comment3,
            'exception3': exception3,
            'labour_relations': labour_relations,
            's_comment4': s_comment4,
            'exception4': exception4,
            'investment_human_capital': investment_human_capital,
            's_comment5': s_comment5,
            'exception5': exception5,
            'economically_socially_communities': economically_socially_communities,
            's_comment6': s_comment6,
            'exception6': exception6,
            'supply_chain_management_s': supply_chain_management_s,
            's_comment7': s_comment7,
            'exception7': exception7,
        }

        table = s_socialCalculations(input_data, request)
        s_total_score = table.s_all_score()
        s_na_count = table.s_all_na()
        s_avg_score = round(s_total_score/(7 - s_na_count))

        context = {
            'input_data': input_data,
            'company_name': request.session.get('company_name'),
            'e2_1': request.session.get('e2_1'),
            'e2_2': request.session.get('e2_2'),
            'e2_3': request.session.get('e2_3'),
            'e2_4': request.session.get('e2_4'),
            'e2_5': request.session.get('e2_5'),
            'e2_6': request.session.get('e2_6'),
            'e2_7': request.session.get('e2_7'),
            'e2_8': request.session.get('e2_8'),
            'e2_9': request.session.get('e2_9'),
            'e2_10': request.session.get('e2_10'),
            'comment1': request.session.get('comment1'),
            'comment2': request.session.get('comment2'),
            'comment3': request.session.get('comment3'),
            'comment4': request.session.get('comment4'),
            'comment5': request.session.get('comment5'),
            'comment6': request.session.get('comment6'),
            'comment7': request.session.get('comment7'),
            'comment8': request.session.get('comment8'),
            'comment9': request.session.get('comment9'),
            'comment10': request.session.get('comment10'),
            'total_score': request.session.get('total_score'),
            'avg_score': request.session.get('avg_score'),
            's1_1': inequality,
            's1_2': social_cohesion,
            's1_3': social_integration,
            's1_4': labour_relations,
            's1_5': investment_human_capital,
            's1_6': economically_socially_communities,
            's1_7': supply_chain_management_s,
            's_comment1': s_comment1,
            's_comment2': s_comment2,
            's_comment3': s_comment3,
            's_comment4': s_comment4,
            's_comment5': s_comment5,
            's_comment6': s_comment6,
            's_comment7': s_comment7,
            's_total_score': s_total_score,
            's_avg_score': s_avg_score,

        }
        return render(request, 'final_scoring_client.html', context)
    return render(request, 'social_score.html')


class s_socialCalculations:
    def __init__(self, input_data, request):
        self.input_data = input_data
        self.score = 0
        self.value = 0
        self.na_count_s = 0
        self.request = request

    # Social Final Scoring calculation
    def s1_1(self):
        self.value = 0
        if self.input_data.get('inequality') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('inequality') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('inequality') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('inequality') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('inequality') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('inequality') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_s += 1
        return [self.score, self.value, self.na_count_s]

    def s1_2(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('social_cohesion') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('social_cohesion') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('social_cohesion') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('social_cohesion') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('social_cohesion') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('social_cohesion') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_s += 1
        return [self.score, self.value, self.na_count_s]

    def s1_3(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('social_integration') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('social_integration') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('social_integration') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('social_integration') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('social_integration') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('social_integration') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_s += 1
        return [self.score, self.value, self.na_count_s]

    def s1_4(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('labour_relations') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('labour_relations') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('labour_relations') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('labour_relations') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('labour_relations') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('labour_relations') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_s += 1
        return [self.score, self.value, self.na_count_s]

    def s1_5(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('investment_human_capital') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('investment_human_capital') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('investment_human_capital') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('investment_human_capital') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('investment_human_capital') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('investment_human_capital') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_s += 1
        return [self.score, self.value, self.na_count_s]

    def s1_6(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('economically_socially_communities') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('economically_socially_communities') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('economically_socially_communities') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('economically_socially_communities') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('economically_socially_communities') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('economically_socially_communities') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_s += 1
        return [self.score, self.value, self.na_count_s]

    def s1_7(self):
        self.score = 0
        if self.input_data.get('supply_chain_management_s') == '0':
            self.score = 0
        elif self.input_data.get('supply_chain_management_s') == '1':
            self.score = 1
        elif self.input_data.get('supply_chain_management_s') == '2':
            self.score = 2
        elif self.input_data.get('supply_chain_management_s') == '3':
            self.score = 3
        elif self.input_data.get('supply_chain_management_s') == '4':
            self.score = 4
        elif self.input_data.get('supply_chain_management_s') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_s += 1
        return [self.score, self.value, self.na_count_s]

    def s_all_na(self):
        s1_7 = self.s1_7()[2]
        return s1_7

    def s_all_score(self):
        s1_1_score = self.s1_1()[0]
        s1_2_score = self.s1_2()[0]
        s1_3_score = self.s1_3()[0]
        s1_4_score = self.s1_4()[0]
        s1_5_score = self.s1_5()[0]
        s1_6_score = self.s1_6()[0]
        s1_7_score = self.s1_7()[0]

        s_total_score = s1_1_score + s1_2_score + s1_3_score + s1_4_score + s1_5_score + s1_6_score + s1_7_score
        s_na_count = self.s_all_na()
        # s_avg_score = round(s_total_score/(7 - na_count_s))
        return s_total_score



# if client select only Governance and Governance scoring :
@login_required
def only_governance(request):
    if request.method == 'POST':
        f1_1 = request.POST.get("f1_1")
        comment1_1 = request.POST.get("comment1_1")
        exception1_1 = request.POST.get("exception1_1")
        f1_2 = request.POST.get("f1_2")
        comment1_2 = request.POST.get("comment1_2")
        exception1_2 = request.POST.get("exception1_2")
        f1_3 = request.POST.get("f1_3")
        comment1_3 = request.POST.get("comment1_3")
        exception1_3 = request.POST.get("exception1_3")
        f1_4 = request.POST.get("f1_4")
        comment1_4 = request.POST.get("comment1_4")
        exception1_4 = request.POST.get("exception1_4")
        f1_5 = request.POST.get("f1_5")
        comment1_5 = request.POST.get("comment1_5")
        exception1_5 = request.POST.get("exception1_5")
        f1_6 = request.POST.get("f1_6")
        comment1_6 = request.POST.get("comment1_6")
        exception1_6 = request.POST.get("exception1_6")
        f1_7 = request.POST.get("f1_7")
        comment1_7 = request.POST.get("comment1_7")
        exception1_7 = request.POST.get("exception1_7")
        f1_8 = request.POST.get("f1_8")
        comment1_8 = request.POST.get("comment1_8")
        exception1_8 = request.POST.get("exception1_8")
        f1_9 = request.POST.get("f1_9")
        comment1_9 = request.POST.get("comment1_9")
        exception1_9 = request.POST.get("exception1_9")
        f2_1 = request.POST.get("f2_1")
        comment2_1 = request.POST.get("comment2_1")
        exception2_1 = request.POST.get("exception2_1")
        f2_2 = request.POST.get("f2_2")
        comment2_2 = request.POST.get("comment2_2")
        exception2_2 = request.POST.get("exception2_2")
        f2_3 = request.POST.get("f2_3")
        comment2_3 = request.POST.get("comment2_3")
        exception2_3 = request.POST.get("exception2_3")
        f2_4 = request.POST.get("f2_4")
        comment2_4 = request.POST.get("comment2_4")
        exception2_4 = request.POST.get("exception2_4")
        f2_5 = request.POST.get("f2_5")
        comment2_5 = request.POST.get("comment2_5")
        exception2_5 = request.POST.get("exception2_5")
        f3_1 = request.POST.get("f3_1")
        comment3_1 = request.POST.get("comment3_1")
        exception3_1 = request.POST.get("exception3_1")
        f3_2 = request.POST.get("f3_2")
        comment3_2 = request.POST.get("comment3_2")
        exception3_2 = request.POST.get("exception3_2")
        f3_3 = request.POST.get("f3_3")
        comment3_3 = request.POST.get("comment3_3")
        exception3_3 = request.POST.get("exception3_3")
        f3_4 = request.POST.get("f3_4")
        comment3_4 = request.POST.get("comment3_4")
        exception3_4 = request.POST.get("exception3_4")
        f3_5 = request.POST.get("f3_5")
        comment3_5 = request.POST.get("comment3_5")
        exception3_5 = request.POST.get("exception3_5")
        f4_1 = request.POST.get("f4_1")
        comment4_1 = request.POST.get("comment4_1")
        exception4_1 = request.POST.get("exception4_1")
        f4_2 = request.POST.get("f4_2")
        comment4_2 = request.POST.get("comment4_2")
        exception4_2 = request.POST.get("exception4_2")
        f4_3 = request.POST.get("f4_3")
        comment4_3 = request.POST.get("comment4_3")
        exception4_3 = request.POST.get("exception4_3")
        f5_1 = request.POST.get("f5_1")
        comment5_1 = request.POST.get("comment5_1")
        exception5_1 = request.POST.get("exception5_1")
        f5_2 = request.POST.get("f5_2")
        comment5_2 = request.POST.get("comment5_2")
        exception5_2 = request.POST.get("exception5_2")
        f5_3 = request.POST.get("f5_3")
        comment5_3 = request.POST.get("comment5_3")
        exception5_3 = request.POST.get("exception5_3")
        f5_4 = request.POST.get("f5_4")
        comment5_4 = request.POST.get("comment5_4")
        exception5_4 = request.POST.get("exception5_4")
        f5_5 = request.POST.get("f5_5")
        comment5_5 = request.POST.get("comment5_5")
        exception5_5 = request.POST.get("exception5_5")
        f5_6 = request.POST.get("f5_6")
        comment5_6 = request.POST.get("comment5_6")
        exception5_6 = request.POST.get("exception5_6")
        f6_1 = request.POST.get("f6_1")
        comment6_1 = request.POST.get("comment6_1")
        exception6_1 = request.POST.get("exception6_1")
        f6_2 = request.POST.get("f6_2")
        comment6_2 = request.POST.get("comment6_2")
        exception6_2 = request.POST.get("exception6_2")
        f6_3 = request.POST.get("f6_3")
        comment6_3 = request.POST.get("comment6_3")
        exception6_3 = request.POST.get("exception6_3")
        f6_4 = request.POST.get("f6_4")
        comment6_4 = request.POST.get("comment6_4")
        exception6_4 = request.POST.get("exception6_4")
        f6_5 = request.POST.get("f6_5")
        comment6_5 = request.POST.get("comment6_5")
        exception6_5 = request.POST.get("exception6_5")
        f6_6 = request.POST.get("f6_6")
        comment6_6 = request.POST.get("comment6_6")
        exception6_6 = request.POST.get("exception6_6")
        f6_7 = request.POST.get("f6_7")
        comment6_7 = request.POST.get("comment6_7")
        exception6_7 = request.POST.get("exception6_7")
        f6_8 = request.POST.get("f6_8")
        comment6_8 = request.POST.get("comment6_8")
        exception6_8 = request.POST.get("exception6_8")
        f6_9 = request.POST.get("f6_9")
        comment6_9 = request.POST.get("comment6_9")
        exception6_9 = request.POST.get("exception6_9")

        input_data = {
            'f1_1': f1_1,
            'comment1_1': comment1_1,
            'exception1_1': exception1_1,
            'f1_2': f1_2,
            'comment1_2': comment1_2,
            'exception1_2': exception1_2,
            'f1_3': f1_3,
            'comment1_3': comment1_3,
            'exception1_3': exception1_3,
            'f1_4': f1_4,
            'comment1_4': comment1_4,
            'exception1_4': exception1_4,
            'f1_5': f1_5,
            'comment1_5': comment1_5,
            'exception1_5': exception1_5,
            'f1_6': f1_6,
            'comment1_6': comment1_6,
            'exception1_6': exception1_6,
            'f1_7': f1_7,
            'comment1_7': comment1_7,
            'exception1_7': exception1_7,
            'f1_8': f1_8,
            'comment1_8': comment1_8,
            'exception1_8': exception1_8,
            'f1_9': f1_9,
            'comment1_9': comment1_9,
            'exception1_9': exception1_9,
            'f2_1': f2_1,
            'comment2_1': comment2_1,
            'exception2_1': exception2_1,
            'f2_2': f2_2,
            'comment2_2': comment2_2,
            'exception2_2': exception2_2,
            'f2_3': f2_3,
            'comment2_3': comment2_3,
            'exception2_3': exception2_3,
            'f2_4': f2_4,
            'comment2_4': comment2_4,
            'exception2_4': exception2_4,
            'f2_5': f2_5,
            'comment2_5': comment2_5,
            'exception2_5': exception2_5,
            'f3_1': f3_1,
            'comment3_1': comment3_1,
            'exception3_1': exception3_1,
            'f3_2': f3_2,
            'comment3_2': comment3_2,
            'exception3_2': exception3_2,
            'f3_3': f3_3,
            'comment3_3': comment3_3,
            'exception3_3': exception3_3,
            'f3_4': f3_4,
            'comment3_4': comment3_4,
            'exception3_4': exception3_4,
            'f3_5': f3_5,
            'comment3_5': comment3_5,
            'exception3_5': exception3_5,
            'f4_1': f4_1,
            'comment4_1': comment4_1,
            'exception4_1': exception4_1,
            'f4_2': f4_2,
            'comment4_2': comment4_2,
            'exception4_2': exception4_2,
            'f4_3': f4_3,
            'comment4_3': comment4_3,
            'exception4_3': exception4_3,
            'f5_1': f5_1,
            'comment5_1': comment5_1,
            'exception5_1': exception5_1,
            'f5_2': f5_2,
            'comment5_2': comment5_2,
            'exception5_2': exception5_2,
            'f5_3': f5_3,
            'comment5_3': comment5_3,
            'exception5_3': exception5_3,
            'f5_4': f5_4,
            'comment5_4': comment5_4,
            'exception5_4': exception5_4,
            'f5_5': f5_5,
            'comment5_5': comment5_5,
            'exception5_5': exception5_5,
            'f5_6': f5_6,
            'comment5_6': comment5_6,
            'exception5_6': exception5_6,
            'f6_1': f6_1,
            'comment6_1': comment6_1,
            'exception6_1': exception6_1,
            'f6_2': f6_2,
            'comment6_2': comment6_2,
            'exception6_2': exception6_2,
            'f6_3': f6_3,
            'comment6_3': comment6_3,
            'exception6_3': exception6_3,
            'f6_4': f6_4,
            'comment6_4': comment6_4,
            'exception6_4': exception6_4,
            'f6_5': f6_5,
            'comment6_5': comment6_5,
            'exception6_5': exception6_5,
            'f6_6': f6_6,
            'comment6_6': comment6_6,
            'exception6_6': exception6_6,
            'f6_7': f6_7,
            'comment6_7': comment6_7,
            'exception6_7': exception6_7,
            'f6_8': f6_8,
            'comment6_8': comment6_8,
            'exception6_8': exception6_8,
            'f6_9': f6_9,
            'comment6_9': comment6_9,
            'exception6_9': exception6_9,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'only_governance_scoring.html', context)
    return render(request, 'only_governance.html')


@login_required
def only_governance_scoring(request):
    if request.method == 'POST':
        employee_relations = request.POST.get("employee_relations")
        g_comment1 = request.POST.get("g_comment1")
        exception1 = request.POST.get("exception1")
        sound_management_structures = request.POST.get("sound_management_structures")
        g_comment2 = request.POST.get("g_comment2")
        exception2 = request.POST.get("exception2")
        remuneration_staff = request.POST.get("remuneration_staff")
        g_comment3 = request.POST.get("g_comment3")
        exception3 = request.POST.get("exception3")
        tax = request.POST.get("tax")
        g_comment4 = request.POST.get("g_comment4")
        exception4 = request.POST.get("exception4")
        corporate_governance = request.POST.get("corporate_governance")
        g_comment5 = request.POST.get("g_comment5")
        exception5 = request.POST.get("exception5")
        governance_other = request.POST.get("governance_other")
        g_comment6 = request.POST.get("g_comment6")
        exception6 = request.POST.get("exception6")

        input_data = {
            'employee_relations': employee_relations,
            'g_comment1': g_comment1,
            'exception1': exception1,
            'sound_management_structures': sound_management_structures,
            'g_comment2': g_comment2,
            'exception2': exception2,
            'remuneration_staff': remuneration_staff,
            'g_comment3': g_comment3,
            'exception3': exception3,
            'tax': tax,
            'g_comment4': g_comment4,
            'exception4': exception4,
            'corporate_governance': corporate_governance,
            'g_comment5': g_comment5,
            'exception5': exception5,
            'governance_other': governance_other,
            'g_comment6': g_comment6,
            'exception6': exception6,
        }

        table = governanceCalculations(input_data, request)
        g_total_score = table.g1_all_score()
        na_count_g = table.g1_all_na()
        g_avg_score = round(g_total_score / (6 - na_count_g))

        context = {
            'input_data': input_data,
            'e2_1': request.session.get('e2_1'),
            'e2_2': request.session.get('e2_2'),
            'e2_3': request.session.get('e2_3'),
            'e2_4': request.session.get('e2_4'),
            'e2_5': request.session.get('e2_5'),
            'e2_6': request.session.get('e2_6'),
            'e2_7': request.session.get('e2_7'),
            'e2_8': request.session.get('e2_8'),
            'e2_9': request.session.get('e2_9'),
            'e2_10': request.session.get('e2_10'),
            'comment1': request.session.get('comment1'),
            'comment2': request.session.get('comment2'),
            'comment3': request.session.get('comment3'),
            'comment4': request.session.get('comment4'),
            'comment5': request.session.get('comment5'),
            'comment6': request.session.get('comment6'),
            'comment7': request.session.get('comment7'),
            'comment8': request.session.get('comment8'),
            'comment9': request.session.get('comment9'),
            'comment10': request.session.get('comment10'),
            'total_score': request.session.get('total_score'),
            'avg_score': request.session.get('avg_score'),
            'company_name': request.session.get('company_name'),
            # 's1_1': request.session.get('s1_1'),
            # 's1_2': request.session.get('s1_2'),
            # 's1_3': request.session.get('s1_3'),
            # 's1_4': request.session.get('s1_4'),
            # 's1_5': request.session.get('s1_5'),
            # 's1_6': request.session.get('s1_6'),
            # 's1_7': request.session.get('s1_7'),
            # 's_comment1': request.session.get('s_comment1'),
            # 's_comment2': request.session.get('s_comment2'),
            # 's_comment3': request.session.get('s_comment3'),
            # 's_comment4': request.session.get('s_comment4'),
            # 's_comment5': request.session.get('s_comment5'),
            # 's_comment6': request.session.get('s_comment6'),
            # 's_comment7': request.session.get('s_comment7'),
            # 's_total_score': request.session.get('s_total_score'),
            # 's_avg_score': request.session.get('s_avg_score'),
            'g1_1': employee_relations,
            'g_comment1': g_comment1,
            'g1_2': sound_management_structures,
            'g_comment2': g_comment2,
            'g1_3': remuneration_staff,
            'g_comment3': g_comment3,
            'g1_4': tax,
            'g_comment4': g_comment4,
            'g1_5': corporate_governance,
            'g_comment5': g_comment5,
            'g1_6': governance_other,
            'g_comment6': g_comment6,
            'g_total_score': g_total_score,
            'g_avg_score': g_avg_score,

        }
        return render(request, 'final_scoring_client.html', context)
    return render(request, 'only_governance_scoring.html')


# if client select Social and Governance option to fill form :
@login_required
def social_1_select(request):
    if request.method == 'POST':
        f1_1 = request.POST.get("f1_1")
        comment1_1 = request.POST.get("comment1_1")
        exception1_1 = request.POST.get("exception1_1")
        f1_2 = request.POST.get("f1_2")
        comment1_2 = request.POST.get("comment1_2")
        exception1_2 = request.POST.get("exception1_2")
        f1_3 = request.POST.get("f1_3")
        comment1_3 = request.POST.get("comment1_3")
        exception1_3 = request.POST.get("exception1_3")
        f1_4 = request.POST.get("f1_4")
        comment1_4 = request.POST.get("comment1_4")
        exception1_4 = request.POST.get("exception1_4")
        f1_5 = request.POST.get("f1_5")
        comment1_5 = request.POST.get("comment1_5")
        exception1_5 = request.POST.get("exception1_5")
        f2_1 = request.POST.get("f2_1")
        comment2_1 = request.POST.get("comment2_1")
        exception2_1 = request.POST.get("exception2_1")
        f2_2 = request.POST.get("f2_2")
        comment2_2 = request.POST.get("comment2_2")
        exception2_2 = request.POST.get("exception2_2")
        f2_3 = request.POST.get("f2_3")
        comment2_3 = request.POST.get("comment2_3")
        exception2_3 = request.POST.get("exception2_3")
        f2_4 = request.POST.get("f2_4")
        comment2_4 = request.POST.get("comment2_4")
        exception2_4 = request.POST.get("exception2_4")
        f2_5 = request.POST.get("f2_5")
        comment2_5 = request.POST.get("comment2_5")
        exception2_5 = request.POST.get("exception2_5")
        f2_6 = request.POST.get("f2_6")
        comment2_6 = request.POST.get("comment2_6")
        exception2_6 = request.POST.get("exception2_6")
        f3_1 = request.POST.get("f3_1")
        comment3_1 = request.POST.get("comment3_1")
        exception3_1 = request.POST.get("exception3_1")
        f3_2 = request.POST.get("f3_2")
        comment3_2 = request.POST.get("comment3_2")
        exception3_2 = request.POST.get("exception3_2")
        f3_3 = request.POST.get("f3_3")
        comment3_3 = request.POST.get("comment3_3")
        exception3_3 = request.POST.get("exception3_3")
        f3_4 = request.POST.get("f3_4")
        comment3_4 = request.POST.get("comment3_4")
        exception3_4 = request.POST.get("exception3_4")
        f3_5 = request.POST.get("f3_5")
        comment3_5 = request.POST.get("comment3_5")
        exception3_5 = request.POST.get("exception3_5")
        f4_1 = request.POST.get("f4_1")
        comment4_1 = request.POST.get("comment4_1")
        exception4_1 = request.POST.get("exception4_1")
        f4_2 = request.POST.get("f4_2")
        comment4_2 = request.POST.get("comment4_2")
        exception4_2 = request.POST.get("exception4_2")
        f4_3 = request.POST.get("f4_3")
        comment4_3 = request.POST.get("comment4_3")
        exception4_3 = request.POST.get("exception4_3")
        f4_4 = request.POST.get("f4_4")
        comment4_4 = request.POST.get("comment4_4")
        exception4_4 = request.POST.get("exception4_4")
        f5_1 = request.POST.get("f5_1")
        comment5_1 = request.POST.get("comment5_1")
        exception5_1 = request.POST.get("exception5_1")
        f5_2 = request.POST.get("f5_2")
        comment5_2 = request.POST.get("comment5_2")
        exception5_2 = request.POST.get("exception5_2")
        f5_3 = request.POST.get("f5_3")
        comment5_3 = request.POST.get("comment5_3")
        exception5_3 = request.POST.get("exception5_3")
        f5_4 = request.POST.get("f5_4")
        comment5_4 = request.POST.get("comment5_4")
        exception5_4 = request.POST.get("exception5_4")
        f5_5 = request.POST.get("f5_5")
        comment5_5 = request.POST.get("comment5_5")
        exception5_5 = request.POST.get("exception5_5")
        f5_6 = request.POST.get("f5_6")
        comment5_6 = request.POST.get("comment5_6")
        exception5_6 = request.POST.get("exception5_6")
        f6_1 = request.POST.get("f6_1")
        comment6_1 = request.POST.get("comment6_1")
        exception6_1 = request.POST.get("exception6_1")
        f6_2 = request.POST.get("f6_2")
        comment6_2 = request.POST.get("comment6_2")
        exception6_2 = request.POST.get("exception6_2")
        f6_3 = request.POST.get("f6_3")
        comment6_3 = request.POST.get("comment6_3")
        exception6_3 = request.POST.get("exception6_3")
        f6_4 = request.POST.get("f6_4")
        comment6_4 = request.POST.get("comment6_4")
        exception6_4 = request.POST.get("exception6_4")
        f6_5 = request.POST.get("f6_5")
        comment6_5 = request.POST.get("comment6_5")
        exception6_5 = request.POST.get("exception6_5")
        f6_6 = request.POST.get("f6_6")
        comment6_6 = request.POST.get("comment6_6")
        exception6_6 = request.POST.get("exception6_6")
        f6_7 = request.POST.get("f6_7")
        comment6_7 = request.POST.get("comment6_7")
        exception6_7 = request.POST.get("exception6_7")
        f6_8 = request.POST.get("f6_8")
        comment6_8 = request.POST.get("comment6_8")
        exception6_8 = request.POST.get("exception6_8")
        f6_9 = request.POST.get("f6_9")
        comment6_9 = request.POST.get("comment6_9")
        exception6_9 = request.POST.get("exception6_9")
        f7_1 = request.POST.get("f7_1")
        comment7_1 = request.POST.get("comment7_1")
        exception7_1 = request.POST.get("exception7_1")
        f7_2 = request.POST.get("f7_2")
        comment7_2 = request.POST.get("comment7_2")
        exception7_2 = request.POST.get("exception7_2")
        f7_3 = request.POST.get("f7_3")
        comment7_3 = request.POST.get("comment7_3")
        exception7_3 = request.POST.get("exception7_3")
        f7_4 = request.POST.get("f7_4")
        comment7_4 = request.POST.get("comment7_4")
        exception7_4 = request.POST.get("exception7_4")
        f7_5 = request.POST.get("f7_5")
        comment7_5 = request.POST.get("comment7_5")
        exception7_5 = request.POST.get("exception7_5")
        f8_1 = request.POST.get("f8_1")
        comment8_1 = request.POST.get("comment8_1")
        exception8_1 = request.POST.get("exception8_1")
        f8_2 = request.POST.get("f8_2")
        comment8_2 = request.POST.get("comment8_1")
        exception8_2 = request.POST.get("exception8_2")
        f8_3 = request.POST.get("f8_3")
        comment8_3 = request.POST.get("comment8_3")
        exception8_3 = request.POST.get("exception8_3")
        f8_4 = request.POST.get("f8_4")
        comment8_4 = request.POST.get("comment8_4")
        exception8_4 = request.POST.get("exception8_4")
        f8_5 = request.POST.get("f8_5")
        comment8_5 = request.POST.get("comment8_5")
        exception8_5 = request.POST.get("exception8_5")
        f8_6 = request.POST.get("f8_6")
        comment8_6 = request.POST.get("comment8_6")
        exception8_6 = request.POST.get("exception8_6")
        f9_1 = request.POST.get("f9_1")
        comment9_1= request.POST.get("comment9_1")
        exception9_1 = request.POST.get("exception9_1")
        f9_2 = request.POST.get("f9_2")
        comment9_2 = request.POST.get("comment9_2")
        exception9_2 = request.POST.get("exception9_2")
        f9_3 = request.POST.get("f9_3")
        comment9_3 = request.POST.get("comment9_3")
        exception9_3 = request.POST.get("exception9_3")
        f9_4 = request.POST.get("f9_4")
        comment9_4 = request.POST.get("comment9_4")
        exception9_4 = request.POST.get("exception9_4")
        f9_5 = request.POST.get("f9_5")
        comment9_5 = request.POST.get("comment9_5")
        exception9_5 = request.POST.get("exception9_5")
        f9_6 = request.POST.get("f9_6")
        comment9_6= request.POST.get("comment9_6")
        exception9_6 = request.POST.get("exception9_6")
        f9_7 = request.POST.get("f9_7")
        comment9_7 = request.POST.get("comment9_7")
        exception9_7 = request.POST.get("exception9_7")
        f10_1 = request.POST.get("f10_1")
        comment10_1 = request.POST.get("comment10_1")
        exception10_1 = request.POST.get("exception10_1")
        f10_2 = request.POST.get("f10_2")
        comment10_2 = request.POST.get("comment10_2")
        exception10_2 = request.POST.get("exception10_2")
        f10_3 = request.POST.get("f10_3")
        comment10_3 = request.POST.get("comment10_3")
        exception10_3 = request.POST.get("exception10_3")

        input_data = {
            'f1_1': f1_1,
            'comment1_1': comment1_1,
            'exception1_1': exception1_1,
            'f1_2': f1_2,
            'comment1_2': comment1_2,
            'exception1_2': exception1_2,
            'f1_3': f1_3,
            'comment1_3': comment1_3,
            'exception1_3': exception1_3,
            'f1_4': f1_4,
            'comment1_4': comment1_4,
            'exception1_4': exception1_4,
            'f1_5': f1_5,
            'comment1_5': comment1_5,
            'exception1_5': exception1_5,
            'f2_1': f2_1,
            'comment2_1': comment2_1,
            'exception2_1': exception2_1,
            'f2_2': f2_2,
            'comment2_2': comment2_2,
            'exception2_2': exception2_2,
            'f2_3': f2_3,
            'comment2_3': comment2_3,
            'exception2_3': exception2_3,
            'f2_4': f2_4,
            'comment2_4': comment2_4,
            'exception2_4': exception2_4,
            'f2_5': f2_5,
            'comment2_5': comment2_5,
            'exception2_5': exception2_5,
            'f2_6': f2_6,
            'comment2_6': comment2_6,
            'exception2_6': exception2_6,
            'f3_1': f3_1,
            'comment3_1': comment3_1,
            'exception3_1': exception3_1,
            'f3_2': f3_2,
            'comment3_2': comment3_2,
            'exception3_2': exception3_2,
            'f3_3': f3_3,
            'comment3_3': comment3_3,
            'exception3_3': exception3_3,
            'f3_4': f3_4,
            'comment3_4': comment3_4,
            'exception3_4': exception3_4,
            'f3_5': f3_5,
            'comment3_5': comment3_5,
            'exception3_5': exception3_5,
            'f4_1': f4_1,
            'comment4_1': comment4_1,
            'exception4_1': exception4_1,
            'f4_2': f4_2,
            'comment4_2': comment4_2,
            'exception4_2': exception4_2,
            'f4_3': f4_3,
            'comment4_3': comment4_3,
            'exception4_3': exception4_3,
            'f4_4': f4_4,
            'comment4_4': comment4_4,
            'exception4_4': exception4_4,
            'f5_1': f5_1,
            'comment5_1': comment5_1,
            'exception5_1': exception5_1,
            'f5_2': f5_2,
            'comment5_2': comment5_2,
            'exception5_2': exception5_2,
            'f5_3': f5_3,
            'comment5_3': comment5_3,
            'exception5_3': exception5_3,
            'f5_4': f5_4,
            'comment5_4': comment5_4,
            'exception5_4': exception5_4,
            'f5_5': f5_5,
            'comment5_5': comment5_5,
            'exception5_5': exception5_5,
            'f5_6': f5_6,
            'comment5_6': comment5_6,
            'exception5_6': exception5_6,
            'f6_1': f6_1,
            'comment6_1': comment6_1,
            'exception6_1': exception6_1,
            'f6_2': f6_2,
            'comment6_2': comment6_2,
            'exception6_2': exception6_2,
            'f6_3': f6_3,
            'comment6_3': comment6_3,
            'exception6_3': exception6_3,
            'f6_4': f6_4,
            'comment6_4': comment6_4,
            'exception6_4': exception6_4,
            'f6_5': f6_5,
            'comment6_5': comment6_5,
            'exception6_5': exception6_5,
            'f6_6': f6_6,
            'comment6_6': comment6_6,
            'exception6_6': exception6_6,
            'f6_7': f6_7,
            'comment6_7': comment6_7,
            'exception6_7': exception6_7,
            'f6_8': f6_8,
            'comment6_8': comment6_8,
            'exception6_8': exception6_8,
            'f6_9': f6_9,
            'comment6_9': comment6_9,
            'exception6_9': exception6_9,
            'f7_1': f7_1,
            'comment7_1': comment7_1,
            'exception7_1': exception7_1,
            'f7_2': f7_2,
            'comment7_2': comment7_2,
            'exception7_2': exception7_2,
            'f7_3': f7_3,
            'comment7_3': comment7_3,
            'exception7_3': exception7_3,
            'f7_4': f7_4,
            'comment7_4': comment7_4,
            'exception7_4': exception7_4,
            'f7_5': f7_5,
            'comment7_5': comment7_5,
            'exception7_5': exception7_5,
            'f8_1': f8_1,
            'comment8_1': comment8_1,
            'exception8_1': exception8_1,
            'f8_2': f8_2,
            'comment8_2': comment8_2,
            'exception8_2': exception8_2,
            'f8_3': f8_3,
            'comment8_3': comment8_3,
            'exception8_3': exception8_3,
            'f8_4': f8_4,
            'comment8_4': comment8_4,
            'exception8_4': exception8_4,
            'f8_5': f8_5,
            'comment8_5': comment8_5,
            'exception8_5': exception8_5,
            'f8_6': f8_6,
            'comment8_6': comment8_6,
            'exception8_6': exception8_6,
            'f9_1':f9_1,
            'comment9_1': comment9_1,
            'exception9_1': exception9_1,
            'f9_2': f9_2,
            'comment9_2': comment9_2,
            'exception9_2': exception9_2,
            'f9_3': f9_3,
            'comment9_3': comment9_3,
            'exception9_3': exception9_3,
            'f9_4': f9_4,
            'comment9_4': comment9_4,
            'exception9_4': exception9_4,
            'f9_5': f9_5,
            'comment9_5': comment9_5,
            'exception9_5': exception9_5,
            'f9_6': f9_6,
            'comment9_6': comment9_6,
            'exception9_6': exception9_6,
            'f9_7': f9_7,
            'comment9_7': comment9_7,
            'exception9_7': exception9_7,
            'f10_1': f10_1,
            'comment10_1': comment10_1,
            'exception10_1': exception10_1,
            'f10_2': f10_2,
            'comment10_2': comment10_2,
            'exception10_2': exception10_2,
            'f10_3': f10_3,
            'comment10_3': comment10_3,
            'exception10_3': exception10_3,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'social_screening.html', context)
    return render(request, 'social_1_select.html')


@login_required
def self_assessment_1(request):
    if request.method == 'POST':
        sa1_1 = request.POST.get("sa1_1")
        comment1_1 = request.POST.get("comment1_1")
        exception1_1 = request.POST.get("exception1_1")
        sa2_1 = request.POST.get("sa2_1")
        comment2_1 = request.POST.get("comment2_1")
        exception2_1 = request.POST.get("exception2_1")

        input_data = {
            'sa1_1': sa1_1,
            'comment1_1': comment1_1,
            'exception1_1': exception1_1,
            'sa2_1': sa2_1,
            'comment2_1': comment2_1,
            'exception2_1': exception2_1,
        }

        context = {
            'input_data' : input_data,
        }
        return render(request, 'self_assessment_2.html', context)
    return render(request, 'self_assessment_1.html')


@login_required
def self_assessment_2(request):
    if request.method == 'POST':
        sa3_1 = request.POST.get("sa3_1")
        comment3_1 = request.POST.get("comment3_1")
        exception3_1 = request.POST.get("exception3_1")
        sa3_2 = request.POST.get("sa3_2")
        comment3_2 = request.POST.get("comment3_2")
        exception3_2 = request.POST.get("exception3_2")
        sa3_3 = request.POST.get("sa3_3")
        comment3_3 = request.POST.get("comment3_3")
        exception3_3 = request.POST.get("exception3_3")
        sa3_4 = request.POST.get("sa3_4 ")
        comment3_4 = request.POST.get("comment3_4")
        exception3_4 = request.POST.get("exception3_4")
        sa3_5 = request.POST.get("sa3_5")
        comment3_5 = request.POST.get("comment3_5")
        exception3_5 = request.POST.get("exception3_5")
        sa3_6 = request.POST.get("sa3_6")
        comment3_6 = request.POST.get("comment3_6")
        exception3_6 = request.POST.get("exception3_6")
        sa3_7 = request.POST.get("sa3_7")
        comment3_7 = request.POST.get("comment3_7")
        exception3_7 = request.POST.get("exception3_6")
        sa3_8 = request.POST.get("sa3_8")
        comment3_8 = request.POST.get("comment3_8")
        exception3_8 = request.POST.get("exception3_8")
        sa3_9 = request.POST.get("sa3_9")
        comment3_9 = request.POST.get("comment3_9")
        exception3_9 = request.POST.get("exception3_9")
        sa3_10 = request.POST.get("sa3_10")
        comment3_10 = request.POST.get("comment3_10")
        exception3_10 = request.POST.get("exception3_10")
        sa3_11 = request.POST.get("sa3_11")
        comment3_11 = request.POST.get("comment3_11")
        exception3_11 = request.POST.get("exception3_11")

        input_data = {
            'sa3_1': sa3_1,
            'comment3_1': comment3_1,
            'exception3_1': exception3_1,
            'sa3_2': sa3_2,
            'comment3_2': comment3_2,
            'exception3_2': exception3_2,
            'sa3_3': sa3_3,
            'comment3_3': comment3_3,
            'exception3_3': exception3_3,
            'sa3_4 ': sa3_4 ,
            'comment3_4': comment3_4,
            'exception3_4': exception3_4,
            'sa3_5': sa3_5,
            'comment3_5': comment3_5,
            'exception3_5': exception3_5,
            'sa3_6': sa3_6,
            'comment3_6': comment3_6,
            'exception3_6': exception3_6,
            'sa3_7': sa3_7,
            'comment3_7': comment3_7,
            'exception3_7': exception3_7,
            'sa3_8': sa3_8,
            'comment3_8': comment3_8,
            'exception3_8': exception3_8,
            'sa3_9': sa3_9,
            'comment3_9': comment3_9,
            'exception3_9': exception3_9,
            'sa3_10': sa3_10,
            'comment3_10': comment3_10,
            'exception3_10': exception3_10,
            'sa3_11': sa3_11,
            'comment3_11': comment3_11,
            'exception3_11': exception3_11,
        }
        context = {
            'input_data': input_data,
        }
        return render(request, 'self_assessment1_3.html', context)
    return render(request, 'self_assessment_2.html')


@login_required
def self_assessment1_3(request):
    if request.method == 'POST':
        sa4_1 = request.POST.get("sa4_1")
        comment4_1 = request.POST.get("comment4_1")
        exception4_1 = request.POST.get("exception4_1")
        sa4_2 = request.POST.get("sa4_2")
        comment4_2 = request.POST.get("comment4_2")
        exception4_2 = request.POST.get("exception4_2")
        sa4_3 = request.POST.get("sa4_3")
        comment4_3 = request.POST.get("comment4_3")
        exception4_3 = request.POST.get("exception4_3")
        sa4_4 = request.POST.get("sa4_4 ")
        comment4_4 = request.POST.get("comment4_4")
        exception4_4 = request.POST.get("exception4_4")
        sa4_5 = request.POST.get("sa4_5")
        comment4_5 = request.POST.get("comment4_5")
        exception4_5 = request.POST.get("exception4_5")

        input_data = {
            'sa4_1': sa4_1,
            'comment4_1': comment4_1,
            'exception4_1': exception4_1,
            'sa4_2': sa4_2,
            'comment4_2': comment4_2,
            'exception4_2': exception4_2,
            'sa4_3': sa4_3,
            'comment4_3': comment4_3,
            'exception4_3': exception4_3,
            'sa4_4 ': sa4_4 ,
            'comment4_4': comment4_4,
            'exception4_4': exception4_4,
            'sa4_5': sa4_5,
            'comment4_5': comment4_5,
            'exception4_5': exception4_5,
        }
        context = {
            'input_data': input_data,
        }
        return render(request, 'self_assessment_4.html', context)
    return render(request, 'self_assessment1_3.html')


@login_required
def self_assessment_4(request):
    if request.method == 'POST':
        sa5_1 = request.POST.get("sa5_1")
        comment5_1 = request.POST.get("comment5_1")
        exception5_1 = request.POST.get("exception5_1")
        sa5_2 = request.POST.get("sa5_2")
        comment5_2 = request.POST.get("comment5_2")
        exception5_2 = request.POST.get("exception5_2")
        sa5_3 = request.POST.get("sa5_3")
        comment5_3 = request.POST.get("comment5_3")
        exception5_3 = request.POST.get("exception5_3")

        input_data = {
            'sa5_1': sa5_1,
            'comment5_1': comment5_1,
            'exception5_1': exception5_1,
            'sa5_2': sa5_2,
            'comment5_2': comment5_2,
            'exception5_2': exception5_2,
            'sa5_3': sa5_3,
            'comment5_3': comment5_3,
            'exception5_3': exception5_3,
        }
        context = {
            'input_data': input_data,
        }
        return render(request, 'self_assessment_5.html', context)
    return render(request, 'self_assessment_4.html')


@login_required
def self_assessment_5(request):
    if request.method == 'POST':
        sa6_1 = request.POST.get("sa6_1")
        comment6_1 = request.POST.get("comment6_1")
        exception6_1 = request.POST.get("exception6_1")
        sa6_2 = request.POST.get("sa6_2")
        comment6_2 = request.POST.get("comment6_2")
        exception6_2 = request.POST.get("exception6_2")

        input_data = {
            'sa6_1': sa6_1,
            'comment6_1': comment6_1,
            'exception6_1': exception6_1,
            'sa6_2': sa6_2,
            'comment6_2': comment6_2,
            'exception6_2': exception6_2,
        }
        context = {
            'input_data': input_data,
        }
        return render(request, 'self_assessment_6.html', context)
    return render(request, 'self_assessment_5.html')


@login_required
def self_assessment_6(request):
    if request.method == 'POST':
        sa7_1 = request.POST.get("sa7_1")
        comment7_1 = request.POST.get("comment7_1")
        exception7_1 = request.POST.get("exception7_1")
        sa7_2 = request.POST.get("sa7_2")
        comment7_2 = request.POST.get("comment7_2")
        exception7_2 = request.POST.get("exception7_2")
        sa7_3 = request.POST.get("sa7_3")
        comment7_3 = request.POST.get("comment7_3")
        exception7_3 = request.POST.get("exception7_3")
        sa7_4 = request.POST.get("sa7_4")
        comment7_4 = request.POST.get("comment7_4")
        exception7_4 = request.POST.get("exception7_4")
        sa7_5 = request.POST.get("sa7_5")
        comment7_5 = request.POST.get("comment7_5")
        exception7_5 = request.POST.get("exception7_5")
        sa7_6 = request.POST.get("sa7_6")
        comment7_6 = request.POST.get("comment7_6")
        exception7_6 = request.POST.get("exception7_6")

        input_data = {
            'sa7_1': sa7_1,
            'comment7_1': comment7_1,
            'exception7_1': exception7_1,
            'sa7_2': sa7_2,
            'comment7_2': comment7_2,
            'exception7_2': exception7_2,
            'sa7_3': sa7_3,
            'comment7_3': comment7_3,
            'exception7_3': exception7_3,
            'sa7_4': sa7_4,
            'comment7_4': comment7_4,
            'exception7_4': exception7_4,
            'sa7_5': sa7_5,
            'comment7_5': comment7_5,
            'exception7_5': exception7_5,
            'sa7_6': sa7_6,
            'comment7_6': comment7_6,
            'exception7_6': exception7_6,
        }
        context = {
            'input_data': input_data,
        }
        return render(request, 'self_assessment_7.html', context)
    return render(request, 'self_assessment_6.html')


@login_required
def self_assessment_7(request):
    if request.method == 'POST':
        sa8_1 = request.POST.get("sa8_1")
        comment8_1 = request.POST.get("comment8_1")
        exception8_1 = request.POST.get("exception8_1")
        sa8_2 = request.POST.get("sa8_2")
        comment8_2 = request.POST.get("comment8_2")
        exception8_2 = request.POST.get("exception8_2")
        sa8_3 = request.POST.get("sa8_3")
        comment8_3 = request.POST.get("comment8_3")
        exception8_3 = request.POST.get("exception8_3")
        sa8_4 = request.POST.get("sa8_4")
        comment8_4 = request.POST.get("comment8_4")
        exception8_4 = request.POST.get("exception8_4")
        sa8_5 = request.POST.get("sa8_5")
        comment8_5 = request.POST.get("comment8_5")
        exception8_5 = request.POST.get("exception8_5")
        sa8_6 = request.POST.get("sa8_6")
        comment8_6 = request.POST.get("comment8_6")
        exception8_6 = request.POST.get("exception8_6")
        sa8_7 = request.POST.get("sa8_7")
        comment8_7 = request.POST.get("comment8_7")
        exception8_7 = request.POST.get("exception8_7")
        sa8_8 = request.POST.get("sa8_8")
        comment8_8 = request.POST.get("comment8_8")
        exception8_8 = request.POST.get("exception8_8")
        sa8_9 = request.POST.get("sa8_9")
        comment8_9 = request.POST.get("comment8_9")
        exception8_9 = request.POST.get("exception8_9")
        sa8_10 = request.POST.get("sa8_10")
        comment8_10 = request.POST.get("comment8_10")
        exception8_10 = request.POST.get("exception8_10")

        input_data = {
            'sa8_1': sa8_1,
            'comment8_1': comment8_1,
            'exception8_1': exception8_1,
            'sa8_2': sa8_2,
            'comment8_2': comment8_2,
            'exception8_2': exception8_2,
            'sa8_3': sa8_3,
            'comment8_3': comment8_3,
            'exception8_3': exception8_3,
            'sa8_4': sa8_4,
            'comment8_4': comment8_4,
            'exception8_4': exception8_4,
            'sa8_5': sa8_5,
            'comment8_5': comment8_5,
            'exception8_5': exception8_5,
            'sa8_6': sa8_6,
            'comment8_6': comment8_6,
            'exception8_6': exception8_6,
            'sa8_7': sa8_7,
            'comment8_7': comment8_7,
            'exception8_7': exception8_7,
            'sa8_8': sa8_8,
            'comment8_8': comment8_8,
            'exception8_8': exception8_8,
            'sa8_9': sa8_9,
            'comment8_9': comment8_9,
            'exception8_9': exception8_9,
            'sa8_10': sa8_10,
            'comment8_10': comment8_10,
            'exception8_10': exception8_10,
        }
        context = {
            'input_data': input_data,
        }
        return render(request, 'self_assessment_8.html', context)
    return render(request, 'self_assessment_7.html')


@login_required
def self_assessment_8(request):
    if request.method == 'POST':
        sa9_1 = request.POST.get("sa9_1")
        comment9_1 = request.POST.get("comment9_1")
        exception9_1 = request.POST.get("exception9_1")
        sa9_2 = request.POST.get("sa9_2")
        comment9_2 = request.POST.get("comment9_2")
        exception9_2 = request.POST.get("exception9_2")
        sa9_3 = request.POST.get("sa9_3")
        comment9_3 = request.POST.get("comment9_3")
        exception9_3 = request.POST.get("exception9_3")
        sa10_1 = request.POST.get("sa10_1")
        comment10_1 = request.POST.get("comment10_1")
        exception10_1 = request.POST.get("exception10_1")
        sa10_2 = request.POST.get("sa10_2")
        comment10_2 = request.POST.get("comment10_2")
        exception10_2 = request.POST.get("exception10_2")
        sa10_3 = request.POST.get("sa10_3")
        comment10_3 = request.POST.get("comment10_3")
        exception10_3 = request.POST.get("exception10_3")
        sa10_4 = request.POST.get("sa10_4")
        comment10_4 = request.POST.get("comment10_4")
        exception10_4 = request.POST.get("exception10_4")
        sa10_5 = request.POST.get("sa10_5")
        comment10_5 = request.POST.get("comment10_5")
        exception10_5 = request.POST.get("exception10_5")
        sa10_6 = request.POST.get("sa10_6")
        comment10_6 = request.POST.get("comment10_6")
        exception10_6 = request.POST.get("exception10_6")
        sa11_1 = request.POST.get("sa11_1")
        comment11_1 = request.POST.get("comment11_1")
        exception11_1 = request.POST.get("exception11_1")

        input_data = {
            'sa9_1': sa9_1,
            'comment9_1': comment9_1,
            'exception9_1': exception9_1,
            'sa9_2': sa9_2,
            'comment9_2': comment9_2,
            'exception9_2': exception9_2,
            'sa9_3': sa9_3,
            'comment9_3': comment9_3,
            'exception9_3': exception9_3,
            'sa10_1': sa10_1,
            'comment10_1': comment10_1,
            'exception10_1': exception10_1,
            'sa10_2': sa10_2,
            'comment10_2': comment10_2,
            'exception10_2': exception10_2,
            'sa10_3': sa10_3,
            'comment10_3': comment10_3,
            'exception10_3': exception10_3,
            'sa10_4': sa10_4,
            'comment10_4': comment10_4,
            'exception10_4': exception10_4,
            'sa10_5': sa10_5,
            'comment10_5': comment10_5,
            'exception10_5': exception10_5,
            'sa10_6': sa10_6,
            'comment10_6': comment10_6,
            'exception10_6': exception10_6,
            'sa11_1': sa11_1,
            'comment11_1': comment11_1,
            'exception11_1': exception11_1,
        }
        context = {
            'input_data': input_data,
        }
        return render(request, 'self_assessment_9.html', context)
    return render(request, 'self_assessment_8.html')


@login_required
def self_assessment_9(request):
    if request.method == 'POST':
        sa12_1 = request.POST.get("sa12_1")
        comment12_1 = request.POST.get("comment12_1")
        exception12_1 = request.POST.get("exception12_1")
        sa12_2 = request.POST.get("sa12_2")
        comment12_2 = request.POST.get("comment12_2")
        exception12_2 = request.POST.get("exception12_2")
        sa12_3 = request.POST.get("sa12_3")
        comment12_3 = request.POST.get("comment12_3")
        exception12_3 = request.POST.get("exception12_3")
        sa12_4 = request.POST.get("sa12_4")
        comment12_4 = request.POST.get("comment12_4")
        exception12_4 = request.POST.get("exception12_4")
        sa13_1 = request.POST.get("sa13_1")
        comment13_1 = request.POST.get("comment13_1")
        exception13_1 = request.POST.get("exception13_1")
        sa13_2 = request.POST.get("sa13_2")
        comment13_2 = request.POST.get("comment13_2")
        exception13_2 = request.POST.get("exception13_2")
        sa13_3 = request.POST.get("sa13_3")
        comment13_3 = request.POST.get("comment13_3")
        exception13_3 = request.POST.get("exception13_3")
        sa13_4 = request.POST.get("sa13_4")
        comment13_4 = request.POST.get("comment13_4")
        exception13_4 = request.POST.get("exception13_4")
        sa13_5 = request.POST.get("sa13_5")
        comment13_5 = request.POST.get("comment13_5")
        exception13_5 = request.POST.get("exception13_5")
        sa13_6 = request.POST.get("sa13_6")
        comment13_6 = request.POST.get("comment13_6")
        exception13_6 = request.POST.get("exception13_6")

        input_data = {
            'sa12_1': sa12_1,
            'comment12_1': comment12_1,
            'exception12_1': exception12_1,
            'sa12_2': sa12_2,
            'comment12_2': comment12_2,
            'exception12_2': exception12_2,
            'sa12_3': sa12_3,
            'comment12_3': comment12_3,
            'exception12_3': exception12_3,
            'sa12_4': sa12_4,
            'comment12_4': comment12_4,
            'exception12_4': exception12_4,
            'sa13_1': sa13_1,
            'comment13_1': comment13_1,
            'exception13_1': exception13_1,
            'sa13_2': sa13_2,
            'comment13_2': comment13_2,
            'exception13_2': exception13_2,
            'sa13_3': sa13_3,
            'comment13_3': comment13_3,
            'exception13_3': exception13_3,
            'sa13_4': sa13_4,
            'comment13_4': comment13_4,
            'exception13_4': exception13_4,
            'sa13_5': sa13_5,
            'comment13_5': comment13_5,
            'exception13_5': exception13_5,
            'sa13_6': sa13_6,
            'comment13_6': comment13_6,
            'exception13_6': exception13_6,
        }
        context = {
            'input_data': input_data,
        }
        return render(request, 'self_assessment_10.html', context)
    return render(request, 'self_assessment_9.html')


@login_required
def self_assessment_10(request):
    if request.method == 'POST':
        sa14_1 = request.POST.get("sa14_1")
        comment14_1 = request.POST.get("comment14_1")
        exception14_1 = request.POST.get("exception14_1")
        sa14_2 = request.POST.get("sa14_2")
        comment14_2 = request.POST.get("comment14_2")
        exception14_2 = request.POST.get("exception14_2")
        sa14_3 = request.POST.get("sa14_3")
        comment14_3 = request.POST.get("comment14_3")
        exception14_3 = request.POST.get("exception14_3")
        sa14_4 = request.POST.get("sa14_4")
        comment14_4 = request.POST.get("comment14_4")
        exception14_4 = request.POST.get("exception14_4")
        sa14_5 = request.POST.get("sa14_5")
        comment14_5 = request.POST.get("comment14_5")
        exception14_5 = request.POST.get("exception14_5")
        sa14_6 = request.POST.get("sa14_6")
        comment14_6 = request.POST.get("comment14_6")
        exception14_6 = request.POST.get("exception14_6")

        input_data = {
            'sa14_1': sa14_1,
            'comment14_1': comment14_1,
            'exception14_1': exception14_1,
            'sa14_2': sa14_2,
            'comment14_2': comment14_2,
            'exception14_2': exception14_2,
            'sa14_3': sa14_3,
            'comment14_3': comment14_3,
            'exception14_3': exception14_3,
            'sa14_4': sa14_4,
            'comment14_4': comment14_4,
            'exception14_4': exception14_4,
            'sa14_5': sa14_5,
            'comment14_5': comment14_5,
            'exception14_5': exception14_5,
            'sa14_6': sa14_6,
            'comment14_6': comment14_6,
            'exception14_6': exception14_6,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'self_assessment_11.html', context)
    return render(request, 'self_assessment_10.html')


@login_required
def self_assessment_11(request):
    if request.method == 'POST':
        sa15_1 = request.POST.get("sa15_1")
        comment15_1 = request.POST.get("comment15_1")
        exception15_1 = request.POST.get("exception15_1")
        sa15_2 = request.POST.get("sa15_2")
        comment15_2 = request.POST.get("comment15_2")
        exception15_2 = request.POST.get("exception15_2")
        sa15_3 = request.POST.get("sa15_3")
        comment15_3 = request.POST.get("comment15_3")
        exception15_3 = request.POST.get("exception15_3")
        sa15_4 = request.POST.get("sa15_4")
        comment15_4 = request.POST.get("comment15_4")
        exception15_4 = request.POST.get("exception15_4")
        sa15_5 = request.POST.get("sa15_5")
        comment15_5 = request.POST.get("comment15_5")
        exception15_5 = request.POST.get("exception15_5")
        sa15_6 = request.POST.get("sa15_6")
        comment15_6 = request.POST.get("comment15_6")
        exception15_6 = request.POST.get("exception15_6")
        sa15_7 = request.POST.get("sa15_7")
        comment15_7 = request.POST.get("comment15_7")
        exception15_7 = request.POST.get("exception15_7")
        sa15_8 = request.POST.get("sa15_8")
        comment15_8 = request.POST.get("comment15_8")
        exception15_8 = request.POST.get("exception15_8")
        sa15_9 = request.POST.get("sa15_9")
        comment15_9 = request.POST.get("comment15_9")
        exception15_9 = request.POST.get("exception15_9")
        sa15_10 = request.POST.get("sa15_10")
        comment15_10 = request.POST.get("comment15_10")
        exception15_10 = request.POST.get("exception15_10")
        sa15_11 = request.POST.get("sa15_11")
        comment15_11 = request.POST.get("comment15_11")
        exception15_11 = request.POST.get("exception15_11")
        sa15_12 = request.POST.get("sa15_12")
        comment15_12 = request.POST.get("comment15_12")
        exception15_12 = request.POST.get("exception15_12")
        sa15_13 = request.POST.get("sa15_13")
        comment15_13 = request.POST.get("comment15_13")
        exception15_13 = request.POST.get("exception15_13")

        input_data = {
            'sa15_1': sa15_1,
            'comment15_1': comment15_1,
            'exception15_1': exception15_1,
            'sa15_2': sa15_2,
            'comment15_2': comment15_2,
            'exception15_2': exception15_2,
            'sa15_3': sa15_3,
            'comment15_3': comment15_3,
            'exception15_3': exception15_3,
            'sa15_4': sa15_4,
            'comment15_4': comment15_4,
            'exception15_4': exception15_4,
            'sa15_5': sa15_5,
            'comment15_5': comment15_5,
            'exception15_5': exception15_5,
            'sa15_6': sa15_6,
            'comment15_6': comment15_6,
            'exception15_6': exception15_6,
            'sa15_7': sa15_7,
            'comment15_7': comment15_7,
            'exception15_7': exception15_7,
            'sa15_8': sa15_8,
            'comment15_8': comment15_8,
            'exception15_8': exception15_8,
            'sa15_9': sa15_9,
            'comment15_9': comment15_9,
            'exception15_9': exception15_9,
            'sa15_10': sa15_10,
            'comment15_10': comment15_10,
            'exception15_10': exception15_10,
            'sa15_11': sa15_11,
            'comment15_11': comment15_11,
            'exception15_11': exception15_11,
            'sa15_12': sa15_12,
            'comment15_12': comment15_12,
            'exception15_12': exception15_12,
            'sa15_13': sa15_13,
            'comment15_13': comment15_13,
            'exception15_13': exception15_13,
        }
        context = {
            'input_data': input_data,
        }
        return render(request, 'self_assessment_12.html', context)
    return render(request, 'self_assessment_11.html')


@login_required
def self_assessment_12(request):
    if request.method == 'POST':
        sa16_1 = request.POST.get("sa16_1")
        comment16_1 = request.POST.get("comment16_1")
        exception16_1 = request.POST.get("exception16_1")
        sa16_2 = request.POST.get("sa16_2")
        comment16_2 = request.POST.get("comment16_2")
        exception16_2 = request.POST.get("exception16_2")
        sa16_3 = request.POST.get("sa16_3")
        comment16_3 = request.POST.get("comment16_3")
        exception16_3 = request.POST.get("exception16_3")
        sa16_4 = request.POST.get("sa16_4")
        comment16_4 = request.POST.get("comment16_4")
        exception16_4 = request.POST.get("exception16_4")
        sa16_5 = request.POST.get("sa16_5")
        comment16_5 = request.POST.get("comment16_5")
        exception16_5 = request.POST.get("exception16_5")
        sa16_6 = request.POST.get("sa16_6")
        comment16_6 = request.POST.get("comment16_6")
        exception16_6 = request.POST.get("exception16_6")
        sa16_7 = request.POST.get("sa16_7")
        comment16_7 = request.POST.get("comment16_7")
        exception16_7 = request.POST.get("exception16_7")
        sa17_1 = request.POST.get("sa17_1")
        comment17_1 = request.POST.get("comment17_1")
        exception17_1 = request.POST.get("exception17_1")
        sa17_2 = request.POST.get("sa17_2")
        comment17_2 = request.POST.get("comment17_2")
        exception17_2 = request.POST.get("exception17_2")
        sa17_3 = request.POST.get("sa17_3")
        comment17_3 = request.POST.get("comment17_3")
        exception17_3 = request.POST.get("exception17_3")
        sa17_4 = request.POST.get("sa17_4")
        comment17_4 = request.POST.get("comment17_4")
        exception17_4 = request.POST.get("exception17_4")
        sa17_5 = request.POST.get("sa17_5")
        comment17_5 = request.POST.get("comment17_5")
        exception17_5 = request.POST.get("exception17_5")
        sa17_6 = request.POST.get("sa17_6")
        comment17_6 = request.POST.get("comment17_6")
        exception17_6 = request.POST.get("exception17_6")
        sa17_7 = request.POST.get("sa17_7")
        comment17_7 = request.POST.get("comment17_7")
        exception17_7 = request.POST.get("exception17_7")

        input_data = {
            'sa16_1': sa16_1,
            'comment16_1': comment16_1,
            'exception16_1': exception16_1,
            'sa16_2': sa16_2,
            'comment16_2': comment16_2,
            'exception16_2': exception16_2,
            'sa16_3': sa16_3,
            'comment16_3': comment16_3,
            'exception16_3': exception16_3,
            'sa16_4': sa16_4,
            'comment16_4': comment16_4,
            'exception16_4': exception16_4,
            'sa16_5': sa16_5,
            'comment16_5': comment16_5,
            'exception16_5': exception16_5,
            'sa16_6': sa16_6,
            'comment16_6': comment16_6,
            'exception16_6': exception16_6,
            'sa16_7': sa16_7,
            'comment16_7': comment16_7,
            'exception16_7': exception16_7,
            'sa17_1': sa17_1,
            'comment17_1': comment17_1,
            'exception17_1': exception17_1,
            'sa17_2': sa17_2,
            'comment17_2': comment17_2,
            'exception17_2': exception17_2,
            'sa17_3': sa17_3,
            'comment17_3': comment17_3,
            'exception17_3': exception17_3,
            'sa13_4': sa17_4,
            'comment17_4': comment17_4,
            'exception17_4': exception17_4,
            'sa17_5': sa17_5,
            'comment17_5': comment17_5,
            'exception17_5': exception17_5,
            'sa17_6': sa17_6,
            'comment17_6': comment17_6,
            'exception17_6': exception17_6,
            'sa17_7': sa17_7,
            'comment17_7': comment17_7,
            'exception17_7': exception17_7,
        }
        context = {
            'input_data': input_data,
        }
        return render(request, 'self_assessment_13.html', context)
    return render(request, 'self_assessment_12.html')


@login_required
def self_assessment_13(request):
    if request.method == 'POST':
        sa18_1 = request.POST.get("sa18_1")
        comment18_1 = request.POST.get("comment18_1")
        exception18_1 = request.POST.get("exception18_1")
        sa18_2 = request.POST.get("sa18_2")
        comment18_2 = request.POST.get("comment18_2")
        exception18_2 = request.POST.get("exception18_2")
        sa18_3 = request.POST.get("sa18_3")
        comment18_3 = request.POST.get("comment18_3")
        exception18_3 = request.POST.get("exception18_3")
        sa18_4 = request.POST.get("sa18_4")
        comment18_4 = request.POST.get("comment18_4")
        exception18_4 = request.POST.get("exception18_4")
        sa18_5 = request.POST.get("sa18_5")
        comment18_5 = request.POST.get("comment18_5")
        exception18_5 = request.POST.get("exception18_5")
        sa18_6 = request.POST.get("sa18_6")
        comment18_6 = request.POST.get("comment18_6")
        exception18_6 = request.POST.get("exception18_6")
        sa19_1 = request.POST.get("sa19_1")
        comment19_1 = request.POST.get("comment19_1")
        exception19_1 = request.POST.get("exception19_1")
        sa19_2 = request.POST.get("sa19_2")
        comment19_2 = request.POST.get("comment19_2")
        exception19_2 = request.POST.get("exception19_2")
        sa19_3 = request.POST.get("sa19_3")
        comment19_3 = request.POST.get("comment19_3")
        exception19_3 = request.POST.get("exception19_3")

        input_data = {
            'sa18_1': sa18_1,
            'comment18_1': comment18_1,
            'exception18_1': exception18_1,
            'sa18_2': sa18_2,
            'comment18_2': comment18_2,
            'exception18_2': exception18_2,
            'sa18_3': sa18_3,
            'comment18_3': comment18_3,
            'exception18_3': exception18_3,
            'sa18_4': sa18_4,
            'comment18_4': comment18_4,
            'exception18_4': exception18_4,
            'sa18_5': sa18_5,
            'comment18_5': comment18_5,
            'exception18_5': exception18_5,
            'sa18_6': sa18_6,
            'comment8_6': comment18_6,
            'exception18_6': exception18_6,
            'sa19_1': sa19_1,
            'comment19_1': comment19_1,
            'exception19_1': exception19_1,
            'sa19_2': sa19_2,
            'comment19_2': comment19_2,
            'exception19_2': exception19_2,
            'sa19_3': sa19_3,
            'comment19_3': comment19_3,
            'exception19_3': exception19_3,
        }
        context = {
            'input_data': input_data,
        }
        return render(request, 'self_assessment_scoring.html', context)
    return render(request, 'self_assessment_13.html')


@login_required
def self_assessment_scoring(request):
    if request.method == 'POST':
        recommendations = request.POST.get("recommendations")
        comment1 = request.POST.get("comment1")
        exception1 = request.POST.get("exception1")
        general = request.POST.get("general")
        comment2 = request.POST.get("comment2")
        exception2 = request.POST.get("exception2")
        sources_and_types = request.POST.get("sources_and_types")
        comment3 = request.POST.get("comment3")
        exception3 = request.POST.get("exception3")
        systematic = request.POST.get("systematic")
        comment4 = request.POST.get("comment4")
        exception4 = request.POST.get("exception4")
        universe = request.POST.get("universe")
        comment5 = request.POST.get("comment5")
        exception5 = request.POST.get("exception5")
        screening = request.POST.get("screening")
        comment6 = request.POST.get("comment6")
        exception6 = request.POST.get("exception6")
        characteristics = request.POST.get("characteristics")
        comment7 = request.POST.get("comment7")
        exception7 = request.POST.get("exception7")
        targets = request.POST.get("targets")
        comment8 = request.POST.get("comment8")
        exception8 = request.POST.get("exception8")
        stewardship_activities = request.POST.get("stewardship_activities")
        comment9 = request.POST.get("comment9")
        exception9 = request.POST.get("exception9")
        social_impact = request.POST.get("social_impact")
        comment10 = request.POST.get("comment10")
        exception10 = request.POST.get("exception10")
        organisational_requirements = request.POST.get("organisational_requirements")
        comment11 = request.POST.get("comment11")
        exception11 = request.POST.get("exception11")
        risk_management = request.POST.get("risk_management")
        comment12 = request.POST.get("comment12")
        exception12 = request.POST.get("exception12")
        conflicts_of_interest = request.POST.get("conflicts_of_interest")
        comment13 = request.POST.get("comment13")
        exception13 = request.POST.get("exception13")
        product_governance = request.POST.get("product_governance")
        comment14 = request.POST.get("comment14")
        exception14 = request.POST.get("exception14")
        cost = request.POST.get("cost")
        comment15 = request.POST.get("comment15")
        exception15 = request.POST.get("exception15")
        provided = request.POST.get("provided")
        comment16 = request.POST.get("comment16")
        exception16 = request.POST.get("exception16")
        gathered = request.POST.get("gathered")
        comment17 = request.POST.get("comment17")
        exception17 = request.POST.get("exception17")
        sustainability = request.POST.get("sustainability")
        comment18 = request.POST.get("comment18")
        exception18 = request.POST.get("exception18")

        input_data = {
            'recommendations': recommendations,
            'comment1': comment1,
            'exception1': exception1,
            'general': general,
            'comment2': comment2,
            'exception2': exception2,
            'sources_and_types': sources_and_types,
            'comment3': comment3,
            'exception3': exception3,
            'systematic': systematic,
            'comment4': comment4,
            'exception4': exception4,
            'universe': universe,
            'comment5': comment5,
            'exception5': exception5,
            'screening': screening,
            'comment6': comment6,
            'exception6': exception6,
            'characteristics': characteristics,
            'comment7': comment7,
            'exception7': exception7,
            'targets': targets,
            'comment8': comment8,
            'exception8': exception8,
            'stewardship_activities': stewardship_activities,
            'comment9': comment9,
            'exception9': exception9,
            'social_impact': social_impact,
            'comment10': comment10,
            'exception10': exception10,
            'organisational_requirements': organisational_requirements,
            'comment11': comment11,
            'exception11': exception11,
            'risk_management': risk_management,
            'comment12': comment12,
            'exception12': exception12,
            'conflicts_of_interest': conflicts_of_interest,
            'comment13': comment13,
            'exception13': exception13,
            'product_governance': product_governance,
            'comment14': comment14,
            'exception14': exception14,
            'cost': cost,
            'comment15': comment15,
            'exception15': exception15,
            'provided': provided,
            'comment16': comment16,
            'exception16': exception16,
            'gathered': gathered,
            'comment17': comment17,
            'exception17': exception17,
            'sustainability': sustainability,
            'comment18': comment18,
            'exception18': exception18,
        }

        table = selfCalculations(input_data, request)
        total_score = table.f1_all_score()[0]
        na_count = table.f1_all_na()
        avg_score = round(total_score/(18 - na_count))

        context = {
            'input_data': input_data,
            'f1': recommendations,
            # 'score1': table.f1_all(),
            'comment1': comment1,
            'f2': general,
            'comment2': comment2,
            'f3': sources_and_types,
            'comment3': comment3,
            'f4': systematic,
            'comment4': comment4,
            'f5': universe,
            'comment5': comment5,
            'f6': screening,
            'comment6': comment6,
            'f7': characteristics,
            'comment7': comment7,
            'f8': targets,
            'comment8': comment8,
            'f9': stewardship_activities,
            'comment9': comment9,
            'f10': social_impact,
            'comment10': comment10,
            'f11': organisational_requirements,
            'comment11': comment11,
            'f12': risk_management,
            'comment12': comment12,
            'f13': conflicts_of_interest,
            'comment13': comment13,
            'f14': product_governance,
            'comment14': comment14,
            'f15': cost,
            'comment15': comment15,
            'f16': provided,
            'comment16': comment16,
            'f17': gathered,
            'comment17': comment17,
            'f18': sustainability,
            'comment18': comment18,
            'total_score': total_score,
            'avg_score': avg_score,
        }
        return render(request, 'final_scoring.html', context)
    return render(request, 'self_assessment_scoring.html')


class selfCalculations:
    def __init__(self, input_data, request):
        self.input_data = input_data
        self.score = 0
        self.value = 0
        self.na_count = 0
        self.request = request

    # Self assessment Final Scoring calculation
    def f1_1(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('recommendations') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('recommendations') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('recommendations') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('recommendations') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('recommendations') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('recommendations') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_2(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('general') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('general') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('general') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('general') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('general') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('general') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_3(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('sources_and_types') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('sources_and_types') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('sources_and_types') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('sources_and_types') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('sources_and_types') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('sources_and_types') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_4(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('systematic') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('systematic') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('systematic') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('systematic') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('systematic') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('systematic') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_5(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('universe') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('universe') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('universe') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('universe') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('universe') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('universe') == 'NA':
            self.score = 0
            self.value = 0
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_6(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('screening') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('screening') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('screening') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('screening') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('screening') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('screening') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_7(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('characteristics') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('characteristics') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('characteristics') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('characteristics') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('characteristics') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('characteristics') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_8(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('targets') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('targets') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('targets') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('targets') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('targets') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('targets') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_9(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('stewardship_activities') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('stewardship_activities') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('stewardship_activities') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('stewardship_activities') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('stewardship_activities') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('stewardship_activities') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_10(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('social_impact') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('social_impact') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('social_impact') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('social_impact') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('social_impact') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('social_impact') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_11(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('organisational_requirements') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('organisational_requirements') == '1':
            self.score = 1
            self.value = 0
        elif self.input_data.get('organisational_requirements') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('organisational_requirements') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('organisational_requirements') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('organisational_requirements') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_12(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('risk_management') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('risk_management') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('risk_management') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('risk_management') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('risk_management') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('risk_management') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_13(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('conflicts_of_interest') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('conflicts_of_interest') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('conflicts_of_interest') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('conflicts_of_interest') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('conflicts_of_interest') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('conflicts_of_interest') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_14(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('product_governance') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('product_governance') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('product_governance') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('product_governance') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('product_governance') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('product_governance') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_15(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('cost') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('cost') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('cost') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('cost') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('cost') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('cost') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_16(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('provided') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('provided') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('provided') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('provided') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('provided') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('provided') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_17(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('gathered') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('gathered') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('gathered') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('gathered') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('gathered') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('gathered') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_18(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('sustainability') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('sustainability') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('sustainability') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('sustainability') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('sustainability') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('sustainability') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
        return [self.score, self.value, self.na_count]

    def f1_all_na(self):
        f1_18 = self.f1_18()[2]
        return f1_18

    def f1_all_score(self):
        f1_1_score = self.f1_1()[0]
        f1_2_score = self.f1_2()[0]
        f1_3_score = self.f1_3()[0]
        f1_4_score = self.f1_4()[0]
        f1_5_score = self.f1_5()[0]
        f1_6_score = self.f1_6()[0]
        f1_7_score = self.f1_7()[0]
        f1_8_score = self.f1_8()[0]
        f1_9_score = self.f1_9()[0]
        f1_10_score = self.f1_10()[0]
        f1_11_score = self.f1_11()[0]
        f1_12_score = self.f1_12()[0]
        f1_13_score = self.f1_13()[0]
        f1_14_score = self.f1_14()[0]
        f1_15_score = self.f1_15()[0]
        f1_16_score = self.f1_16()[0]
        f1_17_score = self.f1_17()[0]
        f1_18_score = self.f1_18()[0]

        total_score = f1_1_score + f1_2_score + f1_3_score + f1_4_score + f1_5_score + f1_6_score + f1_7_score + f1_8_score + f1_9_score \
                      + f1_10_score + f1_11_score + f1_12_score + f1_13_score + f1_14_score + f1_15_score + f1_16_score + f1_17_score + f1_18_score
        na_count = self.f1_all_na()
        return [total_score, na_count]


@login_required
def environment1_1(request):
    if request.method == 'POST':
        set_of_policies = request.POST.get("set_of_policies")
        comment1_1 = request.POST.get("comment1_1")
        exception1_1 = request.POST.get("exception1_1")
        keep_records = request.POST.get("keep_records")
        comment1_2 = request.POST.get("comment1_2")
        exception1_2 = request.POST.get("exception1_2")
        evaluation_exercise = request.POST.get("evaluation_exercise")
        comment1_3 = request.POST.get("comment1_3")
        exception1_3 = request.POST.get("exception1_3")
        reduce_consumption = request.POST.get("reduce_consumption")
        comment1_4 = request.POST.get("comment1_4")
        exception1_4 = request.POST.get("exception1_4")
        Investee_renewable_sources = request.POST.get("Investee_renewable_sources")
        comment1_5 = request.POST.get("comment1_5")
        exception1_5 = request.POST.get("exception1_5")

        input_data = {
            'set_of_policies': set_of_policies,
            'comment1_1': comment1_1,
            'exception1_1': exception1_1,
            'keep_records': keep_records,
            'comment1_2': comment1_2,
            'exception1_2': exception1_2,
            'evaluation_exercise': evaluation_exercise,
            'comment1_3': comment1_3,
            'exception1_3': exception1_3,
            'reduce_consumption': reduce_consumption,
            'comment1_4': comment1_4,
            'exception1_4': exception1_4,
            'Investee_renewable_sources': Investee_renewable_sources,
            'comment1_5': comment1_5,
            'exception1_5': exception1_5,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'environment1_2.html', context)
    return render(request, 'environment1_1.html')


def environment1_2(request):
    if request.method == 'POST':
        set_of_strategies = request.POST.get("set_of_strategies")
        comment2_1 = request.POST.get("comment2_1")
        exception2_1 = request.POST.get("exception2_1")
        handling_raw_materials = request.POST.get("handling_raw_materials")
        comment2_2 = request.POST.get("comment2_2")
        exception2_2 = request.POST.get("exception2_2")
        dependence_raw_materials = request.POST.get("dependence_raw_materials")
        comment2_3 = request.POST.get("comment2_3")
        exception2_3 = request.POST.get("exception2_3")
        sourcing_raw_materials = request.POST.get("sourcing_raw_materials")
        comment2_4 = request.POST.get("comment2_4")
        exception2_4 = request.POST.get("exception2_4")
        use_recycled_materials = request.POST.get("use_recycled_materials")
        comment2_5 = request.POST.get("comment2_5")
        exception2_5 = request.POST.get("exception2_5")
        recyclable_packaging = request.POST.get("recyclable_packaging")
        comment2_6 = request.POST.get("comment2_6")
        exception2_6 = request.POST.get("exception2_6")

        input_data = {
            'set_of_strategies': set_of_strategies,
            'comment2_1': comment2_1,
            'exception2_1': exception2_1,
            'handling_raw_materials': handling_raw_materials,
            'comment2_2': comment2_2,
            'exception2_2': exception2_2,
            'dependence_raw_materials': dependence_raw_materials,
            'comment2_3': comment2_3,
            'exception2_3': exception2_3,
            'sourcing_raw_materials': sourcing_raw_materials,
            'comment2_4': comment2_4,
            'exception2_4': exception2_4,
            'use_recycled_materials': use_recycled_materials,
            'comment2_5': comment2_5,
            'exception2_5': exception2_5,
            'recyclable_packaging': recyclable_packaging,
            'comment2_6': comment2_6,
            'exception2_6': exception2_6,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'environment1_3.html', context)
    return render(request, 'environment1_2.html')


@login_required
def environment1_3(request):
    if request.method == 'POST':
        set_of_policies_water = request.POST.get("set_of_policies_water")
        comment3_1 = request.POST.get("comment3_1")
        exception3_1 = request.POST.get("exception3_1")
        consume_water = request.POST.get("consume_water")
        comment3_2 = request.POST.get("comment3_2")
        exception3_2 = request.POST.get("exception3_2")
        face_risk_water_scarcity = request.POST.get("face_risk_water_scarcity")
        comment3_3 = request.POST.get("comment3_3")
        exception3_3 = request.POST.get("exception3_3")
        recycling_water_used_by_organisation = request.POST.get("recycling_water_used_by_organisation")
        comment3_4 = request.POST.get("comment3_4")
        exception3_4 = request.POST.get("exception3_4")
        mention_amount_of_water_recycle = request.POST.get("mention_amount_of_water_recycle")
        comment3_5 = request.POST.get("comment3_5")
        exception3_5 = request.POST.get("exception3_5")

        input_data = {
            'set_of_policies_water': set_of_policies_water,
            'comment3_1': comment3_1,
            'exception3_1': exception3_1,
            'consume_water': consume_water,
            'comment3_2': comment3_2,
            'exception3_2': exception3_2,
            'face_risk_water_scarcity': face_risk_water_scarcity,
            'comment3_3': comment3_3,
            'exception3_3': exception3_3,
            'recycling_water_used_by_organisation': recycling_water_used_by_organisation,
            'comment3_4': comment3_4,
            'exception3_4': exception3_4,
            'mention_amount_of_water_recycle': mention_amount_of_water_recycle,
            'comment3_5': comment3_5,
            'exception3_5': exception3_5,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'environment1_4.html', context)
    return render(request, 'environment1_3.html')


@login_required
def environment1_4(request):
    if request.method == 'POST':
        land_clearance = request.POST.get("land_clearance")
        comment4_1 = request.POST.get("comment4_1")
        exception4_1 = request.POST.get("exception4_1")
        set_policies_land_clearance = request.POST.get("set_policies_land_clearance")
        comment4_2 = request.POST.get("comment4_2")
        exception4_2 = request.POST.get("exception4_2")
        result_land_clearance = request.POST.get("result_land_clearance")
        comment4_3 = request.POST.get("comment4_3")
        exception4_3 = request.POST.get("exception4_3")
        impact_environment = request.POST.get("impact_environment")
        comment4_4 = request.POST.get("comment4_4")
        exception4_4 = request.POST.get("exception4_4")

        input_data = {
            'land_clearance': land_clearance,
            'comment4_1': comment4_1,
            'exception4_1': exception4_1,
            'set_policies_land_clearance': set_policies_land_clearance,
            'comment4_2': comment4_2,
            'exception4_2': exception4_2,
            'result_land_clearance': result_land_clearance,
            'comment4_3': comment4_3,
            'exception4_3': exception4_3,
            'impact_environment': impact_environment,
            'comment4_4': comment4_4,
            'exception4_4': exception4_4,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'environment1_5.html', context)
    return render(request, 'environment1_4.html')


@login_required
def environment1_5(request):
    if request.method == 'POST':
        set_policies_waste = request.POST.get("set_policies_waste")
        comment5_1 = request.POST.get("comment5_1")
        exception5_1 = request.POST.get("exception5_1")
        waste_generates = request.POST.get("waste_generates")
        comment5_2 = request.POST.get("comment5_2")
        exception5_2 = request.POST.get("exception5_2")
        waste_generated_toxic = request.POST.get("waste_generated_toxic")
        comment5_3 = request.POST.get("comment5_3")
        exception5_3 = request.POST.get("exception5_3")
        method_reduce_waste = request.POST.get("method_reduce_waste")
        comment5_4 = request.POST.get("comment5_4")
        exception5_4 = request.POST.get("exception5_4")
        total_waste_generated = request.POST.get("total_waste_generated")
        comment5_5 = request.POST.get("comment5_5")
        exception5_5 = request.POST.get("exception5_5")

        input_data = {
            'set_policies_waste': set_policies_waste,
            'comment5_1': comment5_1,
            'exception5_1': exception5_1,
            'waste_generates': waste_generates,
            'comment5_2': comment5_2,
            'exception5_2': exception5_2,
            'waste_generated_toxic': waste_generated_toxic,
            'comment5_3': comment5_3,
            'exception5_3': exception5_3,
            'method_reduce_waste': method_reduce_waste,
            'comment5_4': comment5_4,
            'exception5_4': exception5_4,
            'total_waste_generated': total_waste_generated,
            'comment5_5': comment5_5,
            'exception5_5': exception5_5,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'environment1_6.html', context)
    return render(request, 'environment1_5.html')


@login_required
def environment1_6(request):
    if request.method == 'POST':
        carbon_intensive = request.POST.get("carbon_intensive")
        comment6_1 = request.POST.get("comment6_1")
        exception6_1 = request.POST.get("exception6_1")
        set_policies_gas_emission = request.POST.get("set_policies_gas_emission")
        comment6_2 = request.POST.get("comment6_2")
        exception6_2 = request.POST.get("exception6_2")
        impact_environment_documented = request.POST.get("impact_environment_documented")
        comment6_3 = request.POST.get("comment6_3")
        exception6_3 = request.POST.get("exception6_3")
        direct_ghg_emissions = request.POST.get("direct_ghg_emissions")
        comment6_4 = request.POST.get("comment6_4")
        exception6_4 = request.POST.get("exception6_4")
        ghg_emissions = request.POST.get("ghg_emissions")
        comment6_5 = request.POST.get("comment6_5")
        exception6_5 = request.POST.get("exception6_5")
        indirect_ghg_emissions_scope3 = request.POST.get("indirect_ghg_emissions_scope3")
        comment6_6 = request.POST.get("comment6_6")
        exception6_6 = request.POST.get("exception6_6")
        indirect_ghg_emissions_scope4 = request.POST.get("indirect_ghg_emissions_scope4")
        comment6_7 = request.POST.get("comment6_7")
        exception6_7 = request.POST.get("exception6_7")
        air_quality = request.POST.get("air_quality")
        comment6_8 = request.POST.get("comment6_8")
        exception6_8 = request.POST.get("exception6_8")
        provide_detail_investment_technology = request.POST.get("provide_detail_investment_technology")
        comment6_9 = request.POST.get("comment6_9")
        exception6_9 = request.POST.get("exception6_9")

        input_data = {
            'carbon_intensive': carbon_intensive,
            'comment6_1': comment6_1,
            'exception6_1': exception6_1,
            'set_policies_gas_emission': set_policies_gas_emission,
            'comment6_2': comment6_2,
            'exception6_2': exception6_2,
            'impact_environment_documented': impact_environment_documented,
            'comment6_3': comment6_3,
            'exception6_3': exception6_3,
            'direct_ghg_emissions': direct_ghg_emissions,
            'comment6_4': comment6_4,
            'exception6_4': exception6_4,
            'ghg_emissions': ghg_emissions,
            'comment6_5': comment6_5,
            'exception6_5': exception6_5,
            'indirect_ghg_emissions_scope3': indirect_ghg_emissions_scope3,
            'comment6_6': comment6_6,
            'exception6_6': exception6_6,
            'indirect_ghg_emissions_scope4': indirect_ghg_emissions_scope4,
            'comment6_7': comment6_7,
            'exception6_7': exception6_7,
            'air_quality': air_quality,
            'comment6_8': comment6_8,
            'exception6_8': exception6_8,
            'provide_detail_investment_technology': provide_detail_investment_technology,
            'comment6_9': comment6_9,
            'exception6_9': exception6_9,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'environment1_7.html', context)
    return render(request, 'environment1_6.html')


@login_required
def environment1_7(request):
    if request.method == 'POST':
        set_policies_biodiversity = request.POST.get("set_policies_biodiversity")
        comment7_1 = request.POST.get("comment7_1")
        exception7_1 = request.POST.get("exception7_1")
        operations_biodiversity = request.POST.get("operations_biodiversity")
        comment7_2 = request.POST.get("comment7_2")
        exception7_2 = request.POST.get("exception7_2")
        different_types_species = request.POST.get("different_types_species")
        comment7_3 = request.POST.get("comment7_3")
        exception7_3 = request.POST.get("exception7_3")
        control_biodiversity = request.POST.get("control_biodiversity")
        comment7_4 = request.POST.get("comment7_4")
        exception7_4 = request.POST.get("exception7_4")
        positive_biodiversity = request.POST.get("positive_biodiversity")
        comment7_5 = request.POST.get("comment7_5")
        exception7_5 = request.POST.get("exception7_5")

        input_data = {
            'set_policies_biodiversity': set_policies_biodiversity,
            'comment7_1': comment7_1,
            'exception7_1': exception7_1,
            'operations_biodiversity': operations_biodiversity,
            'comment7_2': comment7_2,
            'exception7_2': exception7_2,
            'different_types_species': different_types_species,
            'comment7_3': comment7_3,
            'exception7_3': exception7_3,
            'control_biodiversity': control_biodiversity,
            'comment7_4': comment7_4,
            'exception7_4': exception7_4,
            'positive_biodiversity': positive_biodiversity,
            'comment7_5': comment7_5,
            'exception7_5': exception7_5,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'environment1_8.html', context)
    return render(request, 'environment1_7.html')


@login_required
def environment1_8(request):
    if request.method == 'POST':
        set_policies_circular_economy = request.POST.get("set_policies_circular_economy")
        comment8_1 = request.POST.get("comment8_1")
        exception8_1 = request.POST.get("exception8_1")
        company_use_biodegradable_materials = request.POST.get("company_use_biodegradable_materials")
        comment8_2 = request.POST.get("comment8_2")
        exception8_2 = request.POST.get("exception8_2")
        company_recyclable = request.POST.get("company_recyclable")
        comment8_3 = request.POST.get("comment8_3")
        exception8_3 = request.POST.get("exception8_3")
        scarce_products = request.POST.get("scarce_products")
        comment8_4 = request.POST.get("comment8_4")
        exception8_4 = request.POST.get("exception8_4")
        packaging_process = request.POST.get("packaging_process")
        comment8_5 = request.POST.get("comment8_5")
        exception8_5 = request.POST.get("exception8_5")
        procuring_raw_materials = request.POST.get("procuring_raw_materials")
        comment8_6 = request.POST.get("comment8_6")
        exception8_6 = request.POST.get("exception8_6")

        input_data = {
            'set_policies_circular_economy': set_policies_circular_economy,
            'comment8_1': comment8_1,
            'exception8_1': exception8_1,
            'company_use_biodegradable_materials': company_use_biodegradable_materials,
            'comment8_2': comment8_2,
            'exception8_2': exception8_2,
            'company_recyclable': company_recyclable,
            'comment8_3': comment8_3,
            'exception8_3': exception8_3,
            'scarce_products': scarce_products,
            'comment8_4': comment8_4,
            'Exception8_4': exception8_4,
            'packaging_process': packaging_process,
            'comment8_5': comment8_5,
            'exception8_5': exception8_5,
            'procuring_raw_materials': procuring_raw_materials,
            'comment8_6': comment8_6,
            'exception8_6': exception8_6,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'environment1_9.html', context)
    return render(request, 'environment1_8.html')


@login_required
def environment1_9(request):
    if request.method == 'POST':
        local_laws_regulations = request.POST.get("local_laws_regulations")
        comment9_1 = request.POST.get("comment9_1")
        exception9_1 = request.POST.get("exception9_1")
        licenses_concerned_local_authorities = request.POST.get("licenses_concerned_local_authorities")
        comment9_2 = request.POST.get("comment9_2")
        exception9_2 = request.POST.get("exception9_2")
        principle_adverse_impacts = request.POST.get("principle_adverse_impacts")
        comment9_3 = request.POST.get("comment9_3")
        exception9_3 = request.POST.get("exception9_3")
        consequential_action = request.POST.get("consequential_action")
        comment9_4 = request.POST.get("comment9_4")
        exception9_4 = request.POST.get("exception9_4")
        non_compliance_environmental_laws = request.POST.get("non_compliance_environmental_laws")
        comment9_5 = request.POST.get("comment9_5")
        exception9_5 = request.POST.get("exception9_5")
        consequent_positive_environmental_impact = request.POST.get("consequent_positive_environmental_impact")
        comment9_6 = request.POST.get("comment9_6")
        exception9_6 = request.POST.get("exception9_6")
        monitor_risks_opportunities = request.POST.get("monitor_risks_opportunities")
        comment9_7 = request.POST.get("comment9_7")
        exception9_7 = request.POST.get("exception9_7")

        input_data = {
            'local_laws_regulations': local_laws_regulations,
            'comment9_1': comment9_1,
            'exception9_1': exception9_1,
            'licenses_concerned_local_authorities': licenses_concerned_local_authorities,
            'comment9_2': comment9_2,
            'exception9_2': exception9_2,
            'principle_adverse_impacts': principle_adverse_impacts,
            'comment9_3': comment9_3,
            'exception9_3': exception9_3,
            'consequential_action': consequential_action,
            'comment9_4': comment9_4,
            'exception9_4': exception9_4,
            'non_compliance_environmental_laws': non_compliance_environmental_laws,
            'comment9_5': comment9_5,
            'exception9_5': exception9_5,
            'consequent_positive_environmental_impact': consequent_positive_environmental_impact,
            'comment9_6': comment9_6,
            'exception9_6': exception9_6,
            'monitor_risks_opportunities': monitor_risks_opportunities,
            'comment9_7': comment9_7,
            'exception9_7': exception9_7,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'environment1_10.html', context)
    return render(request, 'environment1_9.html')


@login_required
def environment1_10(request):
    if request.method == 'POST':
        management_approach = request.POST.get("management_approach")
        comment10_1 = request.POST.get("comment10_1")
        exception10_1 = request.POST.get("exception10_1")
        environmental_best_practices = request.POST.get("environmental_best_practices")
        comment10_2 = request.POST.get("comment10_2")
        exception10_2 = request.POST.get("exception10_2")
        supply_chain = request.POST.get("supply_chain")
        comment10_3 = request.POST.get("comment10_3")
        exception10_3 = request.POST.get("exception10_3")

        input_data = {
            'management_approach': management_approach,
            'comment10_1': comment10_1,
            'exception10_1': exception10_1,
            'environmental_best_practices': environmental_best_practices,
            'comment10_2': comment10_2,
            'exception10_2': exception10_2,
            'supply_chain': supply_chain,
            'comment10_3': comment10_3,
            'exception10_3': exception10_3,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'environment_2.html', context)
    return render(request, 'environment1_10.html')


@login_required
def environment_2(request):
    if request.method == 'POST':
        energy_and_renewable_energy = request.POST.get("energy_and_renewable_energy")
        comment1 = request.POST.get("comment1")
        exception1 = request.POST.get("exception1")
        raw_materials = request.POST.get("raw_materials")
        comment2 = request.POST.get("comment2")
        exception2 = request.POST.get("exception2")
        water = request.POST.get("water")
        comment3 = request.POST.get("comment3")
        exception3 = request.POST.get("exception3")
        land = request.POST.get("land")
        comment4 = request.POST.get("comment4")
        exception4 = request.POST.get("exception4")
        waste = request.POST.get("waste")
        comment5 = request.POST.get("comment5")
        exception5 = request.POST.get("exception5")
        greenhouse_gas_emissions = request.POST.get("greenhouse_gas_emissions")
        comment6 = request.POST.get("comment6")
        exception6 = request.POST.get("exception6")
        biodiversity = request.POST.get("biodiversity")
        comment7 = request.POST.get("comment7")
        exception7 = request.POST.get("exception7")
        circular_economy = request.POST.get("circular_economy")
        comment8 = request.POST.get("comment8")
        exception8 = request.POST.get("exception8")
        environmental_compliance = request.POST.get("environmental_compliance")
        comment9 = request.POST.get("comment9")
        exception9 = request.POST.get("exception9")
        supply_chain_management= request.POST.get("supply_chain_management")
        comment10 = request.POST.get("comment10")
        exception10 = request.POST.get("exception10")

        input_data = {
            'energy_and_renewable_energy': energy_and_renewable_energy,
            'comment1': comment1,
            'exception1': exception1,
            'raw_materials': raw_materials,
            'comment2': comment2,
            'exception2': exception2,
            'water': water,
            'comment3': comment3,
            'exception3': exception3,
            'land': land,
            'comment4': comment4,
            'exception4': exception4,
            'waste': waste,
            'comment5': comment5,
            'exception5': exception5,
            'greenhouse_gas_emissions': greenhouse_gas_emissions,
            'comment6': comment6,
            'exception6': exception6,
            'biodiversity': biodiversity,
            'comment7': comment7,
            'exception7': exception7,
            'circular_economy':circular_economy,
            'comment8': comment8,
            'exception8': exception8,
            'environmental_compliance': environmental_compliance,
            'comment9': comment9,
            'exception9': exception9,
            'supply_chain_management': supply_chain_management,
            'comment10': comment10,
            'exception10': exception10,
        }

        table = environmentscore(input_data, request)
        total_score = table.f2_all_score()
        e_na_count = table.f2_all_na()
        avg_score = round(total_score/(10 - e_na_count))
        # avg_score = table.f2_all_score()[1]

        request.session['e2_1'] = energy_and_renewable_energy
        request.session['e2_2'] = raw_materials
        request.session['e2_3'] = water
        request.session['e2_4'] = land
        request.session['e2_5'] = waste
        request.session['e2_6'] = greenhouse_gas_emissions
        request.session['e2_7'] = biodiversity
        request.session['e2_8'] = circular_economy
        request.session['e2_9'] = environmental_compliance
        request.session['e2_10'] = supply_chain_management
        request.session['comment1'] = comment1
        request.session['comment2'] = comment2
        request.session['comment3'] = comment3
        request.session['comment4'] = comment4
        request.session['comment5'] = comment5
        request.session['comment6'] = comment6
        request.session['comment7'] = comment7
        request.session['comment8'] = comment8
        request.session['comment9'] = comment9
        request.session['comment10'] = comment10
        request.session['total_score'] = total_score
        request.session['avg_score'] = avg_score


        context = {
            'input_data': input_data,
            'e2_1': energy_and_renewable_energy,
            'comment1': comment1,
            'e2_2': raw_materials,
            'comment2': comment2,
            'e2_3': water,
            'comment3': comment3,
            'e2_4': land,
            'comment4': comment4,
            'e2_5': waste,
            'comment5': comment5,
            'e2_6': greenhouse_gas_emissions,
            'comment6': comment6,
            'e2_7': biodiversity,
            'comment7': comment7,
            'e2_8':circular_economy,
            'comment8': comment8,
            'e2_9': environmental_compliance,
            'comment9': comment9,
            'e2_10': supply_chain_management,
            'comment10': comment10,
            'total_score': total_score,
            'avg_score': avg_score,
        }
        return render(request, 'social_1.html', context)
    return render(request, 'environment_2.html')


class environmentscore:
    def __init__(self, input_data, request):
        self.input_data = input_data
        self.score = 0
        self.value = 0
        self.na_count = 0
        self.request = request

    # Self assessment Final Scoring calculation
    def f2_1(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('energy_and_renewable_energy') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('energy_and_renewable_energy') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('energy_and_renewable_energy') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('energy_and_renewable_energy') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('energy_and_renewable_energy') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('energy_and_renewable_energy') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
            print(self.na_count)
        return [self.score, self.value, self.na_count]

    def f2_2(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('raw_materials') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('raw_materials') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('raw_materials') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('raw_materials') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('raw_materials') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('raw_materials') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
            print(self.na_count)
        return [self.score, self.value, self.na_count]

    def f2_3(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('water') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('water') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('water') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('water') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('water') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('water') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
            print(self.na_count)
        return [self.score, self.value, self.na_count]

    def f2_4(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('land') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('land') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('land') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('land') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('land') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('land') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
            print(self.na_count)
        return [self.score, self.value, self.na_count]

    def f2_5(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('waste') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('waste') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('waste') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('waste') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('waste') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('waste') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
            print(self.na_count)
        return [self.score, self.value, self.na_count]

    def f2_6(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('greenhouse_gas_emissions') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('greenhouse_gas_emissions') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('greenhouse_gas_emissions') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('greenhouse_gas_emissions') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('greenhouse_gas_emissions') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('greenhouse_gas_emissions') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
            print(self.na_count)
        return [self.score, self.value, self.na_count]

    def f2_7(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('biodiversity') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('biodiversity') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('biodiversity') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('biodiversity') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('biodiversity') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('biodiversity') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
            print(self.na_count)
        return [self.score, self.value, self.na_count]

    def f2_8(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('circular_economy') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('circular_economy') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('circular_economy') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('circular_economy') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('circular_economy') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('circular_economy') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
            print(self.na_count)
        return [self.score, self.value, self.na_count]

    def f2_9(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('environmental_compliance') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('environmental_compliance') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('environmental_compliance') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('environmental_compliance') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('environmental_compliance') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('environmental_compliance') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
            print(self.na_count)
        return [self.score, self.value, self.na_count]

    def f2_10(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('supply_chain_management') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('supply_chain_management') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('supply_chain_management') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('supply_chain_management') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('supply_chain_management') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('supply_chain_management') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count += 1
            print(self.na_count)
        return [self.score, self.value, self.na_count]

    def f2_all_na(self):
        f2_10 = self.f2_10()[2]
        return f2_10

    def f2_all_score(self):
        f2_1_score = self.f2_1()[0]
        f2_2_score = self.f2_2()[0]
        f2_3_score = self.f2_3()[0]
        f2_4_score = self.f2_4()[0]
        f2_5_score = self.f2_5()[0]
        f2_6_score = self.f2_6()[0]
        f2_7_score = self.f2_7()[0]
        f2_8_score = self.f2_8()[0]
        f2_9_score = self.f2_9()[0]
        f2_10_score = self.f2_10()[0]

        total_score = f2_1_score + f2_2_score + f2_3_score + f2_4_score + f2_5_score + f2_6_score + f2_7_score + f2_8_score + f2_9_score + f2_10_score
        return total_score

@login_required
def env_score(request):
    if request.method == 'POST':
        energy_and_renewable_energy = request.POST.get("energy_and_renewable_energy")
        comment1 = request.POST.get("comment1")
        exception1 = request.POST.get("exception1")
        raw_materials = request.POST.get("raw_materials")
        comment2 = request.POST.get("comment2")
        exception2 = request.POST.get("exception2")
        water = request.POST.get("water")
        comment3 = request.POST.get("comment3")
        exception3 = request.POST.get("exception3")
        land = request.POST.get("land")
        comment4 = request.POST.get("comment4")
        exception4 = request.POST.get("exception4")
        waste = request.POST.get("waste")
        comment5 = request.POST.get("comment5")
        exception5 = request.POST.get("exception5")
        greenhouse_gas_emissions = request.POST.get("greenhouse_gas_emissions")
        comment6 = request.POST.get("comment6")
        exception6 = request.POST.get("exception6")
        biodiversity = request.POST.get("biodiversity")
        comment7 = request.POST.get("comment7")
        exception7 = request.POST.get("exception7")
        circular_economy = request.POST.get("circular_economy")
        comment8 = request.POST.get("comment8")
        exception8 = request.POST.get("exception8")
        environmental_compliance = request.POST.get("environmental_compliance")
        comment9 = request.POST.get("comment9")
        exception9 = request.POST.get("exception9")
        supply_chain_management= request.POST.get("supply_chain_management")
        comment10 = request.POST.get("comment10")
        exception10 = request.POST.get("exception10")

        input_data = {
            'energy_and_renewable_energy': energy_and_renewable_energy,
            'comment1': comment1,
            'exception1': exception1,
            'raw_materials': raw_materials,
            'comment2': comment2,
            'exception2': exception2,
            'water': water,
            'comment3': comment3,
            'exception3': exception3,
            'land': land,
            'comment4': comment4,
            'exception4': exception4,
            'waste': waste,
            'comment5': comment5,
            'exception5': exception5,
            'greenhouse_gas_emissions': greenhouse_gas_emissions,
            'comment6': comment6,
            'exception6': exception6,
            'biodiversity': biodiversity,
            'comment7': comment7,
            'exception7': exception7,
            'circular_economy':circular_economy,
            'comment8': comment8,
            'exception8': exception8,
            'environmental_compliance': environmental_compliance,
            'comment9': comment9,
            'exception9': exception9,
            'supply_chain_management': supply_chain_management,
            'comment10': comment10,
            'exception10': exception10,
        }

        table = environmentscore(input_data, request)
        total_score = table.f2_all_score()
        e_na_count = table.f2_all_na()
        avg_score = round(total_score/(10 - e_na_count))
        # avg_score = table.f2_all_score()[1]

        request.session['e2_1'] = energy_and_renewable_energy
        request.session['e2_2'] = raw_materials
        request.session['e2_3'] = water
        request.session['e2_4'] = land
        request.session['e2_5'] = waste
        request.session['e2_6'] = greenhouse_gas_emissions
        request.session['e2_7'] = biodiversity
        request.session['e2_8'] = circular_economy
        request.session['e2_9'] = environmental_compliance
        request.session['e2_10'] = supply_chain_management
        request.session['comment1'] = comment1
        request.session['comment2'] = comment2
        request.session['comment3'] = comment3
        request.session['comment4'] = comment4
        request.session['comment5'] = comment5
        request.session['comment6'] = comment6
        request.session['comment7'] = comment7
        request.session['comment8'] = comment8
        request.session['comment9'] = comment9
        request.session['comment10'] = comment10
        request.session['total_score'] = total_score
        request.session['avg_score'] = avg_score


        context = {
            'input_data': input_data,
            'e2_1': energy_and_renewable_energy,
            'comment1': comment1,
            'e2_2': raw_materials,
            'comment2': comment2,
            'e2_3': water,
            'comment3': comment3,
            'e2_4': land,
            'comment4': comment4,
            'e2_5': waste,
            'comment5': comment5,
            'e2_6': greenhouse_gas_emissions,
            'comment6': comment6,
            'e2_7': biodiversity,
            'comment7': comment7,
            'e2_8':circular_economy,
            'comment8': comment8,
            'e2_9': environmental_compliance,
            'comment9': comment9,
            'e2_10': supply_chain_management,
            'comment10': comment10,
            'total_score': total_score,
            'avg_score': avg_score,
        }
        return render(request, 'final_scoring_client.html', context)
    return render(request, 'env_score.html')



@login_required
def only_env_score(request):
    if request.method == 'POST':
        energy_and_renewable_energy = request.POST.get("energy_and_renewable_energy")
        comment1 = request.POST.get("comment1")
        exception1 = request.POST.get("exception1")
        raw_materials = request.POST.get("raw_materials")
        comment2 = request.POST.get("comment2")
        exception2 = request.POST.get("exception2")
        water = request.POST.get("water")
        comment3 = request.POST.get("comment3")
        exception3 = request.POST.get("exception3")
        land = request.POST.get("land")
        comment4 = request.POST.get("comment4")
        exception4 = request.POST.get("exception4")
        waste = request.POST.get("waste")
        comment5 = request.POST.get("comment5")
        exception5 = request.POST.get("exception5")
        greenhouse_gas_emissions = request.POST.get("greenhouse_gas_emissions")
        comment6 = request.POST.get("comment6")
        exception6 = request.POST.get("exception6")
        biodiversity = request.POST.get("biodiversity")
        comment7 = request.POST.get("comment7")
        exception7 = request.POST.get("exception7")
        circular_economy = request.POST.get("circular_economy")
        comment8 = request.POST.get("comment8")
        exception8 = request.POST.get("exception8")
        environmental_compliance = request.POST.get("environmental_compliance")
        comment9 = request.POST.get("comment9")
        exception9 = request.POST.get("exception9")
        supply_chain_management= request.POST.get("supply_chain_management")
        comment10 = request.POST.get("comment10")
        exception10 = request.POST.get("exception10")

        input_data = {
            'energy_and_renewable_energy': energy_and_renewable_energy,
            'comment1': comment1,
            'exception1': exception1,
            'raw_materials': raw_materials,
            'comment2': comment2,
            'exception2': exception2,
            'water': water,
            'comment3': comment3,
            'exception3': exception3,
            'land': land,
            'comment4': comment4,
            'exception4': exception4,
            'waste': waste,
            'comment5': comment5,
            'exception5': exception5,
            'greenhouse_gas_emissions': greenhouse_gas_emissions,
            'comment6': comment6,
            'exception6': exception6,
            'biodiversity': biodiversity,
            'comment7': comment7,
            'exception7': exception7,
            'circular_economy':circular_economy,
            'comment8': comment8,
            'exception8': exception8,
            'environmental_compliance': environmental_compliance,
            'comment9': comment9,
            'exception9': exception9,
            'supply_chain_management': supply_chain_management,
            'comment10': comment10,
            'exception10': exception10,
        }

        table = environmentscore(input_data, request)
        total_score = table.f2_all_score()
        e_na_count = table.f2_all_na()
        avg_score = round(total_score/(10 - e_na_count))
        # avg_score = table.f2_all_score()[1]

        request.session['e2_1'] = energy_and_renewable_energy
        request.session['e2_2'] = raw_materials
        request.session['e2_3'] = water
        request.session['e2_4'] = land
        request.session['e2_5'] = waste
        request.session['e2_6'] = greenhouse_gas_emissions
        request.session['e2_7'] = biodiversity
        request.session['e2_8'] = circular_economy
        request.session['e2_9'] = environmental_compliance
        request.session['e2_10'] = supply_chain_management
        request.session['comment1'] = comment1
        request.session['comment2'] = comment2
        request.session['comment3'] = comment3
        request.session['comment4'] = comment4
        request.session['comment5'] = comment5
        request.session['comment6'] = comment6
        request.session['comment7'] = comment7
        request.session['comment8'] = comment8
        request.session['comment9'] = comment9
        request.session['comment10'] = comment10
        request.session['total_score'] = total_score
        request.session['avg_score'] = avg_score

        context = {
            'input_data': input_data,
            'e2_1': energy_and_renewable_energy,
            'comment1': comment1,
            'e2_2': raw_materials,
            'comment2': comment2,
            'e2_3': water,
            'comment3': comment3,
            'e2_4': land,
            'comment4': comment4,
            'e2_5': waste,
            'comment5': comment5,
            'e2_6': greenhouse_gas_emissions,
            'comment6': comment6,
            'e2_7': biodiversity,
            'comment7': comment7,
            'e2_8':circular_economy,
            'comment8': comment8,
            'e2_9': environmental_compliance,
            'comment9': comment9,
            'e2_10': supply_chain_management,
            'comment10': comment10,
            'total_score': total_score,
            'avg_score': avg_score,
        }
        return render(request, 'social_1_scoring.html', context)
    return render(request, 'only_env_score.html')


@login_required
def env_gov_score(request):
    if request.method == 'POST':
        energy_and_renewable_energy = request.POST.get("energy_and_renewable_energy")
        comment1 = request.POST.get("comment1")
        exception1 = request.POST.get("exception1")
        raw_materials = request.POST.get("raw_materials")
        comment2 = request.POST.get("comment2")
        exception2 = request.POST.get("exception2")
        water = request.POST.get("water")
        comment3 = request.POST.get("comment3")
        exception3 = request.POST.get("exception3")
        land = request.POST.get("land")
        comment4 = request.POST.get("comment4")
        exception4 = request.POST.get("exception4")
        waste = request.POST.get("waste")
        comment5 = request.POST.get("comment5")
        exception5 = request.POST.get("exception5")
        greenhouse_gas_emissions = request.POST.get("greenhouse_gas_emissions")
        comment6 = request.POST.get("comment6")
        exception6 = request.POST.get("exception6")
        biodiversity = request.POST.get("biodiversity")
        comment7 = request.POST.get("comment7")
        exception7 = request.POST.get("exception7")
        circular_economy = request.POST.get("circular_economy")
        comment8 = request.POST.get("comment8")
        exception8 = request.POST.get("exception8")
        environmental_compliance = request.POST.get("environmental_compliance")
        comment9 = request.POST.get("comment9")
        exception9 = request.POST.get("exception9")
        supply_chain_management= request.POST.get("supply_chain_management")
        comment10 = request.POST.get("comment10")
        exception10 = request.POST.get("exception10")

        input_data = {
            'energy_and_renewable_energy': energy_and_renewable_energy,
            'comment1': comment1,
            'exception1': exception1,
            'raw_materials': raw_materials,
            'comment2': comment2,
            'exception2': exception2,
            'water': water,
            'comment3': comment3,
            'exception3': exception3,
            'land': land,
            'comment4': comment4,
            'exception4': exception4,
            'waste': waste,
            'comment5': comment5,
            'exception5': exception5,
            'greenhouse_gas_emissions': greenhouse_gas_emissions,
            'comment6': comment6,
            'exception6': exception6,
            'biodiversity': biodiversity,
            'comment7': comment7,
            'exception7': exception7,
            'circular_economy':circular_economy,
            'comment8': comment8,
            'exception8': exception8,
            'environmental_compliance': environmental_compliance,
            'comment9': comment9,
            'exception9': exception9,
            'supply_chain_management': supply_chain_management,
            'comment10': comment10,
            'exception10': exception10,
        }

        table = environmentscore(input_data, request)
        total_score = table.f2_all_score()
        e_na_count = table.f2_all_na()
        avg_score = round(total_score/(10 - e_na_count))
        # avg_score = table.f2_all_score()[1]

        request.session['e2_1'] = energy_and_renewable_energy
        request.session['e2_2'] = raw_materials
        request.session['e2_3'] = water
        request.session['e2_4'] = land
        request.session['e2_5'] = waste
        request.session['e2_6'] = greenhouse_gas_emissions
        request.session['e2_7'] = biodiversity
        request.session['e2_8'] = circular_economy
        request.session['e2_9'] = environmental_compliance
        request.session['e2_10'] = supply_chain_management
        request.session['comment1'] = comment1
        request.session['comment2'] = comment2
        request.session['comment3'] = comment3
        request.session['comment4'] = comment4
        request.session['comment5'] = comment5
        request.session['comment6'] = comment6
        request.session['comment7'] = comment7
        request.session['comment8'] = comment8
        request.session['comment9'] = comment9
        request.session['comment10'] = comment10
        request.session['total_score'] = total_score
        request.session['avg_score'] = avg_score

        context = {
            'input_data': input_data,
            'e2_1': energy_and_renewable_energy,
            'comment1': comment1,
            'e2_2': raw_materials,
            'comment2': comment2,
            'e2_3': water,
            'comment3': comment3,
            'e2_4': land,
            'comment4': comment4,
            'e2_5': waste,
            'comment5': comment5,
            'e2_6': greenhouse_gas_emissions,
            'comment6': comment6,
            'e2_7': biodiversity,
            'comment7': comment7,
            'e2_8':circular_economy,
            'comment8': comment8,
            'e2_9': environmental_compliance,
            'comment9': comment9,
            'e2_10': supply_chain_management,
            'comment10': comment10,
            'total_score': total_score,
            'avg_score': avg_score,
        }
        return render(request, 'only_governance.html', context)
    return render(request, 'env_gov_score.html')

@login_required
def social_1(request):
    if request.method == 'POST':
        f1_1 = request.POST.get("f1_1")
        comment1_1 = request.POST.get("comment1_1")
        exception1_1 = request.POST.get("exception1_1")
        f1_2 = request.POST.get("f1_2")
        comment1_2 = request.POST.get("comment1_2")
        exception1_2 = request.POST.get("exception1_2")
        f1_3 = request.POST.get("f1_3")
        comment1_3 = request.POST.get("comment1_3")
        exception1_3 = request.POST.get("exception1_3")
        f1_4 = request.POST.get("f1_4")
        comment1_4 = request.POST.get("comment1_4")
        exception1_4 = request.POST.get("exception1_4")
        f1_5 = request.POST.get("f1_5")
        comment1_5 = request.POST.get("comment1_5")
        exception1_5 = request.POST.get("exception1_5")
        f2_1 = request.POST.get("f2_1")
        comment2_1 = request.POST.get("comment2_1")
        exception2_1 = request.POST.get("exception2_1")
        f2_2 = request.POST.get("f2_2")
        comment2_2 = request.POST.get("comment2_2")
        exception2_2 = request.POST.get("exception2_2")
        f2_3 = request.POST.get("f2_3")
        comment2_3 = request.POST.get("comment2_3")
        exception2_3 = request.POST.get("exception2_3")
        f2_4 = request.POST.get("f2_4")
        comment2_4 = request.POST.get("comment2_4")
        exception2_4 = request.POST.get("exception2_4")
        f2_5 = request.POST.get("f2_5")
        comment2_5 = request.POST.get("comment2_5")
        exception2_5 = request.POST.get("exception2_5")
        f2_6 = request.POST.get("f2_6")
        comment2_6 = request.POST.get("comment2_6")
        exception2_6 = request.POST.get("exception2_6")
        f3_1 = request.POST.get("f3_1")
        comment3_1 = request.POST.get("comment3_1")
        exception3_1 = request.POST.get("exception3_1")
        f3_2 = request.POST.get("f3_2")
        comment3_2 = request.POST.get("comment3_2")
        exception3_2 = request.POST.get("exception3_2")
        f3_3 = request.POST.get("f3_3")
        comment3_3 = request.POST.get("comment3_3")
        exception3_3 = request.POST.get("exception3_3")
        f3_4 = request.POST.get("f3_4")
        comment3_4 = request.POST.get("comment3_4")
        exception3_4 = request.POST.get("exception3_4")
        f3_5 = request.POST.get("f3_5")
        comment3_5 = request.POST.get("comment3_5")
        exception3_5 = request.POST.get("exception3_5")
        f4_1 = request.POST.get("f4_1")
        comment4_1 = request.POST.get("comment4_1")
        exception4_1 = request.POST.get("exception4_1")
        f4_2 = request.POST.get("f4_2")
        comment4_2 = request.POST.get("comment4_2")
        exception4_2 = request.POST.get("exception4_2")
        f4_3 = request.POST.get("f4_3")
        comment4_3 = request.POST.get("comment4_3")
        exception4_3 = request.POST.get("exception4_3")
        f4_4 = request.POST.get("f4_4")
        comment4_4 = request.POST.get("comment4_4")
        exception4_4 = request.POST.get("exception4_4")
        f5_1 = request.POST.get("f5_1")
        comment5_1 = request.POST.get("comment5_1")
        exception5_1 = request.POST.get("exception5_1")
        f5_2 = request.POST.get("f5_2")
        comment5_2 = request.POST.get("comment5_2")
        exception5_2 = request.POST.get("exception5_2")
        f5_3 = request.POST.get("f5_3")
        comment5_3 = request.POST.get("comment5_3")
        exception5_3 = request.POST.get("exception5_3")
        f5_4 = request.POST.get("f5_4")
        comment5_4 = request.POST.get("comment5_4")
        exception5_4 = request.POST.get("exception5_4")
        f5_5 = request.POST.get("f5_5")
        comment5_5 = request.POST.get("comment5_5")
        exception5_5 = request.POST.get("exception5_5")
        f5_6 = request.POST.get("f5_6")
        comment5_6 = request.POST.get("comment5_6")
        exception5_6 = request.POST.get("exception5_6")
        f6_1 = request.POST.get("f6_1")
        comment6_1 = request.POST.get("comment6_1")
        exception6_1 = request.POST.get("exception6_1")
        f6_2 = request.POST.get("f6_2")
        comment6_2 = request.POST.get("comment6_2")
        exception6_2 = request.POST.get("exception6_2")
        f6_3 = request.POST.get("f6_3")
        comment6_3 = request.POST.get("comment6_3")
        exception6_3 = request.POST.get("exception6_3")
        f6_4 = request.POST.get("f6_4")
        comment6_4 = request.POST.get("comment6_4")
        exception6_4 = request.POST.get("exception6_4")
        f6_5 = request.POST.get("f6_5")
        comment6_5 = request.POST.get("comment6_5")
        exception6_5 = request.POST.get("exception6_5")
        f6_6 = request.POST.get("f6_6")
        comment6_6 = request.POST.get("comment6_6")
        exception6_6 = request.POST.get("exception6_6")
        f6_7 = request.POST.get("f6_7")
        comment6_7 = request.POST.get("comment6_7")
        exception6_7 = request.POST.get("exception6_7")
        f6_8 = request.POST.get("f6_8")
        comment6_8 = request.POST.get("comment6_8")
        exception6_8 = request.POST.get("exception6_8")
        f6_9 = request.POST.get("f6_9")
        comment6_9 = request.POST.get("comment6_9")
        exception6_9 = request.POST.get("exception6_9")
        f7_1 = request.POST.get("f7_1")
        comment7_1 = request.POST.get("comment7_1")
        exception7_1 = request.POST.get("exception7_1")
        f7_2 = request.POST.get("f7_2")
        comment7_2 = request.POST.get("comment7_2")
        exception7_2 = request.POST.get("exception7_2")
        f7_3 = request.POST.get("f7_3")
        comment7_3 = request.POST.get("comment7_3")
        exception7_3 = request.POST.get("exception7_3")
        f7_4 = request.POST.get("f7_4")
        comment7_4 = request.POST.get("comment7_4")
        exception7_4 = request.POST.get("exception7_4")
        f7_5 = request.POST.get("f7_5")
        comment7_5 = request.POST.get("comment7_5")
        exception7_5 = request.POST.get("exception7_5")
        f8_1 = request.POST.get("f8_1")
        comment8_1 = request.POST.get("comment8_1")
        exception8_1 = request.POST.get("exception8_1")
        f8_2 = request.POST.get("f8_2")
        comment8_2 = request.POST.get("comment8_1")
        exception8_2 = request.POST.get("exception8_2")
        f8_3 = request.POST.get("f8_3")
        comment8_3 = request.POST.get("comment8_3")
        exception8_3 = request.POST.get("exception8_3")
        f8_4 = request.POST.get("f8_4")
        comment8_4 = request.POST.get("comment8_4")
        exception8_4 = request.POST.get("exception8_4")
        f8_5 = request.POST.get("f8_5")
        comment8_5 = request.POST.get("comment8_5")
        exception8_5 = request.POST.get("exception8_5")
        f8_6 = request.POST.get("f8_6")
        comment8_6 = request.POST.get("comment8_6")
        exception8_6 = request.POST.get("exception8_6")
        f9_1 = request.POST.get("f9_1")
        comment9_1= request.POST.get("comment9_1")
        exception9_1 = request.POST.get("exception9_1")
        f9_2 = request.POST.get("f9_2")
        comment9_2 = request.POST.get("comment9_2")
        exception9_2 = request.POST.get("exception9_2")
        f9_3 = request.POST.get("f9_3")
        comment9_3 = request.POST.get("comment9_3")
        exception9_3 = request.POST.get("exception9_3")
        f9_4 = request.POST.get("f9_4")
        comment9_4 = request.POST.get("comment9_4")
        exception9_4 = request.POST.get("exception9_4")
        f9_5 = request.POST.get("f9_5")
        comment9_5 = request.POST.get("comment9_5")
        exception9_5 = request.POST.get("exception9_5")
        f9_6 = request.POST.get("f9_6")
        comment9_6= request.POST.get("comment9_6")
        exception9_6 = request.POST.get("exception9_6")
        f9_7 = request.POST.get("f9_7")
        comment9_7 = request.POST.get("comment9_7")
        exception9_7 = request.POST.get("exception9_7")
        f10_1 = request.POST.get("f10_1")
        comment10_1 = request.POST.get("comment10_1")
        exception10_1 = request.POST.get("exception10_1")
        f10_2 = request.POST.get("f10_2")
        comment10_2 = request.POST.get("comment10_2")
        exception10_2 = request.POST.get("exception10_2")
        f10_3 = request.POST.get("f10_3")
        comment10_3 = request.POST.get("comment10_3")
        exception10_3 = request.POST.get("exception10_3")

        input_data = {
            'f1_1': f1_1,
            'comment1_1': comment1_1,
            'exception1_1': exception1_1,
            'f1_2': f1_2,
            'comment1_2': comment1_2,
            'exception1_2': exception1_2,
            'f1_3': f1_3,
            'comment1_3': comment1_3,
            'exception1_3': exception1_3,
            'f1_4': f1_4,
            'comment1_4': comment1_4,
            'exception1_4': exception1_4,
            'f1_5': f1_5,
            'comment1_5': comment1_5,
            'exception1_5': exception1_5,
            'f2_1': f2_1,
            'comment2_1': comment2_1,
            'exception2_1': exception2_1,
            'f2_2': f2_2,
            'comment2_2': comment2_2,
            'exception2_2': exception2_2,
            'f2_3': f2_3,
            'comment2_3': comment2_3,
            'exception2_3': exception2_3,
            'f2_4': f2_4,
            'comment2_4': comment2_4,
            'exception2_4': exception2_4,
            'f2_5': f2_5,
            'comment2_5': comment2_5,
            'exception2_5': exception2_5,
            'f2_6': f2_6,
            'comment2_6': comment2_6,
            'exception2_6': exception2_6,
            'f3_1': f3_1,
            'comment3_1': comment3_1,
            'exception3_1': exception3_1,
            'f3_2': f3_2,
            'comment3_2': comment3_2,
            'exception3_2': exception3_2,
            'f3_3': f3_3,
            'comment3_3': comment3_3,
            'exception3_3': exception3_3,
            'f3_4': f3_4,
            'comment3_4': comment3_4,
            'exception3_4': exception3_4,
            'f3_5': f3_5,
            'comment3_5': comment3_5,
            'exception3_5': exception3_5,
            'f4_1': f4_1,
            'comment4_1': comment4_1,
            'exception4_1': exception4_1,
            'f4_2': f4_2,
            'comment4_2': comment4_2,
            'exception4_2': exception4_2,
            'f4_3': f4_3,
            'comment4_3': comment4_3,
            'exception4_3': exception4_3,
            'f4_4': f4_4,
            'comment4_4': comment4_4,
            'exception4_4': exception4_4,
            'f5_1': f5_1,
            'comment5_1': comment5_1,
            'exception5_1': exception5_1,
            'f5_2': f5_2,
            'comment5_2': comment5_2,
            'exception5_2': exception5_2,
            'f5_3': f5_3,
            'comment5_3': comment5_3,
            'exception5_3': exception5_3,
            'f5_4': f5_4,
            'comment5_4': comment5_4,
            'exception5_4': exception5_4,
            'f5_5': f5_5,
            'comment5_5': comment5_5,
            'exception5_5': exception5_5,
            'f5_6': f5_6,
            'comment5_6': comment5_6,
            'exception5_6': exception5_6,
            'f6_1': f6_1,
            'comment6_1': comment6_1,
            'exception6_1': exception6_1,
            'f6_2': f6_2,
            'comment6_2': comment6_2,
            'exception6_2': exception6_2,
            'f6_3': f6_3,
            'comment6_3': comment6_3,
            'exception6_3': exception6_3,
            'f6_4': f6_4,
            'comment6_4': comment6_4,
            'exception6_4': exception6_4,
            'f6_5': f6_5,
            'comment6_5': comment6_5,
            'exception6_5': exception6_5,
            'f6_6': f6_6,
            'comment6_6': comment6_6,
            'exception6_6': exception6_6,
            'f6_7': f6_7,
            'comment6_7': comment6_7,
            'exception6_7': exception6_7,
            'f6_8': f6_8,
            'comment6_8': comment6_8,
            'exception6_8': exception6_8,
            'f6_9': f6_9,
            'comment6_9': comment6_9,
            'exception6_9': exception6_9,
            'f7_1': f7_1,
            'comment7_1': comment7_1,
            'exception7_1': exception7_1,
            'f7_2': f7_2,
            'comment7_2': comment7_2,
            'exception7_2': exception7_2,
            'f7_3': f7_3,
            'comment7_3': comment7_3,
            'exception7_3': exception7_3,
            'f7_4': f7_4,
            'comment7_4': comment7_4,
            'exception7_4': exception7_4,
            'f7_5': f7_5,
            'comment7_5': comment7_5,
            'exception7_5': exception7_5,
            'f8_1': f8_1,
            'comment8_1': comment8_1,
            'exception8_1': exception8_1,
            'f8_2': f8_2,
            'comment8_2': comment8_2,
            'exception8_2': exception8_2,
            'f8_3': f8_3,
            'comment8_3': comment8_3,
            'exception8_3': exception8_3,
            'f8_4': f8_4,
            'comment8_4': comment8_4,
            'exception8_4': exception8_4,
            'f8_5': f8_5,
            'comment8_5': comment8_5,
            'exception8_5': exception8_5,
            'f8_6': f8_6,
            'comment8_6': comment8_6,
            'exception8_6': exception8_6,
            'f9_1':f9_1,
            'comment9_1': comment9_1,
            'exception9_1': exception9_1,
            'f9_2': f9_2,
            'comment9_2': comment9_2,
            'exception9_2': exception9_2,
            'f9_3': f9_3,
            'comment9_3': comment9_3,
            'exception9_3': exception9_3,
            'f9_4': f9_4,
            'comment9_4': comment9_4,
            'exception9_4': exception9_4,
            'f9_5': f9_5,
            'comment9_5': comment9_5,
            'exception9_5': exception9_5,
            'f9_6': f9_6,
            'comment9_6': comment9_6,
            'exception9_6': exception9_6,
            'f9_7': f9_7,
            'comment9_7': comment9_7,
            'exception9_7': exception9_7,
            'f10_1': f10_1,
            'comment10_1': comment10_1,
            'exception10_1': exception10_1,
            'f10_2': f10_2,
            'comment10_2': comment10_2,
            'exception10_2': exception10_2,
            'f10_3': f10_3,
            'comment10_3': comment10_3,
            'exception10_3': exception10_3,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'social_screening.html', context)
    return render(request, 'social_1.html')


# @login_required
# def social_screening(request):
#     if request.method == 'POST':
#         inequality = request.POST.get("inequality")
#         comment1 = request.POST.get("comment1")
#         exception1 = request.POST.get("exception1")
#         social_cohesion = request.POST.get("social_cohesion")
#         comment2 = request.POST.get("comment2")
#         exception2 = request.POST.get("exception2")
#         social_integration = request.POST.get("social_integration")
#         comment3 = request.POST.get("comment3")
#         exception3 = request.POST.get("exception3")
#         labour_relations = request.POST.get("labour_relations")
#         comment4 = request.POST.get("comment4")
#         exception4 = request.POST.get("exception4")
#         investment_human_capital = request.POST.get("investment_human_capital")
#         comment5 = request.POST.get("comment5")
#         exception5 = request.POST.get("exception5")
#         economically_socially_communities = request.POST.get("economically_socially_communities")
#         comment6 = request.POST.get("comment6")
#         exception6 = request.POST.get("exception6")
#         supply_chain_management_s = request.POST.get("supply_chain_management_s")
#         comment7 = request.POST.get("comment7")
#         exception7 = request.POST.get("exception7")
#
#         input_data = {
#             'inequality': inequality,
#             'comment1': comment1,
#             'exception1': exception1,
#             'social_cohesion': social_cohesion,
#             'comment2': comment2,
#             'exception2': exception2,
#             'social_integration': social_integration,
#             'comment3': comment3,
#             'exception3': exception3,
#             'labour_relations': labour_relations,
#             'comment4': comment4,
#             'exception4': exception4,
#             'investment_human_capital': investment_human_capital,
#             'comment5': comment5,
#             'exception5': exception5,
#             'economically_socially_communities': economically_socially_communities,
#             'comment6': comment6,
#             'exception6': exception6,
#             'supply_chain_management_s': supply_chain_management_s,
#             'comment7': comment7,
#             'exception7': exception7,
#         }
#
#         context = {
#             'input_data': input_data,
#         }
#         return render(request, 'governance.html', context)
#     return render(request, 'social_screening.html')


@login_required
def social_screening(request):
    if request.method == 'POST':
        sc_1 = request.POST.get("sc_1")
        s_comment1 = request.POST.get("s_comment1")
        exception1 = request.POST.get("exception1")
        sc_2 = request.POST.get("sc_2")
        s_comment2 = request.POST.get("s_comment2")
        exception2 = request.POST.get("exception2")
        sc_3 = request.POST.get("sc_3")
        s_comment3 = request.POST.get("s_comment3")
        exception3 = request.POST.get("exception3")
        sc_4 = request.POST.get("sc_4")
        s_comment4 = request.POST.get("s_comment4")
        exception4 = request.POST.get("exception4")
        sc_5 = request.POST.get("sc_5")
        s_comment5 = request.POST.get("s_comment5")
        exception5 = request.POST.get("exception5")
        sc_6 = request.POST.get("sc_6")
        s_comment6 = request.POST.get("s_comment6")
        exception6 = request.POST.get("exception6")
        sc_7 = request.POST.get("sc_7")
        s_comment7 = request.POST.get("s_comment7")
        exception7 = request.POST.get("exception7")

        input_data = {
            'sc_1': sc_1,
            's_comment1': s_comment1,
            'exception1': exception1,
            'sc_2': sc_2,
            's_comment2': s_comment2,
            'exception2': exception2,
            'sc_3': sc_3,
            's_comment3': s_comment3,
            'exception3': exception3,
            'sc_4': sc_4,
            's_comment4': s_comment4,
            'exception4': exception4,
            'sc_5': sc_5,
            's_comment5': s_comment5,
            'exception5': exception5,
            'sc_6': sc_6,
            's_comment6': s_comment6,
            'exception6': exception6,
            'sc_7': sc_7,
            's_comment7': s_comment7,
            'exception7': exception7,
        }

        table = socialCalculations(input_data, request)
        s_total_score = table.s1_all_score()
        s_na_count = table.s1_all_na()
        s_avg_score = round(s_total_score/(7 - s_na_count))

        request.session['s1_1'] = sc_1
        request.session['s1_2'] = sc_2
        request.session['s1_3'] = sc_3
        request.session['s1_4'] = sc_4
        request.session['s1_5'] = sc_5
        request.session['s1_6'] = sc_6
        request.session['s1_7'] = sc_7
        request.session['s_comment1'] = s_comment1
        request.session['s_comment2'] = s_comment2
        request.session['s_comment3'] = s_comment3
        request.session['s_comment4'] = s_comment4
        request.session['s_comment5'] = s_comment5
        request.session['s_comment6'] = s_comment6
        request.session['s_comment7'] = s_comment7
        request.session['s_total_score'] = s_total_score
        request.session['s_avg_score'] = s_avg_score

        context = {
            'input_data': input_data,
            's1_1': sc_1,
            's_comment1': s_comment1,
            's1_2': sc_2,
            's_comment2': s_comment2,
            's1_3': sc_3,
            's_comment3': s_comment3,
            's1_4': sc_4,
            's_comment4': s_comment4,
            's1_5': sc_5,
            's_comment5': s_comment5,
            's1_6': sc_6,
            's_comment6': s_comment6,
            's1_7': sc_7,
            's_comment7': s_comment7,
            's_total_score': s_total_score,
            's_avg_score': s_avg_score,
        }
        return render(request, 'governance.html', context)
    return render(request, 'social_screening.html')


class socialCalculations:
    def __init__(self, input_data, request):
        self.input_data = input_data
        self.score = 0
        self.value = 0
        self.na_count_s = 0
        self.request = request

    # Social Final Scoring calculation
    def s1_1(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('sc_1') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('sc_1') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('sc_1') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('sc_1') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('sc_1') == '4':
            self.score = 4
            self.value = 4
        if self.input_data.get('sc_1') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_s += 1
        return [self.score, self.value, self.na_count_s]

    def s1_2(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('sc_2') == '0':
            self.score = 0
            self.value = 0
        if self.input_data.get('sc_2') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('sc_2') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('sc_2') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('sc_2') == '4':
            self.score = 4
            self.value = 4
        if self.input_data.get('sc_2') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_s += 1
        return [self.score, self.value, self.na_count_s]

    def s1_3(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('sc_3') == '0':
            self.score = 0
            self.value = 0
        if self.input_data.get('sc_3') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('sc_3') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('sc_3') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('sc_3') == '4':
            self.score = 4
            self.value = 4
        if self.input_data.get('sc_3') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_s += 1
        return [self.score, self.value, self.na_count_s]

    def s1_4(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('sc_4') == '0':
            self.score = 0
            self.value = 0
        if self.input_data.get('sc_4') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('sc_4') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('sc_4') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('sc_4') == '4':
            self.score = 4
            self.value = 4
        if self.input_data.get('sc_4') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_s += 1
        return [self.score, self.value, self.na_count_s]

    def s1_5(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('sc_5') == '0':
            self.score = 0
            self.value = 0
        if self.input_data.get('sc_5') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('sc_5') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('sc_5') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('sc_5') == '4':
            self.score = 4
            self.value = 4
        if self.input_data.get('sc_5') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_s += 1
        return [self.score, self.value, self.na_count_s]

    def s1_6(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('sc_6') == '0':
            self.score = 0
            self.value = 0
        if self.input_data.get('sc_6') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('sc_6') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('sc_6') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('sc_6') == '4':
            self.score = 4
            self.value = 4
        if self.input_data.get('sc_6') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_s += 1
        return [self.score, self.value, self.na_count_s]

    def s1_7(self):
        self.score = 0
        if self.input_data.get('sc_7') == '0':
            self.score = 0
        if self.input_data.get('sc_7') == '1':
            self.score = 1
        elif self.input_data.get('sc_7') == '2':
            self.score = 2
        elif self.input_data.get('sc_7') == '3':
            self.score = 3
        elif self.input_data.get('sc_7') == '4':
            self.score = 4
        if self.input_data.get('sc_7') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_s += 1
        return [self.score, self.value, self.na_count_s]

    def s1_all_na(self):
        s1_7 = self.s1_7()[2]
        return s1_7

    def s1_all_score(self):
        s1_1_score = self.s1_1()[0]
        s1_2_score = self.s1_2()[0]
        s1_3_score = self.s1_3()[0]
        s1_4_score = self.s1_4()[0]
        s1_5_score = self.s1_5()[0]
        s1_6_score = self.s1_6()[0]
        s1_7_score = self.s1_7()[0]

        s_total_score = s1_1_score + s1_2_score + s1_3_score + s1_4_score + s1_5_score + s1_6_score + s1_7_score
        # s_avg_score = round(s_total_score/(7 - na_count_s))
        return s_total_score

@login_required
def governance(request):
    if request.method == 'POST':
        f1_1 = request.POST.get("f1_1")
        comment1_1 = request.POST.get("comment1_1")
        exception1_1 = request.POST.get("exception1_1")
        f1_2 = request.POST.get("f1_2")
        comment1_2 = request.POST.get("comment1_2")
        exception1_2 = request.POST.get("exception1_2")
        f1_3 = request.POST.get("f1_3")
        comment1_3 = request.POST.get("comment1_3")
        exception1_3 = request.POST.get("exception1_3")
        f1_4 = request.POST.get("f1_4")
        comment1_4 = request.POST.get("comment1_4")
        exception1_4 = request.POST.get("exception1_4")
        f1_5 = request.POST.get("f1_5")
        comment1_5 = request.POST.get("comment1_5")
        exception1_5 = request.POST.get("exception1_5")
        f1_6 = request.POST.get("f1_6")
        comment1_6 = request.POST.get("comment1_6")
        exception1_6 = request.POST.get("exception1_6")
        f1_7 = request.POST.get("f1_7")
        comment1_7 = request.POST.get("comment1_7")
        exception1_7 = request.POST.get("exception1_7")
        f1_8 = request.POST.get("f1_8")
        comment1_8 = request.POST.get("comment1_8")
        exception1_8 = request.POST.get("exception1_8")
        f1_9 = request.POST.get("f1_9")
        comment1_9 = request.POST.get("comment1_9")
        exception1_9 = request.POST.get("exception1_9")
        f2_1 = request.POST.get("f2_1")
        comment2_1 = request.POST.get("comment2_1")
        exception2_1 = request.POST.get("exception2_1")
        f2_2 = request.POST.get("f2_2")
        comment2_2 = request.POST.get("comment2_2")
        exception2_2 = request.POST.get("exception2_2")
        f2_3 = request.POST.get("f2_3")
        comment2_3 = request.POST.get("comment2_3")
        exception2_3 = request.POST.get("exception2_3")
        f2_4 = request.POST.get("f2_4")
        comment2_4 = request.POST.get("comment2_4")
        exception2_4 = request.POST.get("exception2_4")
        f2_5 = request.POST.get("f2_5")
        comment2_5 = request.POST.get("comment2_5")
        exception2_5 = request.POST.get("exception2_5")
        f3_1 = request.POST.get("f3_1")
        comment3_1 = request.POST.get("comment3_1")
        exception3_1 = request.POST.get("exception3_1")
        f3_2 = request.POST.get("f3_2")
        comment3_2 = request.POST.get("comment3_2")
        exception3_2 = request.POST.get("exception3_2")
        f3_3 = request.POST.get("f3_3")
        comment3_3 = request.POST.get("comment3_3")
        exception3_3 = request.POST.get("exception3_3")
        f3_4 = request.POST.get("f3_4")
        comment3_4 = request.POST.get("comment3_4")
        exception3_4 = request.POST.get("exception3_4")
        f3_5 = request.POST.get("f3_5")
        comment3_5 = request.POST.get("comment3_5")
        exception3_5 = request.POST.get("exception3_5")
        f4_1 = request.POST.get("f4_1")
        comment4_1 = request.POST.get("comment4_1")
        exception4_1 = request.POST.get("exception4_1")
        f4_2 = request.POST.get("f4_2")
        comment4_2 = request.POST.get("comment4_2")
        exception4_2 = request.POST.get("exception4_2")
        f4_3 = request.POST.get("f4_3")
        comment4_3 = request.POST.get("comment4_3")
        exception4_3 = request.POST.get("exception4_3")
        f5_1 = request.POST.get("f5_1")
        comment5_1 = request.POST.get("comment5_1")
        exception5_1 = request.POST.get("exception5_1")
        f5_2 = request.POST.get("f5_2")
        comment5_2 = request.POST.get("comment5_2")
        exception5_2 = request.POST.get("exception5_2")
        f5_3 = request.POST.get("f5_3")
        comment5_3 = request.POST.get("comment5_3")
        exception5_3 = request.POST.get("exception5_3")
        f5_4 = request.POST.get("f5_4")
        comment5_4 = request.POST.get("comment5_4")
        exception5_4 = request.POST.get("exception5_4")
        f5_5 = request.POST.get("f5_5")
        comment5_5 = request.POST.get("comment5_5")
        exception5_5 = request.POST.get("exception5_5")
        f5_6 = request.POST.get("f5_6")
        comment5_6 = request.POST.get("comment5_6")
        exception5_6 = request.POST.get("exception5_6")
        f6_1 = request.POST.get("f6_1")
        comment6_1 = request.POST.get("comment6_1")
        exception6_1 = request.POST.get("exception6_1")
        f6_2 = request.POST.get("f6_2")
        comment6_2 = request.POST.get("comment6_2")
        exception6_2 = request.POST.get("exception6_2")
        f6_3 = request.POST.get("f6_3")
        comment6_3 = request.POST.get("comment6_3")
        exception6_3 = request.POST.get("exception6_3")
        f6_4 = request.POST.get("f6_4")
        comment6_4 = request.POST.get("comment6_4")
        exception6_4 = request.POST.get("exception6_4")
        f6_5 = request.POST.get("f6_5")
        comment6_5 = request.POST.get("comment6_5")
        exception6_5 = request.POST.get("exception6_5")
        f6_6 = request.POST.get("f6_6")
        comment6_6 = request.POST.get("comment6_6")
        exception6_6 = request.POST.get("exception6_6")
        f6_7 = request.POST.get("f6_7")
        comment6_7 = request.POST.get("comment6_7")
        exception6_7 = request.POST.get("exception6_7")
        f6_8 = request.POST.get("f6_8")
        comment6_8 = request.POST.get("comment6_8")
        exception6_8 = request.POST.get("exception6_8")
        f6_9 = request.POST.get("f6_9")
        comment6_9 = request.POST.get("comment6_9")
        exception6_9 = request.POST.get("exception6_9")

        input_data = {
            'f1_1': f1_1,
            'comment1_1': comment1_1,
            'exception1_1': exception1_1,
            'f1_2': f1_2,
            'comment1_2': comment1_2,
            'exception1_2': exception1_2,
            'f1_3': f1_3,
            'comment1_3': comment1_3,
            'exception1_3': exception1_3,
            'f1_4': f1_4,
            'comment1_4': comment1_4,
            'exception1_4': exception1_4,
            'f1_5': f1_5,
            'comment1_5': comment1_5,
            'exception1_5': exception1_5,
            'f1_6': f1_6,
            'comment1_6': comment1_6,
            'exception1_6': exception1_6,
            'f1_7': f1_7,
            'comment1_7': comment1_7,
            'exception1_7': exception1_7,
            'f1_8': f1_8,
            'comment1_8': comment1_8,
            'exception1_8': exception1_8,
            'f1_9': f1_9,
            'comment1_9': comment1_9,
            'exception1_9': exception1_9,
            'f2_1': f2_1,
            'comment2_1': comment2_1,
            'exception2_1': exception2_1,
            'f2_2': f2_2,
            'comment2_2': comment2_2,
            'exception2_2': exception2_2,
            'f2_3': f2_3,
            'comment2_3': comment2_3,
            'exception2_3': exception2_3,
            'f2_4': f2_4,
            'comment2_4': comment2_4,
            'exception2_4': exception2_4,
            'f2_5': f2_5,
            'comment2_5': comment2_5,
            'exception2_5': exception2_5,
            'f3_1': f3_1,
            'comment3_1': comment3_1,
            'exception3_1': exception3_1,
            'f3_2': f3_2,
            'comment3_2': comment3_2,
            'exception3_2': exception3_2,
            'f3_3': f3_3,
            'comment3_3': comment3_3,
            'exception3_3': exception3_3,
            'f3_4': f3_4,
            'comment3_4': comment3_4,
            'exception3_4': exception3_4,
            'f3_5': f3_5,
            'comment3_5': comment3_5,
            'exception3_5': exception3_5,
            'f4_1': f4_1,
            'comment4_1': comment4_1,
            'exception4_1': exception4_1,
            'f4_2': f4_2,
            'comment4_2': comment4_2,
            'exception4_2': exception4_2,
            'f4_3': f4_3,
            'comment4_3': comment4_3,
            'exception4_3': exception4_3,
            'f5_1': f5_1,
            'comment5_1': comment5_1,
            'exception5_1': exception5_1,
            'f5_2': f5_2,
            'comment5_2': comment5_2,
            'exception5_2': exception5_2,
            'f5_3': f5_3,
            'comment5_3': comment5_3,
            'exception5_3': exception5_3,
            'f5_4': f5_4,
            'comment5_4': comment5_4,
            'exception5_4': exception5_4,
            'f5_5': f5_5,
            'comment5_5': comment5_5,
            'exception5_5': exception5_5,
            'f5_6': f5_6,
            'comment5_6': comment5_6,
            'exception5_6': exception5_6,
            'f6_1': f6_1,
            'comment6_1': comment6_1,
            'exception6_1': exception6_1,
            'f6_2': f6_2,
            'comment6_2': comment6_2,
            'exception6_2': exception6_2,
            'f6_3': f6_3,
            'comment6_3': comment6_3,
            'exception6_3': exception6_3,
            'f6_4': f6_4,
            'comment6_4': comment6_4,
            'exception6_4': exception6_4,
            'f6_5': f6_5,
            'comment6_5': comment6_5,
            'exception6_5': exception6_5,
            'f6_6': f6_6,
            'comment6_6': comment6_6,
            'exception6_6': exception6_6,
            'f6_7': f6_7,
            'comment6_7': comment6_7,
            'exception6_7': exception6_7,
            'f6_8': f6_8,
            'comment6_8': comment6_8,
            'exception6_8': exception6_8,
            'f6_9': f6_9,
            'comment6_9': comment6_9,
            'exception6_9': exception6_9,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'governance_scoring.html', context)
    return render(request, 'governance.html')


@login_required
def governance_scoring(request):
    if request.method == 'POST':
        employee_relations = request.POST.get("employee_relations")
        g_comment1 = request.POST.get("g_comment1")
        exception1 = request.POST.get("exception1")
        sound_management_structures = request.POST.get("sound_management_structures")
        g_comment2 = request.POST.get("g_comment2")
        exception2 = request.POST.get("exception2")
        remuneration_staff = request.POST.get("remuneration_staff")
        g_comment3 = request.POST.get("g_comment3")
        exception3 = request.POST.get("exception3")
        tax = request.POST.get("tax")
        g_comment4 = request.POST.get("g_comment4")
        exception4 = request.POST.get("exception4")
        corporate_governance = request.POST.get("corporate_governance")
        g_comment5 = request.POST.get("g_comment5")
        exception5 = request.POST.get("exception5")
        governance_other = request.POST.get("governance_other")
        g_comment6 = request.POST.get("g_comment6")
        exception6 = request.POST.get("exception6")

        input_data = {
            'employee_relations': employee_relations,
            'g_comment1': g_comment1,
            'exception1': exception1,
            'sound_management_structures': sound_management_structures,
            'g_comment2': g_comment2,
            'exception2': exception2,
            'remuneration_staff': remuneration_staff,
            'g_comment3': g_comment3,
            'exception3': exception3,
            'tax': tax,
            'g_comment4': g_comment4,
            'exception4': exception4,
            'corporate_governance': corporate_governance,
            'g_comment5': g_comment5,
            'exception5': exception5,
            'governance_other': governance_other,
            'g_comment6': g_comment6,
            'exception6': exception6,
        }

        table = governanceCalculations(input_data, request)
        g_total_score = table.g1_all_score()
        na_count_g = table.g1_all_na()
        g_avg_score = round(g_total_score/(6 - na_count_g))

        context = {
            'input_data': input_data,
            'e2_1': request.session.get('e2_1'),
            'e2_2': request.session.get('e2_2'),
            'e2_3': request.session.get('e2_3'),
            'e2_4': request.session.get('e2_4'),
            'e2_5': request.session.get('e2_5'),
            'e2_6': request.session.get('e2_6'),
            'e2_7': request.session.get('e2_7'),
            'e2_8': request.session.get('e2_8'),
            'e2_9': request.session.get('e2_9'),
            'e2_10': request.session.get('e2_10'),
            'comment1': request.session.get('comment1'),
            'comment2': request.session.get('comment2'),
            'comment3': request.session.get('comment3'),
            'comment4': request.session.get('comment4'),
            'comment5': request.session.get('comment5'),
            'comment6': request.session.get('comment6'),
            'comment7': request.session.get('comment7'),
            'comment8': request.session.get('comment8'),
            'comment9': request.session.get('comment9'),
            'comment10': request.session.get('comment10'),
            'total_score': request.session.get('total_score'),
            'avg_score': request.session.get('avg_score'),
            'company_name': request.session.get('company_name'),
            's1_1': request.session.get('s1_1'),
            's1_2': request.session.get('s1_2'),
            's1_3': request.session.get('s1_3'),
            's1_4': request.session.get('s1_4'),
            's1_5': request.session.get('s1_5'),
            's1_6': request.session.get('s1_6'),
            's1_7': request.session.get('s1_7'),
            's_comment1': request.session.get('s_comment1'),
            's_comment2': request.session.get('s_comment2'),
            's_comment3': request.session.get('s_comment3'),
            's_comment4': request.session.get('s_comment4'),
            's_comment5': request.session.get('s_comment5'),
            's_comment6': request.session.get('s_comment6'),
            's_comment7': request.session.get('s_comment7'),
            's_total_score': request.session.get('s_total_score'),
            's_avg_score': request.session.get('s_avg_score'),
            'g1_1': employee_relations,
            'g_comment1': g_comment1,
            'g1_2': sound_management_structures,
            'g_comment2': g_comment2,
            'g1_3': remuneration_staff,
            'g_comment3': g_comment3,
            'g1_4': tax,
            'g_comment4': g_comment4,
            'g1_5': corporate_governance,
            'g_comment5': g_comment5,
            'g1_6': governance_other,
            'g_comment6': g_comment6,
            'g_total_score': g_total_score,
            'g_avg_score': g_avg_score,
        }
        return render(request, 'final_scoring_client.html', context)
    return render(request, 'governance_scoring.html')


class governanceCalculations:
    def __init__(self, input_data, request):
        self.input_data = input_data
        self.score = 0
        self.value = 0
        self.na_count_g = 0
        self.request = request

    #governance Final Scoring calculation
    def g1_1(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('employee_relations') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('employee_relations') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('employee_relations') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('employee_relations') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('employee_relations') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('employee_relations') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_g += 1
        return [self.score, self.value, self.na_count_g]

    def g1_2(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('sound_management_structures') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('sound_management_structures') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('sound_management_structures') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('sound_management_structures') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('sound_management_structures') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('sound_management_structures') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_g += 1
        return [self.score, self.value, self.na_count_g]

    def g1_3(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('remuneration_staff') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('remuneration_staff') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('remuneration_staff') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('remuneration_staff') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('remuneration_staff') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('remuneration_staff') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_g += 1
        return [self.score, self.value, self.na_count_g]

    def g1_4(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('tax') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('tax') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('tax') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('tax') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('tax') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('tax') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_g += 1
        return [self.score, self.value, self.na_count_g]

    def g1_5(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('corporate_governance') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('corporate_governance') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('corporate_governance') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('corporate_governance') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('corporate_governance') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('corporate_governance') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_g += 1
        return [self.score, self.value, self.na_count_g]

    def g1_6(self):
        self.score = 0
        self.value = 0
        if self.input_data.get('governance_other') == '0':
            self.score = 0
            self.value = 0
        elif self.input_data.get('governance_other') == '1':
            self.score = 1
            self.value = 1
        elif self.input_data.get('governance_other') == '2':
            self.score = 2
            self.value = 2
        elif self.input_data.get('governance_other') == '3':
            self.score = 3
            self.value = 3
        elif self.input_data.get('governance_other') == '4':
            self.score = 4
            self.value = 4
        elif self.input_data.get('governance_other') == 'NA':
            self.score = 0
            self.value = 'NA'
            self.na_count_g += 1
        return [self.score, self.value, self.na_count_g]

    def g1_all_na(self):
        g1_6 = self.g1_6()[2]
        return g1_6

    def g1_all_score(self):
        g1_1_score = self.g1_1()[0]
        g1_2_score = self.g1_2()[0]
        g1_3_score = self.g1_3()[0]
        g1_4_score = self.g1_4()[0]
        g1_5_score = self.g1_5()[0]
        g1_6_score = self.g1_6()[0]

        g_total_score = g1_1_score + g1_2_score + g1_3_score + g1_4_score + g1_5_score + g1_6_score
        return g_total_score


@login_required
def final_scoring(request):
    return render(request, 'final_scoring.html')


@login_required
def final_scoring_client(request):
    # context = {
    #     'company_name': request.session.get('company_name')
    # }
    return render(request, 'final_scoring_client.html')


@login_required
def user_pdf(request):
    return render(request, 'final_scoring.html')


@login_required
def client_pdf(request):
    return render(request, 'final_scoring_client.html')


# @login_required
# def report_pdf(request):
#     #bytestream
#     buf = io.BytesIO()
#     #canvas
#     c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
#     #textobject
#     textob = c.beginText()
#     textob.setTextOrigin(inch, inch)
#     textob.setFont("Helvetica", 12)
#
#     #Add some lines to text
#     lines = [
#         "This is line 1"
#         "This is line 2"
#     ]
#
#     #loop
#     for line in lines:
#         textob.textLine(line)
#
#     #finish
#     c.drawText(textob)
#     c.showPage()
#     c.save()
#     buf.seek(0)
#
#     return FileResponse(buf, as_attachment=True, filename='report.pdf')


@login_required
def report_pdf(request):
    context = {

    }
    return render(request, 'report_pdf.html')


@login_required
def status(request):
    value = request.GET.get('search')
    context = {
        'status': value,
    }
    return render(request, 'status.html', context)


@login_required
def pdf_button(request):
    if request.method=='POSt':
        recommendations = request.POST.get("recommendations")
        comment1 = request.POST.get("comment1")
        exception1 = request.POST.get("exception1")
        general = request.POST.get("general")
        comment2 = request.POST.get("comment2")
        exception2 = request.POST.get("exception2")
        sources_and_types = request.POST.get("sources_and_types")
        comment3 = request.POST.get("comment3")
        exception3 = request.POST.get("exception3")
        systematic = request.POST.get("systematic")
        comment4 = request.POST.get("comment4")
        exception4 = request.POST.get("exception4")
        universe = request.POST.get("universe")
        comment5 = request.POST.get("comment5")
        exception5 = request.POST.get("exception5")
        screening = request.POST.get("screening")
        comment6 = request.POST.get("comment6")
        exception6 = request.POST.get("exception6")
        characteristics = request.POST.get("characteristics")
        comment7 = request.POST.get("comment7")
        exception7 = request.POST.get("exception7")
        targets = request.POST.get("targets")
        comment8 = request.POST.get("comment8")
        exception8 = request.POST.get("exception8")
        stewardship_activities = request.POST.get("stewardship_activities")
        comment9 = request.POST.get("comment9")
        exception9 = request.POST.get("exception9")
        social_impact = request.POST.get("social_impact")
        comment10 = request.POST.get("comment10")
        exception10 = request.POST.get("exception10")
        organisational_requirements = request.POST.get("organisational_requirements")
        comment11 = request.POST.get("comment11")
        exception11 = request.POST.get("exception11")
        risk_management = request.POST.get("risk_management")
        comment12 = request.POST.get("comment12")
        exception12 = request.POST.get("exception12")
        conflicts_of_interest = request.POST.get("conflicts_of_interest")
        comment13 = request.POST.get("comment13")
        exception13 = request.POST.get("exception13")
        product_governance = request.POST.get("product_governance")
        comment14 = request.POST.get("comment14")
        exception14 = request.POST.get("exception14")
        cost = request.POST.get("cost")
        comment15 = request.POST.get("comment15")
        exception15 = request.POST.get("exception15")
        provided = request.POST.get("provided")
        comment16 = request.POST.get("comment16")
        exception16 = request.POST.get("exception16")
        gathered = request.POST.get("gathered")
        comment17 = request.POST.get("comment17")
        exception17 = request.POST.get("exception17")
        sustainability = request.POST.get("sustainability")
        comment18 = request.POST.get("comment18")
        exception18 = request.POST.get("exception18")


        input_data = {
            'recommendations': recommendations,
            'comment1': comment1,
            'exception1': exception1,
            'general': general,
            'comment2': comment2,
            'exception2': exception2,
            'sources_and_types': sources_and_types,
            'comment3': comment3,
            'exception3': exception3,
            'systematic': systematic,
            'comment4': comment4,
            'exception4': exception4,
            'universe': universe,
            'comment5': comment5,
            'exception5': exception5,
            'screening': screening,
            'comment6': comment6,
            'exception6': exception6,
            'characteristics': characteristics,
            'comment7': comment7,
            'exception7': exception7,
            'targets': targets,
            'comment8': comment8,
            'exception8': exception8,
            'stewardship_activities': stewardship_activities,
            'comment9': comment9,
            'exception9': exception9,
            'social_impact': social_impact,
            'comment10': comment10,
            'exception10': exception10,
            'organisational_requirements': organisational_requirements,
            'comment11': comment11,
            'exception11': exception11,
            'risk_management': risk_management,
            'comment12': comment12,
            'exception12': exception12,
            'conflicts_of_interest': conflicts_of_interest,
            'comment13': comment13,
            'exception13': exception13,
            'product_governance': product_governance,
            'comment14': comment14,
            'exception14': exception14,
            'cost': cost,
            'comment15': comment15,
            'exception15': exception15,
            'provided': provided,
            'comment16': comment16,
            'exception16': exception16,
            'gathered': gathered,
            'comment17': comment17,
            'exception17': exception17,
            'sustainability': sustainability,
            'comment18': comment18,
            'exception18': exception18,
        }

        table = selfCalculations(input_data, request)
        total_score = table.f1_all_score()[0]
        na_count = table.f1_all_na()
        avg_score = round(total_score / (18 - na_count))

        context = {
            'input_data': input_data,
            'f1': recommendations,
            # 'score1': table.f1_all(),
            'comment1': comment1,
            'f2': general,
            'comment2': comment2,
            'f3': sources_and_types,
            'comment3': comment3,
            'f4': systematic,
            'comment4': comment4,
            'f5': universe,
            'comment5': comment5,
            'f6': screening,
            'comment6': comment6,
            'f7': characteristics,
            'comment7': comment7,
            'f8': targets,
            'comment8': comment8,
            'f9': stewardship_activities,
            'comment9': comment9,
            'f10': social_impact,
            'comment10': comment10,
            'f11': organisational_requirements,
            'comment11': comment11,
            'f12': risk_management,
            'comment12': comment12,
            'f13': conflicts_of_interest,
            'comment13': comment13,
            'f14': product_governance,
            'comment14': comment14,
            'f15': cost,
            'comment15': comment15,
            'f16': provided,
            'comment16': comment16,
            'f17': gathered,
            'comment17': comment17,
            'f18': sustainability,
            'comment18': comment18,
            'total_score': total_score,
            'avg_score': avg_score,
        }

    return render(request, 'final_scoring.html', context)


class PDF(FPDF):
    pass
    # nothing happens when it is executed.

def get_pdf(request):
    pdf = PDF(orientation='P', unit='mm', format='A4') # landscape
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)

    title = 'SELF ASSESSMENT'
    image = 'media/cg_logo.png'
    pdf.image(image, x=5, y=5, w=42, h=12)
    pdf.cell(ln=1, h=30, align='C', w=0, txt=title,  border=0)
    pdf.output('pdf/output.pdf', 'F')
    return HttpResponse(open('pdf/final_scoring_selfassessment.pdf', 'rb'), content_type='application/pdf')
