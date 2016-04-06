
.. _API---change-bit:

============
__change_bit
============

*man __change_bit(9)*

*4.6.0-rc1*

Toggle a bit in memory


Synopsis
========

.. c:function:: void __change_bit( long nr, volatile unsigned long * addr )

Arguments
=========

``nr``
    the bit to change

``addr``
    the address to start counting from


Description
===========

Unlike ``change_bit``, this function is non-atomic and may be reordered. If it's called on the same region of memory simultaneously, the effect may be that only one operation
succeeds.
