
.. _API-snd-card-set-id:

===============
snd_card_set_id
===============

*man snd_card_set_id(9)*

*4.6.0-rc1*

set card identification name


Synopsis
========

.. c:function:: void snd_card_set_id( struct snd_card * card, const char * nid )

Arguments
=========

``card``
    soundcard structure

``nid``
    new identification string


Description
===========

This function sets the card identification and checks for name collisions.
