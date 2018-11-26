.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/aic94xx/aic94xx_reg.c

.. _`asd_move_swb`:

asd_move_swb
============

.. c:function:: void asd_move_swb(struct asd_ha_struct *asd_ha, u32 reg)

    - move sliding window B

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

    :param reg:
        register desired to be within range of the new window
    :type reg: u32

.. _`asd_read_reg_string`:

asd_read_reg_string
===================

.. c:function:: void asd_read_reg_string(struct asd_ha_struct *asd_ha, void *dst, u32 offs, int count)

    - read a string of bytes from io space memory

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

    :param dst:
        pointer to a destination buffer where data will be written to
    :type dst: void \*

    :param offs:
        start offset (register) to read from
    :type offs: u32

    :param count:
        number of bytes to read
    :type count: int

.. _`asd_write_reg_string`:

asd_write_reg_string
====================

.. c:function:: void asd_write_reg_string(struct asd_ha_struct *asd_ha, void *src, u32 offs, int count)

    - write a string of bytes to io space memory

    :param asd_ha:
        pointer to host adapter structure
    :type asd_ha: struct asd_ha_struct \*

    :param src:
        pointer to source buffer where data will be read from
    :type src: void \*

    :param offs:
        start offset (register) to write to
    :type offs: u32

    :param count:
        number of bytes to write
    :type count: int

.. This file was automatic generated / don't edit.

