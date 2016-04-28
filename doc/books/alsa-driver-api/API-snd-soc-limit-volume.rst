.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-limit-volume:

====================
snd_soc_limit_volume
====================

*man snd_soc_limit_volume(9)*

*4.6.0-rc5*

Set new limit to an existing volume control.


Synopsis
========

.. c:function:: int snd_soc_limit_volume( struct snd_soc_card * card, const char * name, int max )

Arguments
=========

``card``
    where to look for the control

``name``
    Name of the control

``max``
    new maximum limit


Description
===========

Return 0 for success, else error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
