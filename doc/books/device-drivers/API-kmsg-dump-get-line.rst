
.. _API-kmsg-dump-get-line:

==================
kmsg_dump_get_line
==================

*man kmsg_dump_get_line(9)*

*4.6.0-rc1*

retrieve one kmsg log line


Synopsis
========

.. c:function:: bool kmsg_dump_get_line( struct kmsg_dumper * dumper, bool syslog, char * line, size_t size, size_t * len )

Arguments
=========

``dumper``
    registered kmsg dumper

``syslog``
    include the “<4>” prefixes

``line``
    buffer to copy the line to

``size``
    maximum size of the buffer

``len``
    length of line placed into buffer


Description
===========

Start at the beginning of the kmsg buffer, with the oldest kmsg record, and copy one record into the provided buffer.

Consecutive calls will return the next available record moving towards the end of the buffer with the youngest messages.

A return value of FALSE indicates that there are no more records to read.
