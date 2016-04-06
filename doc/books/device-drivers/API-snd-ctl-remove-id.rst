
.. _API-snd-ctl-remove-id:

=================
snd_ctl_remove_id
=================

*man snd_ctl_remove_id(9)*

*4.6.0-rc1*

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

Finds the control instance with the given id, removes it from the card list and releases it.


Return
======

0 if successful, or a negative error code on failure.
