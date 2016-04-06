
.. _API-bh-submit-read:

==============
bh_submit_read
==============

*man bh_submit_read(9)*

*4.6.0-rc1*

Submit a locked buffer for reading


Synopsis
========

.. c:function:: int bh_submit_read( struct buffer_head * bh )

Arguments
=========

``bh``
    struct buffer_head


Description
===========

Returns zero on success and -EIO on error.
