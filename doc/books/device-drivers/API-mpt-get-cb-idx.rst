
.. _API-mpt-get-cb-idx:

==============
mpt_get_cb_idx
==============

*man mpt_get_cb_idx(9)*

*4.6.0-rc1*

obtain cb_idx for registered driver


Synopsis
========

.. c:function:: u8 mpt_get_cb_idx( MPT_DRIVER_CLASS dclass )

Arguments
=========

``dclass``
    class driver enum


Description
===========

Returns cb_idx, or zero means it wasn't found
