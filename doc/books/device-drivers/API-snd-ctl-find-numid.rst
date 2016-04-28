.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ctl-find-numid:

==================
snd_ctl_find_numid
==================

*man snd_ctl_find_numid(9)*

*4.6.0-rc5*

find the control instance with the given number-id


Synopsis
========

.. c:function:: struct snd_kcontrol * snd_ctl_find_numid( struct snd_card * card, unsigned int numid )

Arguments
=========

``card``
    the card instance

``numid``
    the number-id to search


Description
===========

Finds the control instance with the given number-id from the card.

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
