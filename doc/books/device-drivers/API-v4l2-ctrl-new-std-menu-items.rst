.. -*- coding: utf-8; mode: rst -*-

.. _API-v4l2-ctrl-new-std-menu-items:

============================
v4l2_ctrl_new_std_menu_items
============================

*man v4l2_ctrl_new_std_menu_items(9)*

*4.6.0-rc5*

Create a new standard V4L2 menu control with driver specific menu.


Synopsis
========

.. c:function:: struct v4l2_ctrl * v4l2_ctrl_new_std_menu_items( struct v4l2_ctrl_handler * hdl, const struct v4l2_ctrl_ops * ops, u32 id, u8 max, u64 mask, u8 def, const char *const * qmenu )

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
    The control's skip mask for menu controls. This makes it easy to
    skip menu items that are not valid. If bit X is set, then menu item
    X is skipped. Of course, this only works for menus with <= 64 menu
    items. There are no menus that come close to that number, so this is
    OK. Should we ever need more, then this will have to be extended to
    a bit array.

``def``
    The control's default value.

``qmenu``
    The new menu.


Description
===========

Same as ``v4l2_ctrl_new_std_menu``, but ``qmenu`` will be the driver
specific menu of this control.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
