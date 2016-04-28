.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-jack-add-zones:

======================
snd_soc_jack_add_zones
======================

*man snd_soc_jack_add_zones(9)*

*4.6.0-rc5*

Associate voltage zones with jack


Synopsis
========

.. c:function:: int snd_soc_jack_add_zones( struct snd_soc_jack * jack, int count, struct snd_soc_jack_zone * zones )

Arguments
=========

``jack``
    ASoC jack

``count``
    Number of zones

``zones``
    Array of zones


Description
===========

After this function has been called the zones specified in the array
will be associated with the jack.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
