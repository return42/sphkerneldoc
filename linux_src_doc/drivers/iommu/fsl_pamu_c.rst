.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/iommu/fsl_pamu.c

.. _`pamu_get_max_subwin_cnt`:

pamu_get_max_subwin_cnt
=======================

.. c:function:: u32 pamu_get_max_subwin_cnt( void)

    Return the maximum supported subwindow count per liodn.

    :param  void:
        no arguments

.. _`pamu_get_ppaace`:

pamu_get_ppaace
===============

.. c:function:: struct paace *pamu_get_ppaace(int liodn)

    Return the primary PACCE

    :param int liodn:
        liodn PAACT index for desired PAACE

.. _`pamu_get_ppaace.description`:

Description
-----------

Returns the ppace pointer upon success else return
null.

.. _`pamu_enable_liodn`:

pamu_enable_liodn
=================

.. c:function:: int pamu_enable_liodn(int liodn)

    Set valid bit of PACCE

    :param int liodn:
        liodn PAACT index for desired PAACE

.. _`pamu_enable_liodn.description`:

Description
-----------

Returns 0 upon success else error code < 0 returned

.. _`pamu_disable_liodn`:

pamu_disable_liodn
==================

.. c:function:: int pamu_disable_liodn(int liodn)

    Clears valid bit of PACCE

    :param int liodn:
        liodn PAACT index for desired PAACE

.. _`pamu_disable_liodn.description`:

Description
-----------

Returns 0 upon success else error code < 0 returned

.. _`pamu_get_fspi_and_allocate`:

pamu_get_fspi_and_allocate
==========================

.. c:function:: unsigned long pamu_get_fspi_and_allocate(u32 subwin_cnt)

    Allocates fspi index and reserves subwindows required for primary PAACE in the secondary PAACE table.

    :param u32 subwin_cnt:
        Number of subwindows to be reserved.

.. _`pamu_get_fspi_and_allocate.description`:

Description
-----------

A PPAACE entry may have a number of associated subwindows. A subwindow
corresponds to a SPAACE entry in the SPAACT table. Each PAACE entry stores
the index (fspi) of the first SPAACE entry in the SPAACT table. This
function returns the index of the first SPAACE entry. The remaining
SPAACE entries are reserved contiguously from that index.

Returns a valid fspi index in the range of 0 - SPAACE_NUMBER_ENTRIES on success.
If no SPAACE entry is available or the allocator can not reserve the required
number of contiguous entries function returns ULONG_MAX indicating a failure.

.. _`pamu_config_ppaace`:

pamu_config_ppaace
==================

.. c:function:: int pamu_config_ppaace(int liodn, phys_addr_t win_addr, phys_addr_t win_size, u32 omi, unsigned long rpn, u32 snoopid, u32 stashid, u32 subwin_cnt, int prot)

    Sets up PPAACE entry for specified liodn

    :param int liodn:
        Logical IO device number

    :param phys_addr_t win_addr:
        starting address of DSA window

    :param phys_addr_t win_size:
        *undescribed*

    :param u32 omi:
        Operation mapping index -- if ~omi == 0 then omi not defined

    :param unsigned long rpn:
        real (true physical) page number

    :param u32 snoopid:
        snoop id for hardware coherency -- if ~snoopid == 0 then
        snoopid not defined

    :param u32 stashid:
        cache stash id for associated cpu -- if ~stashid == 0 then
        stashid not defined

    :param u32 subwin_cnt:
        number of sub-windows

    :param int prot:
        window permissions

.. _`pamu_config_ppaace.description`:

Description
-----------

Returns 0 upon success else error code < 0 returned

.. _`pamu_config_spaace`:

pamu_config_spaace
==================

.. c:function:: int pamu_config_spaace(int liodn, u32 subwin_cnt, u32 subwin, phys_addr_t subwin_size, u32 omi, unsigned long rpn, u32 snoopid, u32 stashid, int enable, int prot)

    Sets up SPAACE entry for specified subwindow

    :param int liodn:
        Logical IO device number

    :param u32 subwin_cnt:
        number of sub-windows associated with dma-window

    :param u32 subwin:
        subwindow index

    :param phys_addr_t subwin_size:
        size of subwindow

    :param u32 omi:
        Operation mapping index

    :param unsigned long rpn:
        real (true physical) page number

    :param u32 snoopid:
        snoop id for hardware coherency -- if ~snoopid == 0 then
        snoopid not defined

    :param u32 stashid:
        cache stash id for associated cpu

    :param int enable:
        enable/disable subwindow after reconfiguration

    :param int prot:
        sub window permissions

.. _`pamu_config_spaace.description`:

Description
-----------

Returns 0 upon success else error code < 0 returned

.. _`get_ome_index`:

get_ome_index
=============

.. c:function:: void get_ome_index(u32 *omi_index, struct device *dev)

    Returns the index in the operation mapping table for device. \ ````\ \*omi_index: pointer for storing the index value

    :param u32 \*omi_index:
        *undescribed*

    :param struct device \*dev:
        *undescribed*

.. _`get_stash_id`:

get_stash_id
============

.. c:function:: u32 get_stash_id(u32 stash_dest_hint, u32 vcpu)

    Returns stash destination id corresponding to a cache type and vcpu.

    :param u32 stash_dest_hint:
        L1, L2 or L3

    :param u32 vcpu:
        vpcu target for a particular cache type.

.. _`get_stash_id.description`:

Description
-----------

Returs stash on success or ~(u32)0 on failure.

.. _`setup_qbman_paace`:

setup_qbman_paace
=================

.. c:function:: void setup_qbman_paace(struct paace *ppaace, int paace_type)

    Memory accesses to QMAN and BMAN private memory need not be coherent, so clear the PAACE entry coherency attribute for them.

    :param struct paace \*ppaace:
        *undescribed*

    :param int paace_type:
        *undescribed*

.. _`setup_omt`:

setup_omt
=========

.. c:function:: void setup_omt(struct ome *omt)

    table where each table index corresponds to a particular device. PAMU uses this table to translate device transaction to appropriate corenet transaction.

    :param struct ome \*omt:
        *undescribed*

.. This file was automatic generated / don't edit.

