.. -*- coding: utf-8; mode: rst -*-

.. _API-scsi-inq-str:

============
scsi_inq_str
============

*man scsi_inq_str(9)*

*4.6.0-rc5*

print INQUIRY data from min to max index, strip trailing whitespace


Synopsis
========

.. c:function:: unsigned char * scsi_inq_str( unsigned char * buf, unsigned char * inq, unsigned first, unsigned end )

Arguments
=========

``buf``
    Output buffer with at least end-first+1 bytes of space

``inq``
    Inquiry buffer (input)

``first``
    Offset of string into inq

``end``
    Index after last character in inq


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
