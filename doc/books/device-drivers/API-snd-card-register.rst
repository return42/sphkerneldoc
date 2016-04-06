
.. _API-snd-card-register:

=================
snd_card_register
=================

*man snd_card_register(9)*

*4.6.0-rc1*

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

This function registers all the devices assigned to the soundcard. Until calling this, the ALSA control interface is blocked from the external accesses. Thus, you should call this
function at the end of the initialization of the card.


Return
======

Zero otherwise a negative error code if the registration failed.
