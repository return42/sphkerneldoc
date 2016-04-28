.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-jack-get-type:

=====================
snd_soc_jack_get_type
=====================

*man snd_soc_jack_get_type(9)*

*4.6.0-rc5*

Based on the mic bias value, this function returns the type of jack from
the zones declared in the jack type


Synopsis
========

.. c:function:: int snd_soc_jack_get_type( struct snd_soc_jack * jack, int micbias_voltage )

Arguments
=========

``jack``
    ASoC jack

``micbias_voltage``
    mic bias voltage at adc channel when jack is plugged in


Description
===========

Based on the mic bias value passed, this function helps identify the
type of jack from the already declared jack zones


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
