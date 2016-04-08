
.. _API-snd-soc-jack-notifier-unregister:

================================
snd_soc_jack_notifier_unregister
================================

*man snd_soc_jack_notifier_unregister(9)*

*4.6.0-rc1*

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
