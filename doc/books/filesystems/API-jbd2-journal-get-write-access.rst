
.. _API-jbd2-journal-get-write-access:

=============================
jbd2_journal_get_write_access
=============================

*man jbd2_journal_get_write_access(9)*

*4.6.0-rc1*

notify intent to modify a buffer for metadata (not data) update.


Synopsis
========

.. c:function:: int jbd2_journal_get_write_access( handle_t * handle, struct buffer_head * bh )

Arguments
=========

``handle``
    transaction to add buffer modifications to

``bh``
    bh to be used for metadata writes


Description
===========

Returns an error code or 0 on success.

In full data journalling mode the buffer may be of type BJ_AsyncData, because we're ``write`` ing a buffer which is also part of a shared mapping.
