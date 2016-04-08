
.. _API-rio-set-port-lockout:

====================
rio_set_port_lockout
====================

*man rio_set_port_lockout(9)*

*4.6.0-rc1*

Sets/clears LOCKOUT bit (RIO EM 1.3) for a switch port.


Synopsis
========

.. c:function:: int rio_set_port_lockout( struct rio_dev * rdev, u32 pnum, int lock )

Arguments
=========

``rdev``
    Pointer to RIO device control structure

``pnum``
    Switch port number to set LOCKOUT bit

``lock``
    Operation : set (=1) or clear (=0)
