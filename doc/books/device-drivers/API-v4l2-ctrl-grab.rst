.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-ctrl-grab:

==============
v4l2_ctrl_grab
==============

*man v4l2_ctrl_grab(9)*

*4.6.0-rc5*

Mark the control as grabbed or not grabbed.


Synopsis
========

.. c:function:: void v4l2_ctrl_grab( struct v4l2_ctrl * ctrl, bool grabbed )

Arguments
=========

``ctrl``
    The control to (de)activate.

``grabbed``
    True if the control should become grabbed.


Description
===========

This sets or clears the V4L2_CTRL_FLAG_GRABBED flag atomically. Does
nothing if ``ctrl`` == NULL. The V4L2_EVENT_CTRL event will be
generated afterwards. This will usually be called when starting or
stopping streaming in the driver.

This function assumes that the control handler is not locked and will
take the lock itself.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
