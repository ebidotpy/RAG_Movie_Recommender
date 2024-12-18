import weave
from chat_model import movie_chat_model


weave.init('film-search')

chat_model_obj = movie_chat_model()
query = "Recommend some films similar to star wars movies but not part of the star wars universe"

query_constructor = chat_model_obj.query_constructor.invoke(query)

print(f"query_constructor: {query_constructor}")

print("response")
for chunk in chat_model_obj.rag_chain_with_source.stream(query):
  print(chunk)