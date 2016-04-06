
.. _API-jbd2-journal-set-features:

=========================
jbd2_journal_set_features
=========================

*man jbd2_journal_set_features(9)*

*4.6.0-rc1*

Mark a given journal feature in the superblock


Synopsis
========

.. c:function:: int jbd2_journal_set_features( journal_t * journal, unsigned long compat, unsigned long ro, unsigned long incompat )

Arguments
=========

``journal``
    Journal to act on.

``compat``
    bitmask of compatible features

``ro``
    bitmask of features that force read-only mount

``incompat``
    bitmask of incompatible features


Description
===========

Mark a given journal feature as present on the superblock. Returns true if the requested features could be set.
