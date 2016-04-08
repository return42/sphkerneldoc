
.. _API-ccw-device-get-chp-desc:

=======================
ccw_device_get_chp_desc
=======================

*man ccw_device_get_chp_desc(9)*

*4.6.0-rc1*

return newly allocated channel-path descriptor


Synopsis
========

.. c:function:: struct channel_path_desc ⋆ ccw_device_get_chp_desc( struct ccw_device * cdev, int chp_idx )

Arguments
=========

``cdev``
    device to obtain the descriptor for

``chp_idx``
    index of the channel path


Description
===========

On success return a newly allocated copy of the channel-path description data associated with the given channel path. Return ``NULL`` on error.
