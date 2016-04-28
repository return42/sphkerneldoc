.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ctl-find-id:

===============
snd_ctl_find_id
===============

*man snd_ctl_find_id(9)*

*4.6.0-rc5*

find the control instance with the given id


Synopsis
========

.. c:function:: struct snd_kcontrol * snd_ctl_find_id( struct snd_card * card, struct snd_ctl_elem_id * id )

Arguments
=========

``card``
    the card instance

``id``
    the id to search


Description
===========

Finds the control instance with the given id from the card.

The caller must down card->controls_rwsem before calling this function
(if the race condition can happen).


Return
======

The pointer of the instance if found, or ``NULL`` if not.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
