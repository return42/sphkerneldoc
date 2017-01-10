.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/zcrypt_queue.c

.. _`zcrypt_queue_register`:

zcrypt_queue_register
=====================

.. c:function:: int zcrypt_queue_register(struct zcrypt_queue *zq)

    Register a crypto queue device.

    :param struct zcrypt_queue \*zq:
        Pointer to a crypto queue device

.. _`zcrypt_queue_register.description`:

Description
-----------

Register a crypto queue device. Returns 0 if successful.

.. _`zcrypt_queue_unregister`:

zcrypt_queue_unregister
=======================

.. c:function:: void zcrypt_queue_unregister(struct zcrypt_queue *zq)

    Unregister a crypto queue device.

    :param struct zcrypt_queue \*zq:
        Pointer to crypto queue device

.. _`zcrypt_queue_unregister.description`:

Description
-----------

Unregister a crypto queue device.

.. This file was automatic generated / don't edit.

