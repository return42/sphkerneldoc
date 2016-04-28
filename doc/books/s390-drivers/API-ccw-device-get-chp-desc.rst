.. -*- coding: utf-8; mode: rst -*-

.. _API-ccw-device-get-chp-desc:

=======================
ccw_device_get_chp_desc
=======================

*man ccw_device_get_chp_desc(9)*

*4.6.0-rc5*

return newly allocated channel-path descriptor


Synopsis
========

.. c:function:: struct channel_path_desc * ccw_device_get_chp_desc( struct ccw_device * cdev, int chp_idx )

Arguments
=========

``cdev``
    device to obtain the descriptor for

``chp_idx``
    index of the channel path


Description
===========

On success return a newly allocated copy of the channel-path description
data associated with the given channel path. Return ``NULL`` on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
