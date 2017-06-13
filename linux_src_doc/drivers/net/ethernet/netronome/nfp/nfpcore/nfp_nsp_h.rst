.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_nsp.h

.. _`nfp_eth_table`:

struct nfp_eth_table
====================

.. c:type:: struct nfp_eth_table

    ETH table information

.. _`nfp_eth_table.definition`:

Definition
----------

.. code-block:: c

    struct nfp_eth_table {
        unsigned int count;
        struct nfp_eth_table_port ports[0];
    }

.. _`nfp_eth_table.members`:

Members
-------

count
    number of table entries

ports
    table of ports

.. _`nfp_nsp_identify`:

struct nfp_nsp_identify
=======================

.. c:type:: struct nfp_nsp_identify

    NSP static information

.. _`nfp_nsp_identify.definition`:

Definition
----------

.. code-block:: c

    struct nfp_nsp_identify {
        char version[40];
        u8 flags;
        u8 br_primary;
        u8 br_secondary;
        u8 br_nsp;
        u16 primary;
        u16 secondary;
        u16 nsp;
    }

.. _`nfp_nsp_identify.members`:

Members
-------

version
    opaque version string

flags
    version flags

br_primary
    branch id of primary bootloader

br_secondary
    branch id of secondary bootloader

br_nsp
    branch id of NSP

primary
    version of primarary bootloader

secondary
    version id of secondary bootloader

nsp
    version id of NSP

.. This file was automatic generated / don't edit.

