from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import argparse
import json

def main():
    parser = argparse.ArgumentParser(description='Test AWS ES search capability')
    parser.add_argument('--rn', metavar='R', help='AWS region', default='us-east-1')
    parser.add_argument('--ak', metavar='AK', help='aws access key')
    parser.add_argument('--sk', metavar='AS', help='aws secret key')

    args = parser.parse_args()

    awsauth = AWS4Auth(args.ak, args.sk, args.rn, 'es')

    es = Elasticsearch(
        hosts = [{'host': 'search-students-cuqolvi4pazv2l33qlhlpr4ofq.us-east-1.es.amazonaws.com', 'port': 443}],
        http_auth = awsauth,
        use_ssl = True,
        verify_certs = True,
        connection_class = RequestsHttpConnection
    )

    print (json.dumps(es.search(q='sex:M AND last_name:White'), indent=2))

if __name__ == "__main__":
    main()
