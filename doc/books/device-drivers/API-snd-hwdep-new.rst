.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-hwdep-new:

=============
snd_hwdep_new
=============

*man snd_hwdep_new(9)*

*4.6.0-rc5*

create a new hwdep instance


Synopsis
========

.. c:function:: int snd_hwdep_new( struct snd_card * card, char * id, int device, struct snd_hwdep ** rhwdep )

Arguments
=========

``card``
    the card instance

``id``
    the id string

``device``
    the device index (zero-based)

``rhwdep``
    the pointer to store the new hwdep instance


Description
===========

Creates a new hwdep instance with the given index on the card. The
callbacks (hwdep->ops) must be set on the returned instance after this
call manually by the caller.


Return
======

Zero if successful, or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
