.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-jack-new:

============
snd_jack_new
============

*man snd_jack_new(9)*

*4.6.0-rc5*

Create a new jack


Synopsis
========

.. c:function:: int snd_jack_new( struct snd_card * card, const char * id, int type, struct snd_jack ** jjack, bool initial_kctl, bool phantom_jack )

Arguments
=========

``card``
    the card instance

``id``
    an identifying string for this jack

``type``
    a bitmask of enum snd_jack_type values that can be detected by
    this jack

``jjack``
    Used to provide the allocated jack object to the caller.

``initial_kctl``
    if true, create a kcontrol and add it to the jack list.

``phantom_jack``
    Don't create a input device for phantom jacks.


Description
===========

Creates a new jack object.


Return
======

Zero if successful, or a negative error code on failure. On success
``jjack`` will be initialised.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
