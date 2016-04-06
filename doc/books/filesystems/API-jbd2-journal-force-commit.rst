
.. _API-jbd2-journal-force-commit:

=========================
jbd2_journal_force_commit
=========================

*man jbd2_journal_force_commit(9)*

*4.6.0-rc1*

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

Caller want unconditional commit. We can only force the running transaction if we don't have an active handle, otherwise, we will deadlock.
