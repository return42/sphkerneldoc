
.. _API-v4l2-ctrl-find:

==============
v4l2_ctrl_find
==============

*man v4l2_ctrl_find(9)*

*4.6.0-rc1*

Find a control with the given ID.


Synopsis
========

.. c:function:: struct v4l2_ctrl ⋆ v4l2_ctrl_find( struct v4l2_ctrl_handler * hdl, u32 id )

Arguments
=========

``hdl``
    The control handler.

``id``
    The control ID to find.


Description
===========

If ``hdl`` == NULL this will return NULL as well. Will lock the handler so do not use from inside ``v4l2_ctrl_ops``.
