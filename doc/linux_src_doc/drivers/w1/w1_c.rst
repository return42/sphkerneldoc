.. -*- coding: utf-8; mode: rst -*-

====
w1.c
====

.. _`w1_search`:

w1_search
=========

.. c:function:: void w1_search (struct w1_master *dev, u8 search_type, w1_slave_found_callback cb)

    Performs a ROM Search & registers any devices found.

    :param struct w1_master \*dev:
        The master device to search

    :param u8 search_type:
        W1_SEARCH to search all devices, or W1_ALARM_SEARCH
        to return only devices in the alarmed state

    :param w1_slave_found_callback cb:
        Function to call when a device is found


.. _`w1_search.description`:

Description
-----------

The 1-wire search is a simple binary tree search.
For each bit of the address, we read two bits and write one bit.
The bit written will put to sleep all devies that don't match that bit.
When the two reads differ, the direction choice is obvious.
When both bits are 0, we must choose a path to take.
When we can scan all 64 bits without having to choose a path, we are done.

See "Application note 187 1-wire search algorithm" at www.maxim-ic.com


.. _`w1_process_callbacks`:

w1_process_callbacks
====================

.. c:function:: int w1_process_callbacks (struct w1_master *dev)

    execute each dev->async_list callback entry

    :param struct w1_master \*dev:
        w1_master device


.. _`w1_process_callbacks.description`:

Description
-----------

The w1 master list_mutex must be held.

Return: 1 if there were commands to executed 0 otherwise

