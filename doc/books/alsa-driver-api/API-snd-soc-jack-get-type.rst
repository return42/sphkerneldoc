
.. _API-snd-soc-jack-get-type:

=====================
snd_soc_jack_get_type
=====================

*man snd_soc_jack_get_type(9)*

*4.6.0-rc1*

Based on the mic bias value, this function returns the type of jack from the zones declared in the jack type


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

Based on the mic bias value passed, this function helps identify the type of jack from the already declared jack zones
