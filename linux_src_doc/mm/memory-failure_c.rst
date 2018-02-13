.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/memory-failure.c

.. _`get_hwpoison_page`:

get_hwpoison_page
=================

.. c:function:: int get_hwpoison_page(struct page *page)

    Get refcount for memory error handling:

    :param struct page \*page:
        raw error page (hit by memory error)

.. _`get_hwpoison_page.return`:

Return
------

return 0 if failed to grab the refcount, otherwise true (some
non-zero value.)

.. _`memory_failure`:

memory_failure
==============

.. c:function:: int memory_failure(unsigned long pfn, int flags)

    Handle memory failure of a page.

    :param unsigned long pfn:
        Page Number of the corrupted page

    :param int flags:
        fine tune action taken

.. _`memory_failure.description`:

Description
-----------

This function is called by the low level machine check code
of an architecture when it detects hardware memory corruption
of a page. It tries its best to recover, which includes
dropping pages, killing processes etc.

The function is primarily of use for corruptions that
happen outside the current execution context (e.g. when
detected by a background scrubber)

Must run in process context (e.g. a work queue) with interrupts
enabled and no spinlocks hold.

.. _`memory_failure_queue`:

memory_failure_queue
====================

.. c:function:: void memory_failure_queue(unsigned long pfn, int flags)

    Schedule handling memory failure of a page.

    :param unsigned long pfn:
        Page Number of the corrupted page

    :param int flags:
        Flags for memory failure handling

.. _`memory_failure_queue.description`:

Description
-----------

This function is called by the low level hardware error handler
when it detects hardware memory corruption of a page. It schedules
the recovering of error page, including dropping pages, killing
processes etc.

The function is primarily of use for corruptions that
happen outside the current execution context (e.g. when
detected by a background scrubber)

Can run in IRQ context.

.. _`unpoison_memory`:

unpoison_memory
===============

.. c:function:: int unpoison_memory(unsigned long pfn)

    Unpoison a previously poisoned page

    :param unsigned long pfn:
        Page number of the to be unpoisoned page

.. _`unpoison_memory.description`:

Description
-----------

Software-unpoison a page that has been poisoned by
\ :c:func:`memory_failure`\  earlier.

This is only done on the software-level, so it only works
for linux injected failures, not real hardware failures

Returns 0 for success, otherwise -errno.

.. _`soft_offline_page`:

soft_offline_page
=================

.. c:function:: int soft_offline_page(struct page *page, int flags)

    Soft offline a page.

    :param struct page \*page:
        page to offline

    :param int flags:
        flags. Same as \ :c:func:`memory_failure`\ .

.. _`soft_offline_page.description`:

Description
-----------

Returns 0 on success, otherwise negated errno.

Soft offline a page, by migration or invalidation,
without killing anything. This is for the case when
a page is not corrupted yet (so it's still valid to access),
but has had a number of corrected errors and is better taken
out.

The actual policy on when to do that is maintained by
user space.

This should never impact any application or cause data loss,
however it might take some time.

This is not a 100% solution for all memory, but tries to be
\`\`good enough'' for the majority of memory.

.. This file was automatic generated / don't edit.

