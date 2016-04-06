
.. _API-jbd2-journal-clear-err:

======================
jbd2_journal_clear_err
======================

*man jbd2_journal_clear_err(9)*

*4.6.0-rc1*

clears the journal's error state


Synopsis
========

.. c:function:: int jbd2_journal_clear_err( journal_t * journal )

Arguments
=========

``journal``
    journal to act on.


Description
===========

An error must be cleared or acked to take a FS out of readonly mode.
