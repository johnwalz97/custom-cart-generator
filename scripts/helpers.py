import os

import shopify

from backend.libs.shopify_admin import activate_session


os.environ["SHOPIFY_API_KEY"] = "5d9c7da289fe90dcde12d6cdc8cf3a45"
os.environ["SHOPIFY_API_SECRET"] = "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"
os.environ["SHOPIFY_API_VERSION"] = "2020-10"

activate_session("awesome-test-fake-store.myshopify.com", "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")
