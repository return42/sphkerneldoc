
.. _API-jbd2-journal-unlock-updates:

===========================
jbd2_journal_unlock_updates
===========================

*man jbd2_journal_unlock_updates(9)*

*4.6.0-rc1*

release barrier


Synopsis
========

.. c:function:: void jbd2_journal_unlock_updates( journal_t * journal )

Arguments
=========

``journal``
    Journal to release the barrier on.


Description
===========

Release a transaction barrier obtained with ``jbd2_journal_lock_updates``.

Should be called without the journal lock held.
