.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/ata/pata_octeon_cf.c

.. _`ns_to_tim_reg`:

ns_to_tim_reg
=============

.. c:function:: unsigned int ns_to_tim_reg(unsigned int tim_mult, unsigned int nsecs)

    boot bus timing register, based on timing multiple

    :param tim_mult:
        *undescribed*
    :type tim_mult: unsigned int

    :param nsecs:
        *undescribed*
    :type nsecs: unsigned int

.. _`octeon_cf_set_piomode`:

octeon_cf_set_piomode
=====================

.. c:function:: void octeon_cf_set_piomode(struct ata_port *ap, struct ata_device *dev)

    function programs the Octeon bootbus regions to support the timing requirements of the PIO mode.

    :param ap:
        ATA port information
    :type ap: struct ata_port \*

    :param dev:
        ATA device
    :type dev: struct ata_device \*

.. _`octeon_cf_data_xfer8`:

octeon_cf_data_xfer8
====================

.. c:function:: unsigned int octeon_cf_data_xfer8(struct ata_queued_cmd *qc, unsigned char *buffer, unsigned int buflen, int rw)

    :param qc:
        Queued command
    :type qc: struct ata_queued_cmd \*

    :param buffer:
        Data buffer
    :type buffer: unsigned char \*

    :param buflen:
        Length of the buffer.
    :type buflen: unsigned int

    :param rw:
        True to write.
    :type rw: int

.. _`octeon_cf_data_xfer16`:

octeon_cf_data_xfer16
=====================

.. c:function:: unsigned int octeon_cf_data_xfer16(struct ata_queued_cmd *qc, unsigned char *buffer, unsigned int buflen, int rw)

    :param qc:
        Queued command
    :type qc: struct ata_queued_cmd \*

    :param buffer:
        Data buffer
    :type buffer: unsigned char \*

    :param buflen:
        Length of the buffer.
    :type buflen: unsigned int

    :param rw:
        True to write.
    :type rw: int

.. _`octeon_cf_tf_read16`:

octeon_cf_tf_read16
===================

.. c:function:: void octeon_cf_tf_read16(struct ata_port *ap, struct ata_taskfile *tf)

    True IDE only.

    :param ap:
        *undescribed*
    :type ap: struct ata_port \*

    :param tf:
        *undescribed*
    :type tf: struct ata_taskfile \*

.. _`octeon_cf_tf_load16`:

octeon_cf_tf_load16
===================

.. c:function:: void octeon_cf_tf_load16(struct ata_port *ap, const struct ata_taskfile *tf)

    True IDE only.  The device_addr is not loaded, we do this as part of octeon_cf_exec_command16.

    :param ap:
        *undescribed*
    :type ap: struct ata_port \*

    :param tf:
        *undescribed*
    :type tf: const struct ata_taskfile \*

.. _`octeon_cf_dma_start`:

octeon_cf_dma_start
===================

.. c:function:: void octeon_cf_dma_start(struct ata_queued_cmd *qc)

    :param qc:
        Information about the DMA
    :type qc: struct ata_queued_cmd \*

.. This file was automatic generated / don't edit.

