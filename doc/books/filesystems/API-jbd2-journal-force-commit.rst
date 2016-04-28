.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-force-commit:

=========================
jbd2_journal_force_commit
=========================

*man jbd2_journal_force_commit(9)*

*4.6.0-rc5*

force any uncommitted transactions


Synopsis
========

.. c:function:: int jbd2_journal_force_commit( journal_t * journal )

Arguments
=========

``journal``
    journal to force


Description
===========

Caller want unconditional commit. We can only force the running
transaction if we don't have an active handle, otherwise, we will
deadlock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
