.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-destroy:

====================
jbd2_journal_destroy
====================

*man jbd2_journal_destroy(9)*

*4.6.0-rc5*

Release a journal_t structure.


Synopsis
========

.. c:function:: int jbd2_journal_destroy( journal_t * journal )

Arguments
=========

``journal``
    Journal to act on.


Description
===========

Release a journal_t structure once it is no longer in use by the
journaled object. Return <0 if we couldn't clean up the journal.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
