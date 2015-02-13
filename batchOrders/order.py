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
            },
            {
                'id': 56,
                'description': 'Joey',
                'batch_uuid': batch_2_uuid
            }
        ]
        if date == '2015-12-15':
            updated = [
                {
                    'id': 3,
                    'description': 'Dope',
                    'batch_uuid': batch_2_uuid
                },
                {
                    'id': 50,
                    'description': 'Hella',
                    'batch_uuid': batch_2_uuid
                }]
            orders += updated

        return orders
        ###########################################################################
        def createBatchID(self, batch_uuid):
        ###########################################################################
            # count the current batch_uuids to a dictionary
