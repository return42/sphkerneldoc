.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/page_counter.c

.. _`page_counter_cancel`:

page_counter_cancel
===================

.. c:function:: void page_counter_cancel(struct page_counter *counter, unsigned long nr_pages)

    take pages out of the local counter

    :param struct page_counter \*counter:
        counter

    :param unsigned long nr_pages:
        number of pages to cancel

.. _`page_counter_charge`:

page_counter_charge
===================

.. c:function:: void page_counter_charge(struct page_counter *counter, unsigned long nr_pages)

    hierarchically charge pages

    :param struct page_counter \*counter:
        counter

    :param unsigned long nr_pages:
        number of pages to charge

.. _`page_counter_charge.note`:

NOTE
----

This does not consider any configured counter limits.

.. _`page_counter_try_charge`:

page_counter_try_charge
=======================

.. c:function:: bool page_counter_try_charge(struct page_counter *counter, unsigned long nr_pages, struct page_counter **fail)

    try to hierarchically charge pages

    :param struct page_counter \*counter:
        counter

    :param unsigned long nr_pages:
        number of pages to charge

    :param struct page_counter \*\*fail:
        points first counter to hit its limit, if any

.. _`page_counter_try_charge.description`:

Description
-----------

Returns \ ``true``\  on success, or \ ``false``\  and \ ``fail``\  if the counter or one
of its ancestors has hit its configured limit.

.. _`page_counter_uncharge`:

page_counter_uncharge
=====================

.. c:function:: void page_counter_uncharge(struct page_counter *counter, unsigned long nr_pages)

    hierarchically uncharge pages

    :param struct page_counter \*counter:
        counter

    :param unsigned long nr_pages:
        number of pages to uncharge

.. _`page_counter_limit`:

page_counter_limit
==================

.. c:function:: int page_counter_limit(struct page_counter *counter, unsigned long limit)

    limit the number of pages allowed

    :param struct page_counter \*counter:
        counter

    :param unsigned long limit:
        limit to set

.. _`page_counter_limit.description`:

Description
-----------

Returns 0 on success, -EBUSY if the current number of pages on the
counter already exceeds the specified limit.

The caller must serialize invocations on the same counter.

.. _`page_counter_memparse`:

page_counter_memparse
=====================

.. c:function:: int page_counter_memparse(const char *buf, const char *max, unsigned long *nr_pages)

    \ :c:func:`memparse`\  for page counter limits

    :param const char \*buf:
        string to parse

    :param const char \*max:
        string meaning maximum possible value

    :param unsigned long \*nr_pages:
        returns the result in number of pages

.. _`page_counter_memparse.description`:

Description
-----------

Returns -EINVAL, or 0 and \ ``nr_pages``\  on success.  \ ``nr_pages``\  will be
limited to \ ``PAGE_COUNTER_MAX``\ .

.. This file was automatic generated / don't edit.

