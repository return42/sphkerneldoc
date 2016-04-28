.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-card-jack-new:

=====================
snd_soc_card_jack_new
=====================

*man snd_soc_card_jack_new(9)*

*4.6.0-rc5*

Create a new jack


Synopsis
========

.. c:function:: int snd_soc_card_jack_new( struct snd_soc_card * card, const char * id, int type, struct snd_soc_jack * jack, struct snd_soc_jack_pin * pins, unsigned int num_pins )

Arguments
=========

``card``
    ASoC card

``id``
    an identifying string for this jack

``type``
    a bitmask of enum snd_jack_type values that can be detected by
    this jack

``jack``
    structure to use for the jack

``pins``
    Array of jack pins to be added to the jack or NULL

``num_pins``
    Number of elements in the ``pins`` array


Description
===========

Creates a new jack object.

Returns zero if successful, or a negative error code on failure. On
success jack will be initialised.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
