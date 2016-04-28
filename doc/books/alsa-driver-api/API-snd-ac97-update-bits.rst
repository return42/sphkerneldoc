.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ac97-update-bits:

====================
snd_ac97_update_bits
====================

*man snd_ac97_update_bits(9)*

*4.6.0-rc5*

update the bits on the given register


Synopsis
========

.. c:function:: int snd_ac97_update_bits( struct snd_ac97 * ac97, unsigned short reg, unsigned short mask, unsigned short value )

Arguments
=========

``ac97``
    the ac97 instance

``reg``
    the register to change

``mask``
    the bit-mask to change

``value``
    the value to set


Description
===========

Updates the masked-bits on the given register only when the value is
changed.


Return
======

1 if the bits are changed, 0 if no change, or a negative code on
failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
