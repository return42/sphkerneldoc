
.. _API-v4l2-ctrl-handler-free:

======================
v4l2_ctrl_handler_free
======================

*man v4l2_ctrl_handler_free(9)*

*4.6.0-rc1*

Free all controls owned by the handler and free the control list.


Synopsis
========

.. c:function:: void v4l2_ctrl_handler_free( struct v4l2_ctrl_handler * hdl )

Arguments
=========

``hdl``
    The control handler.


Description
===========

Does nothing if ``hdl`` == NULL.
