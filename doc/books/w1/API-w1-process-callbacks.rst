
.. _API-w1-process-callbacks:

====================
w1_process_callbacks
====================

*man w1_process_callbacks(9)*

*4.6.0-rc1*

execute each dev->async_list callback entry


Synopsis
========

.. c:function:: int w1_process_callbacks( struct w1_master * dev )

Arguments
=========

``dev``
    w1_master device


Description
===========

The w1 master list_mutex must be held.


Return
======

1 if there were commands to executed 0 otherwise
