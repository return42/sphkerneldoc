.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-ctrl-new-custom:

====================
v4l2_ctrl_new_custom
====================

*man v4l2_ctrl_new_custom(9)*

*4.6.0-rc5*

Allocate and initialize a new custom V4L2 control.


Synopsis
========

.. c:function:: struct v4l2_ctrl * v4l2_ctrl_new_custom( struct v4l2_ctrl_handler * hdl, const struct v4l2_ctrl_config * cfg, void * priv )

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

If the ``v4l2_ctrl`` struct could not be allocated then NULL is returned
and ``hdl``->error is set to the error code (if it wasn't set already).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
