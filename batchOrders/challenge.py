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
        if v % 3 != 0:
            print str(k) + ': ' + str(v) + ' this is the open pair.'

    return False

###############################################################################
def challenge2():
###############################################################################

    # Challenge 2: 
    # determine if you need to create a new uuid, and if you need to,
    # create the uuid and return that

    # temp dictionary to hold batch_uuid and number of instances
    batch_uuids = {}

    # orders = order.Order().getOrders(date="2015-12-15")
    orders = order.Order().getOrders()
    # return False

        # loop through orders and update temp batch_uuids dictionary
    for o in orders:
        if o['batch_uuid'] in batch_uuids:
            batch_uuids[o['batch_uuid']] += 1
        else:
            batch_uuids[o['batch_uuid']] = 1   
  
        # loop through key / value pairs in batch_uuids
    for k,v in batch_uuids.items():

            # if the returned value isn't 0 
        if v % 3 != 0:

            # we have room to add orders to that batch_uuid.  meaning there are either 1 or 2 orders assigned a certain batch_uuid
            print "There are ", v, " orders assigned to this batch_uuid: ", k, "I don't need to create a new uuid yet."
            for o in orders:
                if o['batch_uuid'] in batch_uuids:
                    batch_uuids[o['batch_uuid']] += 1  
            break
                
            # if the returned value is 0, there are three orders or some number of orders divisible by three 
            # so we need to generate a new uuid and assign it a value of 1 in the temp dict
        else:
            print "There are ", v, " orders  and I need to create a new uuid."   
            new_uuid = str(uuid.uuid4())    
            batch_uuids[str(new_uuid)] = 1
            print "This is the new_uuid ", new_uuid

            orders.append(['batch_uuid', new_uuid])
            print "We need to add ", new_uuid, " to a new order"
            break


    #return False


###############################################################################
def main():
###############################################################################

    challenge1()
    challenge2()

###############################################################################
if __name__ == '__main__':
    main()
