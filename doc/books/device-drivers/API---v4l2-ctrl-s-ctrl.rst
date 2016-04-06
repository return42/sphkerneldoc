
.. _API---v4l2-ctrl-s-ctrl:

==================
__v4l2_ctrl_s_ctrl
==================

*man __v4l2_ctrl_s_ctrl(9)*

*4.6.0-rc1*

Unlocked variant of ``v4l2_ctrl_s_ctrl``.


Synopsis
========

.. c:function:: int __v4l2_ctrl_s_ctrl( struct v4l2_ctrl * ctrl, s32 val )

Arguments
=========

``ctrl``
    The control.

``val``
    The new value.


Description
===========

This set the control's new value safely by going through the control framework. This function will lock the control's handler, so it cannot be used from within the
``v4l2_ctrl_ops`` functions.

This function is for integer type controls only.
