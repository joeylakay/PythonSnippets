#!/usr/bin/env python

import uuid
import order

# Note: Orders need to be batched together in groups of 3. 

###############################################################################
def challenge1():
###############################################################################

    # Challenge 1: return the open uuid 
    # it's the one that does not have 3 orders associated w/ it

    # temp dictionary to hold batch_uuid and number of instances
    batch_uuids = {}

    # get orders
    orders = order.Order().getOrders()

    # loop through orders and update temp batch_uuids dictionary
    for o in orders:
        if o['batch_uuid'] in batch_uuids:
            batch_uuids[o['batch_uuid']] += 1
        else:
            batch_uuids[o['batch_uuid']] = 1

    # loop through key / value pairs in batch_uuids and see what is up
    for k,v in batch_uuids.items():
        print str(k) + ': ' + str(v)

    return False

###############################################################################
def challenge2():
###############################################################################

    # Challenge 2: 
    # determine if you need to create a new uuid, and if you need to,
    # create the uuid and return that

    # temp dictionary to hold batch_uuid and number of instances
    batch_uuids = {}

    # get orders
    orders = order.Order().getOrders(date="2015-12-15")
    return False


###############################################################################
def main():
###############################################################################

    challenge1()
    challenge2()

###############################################################################
if __name__ == '__main__':
    main()
