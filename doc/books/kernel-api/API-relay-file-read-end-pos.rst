
.. _API-relay-file-read-end-pos:

=======================
relay_file_read_end_pos
=======================

*man relay_file_read_end_pos(9)*

*4.6.0-rc1*

return the new read position


Synopsis
========

.. c:function:: size_t relay_file_read_end_pos( struct rchan_buf * buf, size_t read_pos, size_t count )

Arguments
=========

``buf``
    relay channel buffer

``read_pos``
    file read position

``count``
    number of bytes to be read
