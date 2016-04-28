.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-check-available-features:

=====================================
jbd2_journal_check_available_features
=====================================

*man jbd2_journal_check_available_features(9)*

*4.6.0-rc5*

Check feature set in journalling layer


Synopsis
========

.. c:function:: int jbd2_journal_check_available_features( journal_t * journal, unsigned long compat, unsigned long ro, unsigned long incompat )

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

Check whether the journaling code supports the use of all of a given set
of features on this journal. Return true


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
