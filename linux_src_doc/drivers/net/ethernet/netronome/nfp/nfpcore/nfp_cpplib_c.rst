.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_cpplib.c

.. _`nfp_cpp_readl`:

nfp_cpp_readl
=============

.. c:function:: int nfp_cpp_readl(struct nfp_cpp *cpp, u32 cpp_id, unsigned long long address, u32 *value)

    Read a u32 word from a CPP location

    :param struct nfp_cpp \*cpp:
        CPP device handle

    :param u32 cpp_id:
        CPP ID for operation

    :param unsigned long long address:
        Address for operation

    :param u32 \*value:
        Pointer to read buffer

.. _`nfp_cpp_readl.return`:

Return
------

length of the io, or -ERRNO

.. _`nfp_cpp_writel`:

nfp_cpp_writel
==============

.. c:function:: int nfp_cpp_writel(struct nfp_cpp *cpp, u32 cpp_id, unsigned long long address, u32 value)

    Write a u32 word to a CPP location

    :param struct nfp_cpp \*cpp:
        CPP device handle

    :param u32 cpp_id:
        CPP ID for operation

    :param unsigned long long address:
        Address for operation

    :param u32 value:
        Value to write

.. _`nfp_cpp_writel.return`:

Return
------

length of the io, or -ERRNO

.. _`nfp_cpp_readq`:

nfp_cpp_readq
=============

.. c:function:: int nfp_cpp_readq(struct nfp_cpp *cpp, u32 cpp_id, unsigned long long address, u64 *value)

    Read a u64 word from a CPP location

    :param struct nfp_cpp \*cpp:
        CPP device handle

    :param u32 cpp_id:
        CPP ID for operation

    :param unsigned long long address:
        Address for operation

    :param u64 \*value:
        Pointer to read buffer

.. _`nfp_cpp_readq.return`:

Return
------

length of the io, or -ERRNO

.. _`nfp_cpp_writeq`:

nfp_cpp_writeq
==============

.. c:function:: int nfp_cpp_writeq(struct nfp_cpp *cpp, u32 cpp_id, unsigned long long address, u64 value)

    Write a u64 word to a CPP location

    :param struct nfp_cpp \*cpp:
        CPP device handle

    :param u32 cpp_id:
        CPP ID for operation

    :param unsigned long long address:
        Address for operation

    :param u64 value:
        Value to write

.. _`nfp_cpp_writeq.return`:

Return
------

length of the io, or -ERRNO

.. This file was automatic generated / don't edit.

