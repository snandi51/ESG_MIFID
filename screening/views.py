from django.shortcuts import render
from django.http import HttpResponse
# import ipdb


# Create your views here.
def home(request):
    # return HttpResponse('<h1> Screening home </h1>')
    return render(request, 'index.html')


def environment_1(request):
    # ipdb.set_trace()
    if request.method == 'POST':
        set_of_policies = request.POST["set_of_policies"]
        comment1_1 = request.POST["comment1_1"]
        Exception1_1 = request.POST["Exception1_1"]
        keep_records = request.POST["keep_records"]
        comment1_2 = request.POST["comment1_2"]
        Exception1_2 = request.POST["Exception1_2"]
        evaluation_exercise = request.POST["evaluation_exercise"]
        comment1_3 = request.POST["comment1_3"]
        Exception1_3 = request.POST["Exception1_3"]
        reduce_consumption = request.POST["reduce_consumption"]
        comment1_4 = request.POST["comment1_4"]
        Exception1_4 = request.POST["Exception1_4"]
        invested_renewable_sources = request.POST["invested_renewable_sources"]
        comment1_5 = request.POST["comment1_5"]
        Exception1_5 = request.POST["Exception1_5"]
        set_of_strategies = request.POST["set_of_strategies"]
        comment2_1 = request.POST["comment2_1"]
        Exception2_1 = request.POST["Exception2_1"]
        handling_raw_materials = request.POST["handling_raw_materials"]
        comment2_2 = request.POST["comment2_2"]
        Exception2_2 = request.POST["Exception2_2"]
        dependence_raw_materials = request.POST["dependence_raw_materials"]
        comment2_3 = request.POST["comment2_3"]
        Exception2_3 = request.POST["Exception2_3"]
        sourcing_raw_materials = request.POST["sourcing_raw_materials"]
        comment2_4 = request.POST["comment2_4"]
        Exception2_4 = request.POST["Exception2_4"]
        use_recycled_materials = request.POST["use_recycled_materials"]
        comment2_5 = request.POST["comment2_5"]
        Exception2_5 = request.POST["Exception2_5"]
        recyclable_packaging = request.POST["recyclable_packaging"]
        comment2_6 = request.POST["comment2_6"]
        Exception2_6 = request.POST["Exception2_6"]
        set_of_policies_water = request.POST["set_of_policies_water"]
        comment3_1 = request.POST["comment3_1"]
        Exception3_1 = request.POST["Exception3_1"]
        consume_water = request.POST["consume_water"]
        comment3_2 = request.POST["comment3_2"]
        Exception3_2 = request.POST["Exception3_2"]
        face_risk_water_scarcity = request.POST["face_risk_water_scarcity"]
        comment3_3 = request.POST["comment3_3"]
        Exception3_3 = request.POST["Exception3_3"]
        recycling_water_used_by_organisation = request.POST["recycling_water_used_by_organisation"]
        comment3_4 = request.POST["comment3_4"]
        Exception3_4 = request.POST["Exception3_4"]
        mention_amount_of_water_recycle = request.POST["mention_amount_of_water_recycle"]
        comment3_5 = request.POST["comment3_5"]
        Exception3_5 = request.POST["Exception3_5"]
        land_clearance = request.POST["land_clearance"]
        comment4_1 = request.POST["comment4_1"]
        Exception4_1 = request.POST["Exception4_1"]
        set_policies_land_clearance = request.POST["set_policies_land_clearance"]
        comment4_2 = request.POST["comment4_2"]
        Exception4_2 = request.POST["Exception4_2"]
        result_land_clearance = request.POST["result_land_clearance"]
        comment4_3 = request.POST["comment4_3"]
        Exception4_3 = request.POST["Exception4_3"]
        impact_environment = request.POST["impact_environment"]
        comment4_4 = request.POST["comment4_4"]
        Exception4_4 = request.POST["Exception4_4"]
        set_policies_waste = request.POST["set_policies_waste"]
        comment5_1 = request.POST["comment5_1"]
        Exception5_1 = request.POST["Exception5_1"]
        waste_generates = request.POST["waste_generates"]
        comment5_2 = request.POST["comment5_2"]
        Exception5_2 = request.POST["Exception5_2"]
        waste_generated_toxic = request.POST["waste_generated_toxic"]
        comment5_3 = request.POST["comment5_3"]
        Exception5_3 = request.POST["Exception5_3"]
        method_reduce_waste = request.POST["method_reduce_waste"]
        comment5_4 = request.POST["comment5_4"]
        Exception5_4 = request.POST["Exception5_4"]
        total_waste_generated = request.POST["total_waste_generated"]
        comment5_5 = request.POST["comment5_5"]
        Exception5_5 = request.POST["Exception5_5"]
        carbon_intensive = request.POST["carbon_intensive"]
        comment6_1 = request.POST["comment6_1"]
        Exception6_1 = request.POST["Exception6_1"]
        set_policies_gas_emission = request.POST["set_policies_gas_emission"]
        comment6_2 = request.POST["comment6_2"]
        Exception6_2 = request.POST["Exception6_2"]
        impact_environment_documented = request.POST["impact_environment_documented"]
        comment6_3 = request.POST["comment6_3"]
        Exception6_3 = request.POST["Exception6_3"]
        direct_ghg_emissions = request.POST["direct_ghg_emissions"]
        comment6_4 = request.POST["comment6_4"]
        Exception6_4 = request.POST["Exception6_4"]
        ghg_emissions = request.POST["ghg_emissions"]
        comment6_5 = request.POST["comment6_5"]
        Exception6_5 = request.POST["Exception6_5"]
        indirect_ghg_emissions_scope3 = request.POST["indirect_ghg_emissions_scope3"]
        comment6_6 = request.POST["comment6_6"]
        Exception6_6 = request.POST["Exception6_6"]
        indirect_ghg_emissions_scope4 = request.POST["indirect_ghg_emissions_scope4"]
        comment6_7 = request.POST["comment6_7"]
        Exception6_7 = request.POST["Exception6_7"]
        air_quality = request.POST["air_quality"]
        comment6_8 = request.POST["comment6_8"]
        Exception6_8 = request.POST["Exception6_8"]
        provide_detail_investment_technology = request.POST["provide_detail_investment_technology"]
        comment6_9 = request.POST["comment6_9"]
        Exception6_9 = request.POST["Exception6_9"]
        set_policies_biodiversity = request.POST["set_policies_biodiversity"]
        comment7_1 = request.POST["comment7_1"]
        Exception7_1 = request.POST["Exception7_1"]
        operations_biodiversity = request.POST["operations_biodiversity"]
        comment7_2 = request.POST["comment7_2"]
        Exception7_2 = request.POST["Exception7_2"]
        different_types_species = request.POST["different_types_species"]
        comment7_3 = request.POST["comment7_3"]
        Exception7_3 = request.POST["Exception7_3"]
        control_biodiversity = request.POST["control_biodiversity"]
        comment7_4 = request.POST["comment7_4"]
        Exception7_4 = request.POST["Exception7_4"]
        positive_biodiversity = request.POST["positive_biodiversity"]
        comment7_5 = request.POST["comment7_5"]
        Exception7_5 = request.POST["Exception7_5"]
        set_policies_circular_economy = request.POST["set_policies_circular_economy"]
        comment8_1 = request.POST["comment8_1"]
        Exception8_1 = request.POST["Exception8_1"]
        company_use_biodegradable_materials = request.POST["company_use_biodegradable_materials"]
        comment8_2 = request.POST["comment8_2"]
        Exception8_2 = request.POST["Exception8_2"]
        company_recyclable = request.POST["company_recyclable"]
        comment8_3 = request.POST["comment8_3"]
        Exception8_3 = request.POST["Exception8_3"]
        scarce_products = request.POST["scarce_products"]
        comment8_4 = request.POST["comment8_4"]
        Exception8_4 = request.POST["Exception8_4"]
        packaging_process = request.POST["packaging_process"]
        comment8_5 = request.POST["comment8_5"]
        Exception8_5 = request.POST["Exception8_5"]
        procuring_raw_materials = request.POST["procuring_raw_materials"]
        comment8_6 = request.POST["comment8_6"]
        Exception8_6 = request.POST["Exception8_6"]
        local_laws_regulations = request.POST["local_laws_regulations"]
        comment9_1 = request.POST["comment9_1"]
        Exception9_1 = request.POST["Exception9_1"]
        licenses_concerned_local_authorities = request.POST["licenses_concerned_local_authorities"]
        comment9_2 = request.POST["comment9_2"]
        Exception9_2 = request.POST["Exception9_2"]
        principle_adverse_impacts = request.POST["principle_adverse_impacts"]
        comment9_3 = request.POST["comment9_3"]
        Exception9_3 = request.POST["Exception9_3"]
        consequential_action = request.POST["consequential_action"]
        comment9_4 = request.POST["comment9_4"]
        Exception9_4 = request.POST["Exception9_4"]
        non_compliance_environmental_laws = request.POST["non_compliance_environmental_laws"]
        comment9_5 = request.POST["comment9_5"]
        Exception9_5 = request.POST["Exception9_5"]
        consequent_positive_environmental_impact = request.POST["consequent_positive_environmental_impact"]
        comment9_6 = request.POST["comment9_6"]
        Exception9_6 = request.POST["Exception9_6"]
        monitor_risks_opportunities = request.POST["monitor_risks_opportunities"]
        comment9_7 = request.POST["comment9_7"]
        Exception9_7 = request.POST["Exception9_7"]
        management_approach_environmental_assessment = request.POST["management_approach_environmental_assessment"]
        comment10_1 = request.POST["comment10_1"]
        Exception10_1 = request.POST["Exception10_1"]
        environmental_best_practices = request.POST["environmental_best_practices"]
        comment10_2 = request.POST["comment10_2"]
        Exception10_2 = request.POST["Exception10_2"]
        supply_chain = request.POST["supply_chain"]
        comment10_3 = request.POST["comment10_3"]
        Exception10_3 = request.POST["Exception10_3"]

        input_data = {
            'set_of_policies': set_of_policies,
            'comment1_1': comment1_1,
            'Exception1_1': Exception1_1,
            'keep_records': keep_records,
            'comment1_2': comment1_2,
            'Exception1_2': Exception1_2,
            'evaluation_exercise': evaluation_exercise,
            'comment1_3': comment1_3,
            'Exception1_3': Exception1_3,
            'reduce_consumption': reduce_consumption,
            'comment1_4': comment1_4,
            'Exception1_4': Exception1_4,
            'invested_renewable_sources': invested_renewable_sources,
            'comment1_5': comment1_5,
            'Exception1_5': Exception1_5,
            'set_of_strategies': set_of_strategies,
            'comment2_1': comment2_1,
            'Exception2_1': Exception2_1,
            'handling_raw_materials': handling_raw_materials,
            'comment2_2': comment2_2,
            'Exception2_2': Exception2_2,
            'dependence_raw_materials': dependence_raw_materials,
            'comment2_3': comment2_3,
            'Exception2_3': Exception2_3,
            'sourcing_raw_materials': sourcing_raw_materials,
            'comment2_4': comment2_4,
            'Exception2_4': Exception2_4,
            'use_recycled_materials': use_recycled_materials,
            'comment2_5': comment2_5,
            'Exception2_5': Exception2_5,
            'recyclable_packaging': recyclable_packaging,
            'comment2_6': comment2_6,
            'Exception2_6': Exception2_6,
            'set_of_policies_water': set_of_policies_water,
            'comment3_1': comment3_1,
            'Exception3_1': Exception3_1,
            'consume_water': consume_water,
            'comment3_2': comment3_2,
            'Exception3_2': Exception3_2,
            'face_risk_water_scarcity': face_risk_water_scarcity,
            'comment3_3': comment3_3,
            'Exception3_3': Exception3_3,
            'recycling_water_used_by_organisation': recycling_water_used_by_organisation,
            'comment3_4': comment3_4,
            'Exception3_4': Exception3_4,
            'mention_amount_of_water_recycle': mention_amount_of_water_recycle,
            'comment3_5': comment3_5,
            'Exception3_5': Exception3_5,
            'land_clearance': land_clearance,
            'comment4_1': comment4_1,
            'Exception4_1': Exception4_1,
            'set_policies_land_clearance': set_policies_land_clearance,
            'comment4_2': comment4_2,
            'Exception4_2': Exception4_2,
            'result_land_clearance': result_land_clearance,
            'comment4_3': comment4_3,
            'Exception4_3': Exception4_3,
            'impact_environment': impact_environment,
            'comment4_4': comment4_4,
            'Exception4_4': Exception4_4,
            'set_policies_waste': set_policies_waste,
            'comment5_1': comment5_1,
            'Exception5_1': Exception5_1,
            'waste_generates': waste_generates,
            'comment5_2': comment5_2,
            'Exception5_2': Exception5_2,
            'waste_generated_toxic': waste_generated_toxic,
            'comment5_3': comment5_3,
            'Exception5_3': Exception5_3,
            'method_reduce_waste': method_reduce_waste,
            'comment5_4': comment5_4,
            'Exception5_4': Exception5_4,
            'total_waste_generated': total_waste_generated,
            'comment5_5': comment5_5,
            'Exception5_5': Exception5_5,
            'carbon_intensive': carbon_intensive,
            'comment6_1': comment6_1,
            'Exception6_1': Exception6_1,
            'set_policies_gas_emission': set_policies_gas_emission,
            'comment6_2': comment6_2,
            'Exception6_2': Exception6_2,
            'impact_environment_documented': impact_environment_documented,
            'comment6_3': comment6_3,
            'Exception6_3': Exception6_3,
            'direct_ghg_emissions': direct_ghg_emissions,
            'comment6_4': comment6_4,
            'Exception6_4': Exception6_4,
            'ghg_emissions': ghg_emissions,
            'comment6_5': comment6_5,
            'Exception6_5': Exception6_5,
            'indirect_ghg_emissions_scope3': indirect_ghg_emissions_scope3,
            'comment6_6': comment6_6,
            'Exception6_6': Exception6_6,
            'indirect_ghg_emissions_scope4': indirect_ghg_emissions_scope4,
            'comment6_7': comment6_7,
            'Exception6_7': Exception6_7,
            'air_quality': air_quality,
            'comment6_8': comment6_8,
            'Exception6_8': Exception6_8,
            'provide_detail_investment_technology': provide_detail_investment_technology,
            'comment6_9': comment6_9,
            'Exception6_9': Exception6_9,
            'set_policies_biodiversity': set_policies_biodiversity,
            'comment7_1': comment7_1,
            'Exception7_1': Exception7_1,
            'operations_biodiversity': operations_biodiversity,
            'comment7_2': comment7_2,
            'Exception7_2': Exception7_2,
            'different_types_species': different_types_species,
            'comment7_3': comment7_3,
            'Exception7_3': Exception7_3,
            'control_biodiversity': control_biodiversity,
            'comment7_4': comment7_4,
            'Exception7_4': Exception7_4,
            'positive_biodiversity': positive_biodiversity,
            'comment7_5': comment7_5,
            'Exception7_5': Exception7_5,
            'set_policies_circular_economy': set_policies_circular_economy,
            'comment8_1': comment8_1,
            'Exception8_1': Exception8_1,
            'company_use_biodegradable_materials': company_use_biodegradable_materials,
            'comment8_2': comment8_2,
            'Exception8_2': Exception8_2,
            'company_recyclable': company_recyclable,
            'comment8_3': comment8_3,
            'Exception8_3': Exception8_3,
            'scarce_products': scarce_products,
            'comment8_4': comment8_4,
            'Exception8_4': Exception8_4,
            'packaging_process': packaging_process,
            'comment8_5': comment8_5,
            'Exception8_5': Exception8_5,
            'procuring_raw_materials': procuring_raw_materials,
            'comment8_6': comment8_6,
            'Exception8_6': Exception8_6,
            'local_laws_regulations': local_laws_regulations,
            'comment9_1': comment9_1,
            'Exception9_1': Exception9_1,
            'licenses_concerned_local_authorities': licenses_concerned_local_authorities,
            'comment9_2': comment9_2,
            'Exception9_2': Exception9_2,
            'principle_adverse_impacts': principle_adverse_impacts,
            'comment9_3': comment9_3,
            'Exception9_3': Exception9_3,
            'consequential_action': consequential_action,
            'comment9_4': comment9_4,
            'Exception9_4': Exception9_4,
            'non_compliance_environmental_laws': non_compliance_environmental_laws,
            'comment9_5': comment9_5,
            'Exception9_5': Exception9_5,
            'consequent_positive_environmental_impact': consequent_positive_environmental_impact,
            'comment9_6': comment9_6,
            'Exception9_6': Exception9_6,
            'monitor_risks_opportunities': monitor_risks_opportunities,
            'comment9_7': comment9_7,
            'Exception9_7': Exception9_7,
            'management_approach_environmental_assessment': management_approach_environmental_assessment,
            'comment10_1': comment10_1,
            'Exception10_1': Exception10_1,
            'environmental_best_practices': environmental_best_practices,
            'comment10_2': comment10_2,
            'Exception10_2': Exception10_2,
            'supply_chain': supply_chain,
            'comment10_3': comment10_3,
            'Exception10_3': Exception10_3,
        }

        context = {
            'input_data': input_data,
        }
        return render(request, 'environment_2.html')
    return render(request, 'environment_1.html')


def environment_2(request):
    return render(request, 'environment_2.html')


def social_1(request):
    return render(request, 'social_1.html')


