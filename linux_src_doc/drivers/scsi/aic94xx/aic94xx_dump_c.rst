.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aic94xx/aic94xx_dump.c

.. _`asd_dump_target_ddb`:

asd_dump_target_ddb
===================

.. c:function:: void asd_dump_target_ddb(struct asd_ha_struct *asd_ha, u16 site_no)

    - dump a CSEQ DDB site

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

    :param site_no:
        site number of interest
    :type site_no: u16

.. _`asd_dump_scb_sites`:

asd_dump_scb_sites
==================

.. c:function:: void asd_dump_scb_sites(struct asd_ha_struct *asd_ha)

    - dump currently used CSEQ SCB sites

    :param asd_ha:
        pointer to host adapter struct
    :type asd_ha: struct asd_ha_struct \*

.. _`asd_dump_seq_state`:

asd_dump_seq_state
==================

.. c:function:: void asd_dump_seq_state(struct asd_ha_struct *asd_ha, u8 lseq_mask)

    - dump CSEQ and LSEQ states

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

    :param lseq_mask:
        mask of LSEQs of interest
    :type lseq_mask: u8

.. This file was automatic generated / don't edit.

