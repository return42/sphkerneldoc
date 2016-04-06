
.. _API-jbd2-journal-check-used-features:

================================
jbd2_journal_check_used_features
================================

*man jbd2_journal_check_used_features(9)*

*4.6.0-rc1*

Check if features specified are used.


Synopsis
========

.. c:function:: int jbd2_journal_check_used_features( journal_t * journal, unsigned long compat, unsigned long ro, unsigned long incompat )

Arguments
=========

``journal``
    Journal to check.

``compat``
    bitmask of compatible features

``ro``
    bitmask of features that force read-only mount

``incompat``
    bitmask of incompatible features


Description
===========

Check whether the journal uses all of a given set of features. Return true (non-zero) if it does.
