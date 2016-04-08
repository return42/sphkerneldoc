
.. _API-snd-jack-report:

===============
snd_jack_report
===============

*man snd_jack_report(9)*

*4.6.0-rc1*

Report the current status of a jack


Synopsis
========

.. c:function:: void snd_jack_report( struct snd_jack * jack, int status )

Arguments
=========

``jack``
    The jack to report status for

``status``
    The current status of the jack
