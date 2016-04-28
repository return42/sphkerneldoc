.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ctl-enum-info:

=================
snd_ctl_enum_info
=================

*man snd_ctl_enum_info(9)*

*4.6.0-rc5*

fills the info structure for an enumerated control


Synopsis
========

.. c:function:: int snd_ctl_enum_info( struct snd_ctl_elem_info * info, unsigned int channels, unsigned int items, const char *const names[] )

Arguments
=========

``info``
    the structure to be filled

``channels``
    the number of the control's channels; often one

``items``
    the number of control values; also the size of ``names``

``names[]``
    an array containing the names of all control values


Description
===========

Sets all required fields in ``info`` to their appropriate values. If the
control's accessibility is not the default (readable and writable), the
caller has to fill ``info``->access.


Return
======

Zero.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
