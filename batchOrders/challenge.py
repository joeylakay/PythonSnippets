#!/usr/bin/env python

import uuid
import order

# Problem: Orders need to be batched together in groups of 3



###############################################################################
def main():
###############################################################################

    o = order.Order()
    orders = o.getOrders()
    print orders



###############################################################################
if __name__ == '__main__':
    main()
