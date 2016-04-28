.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-dev-info-list-add-str:

==========================
scsi_dev_info_list_add_str
==========================

*man scsi_dev_info_list_add_str(9)*

*4.6.0-rc5*

parse dev_list and add to the scsi_dev_info_list.


Synopsis
========

.. c:function:: int scsi_dev_info_list_add_str( char * dev_list )

Arguments
=========

``dev_list``
    string of device flags to add


Description
===========

Parse dev_list, and add entries to the scsi_dev_info_list. dev_list
is of the form “vendor:product:flag,vendor:product:flag”. dev_list is
modified via strsep. Can be called for command line addition, for proc
or mabye a sysfs interface.


Returns
=======

0 if OK, -error on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
