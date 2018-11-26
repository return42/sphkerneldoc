.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/zcrypt_cex2c.c

.. _`zcrypt_cex2c_rng_supported`:

zcrypt_cex2c_rng_supported
==========================

.. c:function:: int zcrypt_cex2c_rng_supported(struct ap_queue *aq)

    card to find out if large random numbers are supported.

    :param aq:
        *undescribed*
    :type aq: struct ap_queue \*

.. _`zcrypt_cex2c_rng_supported.description`:

Description
-----------

Returns 1 if large random numbers are supported, 0 if not and < 0 on error.

.. _`zcrypt_cex2c_card_probe`:

zcrypt_cex2c_card_probe
=======================

.. c:function:: int zcrypt_cex2c_card_probe(struct ap_device *ap_dev)

    AP device since the bus_match already checked the hardware type.

    :param ap_dev:
        pointer to the AP card device.
    :type ap_dev: struct ap_device \*

.. _`zcrypt_cex2c_card_remove`:

zcrypt_cex2c_card_remove
========================

.. c:function:: void zcrypt_cex2c_card_remove(struct ap_device *ap_dev)

    if an AP card device is removed.

    :param ap_dev:
        *undescribed*
    :type ap_dev: struct ap_device \*

.. _`zcrypt_cex2c_queue_probe`:

zcrypt_cex2c_queue_probe
========================

.. c:function:: int zcrypt_cex2c_queue_probe(struct ap_device *ap_dev)

    AP device since the bus_match already checked the hardware type.

    :param ap_dev:
        pointer to the AP card device.
    :type ap_dev: struct ap_device \*

.. _`zcrypt_cex2c_queue_remove`:

zcrypt_cex2c_queue_remove
=========================

.. c:function:: void zcrypt_cex2c_queue_remove(struct ap_device *ap_dev)

    if an AP queue device is removed.

    :param ap_dev:
        *undescribed*
    :type ap_dev: struct ap_device \*

.. This file was automatic generated / don't edit.

