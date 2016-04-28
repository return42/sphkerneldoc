.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-card-set-id:

===============
snd_card_set_id
===============

*man snd_card_set_id(9)*

*4.6.0-rc5*

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

This function sets the card identification and checks for name
collisions.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
