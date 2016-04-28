.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-card-register:

=================
snd_card_register
=================

*man snd_card_register(9)*

*4.6.0-rc5*

register the soundcard


Synopsis
========

.. c:function:: int snd_card_register( struct snd_card * card )

Arguments
=========

``card``
    soundcard structure


Description
===========

This function registers all the devices assigned to the soundcard. Until
calling this, the ALSA control interface is blocked from the external
accesses. Thus, you should call this function at the end of the
initialization of the card.


Return
======

Zero otherwise a negative error code if the registration failed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
