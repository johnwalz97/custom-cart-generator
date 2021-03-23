import json

from flask import (
    Flask,
    session,
    redirect,
    render_template,
    request,
    url_for,
    send_from_directory,
    jsonify,
)
import shopify

import config
from helpers import shopify_auth_required, shopify_webhook_auth_required
from models import Shop

app = Flask(__name__, template_folder='../public', static_folder='../public')
app.secret_key = 'Pow54321!'
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/<path:path>")
def home(path):
    return send_from_directory('../public', path)


@app.route('/')
@shopify_auth_required
def index(**kwargs):
    return render_template('index.html')


@app.route('/shop_data')
def shop_data(**kwargs):
    shop = kwargs['shop']

    shopify_session = shopify.Session(shop.shop, '2020-10', shop.token)
    shopify.ShopifyResource.activate_session(shopify_session)

    discounts = shopify.PriceRule.find()
    products = shopify.Product.find()

    return jsonify({'products': products, 'discounts': discounts})


@app.route('/uninstall', methods=['POST'])
@shopify_webhook_auth_required
def uninstall():
    webhook_topic = request.headers.get('X-Shopify-Topic')
    webhook_payload = request.get_json()
    print(f"webhook call received {webhook_topic}:\n{json.dumps(webhook_payload, indent=4)}")

    return "OK"


@app.route('/customer_data/request', methods=['POST'])
@shopify_webhook_auth_required
def customer_data_request():
    webhook_topic = request.headers.get('X-Shopify-Topic')
    webhook_payload = request.get_json()
    print(f"webhook call received {webhook_topic}:\n{json.dumps(webhook_payload, indent=4)}")
    return "OK"


@app.route('/customer_data/delete', methods=['POST'])
@shopify_webhook_auth_required
def customer_data_delete():
    webhook_topic = request.headers.get('X-Shopify-Topic')
    webhook_payload = request.get_json()
    print(f"webhook call received {webhook_topic}:\n{json.dumps(webhook_payload, indent=4)}")
    return "OK"


@app.route('/shop_data/delete', methods=['POST'])
@shopify_webhook_auth_required
def shop_data_delete():
    webhook_topic = request.headers.get('X-Shopify-Topic')
    webhook_payload = request.get_json()
    print(f"webhook call received {webhook_topic}:\n{json.dumps(webhook_payload, indent=4)}")
    return "OK"


if __name__ == '__main__':
    context = (
        '/etc/letsencrypt/live/customcartz.us/cert.pem',
        '/etc/letsencrypt/live/customcartz.us/privkey.pem',
    )
    app.run(debug=True, host='customcartz.us', port=443, ssl_context=context)
