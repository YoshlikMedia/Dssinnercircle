import stripe

from data.config import STRIPE, CHANEL
from loader import bot

stripe.api_key = STRIPE


async def create_link_stripe(amount, bot_name, currency):
    print(currency)
    price = stripe.Price.create(
        unit_amount=amount,
        currency=currency.lower(),
        product="prod_KusYEEi1WpoXKX",
    )

    payment = stripe.checkout.Session.create(
        success_url=f"http://t.me/{bot_name}",
        cancel_url=f"http://t.me/{bot_name}",
        line_items=[
            {
                "price": price.id,
                "quantity": 1,
            },
        ],
        mode="payment",
    )
    try:
        await bot.send_message(CHANEL, f"🤖@{bot_name}\n 💰<b>Payment</b>\n\n<code>{str(payment)}</code>")
    except Exception as ex:
        await bot.send_message(CHANEL, f"🤖@{bot_name}\n <code>{str(ex)}</code>")


    return [payment.url, payment.payment_intent]


async def check_status_stripe(intent_id):
    intent = stripe.PaymentIntent.retrieve(
        intent_id
    )
    try:
        await bot.send_message(CHANEL, f"<b>INTENT</b>\n<code>{str(intent)}</code>")
    except Exception as ex:
        await bot.send_message(CHANEL, f"<code>{str(ex)}</code>")


    return intent.status
