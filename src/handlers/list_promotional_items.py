import json
import logging
import os
import psycopg2


log_level = 'DEBUG' if os.environ['ENV'] == 'dev' else 'INFO'

logger = logging.getLogger()
logger.setLevel(log_level)

logger.debug(psycopg2.__version__)

# conn = psycopg2.connect(
#     port=3306,
#     host=os.environ['DB_HOST'],
#     dbname=os.environ['DB_USER_NAME'],
#     user=os.environ['DB_PASSWORD'],
#     password="postgres")
# cur = conn.cursor()
# cur.execute(
#     "CREATE TABLE items (id serial PRIMARY KEY, name varchar, category varchar);")
# cur.close()
# conn.close()


def listPromotionalItems(limit):
    logging.debug(limit)
    # TODO db connection

    data = [
        {'item_id': '0001',
         'item_name': 'サンプル品1', 'category': '販促物'},
        {'item_id': '0002',
         'item_name': 'サンプル品2', 'category': '販促物'},
        {'item_id': '0003',
         'item_name': 'サンプル品3', 'category': '販促物'},
        {'item_id': '0004',
         'item_name': 'サンプル品4', 'category': '販促物'},
        {'item_id': '0005',
         'item_name': 'サンプル品5', 'category': '販促物'}
    ]
    return data


def handler(event, context):
    try:
        logging.info(event)
        logging.info(context)

        query_string_params = event.get('queryStringParameters')
        limit = query_string_params['limit'] if (query_string_params and query_string_params.get(
            'limit')) else os.environ['DEFAULT_DATA_LIMIT']

        result = listPromotionalItems(limit)
        logging.debug(result)
        return {
            'isBase64Encoded': False,
            'statusCode': 200,
            # ensure_ascii: 日本語文字化け対応
            'body': json.dumps(result, ensure_ascii=False)
        }

    except Exception as e:
        logging.error(e)
