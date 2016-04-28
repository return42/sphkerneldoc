.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-flush:

==================
jbd2_journal_flush
==================

*man jbd2_journal_flush(9)*

*4.6.0-rc5*

Flush journal


Synopsis
========

.. c:function:: int jbd2_journal_flush( journal_t * journal )

Arguments
=========

``journal``
    Journal to act on.


Description
===========

Flush all data for a given journal to disk and empty the journal.
Filesystems can use this when remounting readonly to ensure that
recovery does not need to happen on remount.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
