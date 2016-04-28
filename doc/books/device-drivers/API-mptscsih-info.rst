.. -*- coding: utf-8; mode: rst -*-

.. _API-mptscsih-info:

=============
mptscsih_info
=============

*man mptscsih_info(9)*

*4.6.0-rc5*

Return information about MPT adapter


Synopsis
========

.. c:function:: const char * mptscsih_info( struct Scsi_Host * SChost )

Arguments
=========

``SChost``
    Pointer to Scsi_Host structure


Description
===========

(linux scsi_host_template.info routine)

Returns pointer to buffer where information was written.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
