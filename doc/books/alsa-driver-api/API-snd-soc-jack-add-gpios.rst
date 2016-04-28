.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-jack-add-gpios:

======================
snd_soc_jack_add_gpios
======================

*man snd_soc_jack_add_gpios(9)*

*4.6.0-rc5*

Associate GPIO pins with an ASoC jack


Synopsis
========

.. c:function:: int snd_soc_jack_add_gpios( struct snd_soc_jack * jack, int count, struct snd_soc_jack_gpio * gpios )

Arguments
=========

``jack``
    ASoC jack

``count``
    number of pins

``gpios``
    array of gpio pins


Description
===========

This function will request gpio, set data direction and request irq for
each gpio in the array.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
