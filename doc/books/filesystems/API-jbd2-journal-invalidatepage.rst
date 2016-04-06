
.. _API-jbd2-journal-invalidatepage:

===========================
jbd2_journal_invalidatepage
===========================

*man jbd2_journal_invalidatepage(9)*

*4.6.0-rc1*


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

Reap page buffers containing data after in the specified range in page. Can return -EBUSY if buffers are part of the committing transaction and the page is straddling i_size.
Caller then has to wait for current commit and try again.
