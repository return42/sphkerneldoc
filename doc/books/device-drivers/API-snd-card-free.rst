
.. _API-snd-card-free:

=============
snd_card_free
=============

*man snd_card_free(9)*

*4.6.0-rc1*

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

This function releases the soundcard structure and the all assigned devices automatically. That is, you don't have to release the devices by yourself.

This function waits until the all resources are properly released.


Return
======

Zero. Frees all associated devices and frees the control interface associated to given soundcard.
