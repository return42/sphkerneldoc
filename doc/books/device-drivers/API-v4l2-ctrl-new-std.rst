.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-ctrl-new-std:

=================
v4l2_ctrl_new_std
=================

*man v4l2_ctrl_new_std(9)*

*4.6.0-rc5*

Allocate and initialize a new standard V4L2 non-menu control.


Synopsis
========

.. c:function:: struct v4l2_ctrl * v4l2_ctrl_new_std( struct v4l2_ctrl_handler * hdl, const struct v4l2_ctrl_ops * ops, u32 id, s64 min, s64 max, u64 step, s64 def )

Arguments
=========

``hdl``
    The control handler.

``ops``
    The control ops.

``id``
    The control ID.

``min``
    The control's minimum value.

``max``
    The control's maximum value.

``step``
    The control's step value

``def``
    The control's default value.


Description
===========

If the ``v4l2_ctrl`` struct could not be allocated, or the control ID is
not known, then NULL is returned and ``hdl``->error is set to the
appropriate error code (if it wasn't set already).

If ``id`` refers to a menu control, then this function will return NULL.

Use ``v4l2_ctrl_new_std_menu`` when adding menu controls.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
