.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfp_net_main.c

.. _`nfp_net_map_area`:

nfp_net_map_area
================

.. c:function:: u8 __iomem *nfp_net_map_area(struct nfp_cpp *cpp, const char *name, int isl, int target, unsigned long long addr, unsigned long size, struct nfp_cpp_area **area)

    Help function to map an area

    :param struct nfp_cpp \*cpp:
        NFP CPP handler

    :param const char \*name:
        Name for the area

    :param int isl:
        *undescribed*

    :param int target:
        CPP target

    :param unsigned long long addr:
        CPP address

    :param unsigned long size:
        Size of the area

    :param struct nfp_cpp_area \*\*area:
        Area handle (returned).

.. _`nfp_net_map_area.description`:

Description
-----------

This function is primarily to simplify the code in the main probe
function. To undo the effect of this functions call
\ ``nfp_cpp_area_release_free``\ (\*area);

.. _`nfp_net_map_area.return`:

Return
------

Pointer to memory mapped area or ERR_PTR

.. _`nfp_net_get_mac_addr`:

nfp_net_get_mac_addr
====================

.. c:function:: void nfp_net_get_mac_addr(struct nfp_net *nn, struct nfp_cpp *cpp, unsigned int id)

    Get the MAC address.

    :param struct nfp_net \*nn:
        NFP Network structure

    :param struct nfp_cpp \*cpp:
        NFP CPP handle

    :param unsigned int id:
        NFP port id

.. _`nfp_net_get_mac_addr.description`:

Description
-----------

First try to get the MAC address from NSP ETH table. If that
fails try HWInfo.  As a last resort generate a random address.

.. This file was automatic generated / don't edit.

