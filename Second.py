class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request):
        for i in request:
            print(i)
            if 'receipt' in i:
                self.data[f'{i[0]}'] = i[-1]
            elif 'shipment' in i:
                for element in self.data:
                    if element in i:
                        self.data[element] = self.data.get(element) - i[-1]

    def run(self, args):
        self.process_request(args)

manager = WarehouseManager()

requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

manager.run(requests)

print(manager.data)