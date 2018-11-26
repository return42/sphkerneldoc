.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aic94xx/aic94xx_seq.c

.. _`asd_pause_cseq`:

asd_pause_cseq
==============

.. c:function:: int asd_pause_cseq(struct asd_ha_struct *asd_ha)

    pause the central sequencer

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

.. _`asd_pause_cseq.description`:

Description
-----------

Return 0 on success, negative on failure.

.. _`asd_unpause_cseq`:

asd_unpause_cseq
================

.. c:function:: int asd_unpause_cseq(struct asd_ha_struct *asd_ha)

    unpause the central sequencer.

    :param asd_ha:
        pointer to host adapter structure.
    :type asd_ha: struct asd_ha_struct \*

.. _`asd_unpause_cseq.description`:

Description
-----------

Return 0 on success, negative on error.

.. _`asd_seq_pause_lseq`:

asd_seq_pause_lseq
==================

.. c:function:: int asd_seq_pause_lseq(struct asd_ha_struct *asd_ha, int lseq)

    pause a link sequencer

    :param asd_ha:
        pointer to a host adapter structure
    :type asd_ha: struct asd_ha_struct \*

    :param lseq:
        link sequencer of interest
    :type lseq: int

.. _`asd_seq_pause_lseq.description`:

Description
-----------

Return 0 on success, negative on error.

.. _`asd_pause_lseq`:

asd_pause_lseq
==============

.. c:function:: int asd_pause_lseq(struct asd_ha_struct *asd_ha, u8 lseq_mask)

    pause the link sequencer(s)

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

    :param lseq_mask:
        mask of link sequencers of interest
    :type lseq_mask: u8

.. _`asd_pause_lseq.description`:

Description
-----------

Return 0 on success, negative on failure.

.. _`asd_seq_unpause_lseq`:

asd_seq_unpause_lseq
====================

.. c:function:: int asd_seq_unpause_lseq(struct asd_ha_struct *asd_ha, int lseq)

    unpause a link sequencer

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

    :param lseq:
        link sequencer of interest
    :type lseq: int

.. _`asd_seq_unpause_lseq.description`:

Description
-----------

Return 0 on success, negative on error.

.. _`asd_verify_lseq`:

asd_verify_lseq
===============

.. c:function:: int asd_verify_lseq(struct asd_ha_struct *asd_ha, const u8 *_prog, u32 size, int lseq)

    verify the microcode of a link sequencer

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

    :param _prog:
        pointer to the microcode
    :type _prog: const u8 \*

    :param size:
        size of the microcode in bytes
    :type size: u32

    :param lseq:
        link sequencer of interest
    :type lseq: int

.. _`asd_verify_lseq.description`:

Description
-----------

The link sequencer code is accessed in 4 KB pages, which are selected
by setting LmRAMPAGE (bits 8 and 9) of the LmBISTCTL1 register.
The 10 KB LSEQm instruction code is mapped, page at a time, at
LmSEQRAM address.

.. _`asd_verify_seq`:

asd_verify_seq
==============

.. c:function:: int asd_verify_seq(struct asd_ha_struct *asd_ha, const u8 *prog, u32 size, u8 lseq_mask)

    - verify CSEQ/LSEQ microcode

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

    :param prog:
        pointer to microcode
    :type prog: const u8 \*

    :param size:
        size of the microcode
    :type size: u32

    :param lseq_mask:
        if 0, verify CSEQ microcode, else mask of LSEQs of interest
    :type lseq_mask: u8

.. _`asd_verify_seq.description`:

Description
-----------

Return 0 if microcode is correct, negative on mismatch.

.. _`asd_seq_download_seqs`:

asd_seq_download_seqs
=====================

.. c:function:: int asd_seq_download_seqs(struct asd_ha_struct *asd_ha)

    download the sequencer microcode

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

.. _`asd_seq_download_seqs.description`:

Description
-----------

Download the central and link sequencer microcode.

.. _`asd_init_cseq_mip`:

asd_init_cseq_mip
=================

.. c:function:: void asd_init_cseq_mip(struct asd_ha_struct *asd_ha)

    initialize CSEQ mode independent pages 4-7

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

.. _`asd_init_cseq_mdp`:

asd_init_cseq_mdp
=================

.. c:function:: void asd_init_cseq_mdp(struct asd_ha_struct *asd_ha)

    initialize CSEQ Mode dependent pages

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

.. _`asd_init_cseq_scratch`:

asd_init_cseq_scratch
=====================

.. c:function:: void asd_init_cseq_scratch(struct asd_ha_struct *asd_ha)

    - setup and init CSEQ

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

