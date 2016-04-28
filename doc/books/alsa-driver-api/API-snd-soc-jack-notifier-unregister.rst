.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-jack-notifier-unregister:

================================
snd_soc_jack_notifier_unregister
================================

*man snd_soc_jack_notifier_unregister(9)*

*4.6.0-rc5*

Unregister a notifier for jack status


Synopsis
========

.. c:function:: void snd_soc_jack_notifier_unregister( struct snd_soc_jack * jack, struct notifier_block * nb )

Arguments
=========

``jack``
    ASoC jack

``nb``
    Notifier block to unregister


Description
===========

Stop notifying for status changes.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
