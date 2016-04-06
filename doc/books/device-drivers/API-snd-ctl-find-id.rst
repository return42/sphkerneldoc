
.. _API-snd-ctl-find-id:

===============
snd_ctl_find_id
===============

*man snd_ctl_find_id(9)*

*4.6.0-rc1*

find the control instance with the given id


Synopsis
========

.. c:function:: struct snd_kcontrol ⋆ snd_ctl_find_id( struct snd_card * card, struct snd_ctl_elem_id * id )

Arguments
=========

``card``
    the card instance

``id``
    the id to search


Description
===========

Finds the control instance with the given id from the card.

The caller must down card->controls_rwsem before calling this function (if the race condition can happen).


Return
======

The pointer of the instance if found, or ``NULL`` if not.
