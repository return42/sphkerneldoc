
.. _API-mpt-print-ioc-summary:

=====================
mpt_print_ioc_summary
=====================

*man mpt_print_ioc_summary(9)*

*4.6.0-rc1*

Write ASCII summary of IOC to a buffer.


Synopsis
========

.. c:function:: void mpt_print_ioc_summary( MPT_ADAPTER * ioc, char * buffer, int * size, int len, int showlan )

Arguments
=========

``ioc``
    Pointer to MPT_ADAPTER structure

``buffer``
    Pointer to buffer where IOC summary info should be written

``size``
    Pointer to number of bytes we wrote (set by this routine)

``len``
    Offset at which to start writing in buffer

``showlan``
    Display LAN stuff?


Description
===========

This routine writes (english readable) ASCII text, which represents a summary of IOC information, to a buffer.
