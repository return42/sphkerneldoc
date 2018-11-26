.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_cpplib.c

.. _`nfp_cpp_readl`:

nfp_cpp_readl
=============

.. c:function:: int nfp_cpp_readl(struct nfp_cpp *cpp, u32 cpp_id, unsigned long long address, u32 *value)

    Read a u32 word from a CPP location

    :param cpp:
        CPP device handle
    :type cpp: struct nfp_cpp \*

    :param cpp_id:
        CPP ID for operation
    :type cpp_id: u32

    :param address:
        Address for operation
    :type address: unsigned long long

    :param value:
        Pointer to read buffer
    :type value: u32 \*

.. _`nfp_cpp_readl.return`:

Return
------

0 on success, or -ERRNO

.. _`nfp_cpp_writel`:

nfp_cpp_writel
==============

.. c:function:: int nfp_cpp_writel(struct nfp_cpp *cpp, u32 cpp_id, unsigned long long address, u32 value)

    Write a u32 word to a CPP location

    :param cpp:
        CPP device handle
    :type cpp: struct nfp_cpp \*

    :param cpp_id:
        CPP ID for operation
    :type cpp_id: u32

    :param address:
        Address for operation
    :type address: unsigned long long

    :param value:
        Value to write
    :type value: u32

.. _`nfp_cpp_writel.return`:

Return
------

0 on success, or -ERRNO

.. _`nfp_cpp_readq`:

nfp_cpp_readq
=============

.. c:function:: int nfp_cpp_readq(struct nfp_cpp *cpp, u32 cpp_id, unsigned long long address, u64 *value)

    Read a u64 word from a CPP location

    :param cpp:
        CPP device handle
    :type cpp: struct nfp_cpp \*

    :param cpp_id:
        CPP ID for operation
    :type cpp_id: u32

    :param address:
        Address for operation
    :type address: unsigned long long

    :param value:
        Pointer to read buffer
    :type value: u64 \*

.. _`nfp_cpp_readq.return`:

Return
------

0 on success, or -ERRNO

.. _`nfp_cpp_writeq`:

nfp_cpp_writeq
==============

.. c:function:: int nfp_cpp_writeq(struct nfp_cpp *cpp, u32 cpp_id, unsigned long long address, u64 value)

    Write a u64 word to a CPP location

    :param cpp:
        CPP device handle
    :type cpp: struct nfp_cpp \*

    :param cpp_id:
        CPP ID for operation
    :type cpp_id: u32

    :param address:
        Address for operation
    :type address: unsigned long long

    :param value:
        Value to write
    :type value: u64

.. _`nfp_cpp_writeq.return`:

Return
------

0 on success, or -ERRNO

.. _`nfp_cpp_map_area`:

nfp_cpp_map_area
================

.. c:function:: u8 __iomem *nfp_cpp_map_area(struct nfp_cpp *cpp, const char *name, u32 cpp_id, u64 addr, unsigned long size, struct nfp_cpp_area **area)

    Helper function to map an area

    :param cpp:
        NFP CPP handler
    :type cpp: struct nfp_cpp \*

    :param name:
        Name for the area
    :type name: const char \*

    :param cpp_id:
        CPP ID for operation
    :type cpp_id: u32

    :param addr:
        CPP address
    :type addr: u64

    :param size:
        Size of the area
    :type size: unsigned long

    :param area:
        Area handle (output)
    :type area: struct nfp_cpp_area \*\*

.. _`nfp_cpp_map_area.description`:

Description
-----------

Map an area of IOMEM access.  To undo the effect of this function call
\ ``nfp_cpp_area_release_free``\ (\*area).

.. _`nfp_cpp_map_area.return`:

Return
------

Pointer to memory mapped area or ERR_PTR

.. This file was automatic generated / don't edit.

