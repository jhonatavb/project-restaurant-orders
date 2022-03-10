import csv
from collections import defaultdict

def reader_csv(path):
    with open(path, "r") as file:
        restaurant_data = csv.reader(file)
        order_data = []

        for order in restaurant_data:
            order_data.append(order)

        return order_data


def order_history(order, day):
    order_log = {
        "frequency": set(day),
        "orders": defaultdict(int),
    }

    order_log["orders"][order] += 1
    return order_log


def restaurant_report(history):
    report = dict()
    report["days_worked"] = set()
    for client, order, day in history:
        report["days_worked"].add(day)
        if client not in report:
            report[client] = order_history(order, day)
        else:
            report[client]["orders"][order] += 1
            report[client]["frequency"].add(day)

    return report


def analyze_log(path_to_file):
    menu = {"hamburguer", "pizza", "coxinha", "misto-quente"}
    history = reader_csv(path_to_file)
    report = restaurant_report(history)

    days_worked = report["days_worked"]
    maria_orders = report["maria"]["orders"]
    joao_orders = report["joao"]["orders"]
    joao_frequency = report["joao"]["frequency"]
    arnaldo_ordered = report["arnaldo"]["orders"]["hamburguer"]

    highest_order_maria = max(maria_orders, key=maria_orders.get)
    not_ordered_joao = menu.difference(set(joao_orders))
    without_frequency_joao = days_worked.difference(joao_frequency)

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(
            f"{highest_order_maria}\n"
            f"{arnaldo_ordered}\n"
            f"{not_ordered_joao}\n"
            f"{without_frequency_joao}\n"
        )

