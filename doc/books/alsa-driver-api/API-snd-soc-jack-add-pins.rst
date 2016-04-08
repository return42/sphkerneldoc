
.. _API-snd-soc-jack-add-pins:

=====================
snd_soc_jack_add_pins
=====================

*man snd_soc_jack_add_pins(9)*

*4.6.0-rc1*

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

After this function has been called the DAPM pins specified in the pins array will have their status updated to reflect the current state of the jack whenever the jack status is
updated.
