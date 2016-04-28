.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-recover:

====================
jbd2_journal_recover
====================

*man jbd2_journal_recover(9)*

*4.6.0-rc5*

recovers a on-disk journal


Synopsis
========

.. c:function:: int jbd2_journal_recover( journal_t * journal )

Arguments
=========

``journal``
    the journal to recover


Description
===========

The primary function for recovering the log contents when mounting a
journaled device.

Recovery is done in three passes. In the first pass, we look for the end
of the log. In the second, we assemble the list of revoke blocks. In the
third and final pass, we replay any un-revoked blocks in the log.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
