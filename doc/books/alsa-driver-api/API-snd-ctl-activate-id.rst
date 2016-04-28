.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ctl-activate-id:

===================
snd_ctl_activate_id
===================

*man snd_ctl_activate_id(9)*

*4.6.0-rc5*

activate/inactivate the control of the given id


Synopsis
========

.. c:function:: int snd_ctl_activate_id( struct snd_card * card, struct snd_ctl_elem_id * id, int active )

Arguments
=========

``card``
    the card instance

``id``
    the control id to activate/inactivate

``active``
    non-zero to activate


Description
===========

Finds the control instance with the given id, and activate or inactivate
the control together with notification, if changed. The given ID data is
filled with full information.


Return
======

0 if unchanged, 1 if changed, or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
