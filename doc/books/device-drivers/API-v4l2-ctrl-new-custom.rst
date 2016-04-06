
.. _API-v4l2-ctrl-new-custom:

====================
v4l2_ctrl_new_custom
====================

*man v4l2_ctrl_new_custom(9)*

*4.6.0-rc1*

Allocate and initialize a new custom V4L2 control.


Synopsis
========

.. c:function:: struct v4l2_ctrl ⋆ v4l2_ctrl_new_custom( struct v4l2_ctrl_handler * hdl, const struct v4l2_ctrl_config * cfg, void * priv )

Arguments
=========

``hdl``
    The control handler.

``cfg``
    The control's configuration data.

``priv``
    The control's driver-specific private data.


Description
===========

If the ``v4l2_ctrl`` struct could not be allocated then NULL is returned and ``hdl``->error is set to the error code (if it wasn't set already).
