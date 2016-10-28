.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aic94xx/aic94xx_dump.c

.. _`asd_dump_target_ddb`:

asd_dump_target_ddb
===================

.. c:function:: void asd_dump_target_ddb(struct asd_ha_struct *asd_ha, u16 site_no)

    - dump a CSEQ DDB site

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

    :param u16 site_no:
        site number of interest

.. _`asd_dump_scb_sites`:

asd_dump_scb_sites
==================

.. c:function:: void asd_dump_scb_sites(struct asd_ha_struct *asd_ha)

    - dump currently used CSEQ SCB sites

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter struct

.. _`asd_dump_seq_state`:

asd_dump_seq_state
==================

.. c:function:: void asd_dump_seq_state(struct asd_ha_struct *asd_ha, u8 lseq_mask)

    - dump CSEQ and LSEQ states

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

    :param u8 lseq_mask:
        mask of LSEQs of interest

.. This file was automatic generated / don't edit.

