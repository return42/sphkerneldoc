.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-ctrl-new-int-menu:

======================
v4l2_ctrl_new_int_menu
======================

*man v4l2_ctrl_new_int_menu(9)*

*4.6.0-rc5*

Create a new standard V4L2 integer menu control.


Synopsis
========

.. c:function:: struct v4l2_ctrl * v4l2_ctrl_new_int_menu( struct v4l2_ctrl_handler * hdl, const struct v4l2_ctrl_ops * ops, u32 id, u8 max, u8 def, const s64 * qmenu_int )

Arguments
=========

``hdl``
    The control handler.

``ops``
    The control ops.

``id``
    The control ID.

``max``
    The control's maximum value.

``def``
    The control's default value.

``qmenu_int``
    The control's menu entries.


Description
===========

Same as ``v4l2_ctrl_new_std_menu``, but ``mask`` is set to 0 and it
additionaly takes as an argument an array of integers determining the
menu items.

If ``id`` refers to a non-integer-menu control, then this function will
return NULL.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
