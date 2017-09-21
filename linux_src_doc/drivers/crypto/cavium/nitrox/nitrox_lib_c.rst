.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/nitrox/nitrox_lib.c

.. _`crypto_free_context`:

crypto_free_context
===================

.. c:function:: void crypto_free_context(void *ctx)

    Free crypto context to pool

    :param void \*ctx:
        context to free

.. _`nitrox_common_sw_init`:

nitrox_common_sw_init
=====================

.. c:function:: int nitrox_common_sw_init(struct nitrox_device *ndev)

    allocate software resources.

    :param struct nitrox_device \*ndev:
        NITROX device

.. _`nitrox_common_sw_init.description`:

Description
-----------

Allocates crypto context pools and command queues etc.

.. _`nitrox_common_sw_init.return`:

Return
------

0 on success, or a negative error code on error.

.. _`nitrox_common_sw_cleanup`:

nitrox_common_sw_cleanup
========================

.. c:function:: void nitrox_common_sw_cleanup(struct nitrox_device *ndev)

    free software resources.

    :param struct nitrox_device \*ndev:
        NITROX device

.. This file was automatic generated / don't edit.

