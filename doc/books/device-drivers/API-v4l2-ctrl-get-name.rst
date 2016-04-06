
.. _API-v4l2-ctrl-get-name:

==================
v4l2_ctrl_get_name
==================

*man v4l2_ctrl_get_name(9)*

*4.6.0-rc1*

Get the name of the control


Synopsis
========

.. c:function:: const char ⋆ v4l2_ctrl_get_name( u32 id )

Arguments
=========

``id``
    The control ID.


Description
===========

This function returns the name of the given control ID or NULL if it isn't a known control.
