
.. _API-v4l2-ctrl-handler-log-status:

============================
v4l2_ctrl_handler_log_status
============================

*man v4l2_ctrl_handler_log_status(9)*

*4.6.0-rc1*

Log all controls owned by the handler.


Synopsis
========

.. c:function:: void v4l2_ctrl_handler_log_status( struct v4l2_ctrl_handler * hdl, const char * prefix )

Arguments
=========

``hdl``
    The control handler.

``prefix``
    The prefix to use when logging the control values. If the prefix does not end with a space, then “:” will be added after the prefix. If ``prefix`` == NULL, then no prefix will
    be used.


Description
===========

For use with VIDIOC_LOG_STATUS.

Does nothing if ``hdl`` == NULL.
