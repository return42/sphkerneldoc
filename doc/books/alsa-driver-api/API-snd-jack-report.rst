.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-jack-report:

===============
snd_jack_report
===============

*man snd_jack_report(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
