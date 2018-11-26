.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aic94xx/aic94xx_reg.h

.. _`asd_ddbsite_update_word`:

asd_ddbsite_update_word
=======================

.. c:function:: int asd_ddbsite_update_word(struct asd_ha_struct *asd_ha, u16 ddb_site_no, u16 offs, u16 oldval, u16 newval)

    - atomically update a word in a ddb site

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

    :param ddb_site_no:
        the DDB site number
    :type ddb_site_no: u16

    :param offs:
        the offset into the DDB
    :type offs: u16

    :param oldval:
        old value found in that offset
    :type oldval: u16

    :param newval:
        the new value to replace it
    :type newval: u16

.. _`asd_ddbsite_update_word.description`:

Description
-----------

This function is used when the sequencers are running and we need to
update a DDB site atomically without expensive pausing and upausing
of the sequencers and accessing the DDB site through the CIO bus.

Return 0 on success; -EFAULT on parity error; -EAGAIN if the old value
is different than the current value at that offset.

.. This file was automatic generated / don't edit.

