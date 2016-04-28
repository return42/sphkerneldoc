.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-jack-report:

===================
snd_soc_jack_report
===================

*man snd_soc_jack_report(9)*

*4.6.0-rc5*

Report the current status for a jack


Synopsis
========

.. c:function:: void snd_soc_jack_report( struct snd_soc_jack * jack, int status, int mask )

Arguments
=========

``jack``
    the jack

``status``
    a bitmask of enum snd_jack_type values that are currently
    detected.

``mask``
    a bitmask of enum snd_jack_type values that being reported.


Description
===========

If configured using ``snd_soc_jack_add_pins`` then the associated DAPM
pins will be enabled or disabled as appropriate and DAPM synchronised.


Note
====

This function uses mutexes and should be called from a context which can
sleep (such as a workqueue).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
