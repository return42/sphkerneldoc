
.. _API-snd-ctl-enum-info:

=================
snd_ctl_enum_info
=================

*man snd_ctl_enum_info(9)*

*4.6.0-rc1*

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

Sets all required fields in ``info`` to their appropriate values. If the control's accessibility is not the default (readable and writable), the caller has to fill
``info``->access.


Return
======

Zero.
