class Order():
    ###########################################################################
    def getOrders(self, date=None):
    ###########################################################################
        batch_1_uuid = '4c606d32-0cb9-4b0b-9ae5-db33118ba69c'
        batch_2_uuid = 'b3386c00-11ba-4703-ae8b-76020ba46602'
        orders = [
            {
                'id': 42,
                'description': 'Awesome',
                'batch_uuid': batch_1_uuid
            },
            {
                'id': 101,
                'description': 'Rad',
                'batch_uuid': batch_1_uuid
            },
            {
                'id': 1,
                'description': 'Stoked',
                'batch_uuid': batch_2_uuid
            },
            {
                'id': 18,
                'description': 'Dude',
                'batch_uuid': batch_1_uuid
            }
        ]
        if date = '2015-12-15':
            print 'hi'
        return orders
