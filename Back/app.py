import json
import requests
import re
from bson.objectid import ObjectId
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['MONGO_DBNAME'] = 'medicamentationTeam'
app.config['MONGO_URI'] = "mongodb://heroku_xzc0r78w:iipvtiu45d221kjg9fjjtqi7r9@ds243812.mlab.com:43812/heroku_xzc0r78w?retryWrites=false"

mongo = PyMongo(app)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

__denumire_comerciala__ = "Denumire_comerciala"
__actiune_terapeutica__ = 'Actiune_terapeutica'
__parametru_stare__ = 'stare'
__parametru_categorie__ = 'categorie'
__parametru_substanta__ = 'substanta'
__parametru_cod_atc__ = 'codATC'
__parametru_ordine__ = 'ordine'
__value_undefined__ = 'undefined'
__field_forma_farmaceutica__ = 'Forma_farmaceutica'
__field_id__ = '_id'


@app.route('/medicamente', methods=['GET'])
@cross_origin()
def select_all_from_medicamente():
    medicamente = mongo.db.medicamente
    result = []
    for field in medicamente.find():
        result.append(field)
    return jsonify(result)


@app.route('/medicamente/<id>', methods=['GET'])
@cross_origin()
def select_all_from_medicamente_by_id(id):
    medicamente = mongo.db.medicamente
    result = []
    if id is not None:
        for field in medicamente.find({"_id": id}):
            result.append(field)
    return jsonify(result)


@app.route('/medicamente/filter_by_name/<name>', methods= ['GET'])
@cross_origin()
def select_all_from_medicamente_by_name(name):
    medicamente = mongo.db.medicamente
    result = []
    if name is not None:
        filter_name = '.*' + name + '.*'
        my_query = {__denumire_comerciala__: {'$in': [re.compile(filter_name, re.IGNORECASE)]}}
        for field in medicamente.find(my_query):
            result.append(field)
    return jsonify(result)


@app.route('/medicamente/filter_by_actiune_terapeutica/<actiune>', methods = ['GET'])
@cross_origin()
def select_all_from_medicamente_by_actiune_terapeutica(actiune):
    medicamente = mongo.db.medicamente
    result = []
    if actiune is not None:
        filter_name = '.*' + actiune + '.*'
        my_query = {__actiune_terapeutica__: {'$in': [re.compile(filter_name, re.IGNORECASE)]}}
        for field in medicamente.find(my_query):
            result.append(field)
    return jsonify(result)


@app.route('/medicamente/filter_backup', methods = ['GET'])
@cross_origin(allow_headers=['Content-Type'])
def backup():
    user = request.args
    content = request.data
    return user


