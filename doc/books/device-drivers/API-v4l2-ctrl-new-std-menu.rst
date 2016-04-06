
.. _API-v4l2-ctrl-new-std-menu:

======================
v4l2_ctrl_new_std_menu
======================

*man v4l2_ctrl_new_std_menu(9)*

*4.6.0-rc1*

Allocate and initialize a new standard V4L2 menu control.


Synopsis
========

.. c:function:: struct v4l2_ctrl ⋆ v4l2_ctrl_new_std_menu( struct v4l2_ctrl_handler * hdl, const struct v4l2_ctrl_ops * ops, u32 id, u8 max, u64 mask, u8 def )

Arguments
=========

``hdl``
    The control handler.

``ops``
    The control ops.

``id``
    The control ID.

``max``
    The control's maximum value.

``mask``
    The control's skip mask for menu controls. This makes it easy to skip menu items that are not valid. If bit X is set, then menu item X is skipped. Of course, this only works
    for menus with <= 64 menu items. There are no menus that come close to that number, so this is OK. Should we ever need more, then this will have to be extended to a bit array.

``def``
    The control's default value.


Description
===========

Same as ``v4l2_ctrl_new_std``, but ``min`` is set to 0 and the ``mask`` value determines which menu items are to be skipped.

If ``id`` refers to a non-menu control, then this function will return NULL.
