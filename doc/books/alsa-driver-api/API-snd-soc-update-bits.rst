.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-update-bits:

===================
snd_soc_update_bits
===================

*man snd_soc_update_bits(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
