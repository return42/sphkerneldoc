.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_nffw.h

.. _`nfp_rtsym`:

struct nfp_rtsym
================

.. c:type:: struct nfp_rtsym

    RTSYM descriptor

.. _`nfp_rtsym.definition`:

Definition
----------

.. code-block:: c

    struct nfp_rtsym {
        const char *name;
        u64 addr;
        u64 size;
        enum nfp_rtsym_type type;
        int target;
        int domain;
    }

.. _`nfp_rtsym.members`:

Members
-------

name
    Symbol name

addr
    Address in the domain/target's address space

size
    Size (in bytes) of the symbol

type
    NFP_RTSYM_TYPE\_\* of the symbol

target
    CPP Target identifier, or NFP_RTSYM_TARGET\_\*

domain
    CPP Target Domain (island)

.. This file was automatic generated / don't edit.

