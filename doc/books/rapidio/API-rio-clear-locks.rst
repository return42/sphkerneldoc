
.. _API-rio-clear-locks:

===============
rio_clear_locks
===============

*man rio_clear_locks(9)*

*4.6.0-rc1*

Release all host locks and signal enumeration complete


Synopsis
========

.. c:function:: int rio_clear_locks( struct rio_net * net )

Arguments
=========

``net``
    RIO network to run on


Description
===========

Marks the component tag CSR on each device with the enumeration complete flag. When complete, it then release the host locks on each device. Returns 0 on success or ``-EINVAL`` on
failure.
