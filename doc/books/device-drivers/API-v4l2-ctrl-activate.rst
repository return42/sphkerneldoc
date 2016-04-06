
.. _API-v4l2-ctrl-activate:

==================
v4l2_ctrl_activate
==================

*man v4l2_ctrl_activate(9)*

*4.6.0-rc1*

Make the control active or inactive.


Synopsis
========

.. c:function:: void v4l2_ctrl_activate( struct v4l2_ctrl * ctrl, bool active )

Arguments
=========

``ctrl``
    The control to (de)activate.

``active``
    True if the control should become active.


Description
===========

This sets or clears the V4L2_CTRL_FLAG_INACTIVE flag atomically. Does nothing if ``ctrl`` == NULL. This will usually be called from within the s_ctrl op. The V4L2_EVENT_CTRL
event will be generated afterwards.

This function assumes that the control handler is locked.
