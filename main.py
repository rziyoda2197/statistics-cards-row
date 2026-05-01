class StatisticsCard:
    def __init__(self, title, value, icon, color):
        self.title = title
        self.value = value
        self.icon = icon
        self.color = color

class Dashboard:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def display_cards(self):
        for i, card in enumerate(self.cards):
            print(f"Card {i+1}:")
            print(f"Title: {card.title}")
            print(f"Value: {card.value}")
            print(f"Icon: {card.icon}")
            print(f"Color: {card.color}")
            print("------------------------")

# Ustunlar uchun ma'lumotlar
ustunlar = [
    {"title": "Klientlar", "value": 1000, "icon": "fa fa-users", "color": "blue"},
    {"title": "Sotuvlar", "value": 5000, "icon": "fa fa-shopping-cart", "color": "green"},
    {"title": "Mablaglar", "value": 10000, "icon": "fa fa-money", "color": "red"}
]

# Dashboard yaratish
dashboard = Dashboard()

# Kardlar qo'shish
for ustun in ustunlar:
    card = StatisticsCard(ustun["title"], ustun["value"], ustun["icon"], ustun["color"])
    dashboard.add_card(card)

# Kardlar ko'rsatish
dashboard.display_cards()
