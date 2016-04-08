
.. _API-snd-soc-jack-free-gpios:

=======================
snd_soc_jack_free_gpios
=======================

*man snd_soc_jack_free_gpios(9)*

*4.6.0-rc1*

Release GPIO pins' resources of an ASoC jack


Synopsis
========

.. c:function:: void snd_soc_jack_free_gpios( struct snd_soc_jack * jack, int count, struct snd_soc_jack_gpio * gpios )

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

Release gpio and irq resources for gpio pins associated with an ASoC jack.
