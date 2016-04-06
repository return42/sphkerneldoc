
.. _API-v4l2-ctrl-modify-range:

======================
v4l2_ctrl_modify_range
======================

*man v4l2_ctrl_modify_range(9)*

*4.6.0-rc1*

Update the range of a control.


Synopsis
========

.. c:function:: int v4l2_ctrl_modify_range( struct v4l2_ctrl * ctrl, s64 min, s64 max, u64 step, s64 def )

Arguments
=========

``ctrl``
    The control to update.

``min``
    The control's minimum value.

``max``
    The control's maximum value.

``step``
    The control's step value

``def``
    The control's default value.


Description
===========

Update the range of a control on the fly. This works for control types INTEGER, BOOLEAN, MENU, INTEGER MENU and BITMASK. For menu controls the ``step`` value is interpreted as a
menu_skip_mask.

An error is returned if one of the range arguments is invalid for this control type.

This function assumes that the control handler is not locked and will take the lock itself.
