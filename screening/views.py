from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import ipdb


# Create your views here.
@login_required
def home1(request):
    # ipdb.set_trace()
    if request.method == 'POST':
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

        context = {
            'input_data': input_data,
        }
        return render(request, 'self_assessment_1.html', context)
    # return HttpResponse('<h1> Screening home </h1>')
    return render(request, 'index_user.html')


@login_required
def home2(request):
    # ipdb.set_trace()
    if request.method == 'POST':
        investment_name = request.POST.get('investment_name')
        prepare_by = request.POST.get('prepare_by')
        date = request.POST.get('date')
        firm_address = request.POST.get('firm_address')
        brief_project = request.POST.get('brief_project')
        client_name = request.POST.get('client_name')
        client_address = request.POST.get('client_address')
        client_contact_no = request.POST.get('client_contact_no')
        client_email = request.POST.get('client_email')
        company_name = request.POST.get('company_name')
        company_address = request.POST.get('company_address')
        industry_sector = request.POST.get('industry_sector')

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

        context = {
            'input_data': input_data,
        }
        return render(request, 'environment1_1.html', context)
    # return HttpResponse('<h1> Screening home </h1>')
    return render(request, 'index_client.html')


def login_user(request):
    # ipdb.set_trace()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
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
    # ipdb.set_trace()
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
def new(request):
    return render(request, 'new.html')


@login_required
def selection(request):
    # ipdb.set_trace()
    # if request.method == 'POST':
    #     s1 = request.POST.get('s1')
    #
    #     input_data = {
    #         's1': s1,
    #     }
    #
    #     context = {
    #         'input_data': input_data,
    #     }
    #     return render(request, 'selection.html', context)
    return render(request, 'selection.html')


@login_required
def self_assessment_1(request):
    return render(request, 'self_assessment_2.html')


@login_required
def self_assessment_2(request):
    return render(request, 'self_assessment1_3.html')


@login_required
def self_assessment1_3(request):
    return render(request, 'self_assessment_4.html')


@login_required
def self_assessment_4(request):
    return render(request, 'self_assessment_5.html')


@login_required
def self_assessment_5(request):
    return render(request, 'self_assessment_6.html')


@login_required
def self_assessment_6(request):
    return render(request, 'self_assessment_7.html')


@login_required
def self_assessment_7(request):
    return render(request, 'self_assessment_8.html')


@login_required
def self_assessment_8(request):
    return render(request, 'self_assessment_9.html')


@login_required
def self_assessment_9(request):
    return render(request, 'self_assessment_10.html')


@login_required
def self_assessment_10(request):
    return render(request, 'self_assessment_11.html')


@login_required
def self_assessment_11(request):
    return render(request, 'self_assessment_12.html')


@login_required
def self_assessment_12(request):
    return render(request, 'self_assessment_13.html')


@login_required
def self_assessment_13(request):
    return render(request, 'self_assessment_scoring.html')


@login_required
def self_assessment_scoring(request):
    return render(request, 'final_scoring.html')


@login_required
def environment1_1(request):
    # ipdb.set_trace()
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
    # ipdb.set_trace()
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


def environment1_3(request):
    # ipdb.set_trace()
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


def environment1_4(request):
    # ipdb.set_trace()
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


def environment1_5(request):
    # ipdb.set_trace()
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


def environment1_6(request):
    # ipdb.set_trace()
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


def environment1_7(request):
    # ipdb.set_trace()
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


def environment1_8(request):
    # ipdb.set_trace()
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


def environment1_9(request):
    # ipdb.set_trace()
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


def environment1_10(request):
    # ipdb.set_trace()
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
    #ipdb.set_trace()
    if request.method == 'POST':
        energy_and_renewable_energy = request.POST.get("energy_and_renewable_energy")
        comment1 = request.POST.get("comment1")
        exception1 = request.POST.get("exception1")
        raw_materials= request.POST.get("raw_materials")
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

        context = {
            'input_data': input_data,
        }
        return render(request, 'social_1.html', context)
    return render(request, 'environment_2.html')


