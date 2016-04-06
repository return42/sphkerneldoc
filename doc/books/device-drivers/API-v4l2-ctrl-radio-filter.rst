
.. _API-v4l2-ctrl-radio-filter:

======================
v4l2_ctrl_radio_filter
======================

*man v4l2_ctrl_radio_filter(9)*

*4.6.0-rc1*

Standard filter for radio controls.


Synopsis
========

.. c:function:: bool v4l2_ctrl_radio_filter( const struct v4l2_ctrl * ctrl )

Arguments
=========

``ctrl``
    The control that is filtered.


Description
===========

This will return true for any controls that are valid for radio device nodes. Those are all of the V4L2_CID_AUDIO_⋆ user controls and all FM transmitter class controls.

This function is to be used with ``v4l2_ctrl_add_handler``.
