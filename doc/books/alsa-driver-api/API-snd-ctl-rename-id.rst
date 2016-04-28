.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ctl-rename-id:

=================
snd_ctl_rename_id
=================

*man snd_ctl_rename_id(9)*

*4.6.0-rc5*

replace the id of a control on the card


Synopsis
========

.. c:function:: int snd_ctl_rename_id( struct snd_card * card, struct snd_ctl_elem_id * src_id, struct snd_ctl_elem_id * dst_id )

Arguments
=========

``card``
    the card instance

``src_id``
    the old id

``dst_id``
    the new id


Description
===========

Finds the control with the old id from the card, and replaces the id
with the new one.


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
