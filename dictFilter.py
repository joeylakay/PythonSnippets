#!/usr/bin/env python

import uuid

# Problem: Orders need to be batched together in groups of 3

###############################################################################
def getOrders():
###############################################################################
    batch_1_uuid = '4c606d32-0cb9-4b0b-9ae5-db33118ba69c'
    batch_2_uuid = 'b3386c00-11ba-4703-ae8b-76020ba46602'
    return [
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
            'id': 1,
            'description': 'Dude',
            'batch_uuid': batch_1_uuid
        }
    ]


###############################################################################
def main():
###############################################################################

    orders = getOrders()
    print orders


###############################################################################
if __name__ == '__main__':
    main()
