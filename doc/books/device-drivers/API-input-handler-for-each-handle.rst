
.. _API-input-handler-for-each-handle:

=============================
input_handler_for_each_handle
=============================

*man input_handler_for_each_handle(9)*

*4.6.0-rc1*

handle iterator


Synopsis
========

.. c:function:: int input_handler_for_each_handle( struct input_handler * handler, void * data, int (*fn) struct input_handle *, void * )

Arguments
=========

``handler``
    input handler to iterate

``data``
    data for the callback

``fn``
    function to be called for each handle


Description
===========

Iterate over ``bus``'s list of devices, and call ``fn`` for each, passing it ``data`` and stop when ``fn`` returns a non-zero value. The function is using RCU to traverse the list
and therefore may be using in atomic contexts. The ``fn`` callback is invoked from RCU critical section and thus must not sleep.
