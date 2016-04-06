
.. _API-jbd2-journal-load:

=================
jbd2_journal_load
=================

*man jbd2_journal_load(9)*

*4.6.0-rc1*

Read journal from disk.


Synopsis
========

.. c:function:: int jbd2_journal_load( journal_t * journal )

Arguments
=========

``journal``
    Journal to act on.


Description
===========

Given a journal_t structure which tells us which disk blocks contain a journal, read the journal from disk to initialise the in-memory structures.
