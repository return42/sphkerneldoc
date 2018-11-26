.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/scatterlist.h

.. _`sg_assign_page`:

sg_assign_page
==============

.. c:function:: void sg_assign_page(struct scatterlist *sg, struct page *page)

    Assign a given page to an SG entry

    :param sg:
        SG entry
    :type sg: struct scatterlist \*

    :param page:
        The page
    :type page: struct page \*

.. _`sg_assign_page.description`:

Description
-----------

Assign page to sg entry. Also see \ :c:func:`sg_set_page`\ , the most commonly used
variant.

.. _`sg_set_page`:

sg_set_page
===========

.. c:function:: void sg_set_page(struct scatterlist *sg, struct page *page, unsigned int len, unsigned int offset)

    Set sg entry to point at given page

    :param sg:
        SG entry
    :type sg: struct scatterlist \*

    :param page:
        The page
    :type page: struct page \*

    :param len:
        Length of data
    :type len: unsigned int

    :param offset:
        Offset into page
    :type offset: unsigned int

.. _`sg_set_page.description`:

Description
-----------

Use this function to set an sg entry pointing at a page, never assign
the page directly. We encode sg table information in the lower bits
of the page pointer. See \ :c:func:`sg_page`\  for looking up the page belonging
to an sg entry.

.. _`sg_set_buf`:

sg_set_buf
==========

.. c:function:: void sg_set_buf(struct scatterlist *sg, const void *buf, unsigned int buflen)

    Set sg entry to point at given data

    :param sg:
        SG entry
    :type sg: struct scatterlist \*

    :param buf:
        Data
    :type buf: const void \*

    :param buflen:
        Data length
    :type buflen: unsigned int

.. _`sg_chain`:

sg_chain
========

.. c:function:: void sg_chain(struct scatterlist *prv, unsigned int prv_nents, struct scatterlist *sgl)

    Chain two sglists together

    :param prv:
        First scatterlist
    :type prv: struct scatterlist \*

    :param prv_nents:
        Number of entries in prv
    :type prv_nents: unsigned int

    :param sgl:
        Second scatterlist
    :type sgl: struct scatterlist \*

.. _`sg_chain.description`:

Description
-----------

Links \ ``prv``\ @ and \ ``sgl``\ @ together, to form a longer scatterlist.

.. _`sg_mark_end`:

sg_mark_end
===========

.. c:function:: void sg_mark_end(struct scatterlist *sg)

    Mark the end of the scatterlist

    :param sg:
        SG entryScatterlist
    :type sg: struct scatterlist \*

.. _`sg_mark_end.description`:

Description
-----------

Marks the passed in sg entry as the termination point for the sg
table. A call to \ :c:func:`sg_next`\  on this entry will return NULL.

.. _`sg_unmark_end`:

sg_unmark_end
=============

.. c:function:: void sg_unmark_end(struct scatterlist *sg)

    Undo setting the end of the scatterlist

    :param sg:
        SG entryScatterlist
    :type sg: struct scatterlist \*

.. _`sg_unmark_end.description`:

Description
-----------

Removes the termination marker from the given entry of the scatterlist.

.. _`sg_phys`:

sg_phys
=======

.. c:function:: dma_addr_t sg_phys(struct scatterlist *sg)

    Return physical address of an sg entry

    :param sg:
        SG entry
    :type sg: struct scatterlist \*

.. _`sg_phys.description`:

Description
-----------

This calls \ :c:func:`page_to_phys`\  on the page in this sg entry, and adds the
sg offset. The caller must know that it is legal to call \ :c:func:`page_to_phys`\ 
on the sg page.

.. _`sg_virt`:

sg_virt
=======

.. c:function:: void *sg_virt(struct scatterlist *sg)

    Return virtual address of an sg entry

    :param sg:
        SG entry
    :type sg: struct scatterlist \*

.. _`sg_virt.description`:

Description
-----------

This calls \ :c:func:`page_address`\  on the page in this sg entry, and adds the
sg offset. The caller must know that the sg page has a valid virtual
mapping.

.. _`sg_init_marker`:

sg_init_marker
==============

.. c:function:: void sg_init_marker(struct scatterlist *sgl, unsigned int nents)

    Initialize markers in sg table

    :param sgl:
        The SG table
    :type sgl: struct scatterlist \*

    :param nents:
        Number of entries in table
    :type nents: unsigned int

.. _`sg_page_iter_page`:

sg_page_iter_page
=================

.. c:function:: struct page *sg_page_iter_page(struct sg_page_iter *piter)

    get the current page held by the page iterator

    :param piter:
        page iterator holding the page
    :type piter: struct sg_page_iter \*

.. _`sg_page_iter_dma_address`:

sg_page_iter_dma_address
========================

.. c:function:: dma_addr_t sg_page_iter_dma_address(struct sg_page_iter *piter)

    get the dma address of the current page held by the page iterator.

    :param piter:
        page iterator holding the page
    :type piter: struct sg_page_iter \*

.. _`for_each_sg_page`:

for_each_sg_page
================

.. c:function::  for_each_sg_page( sglist,  piter,  nents,  pgoffset)

    iterate over the pages of the given sg list

    :param sglist:
        sglist to iterate over
    :type sglist: 

    :param piter:
        page iterator to hold current page, sg, sg_pgoffset
    :type piter: 

    :param nents:
        maximum number of sg entries to iterate over
    :type nents: 

    :param pgoffset:
        starting page offset
    :type pgoffset: 

.. This file was automatic generated / don't edit.

