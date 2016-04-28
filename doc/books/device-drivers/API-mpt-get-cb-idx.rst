.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-get-cb-idx:

==============
mpt_get_cb_idx
==============

*man mpt_get_cb_idx(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
