.. -*- coding: utf-8; mode: rst -*-

.. _API-mpt-set-taskmgmt-in-progress-flag:

=================================
mpt_set_taskmgmt_in_progress_flag
=================================

*man mpt_set_taskmgmt_in_progress_flag(9)*

*4.6.0-rc5*

set flags associated with task management


Synopsis
========

.. c:function:: int mpt_set_taskmgmt_in_progress_flag( MPT_ADAPTER * ioc )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure


Description
===========

Returns 0 for SUCCESS or -1 if FAILED.

If -1 is return, then it was not possible to set the flags


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