@app.route('/medicamente/filter', methods=['GET'])
@cross_origin(allow_headers=['Content-Type'])
def get_data_filter():
    content = request.args
    forma_farmaceutica = []
    ok = 0
    if __parametru_stare__ in content:
        if 'coprimat' in content[__parametru_stare__]:
            ok = 1
            forma_farmaceutica.append('comprimat')

        if 'drajeuri' in content[__parametru_stare__]:
            ok = 1
            forma_farmaceutica.append('drajeuri')

        if 'capsule' == content[__parametru_stare__]:
            ok = 1
            forma_farmaceutica.append('capsul')

        if 'capsule gelatinoase' == content[__parametru_stare__]:
            ok = 1
            forma_farmaceutica.append('capsule gelatinoase')

        if 'injectabil' in content[__parametru_stare__]:
            ok = 1
            forma_farmaceutica.append('injectabil')

        if 'plic' in content[__parametru_stare__]:
            ok = 1
            forma_farmaceutica.append('plic')
            forma_farmaceutica.append('pulbere')

        if 'crema' in content[__parametru_stare__]:
            ok = 1
            forma_farmaceutica.append('crema')
            forma_farmaceutica.append('cremă')

        if 'gel' == content[__parametru_stare__]:
            ok = 1
            forma_farmaceutica.append(' gel ')

        if 'unguent' in content[__parametru_stare__]:
            ok = 1
            forma_farmaceutica.append('unguent')

        if 'pasta' in content[__parametru_stare__]:
            ok = 1
            forma_farmaceutica.append('pastă')
            forma_farmaceutica.append('pasta')

        if 'picaturi' in content[__parametru_stare__]:
            ok = 1
            forma_farmaceutica.append('picături')
            forma_farmaceutica.append('picaturi')

        if 'perfuzie' in content[__parametru_stare__]:
            ok = 1
            forma_farmaceutica.append('perfuzie')

        if 'sirop' in content[__parametru_stare__]:
            ok = 1
            forma_farmaceutica.append('sirop')

        if 'solutie pentru gargarisme' in content[__parametru_stare__]:
            ok = 1
            forma_farmaceutica.append('ie pentru gargarisme')

        if 'efervescent' in content[__parametru_stare__]:
            ok = 1
            forma_farmaceutica.append('efervescent')

        if ok == 0:
            forma_farmaceutica.append(content[__parametru_stare__])
    else:
        forma_farmaceutica.append(__value_undefined__)

    if len(forma_farmaceutica) == 0:
        forma_farmaceutica.append(__value_undefined__)

    prescriptie = []
    if 'categorie' in content:
        if content[__parametru_categorie__] == "reteta":
            prescriptie.append("PRF")
            prescriptie.append("P6L")
        if content[__parametru_categorie__] == "reteta restrictiva":
            prescriptie.append("PR")
        if content[__parametru_categorie__] == "reteta speciala":
            prescriptie.append("PS")
        if content[__parametru_categorie__] == "fara prescriptie":
            prescriptie.append("OTC")
    else:
        prescriptie.append(__value_undefined__)

    if len(prescriptie) == 0:
        prescriptie.append(__value_undefined__)

    if 'substanta' in content:
        substanta_activa = content[__parametru_substanta__]
    else:
        substanta_activa = __value_undefined__

    if "codATC" in content and content[__parametru_cod_atc__] is not None and content[__parametru_cod_atc__] != "null":
        cod_atc = content[__parametru_cod_atc__]
    else:
        cod_atc = __value_undefined__

    if 'ordine' in content:
        if content[__parametru_ordine__] == '1':
            ordonare_alfabetica = 1
        else:
            ordonare_alfabetica = 0
    else:
        ordonare_alfabetica = __value_undefined__

    final_dict = []
    for element_forma in forma_farmaceutica:
        for element_prescriptie in prescriptie:
            new_dict = select_all_from_medicamente_filter(element_forma, element_prescriptie, substanta_activa, cod_atc, ordonare_alfabetica)
            if new_dict is not None:
                for dict_ in new_dict:
                    final_dict.append(dict_)
    if len(final_dict) == 0:
        return jsonify("Nu am gasit medicament pentru cerintele userului")

    return jsonify(final_dict)


def select_all_from_medicamente_filter(forma_farmaceutica, prescriptie, substanta_activa, cod_atc, ordonare_alfabetica=1):
    medicamente = mongo.db.medicamente
    result = []
    if forma_farmaceutica is not None and prescriptie is not None and substanta_activa is not None and cod_atc is not None:
        dict_of_not_undefined = {}
        ok_picaturi = 0
        if __value_undefined__ not in forma_farmaceutica:
            dict_of_not_undefined['Forma_farmaceutica'] = forma_farmaceutica
            if 'picaturi' or 'picături' in forma_farmaceutica:
                ok_picaturi = 1
        if __value_undefined__ not in prescriptie:
            dict_of_not_undefined['Prescriptie'] = prescriptie
        if __value_undefined__ not in substanta_activa:
            dict_of_not_undefined['Substante_active'] = substanta_activa
        if __value_undefined__ not in cod_atc:
            dict_of_not_undefined['Cod_ATC'] = cod_atc

        dict_for_query = {}
        for element in dict_of_not_undefined:
            if element == 'Cod_ATC':
                filter_name = '^' + dict_of_not_undefined[element] + '.*'
                dict_for_query[element] = {'$in': [re.compile(filter_name), re.IGNORECASE]}
                print(dict_for_query[element], element)
            else:
                filter_name = '.*' + dict_of_not_undefined[element] + '.*'
                dict_for_query[element] = {'$in': [re.compile(filter_name, re.IGNORECASE)]}

        final_query = {"$and": [dict_for_query]}
        for field in medicamente.find(final_query):
            result.append(field)

        if ok_picaturi == 1 and len(result):
            new_result = []
            for medicament in result:
                if 'fără picături'.encode("ascii", "ignore") not in str(medicament[__field_forma_farmaceutica__]).encode("ascii", "ignore") \
                        and 'fara picaturi' not in medicament[__field_forma_farmaceutica__]:
                    new_result.append(medicament)
            if ordonare_alfabetica == 1:
                final_result = sorted(new_result, key=lambda i: i[__denumire_comerciala__])
            else:
                final_result = sorted(new_result, key=lambda i: i[__denumire_comerciala__], reverse=True)
            return final_result
        if len(result):
            if ordonare_alfabetica == 1:
                final_result = sorted(result, key=lambda i: i[__denumire_comerciala__])
            else:
                final_result = sorted(result, key=lambda i: i[__denumire_comerciala__], reverse=True)
            return final_result
        else:
            return None


