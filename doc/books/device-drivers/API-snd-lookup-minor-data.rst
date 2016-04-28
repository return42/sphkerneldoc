.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-lookup-minor-data:

=====================
snd_lookup_minor_data
=====================

*man snd_lookup_minor_data(9)*

*4.6.0-rc5*

get user data of a registered device


Synopsis
========

.. c:function:: void * snd_lookup_minor_data( unsigned int minor, int type )

Arguments
=========

``minor``
    the minor number

``type``
    device type (SNDRV_DEVICE_TYPE_XXX)


Description
===========

Checks that a minor device with the specified type is registered, and
returns its user data pointer.

This function increments the reference counter of the card instance if
an associated instance with the given minor number and type is found.
The caller must call ``snd_card_unref`` appropriately later.


Return
======

The user data pointer if the specified device is found. ``NULL``
otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
