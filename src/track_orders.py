from collections import defaultdict


class TrackOrders:
    def __init__(self):
        self.data = []
        self.menu = set()
        self.working_days = defaultdict(int)
        self.costumer_info = dict()

    def __len__(self):
        return len(self.data)

    def add_new_order(self, costumer, order, day):
        self.menu.add(order)
        log = [costumer, order, day]
        self.data.append(log)
        self.working_days[day] += 1
        costumer_log = dict()
        costumer_log["orders"] = defaultdict(int)
        costumer_log["orders"][order] += 1
        costumer_log["visit"] = set()
        costumer_log["visit"].add(day)
        self.costumer_info[costumer] = log

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_fav_order = max(
            self.costumer_info[costumer]["orders"],
            key=self.costumer_info[costumer]["orders"].get,
        )

        return costumer_fav_order

    def get_never_ordered_per_costumer(self, costumer):
        nerver_ordered = self.menu.difference(
            set(self.costumer_info[costumer]["orders"])
        )

        return nerver_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        never_visited = set(self.working_days)
        never_visited = never_visited.difference(
            self.costumer_info[costumer]["visit"]
        )

        return never_visited

    def get_busiest_day(self):
        return max(self.working_days, key=self.working_days.get)

    def get_least_busy_day(self):
        return min(self.working_days, key=self.working_days.get)
