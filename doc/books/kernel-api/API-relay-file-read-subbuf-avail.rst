
.. _API-relay-file-read-subbuf-avail:

============================
relay_file_read_subbuf_avail
============================

*man relay_file_read_subbuf_avail(9)*

*4.6.0-rc1*

return bytes available in sub-buffer


Synopsis
========

.. c:function:: size_t relay_file_read_subbuf_avail( size_t read_pos, struct rchan_buf * buf )

Arguments
=========

``read_pos``
    file read position

``buf``
    relay channel buffer
