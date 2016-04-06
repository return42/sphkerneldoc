
.. _API-work-busy:

=========
work_busy
=========

*man work_busy(9)*

*4.6.0-rc1*

test whether a work is currently pending or running


Synopsis
========

.. c:function:: unsigned int work_busy( struct work_struct * work )

Arguments
=========

``work``
    the work to be tested


Description
===========

Test whether ``work`` is currently pending or running. There is no synchronization around this function and the test result is unreliable and only useful as advisory hints or for
debugging.


Return
======

OR'd bitmask of WORK_BUSY_⋆ bits.
