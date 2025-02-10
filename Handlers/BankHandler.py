from Classes.Bank import Bank
from Utils.EventTools import authorized


@authorized
def bank(event, context, conn):
    bank_class = Bank(conn)

    methods = {
        "GET": bank_class.list_banks,
        "POST": bank_class.add_bank,
        "PUT": bank_class.update_bank,
        "DELETE": bank_class.delete_bank
    }

    method_to_be_executed = methods.get(event["httpMethod"])
    return method_to_be_executed(event)
