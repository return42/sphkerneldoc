
.. _API-w1-search:

=========
w1_search
=========

*man w1_search(9)*

*4.6.0-rc1*

Performs a ROM Search & registers any devices found.


Synopsis
========

.. c:function:: void w1_search( struct w1_master * dev, u8 search_type, w1_slave_found_callback cb )

Arguments
=========

``dev``
    The master device to search

``search_type``
    W1_SEARCH to search all devices, or W1_ALARM_SEARCH to return only devices in the alarmed state

``cb``
    Function to call when a device is found


Description
===========

The 1-wire search is a simple binary tree search. For each bit of the address, we read two bits and write one bit. The bit written will put to sleep all devies that don't match
that bit. When the two reads differ, the direction choice is obvious. When both bits are 0, we must choose a path to take. When we can scan all 64 bits without having to choose a
path, we are done.

See “Application note 187 1-wire search algorithm” at www.maxim-ic.com