@login_required
def social_1(request):
    #ipdb.set_trace()
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


def social_screening(request):
    #ipdb.set_trace()
    if request.method == 'POST':
        inequality = request.POST.get("inequality")
        comment1 = request.POST.get("comment1")
        exception1 = request.POST.get("exception1")
        social_cohesion = request.POST.get("social_cohesion")
        comment2 = request.POST.get("comment2")
        exception2 = request.POST.get("exception2")
        social_integration = request.POST.get("social_integration")
        comment3 = request.POST.get("comment3")
        exception3 = request.POST.get("exception3")
        labour_relations = request.POST.get("labour_relations")
        comment4 = request.POST.get("comment4")
        exception4 = request.POST.get("exception4")
        investment_human_capital = request.POST.get("investment_human_capital")
        comment5 = request.POST.get("comment5")
        exception5 = request.POST.get("exception5")
        economically_socially_communities = request.POST.get("economically_socially_communities")
        comment6 = request.POST.get("comment6")
        exception6 = request.POST.get("exception6")
        other_supply_chain = request.POST.get("other_supply_chain")
        comment7 = request.POST.get("comment7")
        exception7 = request.POST.get("exception7")

        input_data = {
            'inequality': inequality,
            'comment1': comment1,
            'exception1': exception1,
            'social_cohesion': social_cohesion,
            'comment2': comment2,
            'exception2': exception2,
            'social_integration': social_integration,
            'comment3': comment3,
            'exception3': exception3,
            'labour_relations': labour_relations,
            'comment4': comment4,
            'exception4': exception4,
            'investment_human_capital': investment_human_capital,
            'comment5': comment5,
            'exception5': exception5,
            'economically_socially_communities': economically_socially_communities,
            'comment6': comment6,
            'exception6': exception6,
            'other_supply_chain': other_supply_chain,
            'comment7': comment7,
            'exception7': exception7,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'governance.html', context)
    return render(request, 'social_screening.html')


def governance(request):
    # ipdb.set_trace()
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
        f3_6 = request.POST.get("f3_6")
        comment3_6 = request.POST.get("comment3_6")
        exception3_6 = request.POST.get("exception3_6")
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
            'f3_6': f3_6,
            'comment3_6': comment3_6,
            'exception3_6': exception3_6,
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
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'governance_scoring.html', context)
    return render(request, 'governance.html')


def governance_scoring(request):
    if request.method == 'POST':
        employee_relations = request.POST.get("employee_relations")
        comment1 = request.POST.get("comment1")
        exception1 = request.POST.get("exception1")
        sound_management_structure = request.POST.get("sound_management_structure")
        comment2 = request.POST.get("comment2")
        exception2 = request.POST.get("exception2")
        remuneration_staff = request.POST.get("remuneration_staff")
        comment3 = request.POST.get("comment3")
        exception3 = request.POST.get("exception3")
        tax_compliance = request.POST.get("tax_compliance")
        comment4 = request.POST.get("comment4")
        exception4 = request.POST.get("exception4")
        corporate_governance = request.POST.get("corporate_governance")
        comment5 = request.POST.get("comment5")
        exception5 = request.POST.get("exception5")
        governance_other = request.POST.get("governance_other")
        comment6 = request.POST.get("comment6")
        exception6 = request.POST.get("exception6")

        input_data = {
            'employee_relations': employee_relations,
            'comment1': comment1,
            'exception1': exception1,
            'sound_management_structure': sound_management_structure,
            'comment2': comment2,
            'exception2': exception2,
            'remuneration_staff': remuneration_staff,
            'comment3': comment3,
            'exception3': exception3,
            'tax_compliance ': tax_compliance ,
            'comment4': comment4,
            'exception4': exception4,
            'corporate_governance': corporate_governance,
            'comment5': comment5,
            'exception5': exception5,
            'governance_other': governance_other,
            'comment6': comment6,
            'exception6': exception6,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'final_scoring.html', context)
    return render(request, 'governance_scoring.html')


