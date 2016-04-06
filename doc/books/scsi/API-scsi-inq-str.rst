
.. _API-scsi-inq-str:

============
scsi_inq_str
============

*man scsi_inq_str(9)*

*4.6.0-rc1*

print INQUIRY data from min to max index, strip trailing whitespace


Synopsis
========

.. c:function:: unsigned char ⋆ scsi_inq_str( unsigned char * buf, unsigned char * inq, unsigned first, unsigned end )

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
