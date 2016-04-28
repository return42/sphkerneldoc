.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-clear-err:

======================
jbd2_journal_clear_err
======================

*man jbd2_journal_clear_err(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