@login_required
def social_screening(request):
    #ipdb.set_trace()
    if request.method == 'POST':
        inequality = request.POST.get("inequality")
        comment1 = request.POST.get("comment1")
        exception1 = request.POST.get("exception1")
        social_cohesion = request.POST.get("social_cohesion")
        comment2 = request.POST.get("comment2")
        exception2 = request.POST.get("exception2")
        social_integration = request.POST.get("social_integration")
        comment3 = request.POST.get("comment3")
        exception3 = request.POST.get("exception3")
        labour_relations = request.POST.get("labour_relations")
        comment4 = request.POST.get("comment4")
        exception4 = request.POST.get("exception4")
        investment_human_capital = request.POST.get("investment_human_capital")
        comment5 = request.POST.get("comment5")
        exception5 = request.POST.get("exception5")
        economically_socially_communities = request.POST.get("economically_socially_communities")
        comment6 = request.POST.get("comment6")
        exception6 = request.POST.get("exception6")
        other_supply_chain = request.POST.get("other_supply_chain")
        comment7 = request.POST.get("comment7")
        exception7 = request.POST.get("exception7")

        input_data = {
            'inequality': inequality,
            'comment1': comment1,
            'exception1': exception1,
            'social_cohesion': social_cohesion,
            'comment2': comment2,
            'exception2': exception2,
            'social_integration': social_integration,
            'comment3': comment3,
            'exception3': exception3,
            'labour_relations': labour_relations,
            'comment4': comment4,
            'exception4': exception4,
            'investment_human_capital': investment_human_capital,
            'comment5': comment5,
            'exception5': exception5,
            'economically_socially_communities': economically_socially_communities,
            'comment6': comment6,
            'exception6': exception6,
            'other_supply_chain': other_supply_chain,
            'comment7': comment7,
            'exception7': exception7,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'governance.html', context)
    return render(request, 'social_screening.html')


@login_required
def governance(request):
    # ipdb.set_trace()
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
        f3_6 = request.POST.get("f3_6")
        comment3_6 = request.POST.get("comment3_6")
        exception3_6 = request.POST.get("exception3_6")
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
            'f3_6': f3_6,
            'comment3_6': comment3_6,
            'exception3_6': exception3_6,
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
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'governance_scoring.html', context)
    return render(request, 'governance.html')


@login_required
def governance_scoring(request):
    #ipdb.set_trace()
    if request.method == 'POST':
        employee_relations = request.POST.get("employee_relations")
        comment1 = request.POST.get("comment1")
        exception1 = request.POST.get("exception1")
        sound_management_structure = request.POST.get("sound_management_structure")
        comment2 = request.POST.get("comment2")
        exception2 = request.POST.get("exception2")
        remuneration_staff = request.POST.get("remuneration_staff")
        comment3 = request.POST.get("comment3")
        exception3 = request.POST.get("exception3")
        tax_compliance = request.POST.get("tax_compliance")
        comment4 = request.POST.get("comment4")
        exception4 = request.POST.get("exception4")
        corporate_governance = request.POST.get("corporate_governance")
        comment5 = request.POST.get("comment5")
        exception5 = request.POST.get("exception5")
        governance_other = request.POST.get("governance_other")
        comment6 = request.POST.get("comment6")
        exception6 = request.POST.get("exception6")

        input_data = {
            'employee_relations': employee_relations,
            'comment1': comment1,
            'exception1': exception1,
            'sound_management_structure': sound_management_structure,
            'comment2': comment2,
            'exception2': exception2,
            'remuneration_staff': remuneration_staff,
            'comment3': comment3,
            'exception3': exception3,
            'tax_compliance ': tax_compliance ,
            'comment4': comment4,
            'exception4': exception4,
            'corporate_governance': corporate_governance,
            'comment5': comment5,
            'exception5': exception5,
            'governance_other': governance_other,
            'comment6': comment6,
            'exception6': exception6,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'final_scoring_client.html', context)
    return render(request, 'governance_scoring.html')


@login_required
def final_scoring(request):
    return render(request, 'final_scoring.html')


@login_required
def final_scoring_client(request):
    return render(request, 'final_scoring_client.html')