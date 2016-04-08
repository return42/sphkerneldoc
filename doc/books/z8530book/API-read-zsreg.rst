
.. _API-read-zsreg:

==========
read_zsreg
==========

*man read_zsreg(9)*

*4.6.0-rc1*

Read a register from a Z85230


Synopsis
========

.. c:function:: u8 read_zsreg( struct z8530_channel * c, u8 reg )

Arguments
=========

``c``
    Z8530 channel to read from (2 per chip)

``reg``
    Register to read


FIXME
=====

Use a spinlock.

Most of the Z8530 registers are indexed off the control registers. A read is done by writing to the control register and reading the register back. The caller must hold the lock
