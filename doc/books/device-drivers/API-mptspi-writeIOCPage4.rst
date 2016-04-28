.. -*- coding: utf-8; mode: rst -*-

.. _API-mptspi-writeIOCPage4:

====================
mptspi_writeIOCPage4
====================

*man mptspi_writeIOCPage4(9)*

*4.6.0-rc5*

write IOC Page 4


Synopsis
========

.. c:function:: int mptspi_writeIOCPage4( MPT_SCSI_HOST * hd, u8 channel, u8 id )

Arguments
=========

``hd``
    Pointer to a SCSI Host Structure

``channel``
    channel number

``id``
    write IOC Page4 for this ID & Bus


Return
======

-EAGAIN if unable to obtain a Message Frame or 0 if success.


Remark
======

We do not wait for a return, write pages sequentially.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
