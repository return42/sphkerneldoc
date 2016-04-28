.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-ctrl-get-int-menu:

======================
v4l2_ctrl_get_int_menu
======================

*man v4l2_ctrl_get_int_menu(9)*

*4.6.0-rc5*

Get the integer menu array of the control


Synopsis
========

.. c:function:: const s64 * v4l2_ctrl_get_int_menu( u32 id, u32 * len )

Arguments
=========

``id``
    The control ID.

``len``
    The size of the integer array.


Description
===========

This function returns the integer array of the given control ID or NULL
if it if it isn't a known integer menu control.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
