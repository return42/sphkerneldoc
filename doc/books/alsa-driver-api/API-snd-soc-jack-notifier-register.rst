
.. _API-snd-soc-jack-notifier-register:

==============================
snd_soc_jack_notifier_register
==============================

*man snd_soc_jack_notifier_register(9)*

*4.6.0-rc1*

Register a notifier for jack status


Synopsis
========

.. c:function:: void snd_soc_jack_notifier_register( struct snd_soc_jack * jack, struct notifier_block * nb )

Arguments
=========

``jack``
    ASoC jack

``nb``
    Notifier block to register


Description
===========

Register for notification of the current status of the jack. Note that it is not possible to report additional jack events in the callback from the notifier, this is intended to
support applications such as enabling electrical detection only when a mechanical detection event has occurred.
