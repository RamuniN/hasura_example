import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

graphql_endpoint = "http://localhost:8888/v1/graphql"


###############################################################################################
# GraphQL from python
###############################################################################################

gq = Client(transport=RequestsHTTPTransport(url=graphql_endpoint))

# Using the query string
query = gql("""query getAccounts {
  account {
    id
    email
  }
}""")

data = gq.execute(query)
print(data)


###############################################################################################
from example.utils import file_to_gql_documents

QUERIES = 'query.graphql'
MUTATIONS = 'mutation.graphql'
GRAPHQL_PATH = Path(__file__).parent

queries_path = Path(f'{GRAPHQL_PATH}/{QUERIES}').resolve()
mutations_path = Path(f'{GRAPHQL_PATH}/{MUTATIONS}').resolve()

queries, mutations = map(file_to_gql_documents, [queries_path, mutations_path])

# Using the queries from a file
data = gq.execute(queries.get('getApplicationByAccountID'),{"account_id":"e2815401-beb5-4c7c-8a6f-d1375cea0fdc"})
print(data)