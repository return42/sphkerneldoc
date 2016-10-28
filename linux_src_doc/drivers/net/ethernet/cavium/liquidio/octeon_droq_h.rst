.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/cavium/liquidio/octeon_droq.h

.. _`octeon_init_droq`:

octeon_init_droq
================

.. c:function:: int octeon_init_droq(struct octeon_device *oct_dev, u32 q_no, u32 num_descs, u32 desc_size, void *app_ctx)

    base addr, num desc etc in Octeon registers.

    :param struct octeon_device \*oct_dev:
        *undescribed*

    :param u32 q_no:
        *undescribed*

    :param u32 num_descs:
        *undescribed*

    :param u32 desc_size:
        *undescribed*

    :param void \*app_ctx:
        *undescribed*

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

    :param struct octeon_device \*oct_dev:
        *undescribed*

    :param u32 q_no:
        *undescribed*

.. _`octeon_delete_droq.description`:

Description
-----------

\ ``param``\  oct_dev - pointer to the octeon device structure
\ ``param``\  q_no    - droq no. ranges from 0 - 3.

.. This file was automatic generated / don't edit.

