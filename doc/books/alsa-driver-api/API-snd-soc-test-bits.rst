.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-test-bits:

=================
snd_soc_test_bits
=================

*man snd_soc_test_bits(9)*

*4.6.0-rc5*

test register for change


Synopsis
========

.. c:function:: int snd_soc_test_bits( struct snd_soc_codec * codec, unsigned int reg, unsigned int mask, unsigned int value )

Arguments
=========

``codec``
    audio codec

``reg``
    codec register

``mask``
    register mask

``value``
    new value


Description
===========

Tests a register with a new value and checks if the new value is
different from the old value.

Returns 1 for change else 0.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
