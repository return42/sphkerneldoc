.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/sg_pool.c

.. _`sg_free_table_chained`:

sg_free_table_chained
=====================

.. c:function:: void sg_free_table_chained(struct sg_table *table, bool first_chunk)

    Free a previously mapped sg table

    :param struct sg_table \*table:
        The sg table header to use

    :param bool first_chunk:
        was first_chunk not NULL in sg_alloc_table_chained?

.. _`sg_free_table_chained.description`:

Description
-----------

Free an sg table previously allocated and setup with
\ :c:func:`sg_alloc_table_chained`\ .

.. _`sg_alloc_table_chained`:

sg_alloc_table_chained
======================

.. c:function:: int sg_alloc_table_chained(struct sg_table *table, int nents, struct scatterlist *first_chunk)

    Allocate and chain SGLs in an sg table

    :param struct sg_table \*table:
        The sg table header to use

    :param int nents:
        Number of entries in sg list

    :param struct scatterlist \*first_chunk:
        first SGL

.. _`sg_alloc_table_chained.description`:

Description
-----------

Allocate and chain SGLs in an sg table. If \ ``nents``\ @ is larger than
SG_CHUNK_SIZE a chained sg table will be setup.

.. This file was automatic generated / don't edit.

