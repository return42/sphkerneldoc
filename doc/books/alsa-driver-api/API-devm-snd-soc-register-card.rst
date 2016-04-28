.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-snd-soc-register-card:

==========================
devm_snd_soc_register_card
==========================

*man devm_snd_soc_register_card(9)*

*4.6.0-rc5*

resource managed card registration


Synopsis
========

.. c:function:: int devm_snd_soc_register_card( struct device * dev, struct snd_soc_card * card )

Arguments
=========

``dev``
    Device used to manage card

``card``
    Card to register


Description
===========

Register a card with automatic unregistration when the device is
unregistered.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
