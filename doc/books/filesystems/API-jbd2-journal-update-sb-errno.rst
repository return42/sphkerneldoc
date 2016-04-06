
.. _API-jbd2-journal-update-sb-errno:

============================
jbd2_journal_update_sb_errno
============================

*man jbd2_journal_update_sb_errno(9)*

*4.6.0-rc1*

Update error in the journal.


Synopsis
========

.. c:function:: void jbd2_journal_update_sb_errno( journal_t * journal )

Arguments
=========

``journal``
    The journal to update.


Description
===========

Update a journal's errno. Write updated superblock to disk waiting for IO to complete.
