.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-jack-add-pins:

=====================
snd_soc_jack_add_pins
=====================

*man snd_soc_jack_add_pins(9)*

*4.6.0-rc5*

Associate DAPM pins with an ASoC jack


Synopsis
========

.. c:function:: int snd_soc_jack_add_pins( struct snd_soc_jack * jack, int count, struct snd_soc_jack_pin * pins )

Arguments
=========

``jack``
    ASoC jack

``count``
    Number of pins

``pins``
    Array of pins


Description
===========

After this function has been called the DAPM pins specified in the pins
array will have their status updated to reflect the current state of the
jack whenever the jack status is updated.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
