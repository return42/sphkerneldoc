.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/chelsio/cxgb4vf/t4vf_common.h

.. _`hash_mac_addr`:

hash_mac_addr
=============

.. c:function:: int hash_mac_addr(const u8 *addr)

    return the hash value of a MAC address

    :param addr:
        the 48-bit Ethernet MAC address
    :type addr: const u8 \*

.. _`hash_mac_addr.description`:

Description
-----------

Hashes a MAC address according to the hash function used by hardware
inexact (hash) address matching.

.. This file was automatic generated / don't edit.

