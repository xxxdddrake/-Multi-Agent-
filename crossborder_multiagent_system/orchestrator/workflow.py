import asyncio

from agents.market_agent import MarketAgent
from agents.product_agent import ProductAgent
from agents.seo_agent import SEOAgent
from agents.ads_agent import AdsAgent
from agents.customer_agent import CustomerServiceAgent
from agents.analytics_agent import AnalyticsAgent

market_agent = MarketAgent()
product_agent = ProductAgent()
seo_agent = SEOAgent()
ads_agent = AdsAgent()
customer_agent = CustomerServiceAgent()
analytics_agent = AnalyticsAgent()

async def run_full_workflow(product, market):

    payload = {
        "product": product,
        "market": market
    }

    results = await asyncio.gather(
        market_agent.run(payload),
        product_agent.run(payload),
        seo_agent.run(payload),
        ads_agent.run(payload),
        customer_agent.run(payload),
        analytics_agent.run(payload)
    )

    return {
        "market_analysis": results[0],
        "product_strategy": results[1],
        "seo_strategy": results[2],
        "ads_strategy": results[3],
        "customer_service": results[4],
        "analytics": results[5]
    }