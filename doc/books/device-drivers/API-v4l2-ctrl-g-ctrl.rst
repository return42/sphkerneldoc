.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-ctrl-g-ctrl:

================
v4l2_ctrl_g_ctrl
================

*man v4l2_ctrl_g_ctrl(9)*

*4.6.0-rc5*

Helper function to get the control's value from within a driver.


Synopsis
========

.. c:function:: s32 v4l2_ctrl_g_ctrl( struct v4l2_ctrl * ctrl )

Arguments
=========

``ctrl``
    The control.


Description
===========

This returns the control's value safely by going through the control
framework. This function will lock the control's handler, so it cannot
be used from within the ``v4l2_ctrl_ops`` functions.

This function is for integer type controls only.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
