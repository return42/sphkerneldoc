
.. _API-write-zsctrl:

============
write_zsctrl
============

*man write_zsctrl(9)*

*4.6.0-rc1*

Write to a Z8530 control register


Synopsis
========

.. c:function:: void write_zsctrl( struct z8530_channel * c, u8 val )

Arguments
=========

``c``
    The Z8530 channel

``val``
    Value to write


Description
===========

Write directly to the control register on the Z8530
