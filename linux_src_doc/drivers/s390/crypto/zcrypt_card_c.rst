.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/zcrypt_card.c

.. _`zcrypt_card_register`:

zcrypt_card_register
====================

.. c:function:: int zcrypt_card_register(struct zcrypt_card *zc)

    Register a crypto card device.

    :param zc:
        Pointer to a crypto card device
    :type zc: struct zcrypt_card \*

.. _`zcrypt_card_register.description`:

Description
-----------

Register a crypto card device. Returns 0 if successful.

.. _`zcrypt_card_unregister`:

zcrypt_card_unregister
======================

.. c:function:: void zcrypt_card_unregister(struct zcrypt_card *zc)

    Unregister a crypto card device.

    :param zc:
        Pointer to crypto card device
    :type zc: struct zcrypt_card \*

.. _`zcrypt_card_unregister.description`:

Description
-----------

Unregister a crypto card device.

.. This file was automatic generated / don't edit.

