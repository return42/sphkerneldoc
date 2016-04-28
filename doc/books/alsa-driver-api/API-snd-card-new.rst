.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-card-new:

============
snd_card_new
============

*man snd_card_new(9)*

*4.6.0-rc5*

create and initialize a soundcard structure


Synopsis
========

.. c:function:: int snd_card_new( struct device * parent, int idx, const char * xid, struct module * module, int extra_size, struct snd_card ** card_ret )

Arguments
=========

``parent``
    the parent device object

``idx``
    card index (address) [0 ... (SNDRV_CARDS-1)]

``xid``
    card identification (ASCII string)

``module``
    top level module for locking

``extra_size``
    allocate this extra size after the main soundcard structure

``card_ret``
    the pointer to store the created card instance


Description
===========

Creates and initializes a soundcard structure.

The function allocates snd_card instance via kzalloc with the given
space for the driver to use freely. The allocated struct is stored in
the given card_ret pointer.


Return
======

Zero if successful or a negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
