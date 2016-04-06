
.. _API-bh-uptodate-or-lock:

===================
bh_uptodate_or_lock
===================

*man bh_uptodate_or_lock(9)*

*4.6.0-rc1*

Test whether the buffer is uptodate


Synopsis
========

.. c:function:: int bh_uptodate_or_lock( struct buffer_head * bh )

Arguments
=========

``bh``
    struct buffer_head


Description
===========

Return true if the buffer is up-to-date and false, with the buffer locked, if not.
