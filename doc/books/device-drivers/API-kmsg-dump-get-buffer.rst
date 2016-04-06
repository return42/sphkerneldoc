
.. _API-kmsg-dump-get-buffer:

====================
kmsg_dump_get_buffer
====================

*man kmsg_dump_get_buffer(9)*

*4.6.0-rc1*

copy kmsg log lines


Synopsis
========

.. c:function:: bool kmsg_dump_get_buffer( struct kmsg_dumper * dumper, bool syslog, char * buf, size_t size, size_t * len )

Arguments
=========

``dumper``
    registered kmsg dumper

``syslog``
    include the “<4>” prefixes

``buf``
    buffer to copy the line to

``size``
    maximum size of the buffer

``len``
    length of line placed into buffer


Description
===========

Start at the end of the kmsg buffer and fill the provided buffer with as many of the the ⋆youngest⋆ kmsg records that fit into it. If the buffer is large enough, all available kmsg
records will be copied with a single call.

Consecutive calls will fill the buffer with the next block of available older records, not including the earlier retrieved ones.

A return value of FALSE indicates that there are no more records to read.
