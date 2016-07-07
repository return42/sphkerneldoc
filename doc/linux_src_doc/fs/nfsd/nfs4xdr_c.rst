.. -*- coding: utf-8; mode: rst -*-
.. src-file: fs/nfsd/nfs4xdr.c

.. _`svcxdr_tmpalloc`:

svcxdr_tmpalloc
===============

.. c:function:: void *svcxdr_tmpalloc(struct nfsd4_compoundargs *argp, u32 len)

    allocate memory to be freed after compound processing

    :param struct nfsd4_compoundargs \*argp:
        NFSv4 compound argument structure

    :param u32 len:
        *undescribed*

.. _`svcxdr_tmpalloc.description`:

Description
-----------

Marks \ ``p``\  to be freed when processing the compound operation
described in \ ``argp``\  finishes.

.. _`savemem`:

savemem
=======

.. c:function:: char *savemem(struct nfsd4_compoundargs *argp, __be32 *p, int nbytes)

    duplicate a chunk of memory for later processing

    :param struct nfsd4_compoundargs \*argp:
        NFSv4 compound argument structure to be freed with

    :param __be32 \*p:
        pointer to be duplicated

    :param int nbytes:
        length to be duplicated

.. _`savemem.description`:

Description
-----------

Returns a pointer to a copy of \ ``nbytes``\  bytes of memory at \ ``p``\ 
that are preserved until processing of the NFSv4 compound
operation described by \ ``argp``\  finishes.

.. This file was automatic generated / don't edit.