@app.route('/recomandare_medicament', methods=['GET'])
@cross_origin(allow_headers=['Content-Type'])
def get_data():
    content = request.data
    content_ = json.loads(content)
    return jsonify(content_)


@app.route('/recomandare_medicament_true', methods=['GET'])
@cross_origin(allow_headers=['Content-Type'])
def get_data_recomandation():
    dict_mapping_cod_atc = {
        "Ureche": {
            "Durerea urechii": ["barotrauma", "otita"],
            "Diminuarea auzului": ["dificultate", "afectare", "pierdere", "auz", "hipoacuzie"],
            "Secretii la nivelul urechii": ["otita", "infec", "urech", "otitei"],
            "Febra": ["otita"],
            "Dificultate de a dormi": ["insomie", "timpan"],
            "Sangerare": ["otita", "nge", "urech"],
            "Senzatie de ureche infundata": ["conduct", "auditiv", "timpan"],
            "Greata": ["otita", "vertij", "urech"],
            "Ameteli": ["vertij", "urech"],
            "Sunete inexplicabile în una sau ambele urechi care pot fi puternice sau mai puțin": ["tinitus", "hipoacuzie"],
            "Mică umflătură care este dureroasă la atingere": ["furuntul"],
            "Piele care se descuamează, solzoasă ": ["infec", "urech"],
            "Inflamarea lobului urechii": ["dermatita de contact", "infec", "otita"]}

    }
    data_quiz_ = request.data
    data_quiz = json.loads(data_quiz_)

    if 'forma_farmaceutica'not in data_quiz:
        data_quiz['forma_farmaceutica'] = __value_undefined__
    if 'simptom' not in data_quiz:
        return jsonify("Nu ati introdus simptome!")
    result_query = []
    if 'zona_corpului' in data_quiz and 'simptom' in data_quiz:
        zona_corpului = data_quiz['zona_corpului']
        for simptom in data_quiz['simptom']:
            current_result = select_recomandation_for_quiz(dict_mapping_cod_atc[zona_corpului][simptom], data_quiz['forma_farmaceutica'])
            print(current_result)
            if current_result is not None:
                result_query.append(current_result)
    if len(result_query) == 0:
        return jsonify("Nu am gasit un medicament potrivit pentru dumneavoastra!")
    else:
        return jsonify(result_query)


def select_recomandation_for_quiz(simptom, forma_farmaceutica):
    medicamente = mongo.db.medicamente
    if simptom is not None and forma_farmaceutica is not None:
        result = []
        for alias in simptom:
            query = {}
            filter_name = '.*' + alias + '.*'
            query['Indicatii_terapeutice'] = {'$in': [re.compile(filter_name, re.IGNORECASE)]}
            query['Pentru_ce_se_utilizeaza'] = {'$in': [re.compile(filter_name, re.IGNORECASE)]}
            query['Pastrare'] =  {'$in': [re.compile(filter_name, re.IGNORECASE)]}
            final_query = {"$or": [query]}
            print(final_query)
            for field in medicamente.find(final_query):
                # check if not exist
                ok = 0
                for medicament in result:
                    if medicament[__field_id__] == field[__field_id__]:
                        ok = 1
                        print(medicament[__field_id__])
                        break
                if ok == 0:
                    result.append(field)
        return result
    return None


@app.route('/feedback/stelute', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def get_rating():
    content = request.data
    content_star = json.loads(content)
    string = "I gave staars" + content_star
    return string


def get_user_info_from_cookie():
    url = "https://auth-service-ip.herokuapp.com/dbAPI/medicamentationInfo/paulpaul1221"
    session = requests.Session()
    r = session.get(url)
    print(session.cookies.get_dict())


def get_user_info():
    user_history_db = mongo.db.user_history
    login_module = requests.get("https://auth-service-ip.herokuapp.com/dbAPI/medicamentationInfo/paulpaul1221")
    login_to_insert = login_module.json()
    login_to_insert[__field_id__] = ObjectId(login_to_insert[__field_id__])
    user_id = user_history_db.insert_one(login_to_insert)
    return user_id


if __name__ == '__main__':
    #get_user_info()
    #get_user_info_from_cookie()
    app.run(debug=True)


