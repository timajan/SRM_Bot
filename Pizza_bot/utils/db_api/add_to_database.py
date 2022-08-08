from utils.db_api.db_commands import add_item


async def add_items():
    await add_item(name="Піца 4 сезони",
                   category_name="🍕 Піца", category_code="Pizza",
                   description="\n \"Томатний\" соус,\n моцарела,\nгриби,\n помідори,\n оливки,\n шинка\n Ціна: 119 грн",
                   price="119",
                   photo="AgACAgIAAxkBAAIBA2Fkg4O2ZTMdiU20xjYCXeCIwNeQAAJNtTEbHMUgS8tJZaAd-WLWAQADAgADbQADIQQ"
                   )
    await add_item(name="Піца салямі",
                   category_name="🍕 Піца", category_code="Pizza",
                   description="\n \"Томатний\" соус,\n подвійна моцарела,\n подвійна салямі\n Ціна: 125 грн.",
                   price="125",
                   photo="AgACAgIAAxkBAAMMYWMxuf9zWGs0vuDdgGrWWwRm_pQAAvi3MRsSVRhLW8SfAaH-EvABAAMCAANtAAMhBA"
                   )
    await add_item(name="Піца з Лососем",
                   category_name="🍕 Піца", category_code="Pizza",
                   description="\nВершковий соус,\n моцарела,\n лосось,\n помідор,\n каперси,"
                               "\n пармезан,\n рукола\n Ціна: 146 грн.",
                   price="146",
                   photo="AgACAgIAAxkBAAMGYWMxStTRybGAmAtpbet5AAG9aHfaAALwtzEbElUYS-oYQ-qotEbHAQADAgADbQADIQQ"
                   )
    await add_item(name="Піца Чорізо",
                   category_name="🍕 Піца", category_code="Pizza",
                   description="\n\"Томатний\" соус,\n моцарела,\n салямі чорізо ПОДВІЙНА,"
                               "\n болгарський перець,\nгриби,\n пармезан,\n кунжут\n Ціна: 139 грн.",
                   price="139",
                   photo="AgACAgIAAxkBAAMSYWMyFwMMhE6EukED_84yHEeTEHQAAhK3MRsLERlLCXbxMAztoHoBAAMCAANtAAMhBA"
                   )
    await add_item(name="Піца 4 мяса",
                   category_name="🍕 Піца", category_code="Pizza",
                   description="\n\"Томатний\" соус,\n моцарела,\n бекон,\n шинка,\n салямі,"
                               "\n ковбаски\n Ціна: 139 грн.",
                   price="139",
                   photo="AgACAgIAAxkBAAMQYWMx2OK6UN9ABh9ue27ghVQ9BUQAAvO3MRsSVRhLeSg3kPtMwWMBAAMCAANtAAMhBA"
                   )

