.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-dirty-metadata:

===========================
jbd2_journal_dirty_metadata
===========================

*man jbd2_journal_dirty_metadata(9)*

*4.6.0-rc5*

mark a buffer as containing dirty metadata


Synopsis
========

.. c:function:: int jbd2_journal_dirty_metadata( handle_t * handle, struct buffer_head * bh )

Arguments
=========

``handle``
    transaction to add buffer to.

``bh``
    buffer to mark


Description
===========

mark dirty metadata which needs to be journaled as part of the current
transaction.

The buffer must have previously had ``jbd2_journal_get_write_access``
called so that it has a valid journal_head attached to the buffer head.

The buffer is placed on the transaction's metadata list and is marked as
belonging to the transaction.

Returns error number or 0 on success.

Special care needs to be taken if the buffer already belongs to the
current committing transaction (in which case we should have frozen data
present for that commit). In that case, we don't relink the


buffer
======

that only gets done when the old transaction finally completes its
commit.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
