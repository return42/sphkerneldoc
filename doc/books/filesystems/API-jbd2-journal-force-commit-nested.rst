
.. _API-jbd2-journal-force-commit-nested:

================================
jbd2_journal_force_commit_nested
================================

*man jbd2_journal_force_commit_nested(9)*

*4.6.0-rc1*


Synopsis
========

.. c:function:: int jbd2_journal_force_commit_nested( journal_t * journal )

Arguments
=========

``journal``
    journal to force Returns true if progress was made.


Description
===========

transaction. This is used for forcing out undo-protected data which contains bitmaps, when the fs is running out of space.
