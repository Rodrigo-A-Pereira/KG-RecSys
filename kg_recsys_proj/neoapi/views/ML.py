from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from neoapi.serializer import CardSerializerNeo, PersonSerializerNeo
from neoapi.models import Card, Person
from django.http import Http404, HttpResponse
import neomodel
from neomodel import db
from PykeenMLFlowWrapper import load_model
import mlflow

mlflow.set_tracking_uri("http://mlflow-server:5000")


class RecomendationList(APIView):
    def get(self, request, pid_slug, format=None):
        #try:
            model = load_model("recsys_transe","Production")
            print(str(pid_slug))
            predict_list = model.predict([(str(pid_slug), "BOUGHT")])[0].tolist()

            ##This next part should be done only by cypher query, but i cant find a good way to maintain order in cypher
            ##list compreension
            bought_cards,  meta = db.cypher_query(f"Match (p:Person {{uid:'{pid_slug}'}})-[BOUGHT]->(c:Card) return c.code", "")
            bought_cards_flat = [element for sublist in bought_cards for element in sublist]

            client_list, meta = db.cypher_query(f"Match (p:Person) return p.uid", "")
            client_list_flat = [element for sublist in client_list for element in sublist]
            
            if request.query_params.get('max_len'):
                recomended_codes= [item for item in predict_list if (item not in bought_cards_flat and item not in client_list_flat)][:int(request.query_params.get('max_len'))]
            else:
                recomended_codes= [item for item in predict_list if (item not in bought_cards_flat and item not in client_list_flat)][:20]
            
            card_recomended = []
            for code in recomended_codes:
                card_recomended.append(Card.nodes.get(code__exact=code))
            
            card_serializer = CardSerializerNeo(card_recomended, many=True)

            if request.query_params.get('max_len'):
                data_to_return = card_serializer.data[:int(request.query_params.get('max_len'))]
            else:
                data_to_return =  card_serializer.data
            
            return Response(data_to_return)
        #except:
        #    return HttpResponse(status=500)


class TrainingFile(APIView):
    def get(self, requests, format=None):
        results, meta = db.cypher_query("MATCH (a:Person)-[:BOUGHT]->(b:Card) RETURN a.uid, b.code")

        with open("/ML_dir/trainingFile.txt", "w") as file:
                for r in results:
                    file.write(f'{r[0]}\tBOUGHT\t{r[1]}\n')

        return Response("Written in file ")