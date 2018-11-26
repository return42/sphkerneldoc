.. -*- coding: utf-8; mode: rst -*-
.. src-file: mm/workingset.c

.. _`workingset_eviction`:

workingset_eviction
===================

.. c:function:: void *workingset_eviction(struct address_space *mapping, struct page *page)

    note the eviction of a page from memory

    :param mapping:
        address space the page was backing
    :type mapping: struct address_space \*

    :param page:
        the page being evicted
    :type page: struct page \*

.. _`workingset_eviction.description`:

Description
-----------

Returns a shadow entry to be stored in \ ``mapping->i_pages``\  in place
of the evicted \ ``page``\  so that a later refault can be detected.

.. _`workingset_refault`:

workingset_refault
==================

.. c:function:: void workingset_refault(struct page *page, void *shadow)

    evaluate the refault of a previously evicted page

    :param page:
        the freshly allocated replacement page
    :type page: struct page \*

    :param shadow:
        shadow entry of the evicted page
    :type shadow: void \*

.. _`workingset_refault.description`:

Description
-----------

Calculates and evaluates the refault distance of the previously
evicted page in the context of the node it was allocated in.

.. _`workingset_activation`:

workingset_activation
=====================

.. c:function:: void workingset_activation(struct page *page)

    note a page activation

    :param page:
        page that is being activated
    :type page: struct page \*

.. This file was automatic generated / don't edit.

