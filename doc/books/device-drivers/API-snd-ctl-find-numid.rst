
.. _API-snd-ctl-find-numid:

==================
snd_ctl_find_numid
==================

*man snd_ctl_find_numid(9)*

*4.6.0-rc1*

find the control instance with the given number-id


Synopsis
========

.. c:function:: struct snd_kcontrol ⋆ snd_ctl_find_numid( struct snd_card * card, unsigned int numid )

Arguments
=========

``card``
    the card instance

``numid``
    the number-id to search


Description
===========

Finds the control instance with the given number-id from the card.

The caller must down card->controls_rwsem before calling this function (if the race condition can happen).


Return
======

The pointer of the instance if found, or ``NULL`` if not.
