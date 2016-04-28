.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-stop:

=================
jbd2_journal_stop
=================

*man jbd2_journal_stop(9)*

*4.6.0-rc5*

complete a transaction


Synopsis
========

.. c:function:: int jbd2_journal_stop( handle_t * handle )

Arguments
=========

``handle``
    tranaction to complete.


Description
===========

All done for a particular handle.

There is not much action needed here. We just return any remaining
buffer credits to the transaction and remove the handle. The only
complication is that we need to start a commit operation if the
filesystem is marked for synchronous update.

jbd2_journal_stop itself will not usually return an error, but it may
do so in unusual circumstances. In particular, expect it to return -EIO
if a jbd2_journal_abort has been executed since the transaction began.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
