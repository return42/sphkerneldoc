
.. _API-ilsel-enable-fixed:

==================
ilsel_enable_fixed
==================

*man ilsel_enable_fixed(9)*

*4.6.0-rc1*

Enable an ILSEL set at a fixed interrupt level


Synopsis
========

.. c:function:: int ilsel_enable_fixed( ilsel_source_t set, unsigned int level )

Arguments
=========

``set``
    ILSEL source (see ilsel_source_t enum in include/asm-sh/ilsel.h).

``level``
    Interrupt level (1 - 15)


Description
===========

Enables a given ILSEL source at a fixed interrupt level. Necessary both for level reservation as well as for aliased sources that only exist on special ILSEL#s.

Returns an IRQ number (as ``ilsel_enable``).
