.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-extend:

===================
jbd2_journal_extend
===================

*man jbd2_journal_extend(9)*

*4.6.0-rc5*

extend buffer credits.


Synopsis
========

.. c:function:: int jbd2_journal_extend( handle_t * handle, int nblocks )

Arguments
=========

``handle``
    handle to 'extend'

``nblocks``
    nr blocks to try to extend by.


Description
===========

Some transactions, such as large extends and truncates, can be done
atomically all at once or in several stages. The operation requests a
credit for a number of buffer modications in advance, but can extend its
credit if it needs more.

jbd2_journal_extend tries to give the running handle more buffer
credits. It does not guarantee that allocation - this is a best-effort
only. The calling process MUST be able to deal cleanly with a failure to
extend here.

Return 0 on success, non-zero on failure.

return code < 0 implies an error return code > 0 implies normal
transaction-full status.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
