
.. _API-jbd2-journal-wipe:

=================
jbd2_journal_wipe
=================

*man jbd2_journal_wipe(9)*

*4.6.0-rc1*

Wipe journal contents


Synopsis
========

.. c:function:: int jbd2_journal_wipe( journal_t * journal, int write )

Arguments
=========

``journal``
    Journal to act on.

``write``
    flag (see below)


Description
===========

Wipe out all of the contents of a journal, safely. This will produce a warning if the journal contains any valid recovery information. Must be called between journal_init_⋆() and
``jbd2_journal_load``.

If 'write' is non-zero, then we wipe out the journal on disk; otherwise we merely suppress recovery.
