.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-ctrl-notify:

================
v4l2_ctrl_notify
================

*man v4l2_ctrl_notify(9)*

*4.6.0-rc5*

Function to set a notify callback for a control.


Synopsis
========

.. c:function:: void v4l2_ctrl_notify( struct v4l2_ctrl * ctrl, v4l2_ctrl_notify_fnc notify, void * priv )

Arguments
=========

``ctrl``
    The control.

``notify``
    The callback function.

``priv``
    The callback private handle, passed as argument to the callback.


Description
===========

This function sets a callback function for the control. If ``ctrl`` is
NULL, then it will do nothing. If ``notify`` is NULL, then the notify
callback will be removed.

There can be only one notify. If another already exists, then a WARN_ON
will be issued and the function will do nothing.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
