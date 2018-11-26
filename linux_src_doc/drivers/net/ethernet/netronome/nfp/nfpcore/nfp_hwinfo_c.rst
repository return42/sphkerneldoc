.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_hwinfo.c

.. _`nfp_hwinfo_lookup`:

nfp_hwinfo_lookup
=================

.. c:function:: const char *nfp_hwinfo_lookup(struct nfp_hwinfo *hwinfo, const char *lookup)

    Find a value in the HWInfo table by name

    :param hwinfo:
        NFP HWinfo table
    :type hwinfo: struct nfp_hwinfo \*

    :param lookup:
        HWInfo name to search for
    :type lookup: const char \*

.. _`nfp_hwinfo_lookup.return`:

Return
------

Value of the HWInfo name, or NULL

.. This file was automatic generated / don't edit.

