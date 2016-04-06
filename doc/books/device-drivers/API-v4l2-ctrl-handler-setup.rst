
.. _API-v4l2-ctrl-handler-setup:

=======================
v4l2_ctrl_handler_setup
=======================

*man v4l2_ctrl_handler_setup(9)*

*4.6.0-rc1*

Call the s_ctrl op for all controls belonging to the handler to initialize the hardware to the current control values.


Synopsis
========

.. c:function:: int v4l2_ctrl_handler_setup( struct v4l2_ctrl_handler * hdl )

Arguments
=========

``hdl``
    The control handler.


Description
===========

Button controls will be skipped, as are read-only controls.

If ``hdl`` == NULL, then this just returns 0.
