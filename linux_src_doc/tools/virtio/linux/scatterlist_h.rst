.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/virtio/linux/scatterlist.h

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

.. This file was automatic generated / don't edit.

