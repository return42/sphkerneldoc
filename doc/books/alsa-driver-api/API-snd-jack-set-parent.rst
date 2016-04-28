.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-jack-set-parent:

===================
snd_jack_set_parent
===================

*man snd_jack_set_parent(9)*

*4.6.0-rc5*

Set the parent device for a jack


Synopsis
========

.. c:function:: void snd_jack_set_parent( struct snd_jack * jack, struct device * parent )

Arguments
=========

``jack``
    The jack to configure

``parent``
    The device to set as parent for the jack.


Description
===========

Set the parent for the jack devices in the device tree. This function is
only valid prior to registration of the jack. If no parent is configured
then the parent device will be the sound card.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