.. _`asd_init_cseq_scratch.description`:

Description
-----------

Setup and initialize Central sequencers. Initialize the mode
independent and dependent scratch page to the default settings.

.. _`asd_init_lseq_mip`:

asd_init_lseq_mip
=================

.. c:function:: void asd_init_lseq_mip(struct asd_ha_struct *asd_ha, u8 lseq)

    - initialize LSEQ Mode independent pages 0-3

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

    :param lseq:
        *undescribed*
    :type lseq: u8

.. _`asd_init_lseq_mdp`:

asd_init_lseq_mdp
=================

.. c:function:: void asd_init_lseq_mdp(struct asd_ha_struct *asd_ha, int lseq)

    - initialize LSEQ mode dependent pages.

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

    :param lseq:
        *undescribed*
    :type lseq: int

.. _`asd_init_lseq_scratch`:

asd_init_lseq_scratch
=====================

.. c:function:: void asd_init_lseq_scratch(struct asd_ha_struct *asd_ha)

    - setup and init link sequencers

    :param asd_ha:
        pointer to host adapter struct
    :type asd_ha: struct asd_ha_struct \*

.. _`asd_init_scb_sites`:

asd_init_scb_sites
==================

.. c:function:: void asd_init_scb_sites(struct asd_ha_struct *asd_ha)

    - initialize sequencer SCB sites (memory).

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

.. _`asd_init_scb_sites.description`:

Description
-----------

This should be done before initializing common CSEQ and LSEQ
scratch since those areas depend on some computed values here,
last_scb_site_no, etc.

.. _`asd_init_cseq_cio`:

asd_init_cseq_cio
=================

.. c:function:: void asd_init_cseq_cio(struct asd_ha_struct *asd_ha)

    initialize CSEQ CIO registers

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

.. _`asd_init_lseq_cio`:

asd_init_lseq_cio
=================

.. c:function:: void asd_init_lseq_cio(struct asd_ha_struct *asd_ha, int lseq)

    - initialize LmSEQ CIO registers

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

    :param lseq:
        *undescribed*
    :type lseq: int

.. _`asd_post_init_cseq`:

asd_post_init_cseq
==================

.. c:function:: void asd_post_init_cseq(struct asd_ha_struct *asd_ha)

    - clear CSEQ Mode n Int. status and Response mailbox

    :param asd_ha:
        pointer to host adapter struct
    :type asd_ha: struct asd_ha_struct \*

.. _`asd_init_ddb_0`:

asd_init_ddb_0
==============

.. c:function:: void asd_init_ddb_0(struct asd_ha_struct *asd_ha)

    - initialize DDB 0

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

.. _`asd_init_ddb_0.description`:

Description
-----------

Initialize DDB site 0 which is used internally by the sequencer.

.. _`asd_seq_setup_seqs`:

asd_seq_setup_seqs
==================

.. c:function:: void asd_seq_setup_seqs(struct asd_ha_struct *asd_ha)

    - setup and initialize central and link sequencers

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

.. _`asd_seq_start_cseq`:

asd_seq_start_cseq
==================

.. c:function:: int asd_seq_start_cseq(struct asd_ha_struct *asd_ha)

    - start the central sequencer, CSEQ

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

.. _`asd_seq_start_lseq`:

asd_seq_start_lseq
==================

.. c:function:: int asd_seq_start_lseq(struct asd_ha_struct *asd_ha, int lseq)

    - start a link sequencer

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

    :param lseq:
        the link sequencer of interest
    :type lseq: int

.. _`asd_update_port_links`:

asd_update_port_links
=====================

.. c:function:: void asd_update_port_links(struct asd_ha_struct *asd_ha, struct asd_phy *phy)

    - update port_map_by_links and phy_is_up

    :param asd_ha:
        *undescribed*
    :type asd_ha: struct asd_ha_struct \*

    :param phy:
        *undescribed*
    :type phy: struct asd_phy \*

.. _`asd_update_port_links.description`:

Description
-----------

1) When a link reset has completed and we got BYTES DMAED with a
valid frame we call this function for that phy, to indicate that
the phy is up, i.e. we update the phy_is_up in DDB 0.  The
sequencer checks phy_is_up when pending SCBs are to be sent, and
when an open address frame has been received.

2) When we know of ports, we call this function to update the map
of phys participaing in that port, i.e. we update the
port_map_by_links in DDB 0.  When a HARD_RESET primitive has been
received, the sequencer disables all phys in that port.
port_map_by_links is also used as the conn_mask byte in the
initiator/target port DDB.

.. This file was automatic generated / don't edit.

