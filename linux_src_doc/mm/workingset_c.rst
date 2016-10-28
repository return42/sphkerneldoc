.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/workingset.c

.. _`workingset_eviction`:

workingset_eviction
===================

.. c:function:: void *workingset_eviction(struct address_space *mapping, struct page *page)

    note the eviction of a page from memory

    :param struct address_space \*mapping:
        address space the page was backing

    :param struct page \*page:
        the page being evicted

.. _`workingset_eviction.description`:

Description
-----------

Returns a shadow entry to be stored in \ ``mapping``\ ->page_tree in place
of the evicted \ ``page``\  so that a later refault can be detected.

.. _`workingset_refault`:

workingset_refault
==================

.. c:function:: bool workingset_refault(void *shadow)

    evaluate the refault of a previously evicted page

    :param void \*shadow:
        shadow entry of the evicted page

.. _`workingset_refault.description`:

Description
-----------

Calculates and evaluates the refault distance of the previously
evicted page in the context of the zone it was allocated in.

Returns \ ``true``\  if the page should be activated, \ ``false``\  otherwise.

.. _`workingset_activation`:

workingset_activation
=====================

.. c:function:: void workingset_activation(struct page *page)

    note a page activation

    :param struct page \*page:
        page that is being activated

.. This file was automatic generated / don't edit.

