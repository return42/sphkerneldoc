.. -*- coding: utf-8; mode: rst -*-

.. _API---v4l2-ctrl-s-ctrl-int64:

========================
__v4l2_ctrl_s_ctrl_int64
========================

*man __v4l2_ctrl_s_ctrl_int64(9)*

*4.6.0-rc5*

Unlocked variant of ``v4l2_ctrl_s_ctrl_int64``.


Synopsis
========

.. c:function:: int __v4l2_ctrl_s_ctrl_int64( struct v4l2_ctrl * ctrl, s64 val )

Arguments
=========

``ctrl``
    The control.

``val``
    The new value.


Description
===========

This set the control's new value safely by going through the control
framework. This function will lock the control's handler, so it cannot
be used from within the ``v4l2_ctrl_ops`` functions.

This function is for 64-bit integer type controls only.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
