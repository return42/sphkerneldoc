
.. _API-typedef-journal-t:

=================
typedef journal_t
=================

*man typedef journal_t(9)*

The journal_t maintains all of the journaling state information for a single filesystem.


Synopsis
========
typedef journal_t;

Description
===========

journal_t is linked to from the fs superblock structure.

We use the journal_t to keep track of all outstanding transaction activity on the filesystem, and to manage the state of the log writing process.

This is an opaque datatype.
