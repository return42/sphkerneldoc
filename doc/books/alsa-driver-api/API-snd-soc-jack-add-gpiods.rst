
.. _API-snd-soc-jack-add-gpiods:

=======================
snd_soc_jack_add_gpiods
=======================

*man snd_soc_jack_add_gpiods(9)*

*4.6.0-rc1*

Associate GPIO descriptor pins with an ASoC jack


Synopsis
========

.. c:function:: int snd_soc_jack_add_gpiods( struct device * gpiod_dev, struct snd_soc_jack * jack, int count, struct snd_soc_jack_gpio * gpios )

Arguments
=========

``gpiod_dev``
    GPIO consumer device

``jack``
    ASoC jack

``count``
    number of pins

``gpios``
    array of gpio pins


Description
===========

This function will request gpio, set data direction and request irq for each gpio in the array.
