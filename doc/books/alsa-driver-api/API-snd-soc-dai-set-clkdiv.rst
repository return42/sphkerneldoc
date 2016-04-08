
.. _API-snd-soc-dai-set-clkdiv:

======================
snd_soc_dai_set_clkdiv
======================

*man snd_soc_dai_set_clkdiv(9)*

*4.6.0-rc1*

configure DAI clock dividers.


Synopsis
========

.. c:function:: int snd_soc_dai_set_clkdiv( struct snd_soc_dai * dai, int div_id, int div )

Arguments
=========

``dai``
    DAI

``div_id``
    DAI specific clock divider ID

``div``
    new clock divisor.


Description
===========

Configures the clock dividers. This is used to derive the best DAI bit and frame clocks from the system or master clock. It's best to set the DAI bit and frame clocks as low as
possible to save system power.
