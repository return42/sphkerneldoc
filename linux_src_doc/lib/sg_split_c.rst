.. -*- coding: utf-8; mode: rst -*-
.. src-file: lib/sg_split.c

.. _`sg_split`:

sg_split
========

.. c:function:: int sg_split(struct scatterlist *in, const int in_mapped_nents, const off_t skip, const int nb_splits, const size_t *split_sizes, struct scatterlist **out, int *out_mapped_nents, gfp_t gfp_mask)

    split a scatterlist into several scatterlists

    :param in:
        the input sg list
    :type in: struct scatterlist \*

    :param in_mapped_nents:
        the result of a dma_map_sg(in, ...), or 0 if not mapped.
    :type in_mapped_nents: const int

    :param skip:
        the number of bytes to skip in the input sg list
    :type skip: const off_t

    :param nb_splits:
        the number of desired sg outputs
    :type nb_splits: const int

    :param split_sizes:
        the respective size of each output sg list in bytes
    :type split_sizes: const size_t \*

    :param out:
        an array where to store the allocated output sg lists
    :type out: struct scatterlist \*\*

    :param out_mapped_nents:
        the resulting sg lists mapped number of sg entries. Might
        be NULL if sglist not already mapped (in_mapped_nents = 0)
    :type out_mapped_nents: int \*

    :param gfp_mask:
        the allocation flag
    :type gfp_mask: gfp_t

.. _`sg_split.description`:

Description
-----------

This function splits the input sg list into nb_splits sg lists, which are
allocated and stored into out.
The \ ``in``\  is split into :
- \ ``out``\ [0], which covers bytes [@skip .. \ ``skip``\  + \ ``split_sizes``\ [0] - 1] of \ ``in``\ 
- \ ``out``\ [1], which covers bytes [@skip + split_sizes[0] ..
\ ``skip``\  + \ ``split_sizes``\ [0] + \ ``split_sizes``\ [1] -1]
etc ...
It will be the caller's duty to \ :c:func:`kfree`\  out array members.

Returns 0 upon success, or error code

.. This file was automatic generated / don't edit.

