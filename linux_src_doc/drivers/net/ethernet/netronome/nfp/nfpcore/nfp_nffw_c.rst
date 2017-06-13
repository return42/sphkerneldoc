.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_nffw.c

.. _`nffw_info_version_current`:

NFFW_INFO_VERSION_CURRENT
=========================

.. c:function::  NFFW_INFO_VERSION_CURRENT()

    0: This was never actually used (before versioning), but it refers to the previous struct which had FWINFO_CNT = MEINFO_CNT = 120 that later changed to 200. 1: First versioned struct, with FWINFO_CNT = 120 MEINFO_CNT = 120 2:  FWINFO_CNT = 200 MEINFO_CNT = 200

.. _`nfp_nffw_info_open`:

nfp_nffw_info_open
==================

.. c:function:: struct nfp_nffw_info *nfp_nffw_info_open(struct nfp_cpp *cpp)

    Acquire the lock on the NFFW table

    :param struct nfp_cpp \*cpp:
        NFP CPP handle

.. _`nfp_nffw_info_open.return`:

Return
------

0, or -ERRNO

.. _`nfp_nffw_info_close`:

nfp_nffw_info_close
===================

.. c:function:: void nfp_nffw_info_close(struct nfp_nffw_info *state)

    Release the lock on the NFFW table

    :param struct nfp_nffw_info \*state:
        NFP FW info state

.. _`nfp_nffw_info_close.return`:

Return
------

0, or -ERRNO

.. _`nfp_nffw_info_fwid_first`:

nfp_nffw_info_fwid_first
========================

.. c:function:: struct nffw_fwinfo *nfp_nffw_info_fwid_first(struct nfp_nffw_info *state)

    Return the first firmware ID in the NFFW

    :param struct nfp_nffw_info \*state:
        NFP FW info state

.. _`nfp_nffw_info_fwid_first.return`:

Return
------

First NFFW firmware info, NULL on failure

.. _`nfp_nffw_info_mip_first`:

nfp_nffw_info_mip_first
=======================

.. c:function:: int nfp_nffw_info_mip_first(struct nfp_nffw_info *state, u32 *cpp_id, u64 *off)

    Retrieve the location of the first FW's MIP

    :param struct nfp_nffw_info \*state:
        NFP FW info state

    :param u32 \*cpp_id:
        Pointer to the CPP ID of the MIP

    :param u64 \*off:
        Pointer to the CPP Address of the MIP

.. _`nfp_nffw_info_mip_first.return`:

Return
------

0, or -ERRNO

.. This file was automatic generated / don't edit.

