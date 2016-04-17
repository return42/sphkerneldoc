.. -*- coding: utf-8; mode: rst -*-

=============
scatterlist.h
=============


.. _`sg_assign_page`:

sg_assign_page
==============

.. c:function:: void sg_assign_page (struct scatterlist *sg, struct page *page)

    Assign a given page to an SG entry

    :param struct scatterlist \*sg:
        SG entry

    :param struct page \*page:
        The page



.. _`sg_assign_page.description`:

Description
-----------

Assign page to sg entry. Also see :c:func:`sg_set_page`, the most commonly used
variant.



.. _`sg_set_page`:

sg_set_page
===========

.. c:function:: void sg_set_page (struct scatterlist *sg, struct page *page, unsigned int len, unsigned int offset)

    Set sg entry to point at given page

    :param struct scatterlist \*sg:
        SG entry

    :param struct page \*page:
        The page

    :param unsigned int len:
        Length of data

    :param unsigned int offset:
        Offset into page



.. _`sg_set_page.description`:

Description
-----------

Use this function to set an sg entry pointing at a page, never assign
the page directly. We encode sg table information in the lower bits
of the page pointer. See :c:func:`sg_page` for looking up the page belonging
to an sg entry.



.. _`sg_set_buf`:

sg_set_buf
==========

.. c:function:: void sg_set_buf (struct scatterlist *sg, const void *buf, unsigned int buflen)

    Set sg entry to point at given data

    :param struct scatterlist \*sg:
        SG entry

    :param const void \*buf:
        Data

    :param unsigned int buflen:
        Data length



.. _`sg_chain`:

sg_chain
========

.. c:function:: void sg_chain (struct scatterlist *prv, unsigned int prv_nents, struct scatterlist *sgl)

    Chain two sglists together

    :param struct scatterlist \*prv:
        First scatterlist

    :param unsigned int prv_nents:
        Number of entries in prv

    :param struct scatterlist \*sgl:
        Second scatterlist



.. _`sg_chain.description`:

Description
-----------

Links ``prv``\ @ and ``sgl``\ @ together, to form a longer scatterlist.



.. _`sg_mark_end`:

sg_mark_end
===========

.. c:function:: void sg_mark_end (struct scatterlist *sg)

    Mark the end of the scatterlist

    :param struct scatterlist \*sg:
        SG entryScatterlist



.. _`sg_mark_end.description`:

Description
-----------

Marks the passed in sg entry as the termination point for the sg
table. A call to :c:func:`sg_next` on this entry will return NULL.



.. _`sg_unmark_end`:

sg_unmark_end
=============

.. c:function:: void sg_unmark_end (struct scatterlist *sg)

    Undo setting the end of the scatterlist

    :param struct scatterlist \*sg:
        SG entryScatterlist



.. _`sg_unmark_end.description`:

Description
-----------

Removes the termination marker from the given entry of the scatterlist.



.. _`sg_phys`:

sg_phys
=======

.. c:function:: dma_addr_t sg_phys (struct scatterlist *sg)

    Return physical address of an sg entry

    :param struct scatterlist \*sg:
        SG entry



.. _`sg_phys.description`:

Description
-----------

This calls :c:func:`page_to_phys` on the page in this sg entry, and adds the
sg offset. The caller must know that it is legal to call :c:func:`page_to_phys`
on the sg page.



.. _`sg_virt`:

sg_virt
=======

.. c:function:: void *sg_virt (struct scatterlist *sg)

    Return virtual address of an sg entry

    :param struct scatterlist \*sg:
        SG entry



.. _`sg_virt.description`:

Description
-----------

This calls :c:func:`page_address` on the page in this sg entry, and adds the
sg offset. The caller must know that the sg page has a valid virtual
mapping.



.. _`sg_page_iter_page`:

sg_page_iter_page
=================

.. c:function:: struct page *sg_page_iter_page (struct sg_page_iter *piter)

    get the current page held by the page iterator

    :param struct sg_page_iter \*piter:
        page iterator holding the page



.. _`sg_page_iter_dma_address`:

sg_page_iter_dma_address
========================

.. c:function:: dma_addr_t sg_page_iter_dma_address (struct sg_page_iter *piter)

    get the dma address of the current page held by the page iterator.

    :param struct sg_page_iter \*piter:
        page iterator holding the page



.. _`for_each_sg_page`:

for_each_sg_page
================

.. c:function:: for_each_sg_page ( sglist,  piter,  nents,  pgoffset)

    iterate over the pages of the given sg list

    :param sglist:
        sglist to iterate over

    :param piter:
        page iterator to hold current page, sg, sg_pgoffset

    :param nents:
        maximum number of sg entries to iterate over

    :param pgoffset:
        starting page offset

