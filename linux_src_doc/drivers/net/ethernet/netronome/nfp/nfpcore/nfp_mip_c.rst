.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_mip.c

.. _`nfp_mip_open`:

nfp_mip_open
============

.. c:function:: const struct nfp_mip *nfp_mip_open(struct nfp_cpp *cpp)

    Get device MIP structure

    :param cpp:
        NFP CPP Handle
    :type cpp: struct nfp_cpp \*

.. _`nfp_mip_open.description`:

Description
-----------

Copy MIP structure from NFP device and return it.  The returned
structure is handled internally by the library and should be
freed by calling \ :c:func:`nfp_mip_close`\ .

.. _`nfp_mip_open.return`:

Return
------

pointer to mip, NULL on failure.

.. _`nfp_mip_symtab`:

nfp_mip_symtab
==============

.. c:function:: void nfp_mip_symtab(const struct nfp_mip *mip, u32 *addr, u32 *size)

    Get the address and size of the MIP symbol table

    :param mip:
        MIP handle
    :type mip: const struct nfp_mip \*

    :param addr:
        Location for NFP DDR address of MIP symbol table
    :type addr: u32 \*

    :param size:
        Location for size of MIP symbol table
    :type size: u32 \*

.. _`nfp_mip_strtab`:

nfp_mip_strtab
==============

.. c:function:: void nfp_mip_strtab(const struct nfp_mip *mip, u32 *addr, u32 *size)

    Get the address and size of the MIP symbol name table

    :param mip:
        MIP handle
    :type mip: const struct nfp_mip \*

    :param addr:
        Location for NFP DDR address of MIP symbol name table
    :type addr: u32 \*

    :param size:
        Location for size of MIP symbol name table
    :type size: u32 \*

.. This file was automatic generated / don't edit.

