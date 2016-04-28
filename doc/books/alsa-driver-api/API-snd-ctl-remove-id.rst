.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ctl-remove-id:

=================
snd_ctl_remove_id
=================

*man snd_ctl_remove_id(9)*

*4.6.0-rc5*

remove the control of the given id and release it


Synopsis
========

.. c:function:: int snd_ctl_remove_id( struct snd_card * card, struct snd_ctl_elem_id * id )

Arguments
=========

``card``
    the card instance

``id``
    the control id to remove


Description
===========

Finds the control instance with the given id, removes it from the card
list and releases it.


Return
======

0 if successful, or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
