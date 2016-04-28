.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-card-free:

=============
snd_card_free
=============

*man snd_card_free(9)*

*4.6.0-rc5*

frees given soundcard structure


Synopsis
========

.. c:function:: int snd_card_free( struct snd_card * card )

Arguments
=========

``card``
    soundcard structure


Description
===========

This function releases the soundcard structure and the all assigned
devices automatically. That is, you don't have to release the devices by
yourself.

This function waits until the all resources are properly released.


Return
======

Zero. Frees all associated devices and frees the control interface
associated to given soundcard.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
