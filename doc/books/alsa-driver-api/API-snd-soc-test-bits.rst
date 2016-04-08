
.. _API-snd-soc-test-bits:

=================
snd_soc_test_bits
=================

*man snd_soc_test_bits(9)*

*4.6.0-rc1*

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

Tests a register with a new value and checks if the new value is different from the old value.

Returns 1 for change else 0.
