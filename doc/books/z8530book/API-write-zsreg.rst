
.. _API-write-zsreg:

===========
write_zsreg
===========

*man write_zsreg(9)*

*4.6.0-rc1*

Write to a Z8530 channel register


Synopsis
========

.. c:function:: void write_zsreg( struct z8530_channel * c, u8 reg, u8 val )

Arguments
=========

``c``
    The Z8530 channel

``reg``
    Register number

``val``
    Value to write


Description
===========

Write a value to an indexed register. The caller must hold the lock to honour the irritating delay rules. We know about register 0 being fast to access.

Assumes c->lock is held.
