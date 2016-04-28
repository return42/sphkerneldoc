.. -*- coding: utf-8; mode: rst -*-

.. _API-jbd2-journal-invalidatepage:

===========================
jbd2_journal_invalidatepage
===========================

*man jbd2_journal_invalidatepage(9)*

*4.6.0-rc5*


Synopsis
========

.. c:function:: int jbd2_journal_invalidatepage( journal_t * journal, struct page * page, unsigned int offset, unsigned int length )

Arguments
=========

``journal``
    journal to use for flush...

``page``
    page to flush

``offset``
    start of the range to invalidate

``length``
    length of the range to invalidate


Description
===========

Reap page buffers containing data after in the specified range in page.
Can return -EBUSY if buffers are part of the committing transaction and
the page is straddling i_size. Caller then has to wait for current
commit and try again.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
