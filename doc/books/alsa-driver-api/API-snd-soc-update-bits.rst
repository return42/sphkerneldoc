
.. _API-snd-soc-update-bits:

===================
snd_soc_update_bits
===================

*man snd_soc_update_bits(9)*

*4.6.0-rc1*

update codec register bits


Synopsis
========

.. c:function:: int snd_soc_update_bits( struct snd_soc_codec * codec, unsigned int reg, unsigned int mask, unsigned int value )

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

Writes new register value.

Returns 1 for change, 0 for no change, or negative error code.
