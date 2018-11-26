.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/cavium/liquidio/octeon_droq.h

.. _`octeon_init_droq`:

octeon_init_droq
================

.. c:function:: int octeon_init_droq(struct octeon_device *oct_dev, u32 q_no, u32 num_descs, u32 desc_size, void *app_ctx)

    base addr, num desc etc in Octeon registers.

    :param oct_dev:
        *undescribed*
    :type oct_dev: struct octeon_device \*

    :param q_no:
        *undescribed*
    :type q_no: u32

    :param num_descs:
        *undescribed*
    :type num_descs: u32

    :param desc_size:
        *undescribed*
    :type desc_size: u32

    :param app_ctx:
        *undescribed*
    :type app_ctx: void \*

.. _`octeon_init_droq.description`:

Description
-----------

\ ``param``\   oct_dev    - pointer to the octeon device structure
\ ``param``\   q_no       - droq no. ranges from 0 - 3.
\ ``param``\  app_ctx     - pointer to application context

.. _`octeon_delete_droq`:

octeon_delete_droq
==================

.. c:function:: int octeon_delete_droq(struct octeon_device *oct_dev, u32 q_no)

    :param oct_dev:
        *undescribed*
    :type oct_dev: struct octeon_device \*

    :param q_no:
        *undescribed*
    :type q_no: u32

.. _`octeon_delete_droq.description`:

Description
-----------

\ ``param``\  oct_dev - pointer to the octeon device structure
\ ``param``\  q_no    - droq no. ranges from 0 - 3.

.. This file was automatic generated / don't edit.

