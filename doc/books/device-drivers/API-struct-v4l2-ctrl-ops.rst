.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-v4l2-ctrl-ops:

====================
struct v4l2_ctrl_ops
====================

*man struct v4l2_ctrl_ops(9)*

*4.6.0-rc5*

The control operations that the driver has to provide.


Synopsis
========

.. code-block:: c

    struct v4l2_ctrl_ops {
      int (* g_volatile_ctrl) (struct v4l2_ctrl *ctrl);
      int (* try_ctrl) (struct v4l2_ctrl *ctrl);
      int (* s_ctrl) (struct v4l2_ctrl *ctrl);
    };


Members
=======

g_volatile_ctrl
    Get a new value for this control. Generally only relevant for
    volatile (and usually read-only) controls such as a control that
    returns the current signal strength which changes continuously. If
    not set, then the currently cached value will be returned.

try_ctrl
    Test whether the control's value is valid. Only relevant when the
    usual min/max/step checks are not sufficient.

s_ctrl
    Actually set the new control value. s_ctrl is compulsory. The
    ctrl->handler->lock is held when these ops are called, so no one
    else can access controls owned by that handler.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
