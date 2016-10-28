.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aic94xx/aic94xx_reg.c

.. _`asd_move_swb`:

asd_move_swb
============

.. c:function:: void asd_move_swb(struct asd_ha_struct *asd_ha, u32 reg)

    - move sliding window B

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

    :param u32 reg:
        register desired to be within range of the new window

.. _`asd_read_reg_string`:

asd_read_reg_string
===================

.. c:function:: void asd_read_reg_string(struct asd_ha_struct *asd_ha, void *dst, u32 offs, int count)

    - read a string of bytes from io space memory

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

    :param void \*dst:
        pointer to a destination buffer where data will be written to

    :param u32 offs:
        start offset (register) to read from

    :param int count:
        number of bytes to read

.. _`asd_write_reg_string`:

asd_write_reg_string
====================

.. c:function:: void asd_write_reg_string(struct asd_ha_struct *asd_ha, void *src, u32 offs, int count)

    - write a string of bytes to io space memory

    :param struct asd_ha_struct \*asd_ha:
        pointer to host adapter structure

    :param void \*src:
        pointer to source buffer where data will be read from

    :param u32 offs:
        start offset (register) to write to

    :param int count:
        number of bytes to write

.. This file was automatic generated / don't edit.

