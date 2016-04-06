
.. _API-unlock-page:

===========
unlock_page
===========

*man unlock_page(9)*

*4.6.0-rc1*

unlock a locked page


Synopsis
========

.. c:function:: void unlock_page( struct page * page )

Arguments
=========

``page``
    the page


Description
===========

Unlocks the page and wakes up sleepers in ``___wait_on_page_locked``. Also wakes sleepers in ``wait_on_page_writeback`` because the wakeup mechanism between PageLocked pages and
PageWriteback pages is shared. But that's OK - sleepers in ``wait_on_page_writeback`` just go back to sleep.

The mb is necessary to enforce ordering between the clear_bit and the read of the waitqueue (to avoid SMP races with a parallel ``wait_on_page_locked``).
