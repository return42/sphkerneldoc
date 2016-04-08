
.. _API-ilsel-enable:

============
ilsel_enable
============

*man ilsel_enable(9)*

*4.6.0-rc1*

Enable an ILSEL set.


Synopsis
========

.. c:function:: int ilsel_enable( ilsel_source_t set )

Arguments
=========

``set``
    ILSEL source (see ilsel_source_t enum in include/asm-sh/ilsel.h).


Description
===========

Enables a given non-aliased ILSEL source (<= ILSEL_KEY) at the highest available interrupt level. Callers should take care to order callsites noting descending interrupt levels.
Aliasing FPGA and external board IRQs need to use ``ilsel_enable_fixed``.

The return value is an IRQ number that can later be taken down with ``ilsel_disable``.
