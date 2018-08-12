.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_rtsym.c

.. _`nfp_rtsym_count`:

nfp_rtsym_count
===============

.. c:function:: int nfp_rtsym_count(struct nfp_rtsym_table *rtbl)

    Get the number of RTSYM descriptors

    :param struct nfp_rtsym_table \*rtbl:
        NFP RTsym table

.. _`nfp_rtsym_count.return`:

Return
------

Number of RTSYM descriptors

.. _`nfp_rtsym_get`:

nfp_rtsym_get
=============

.. c:function:: const struct nfp_rtsym *nfp_rtsym_get(struct nfp_rtsym_table *rtbl, int idx)

    Get the Nth RTSYM descriptor

    :param struct nfp_rtsym_table \*rtbl:
        NFP RTsym table

    :param int idx:
        Index (0-based) of the RTSYM descriptor

.. _`nfp_rtsym_get.return`:

Return
------

const pointer to a struct nfp_rtsym descriptor, or NULL

.. _`nfp_rtsym_lookup`:

nfp_rtsym_lookup
================

.. c:function:: const struct nfp_rtsym *nfp_rtsym_lookup(struct nfp_rtsym_table *rtbl, const char *name)

    Return the RTSYM descriptor for a symbol name

    :param struct nfp_rtsym_table \*rtbl:
        NFP RTsym table

    :param const char \*name:
        Symbol name

.. _`nfp_rtsym_lookup.return`:

Return
------

const pointer to a struct nfp_rtsym descriptor, or NULL

.. _`nfp_rtsym_read_le`:

nfp_rtsym_read_le
=================

.. c:function:: u64 nfp_rtsym_read_le(struct nfp_rtsym_table *rtbl, const char *name, int *error)

    Read a simple unsigned scalar value from symbol

    :param struct nfp_rtsym_table \*rtbl:
        NFP RTsym table

    :param const char \*name:
        Symbol name

    :param int \*error:
        Poniter to error code (optional)

.. _`nfp_rtsym_read_le.description`:

Description
-----------

Lookup a symbol, map, read it and return it's value. Value of the symbol
will be interpreted as a simple little-endian unsigned value. Symbol can
be 4 or 8 bytes in size.

.. _`nfp_rtsym_read_le.return`:

Return
------

value read, on error sets the error and returns ~0ULL.

.. _`nfp_rtsym_write_le`:

nfp_rtsym_write_le
==================

.. c:function:: int nfp_rtsym_write_le(struct nfp_rtsym_table *rtbl, const char *name, u64 value)

    Write an unsigned scalar value to a symbol

    :param struct nfp_rtsym_table \*rtbl:
        NFP RTsym table

    :param const char \*name:
        Symbol name

    :param u64 value:
        Value to write

.. _`nfp_rtsym_write_le.description`:

Description
-----------

Lookup a symbol and write a value to it. Symbol can be 4 or 8 bytes in size.
If 4 bytes then the lower 32-bits of 'value' are used. Value will be
written as simple little-endian unsigned value.

.. _`nfp_rtsym_write_le.return`:

Return
------

0 on success or error code.

.. This file was automatic generated / don't edit.

