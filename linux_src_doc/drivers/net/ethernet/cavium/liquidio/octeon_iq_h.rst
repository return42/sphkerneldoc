.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/cavium/liquidio/octeon_iq.h

.. _`octeon_init_instr_queue`:

octeon_init_instr_queue
=======================

.. c:function:: int octeon_init_instr_queue(struct octeon_device *octeon_dev, union oct_txpciq txpciq, u32 num_descs)

    \ ``param``\  octeon_dev      - pointer to the octeon device structure. \ ``param``\  txpciq          - queue to be initialized (0 <= q_no <= 3).

    :param struct octeon_device \*octeon_dev:
        *undescribed*

    :param union oct_txpciq txpciq:
        *undescribed*

    :param u32 num_descs:
        *undescribed*

.. _`octeon_init_instr_queue.description`:

Description
-----------

Called at driver init time for each input queue. iq_conf has the
configuration parameters for the queue.

.. _`octeon_delete_instr_queue`:

octeon_delete_instr_queue
=========================

.. c:function:: int octeon_delete_instr_queue(struct octeon_device *octeon_dev, u32 iq_no)

    \ ``param``\  octeon_dev      - pointer to the octeon device structure. \ ``param``\  iq_no           - queue to be deleted (0 <= q_no <= 3).

    :param struct octeon_device \*octeon_dev:
        *undescribed*

    :param u32 iq_no:
        *undescribed*

.. _`octeon_delete_instr_queue.description`:

Description
-----------

Called at driver unload time for each input queue. Deletes all
allocated resources for the input queue.

.. This file was automatic generated / don't edit.

