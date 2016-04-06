
.. _API-jbd2-journal-lock-updates:

=========================
jbd2_journal_lock_updates
=========================

*man jbd2_journal_lock_updates(9)*

*4.6.0-rc1*

establish a transaction barrier.


Synopsis
========

.. c:function:: void jbd2_journal_lock_updates( journal_t * journal )

Arguments
=========

``journal``
    Journal to establish a barrier on.


Description
===========

This locks out any further updates from being started, and blocks until all existing updates have completed, returning only once the journal is in a quiescent state with no updates
running.

The journal lock should not be held on entry.
