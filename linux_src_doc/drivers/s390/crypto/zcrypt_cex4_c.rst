.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/zcrypt_cex4.c

.. _`zcrypt_cex4_card_probe`:

zcrypt_cex4_card_probe
======================

.. c:function:: int zcrypt_cex4_card_probe(struct ap_device *ap_dev)

    accepts the AP device since the bus_match already checked the hardware type.

    :param ap_dev:
        pointer to the AP device.
    :type ap_dev: struct ap_device \*

.. _`zcrypt_cex4_card_remove`:

zcrypt_cex4_card_remove
=======================

.. c:function:: void zcrypt_cex4_card_remove(struct ap_device *ap_dev)

    if an AP card device is removed.

    :param ap_dev:
        *undescribed*
    :type ap_dev: struct ap_device \*

.. _`zcrypt_cex4_queue_probe`:

zcrypt_cex4_queue_probe
=======================

.. c:function:: int zcrypt_cex4_queue_probe(struct ap_device *ap_dev)

    accepts the AP device since the bus_match already checked the hardware type.

    :param ap_dev:
        pointer to the AP device.
    :type ap_dev: struct ap_device \*

.. _`zcrypt_cex4_queue_remove`:

zcrypt_cex4_queue_remove
========================

.. c:function:: void zcrypt_cex4_queue_remove(struct ap_device *ap_dev)

    information if an AP queue device is removed.

    :param ap_dev:
        *undescribed*
    :type ap_dev: struct ap_device \*

.. This file was automatic generated / don't edit.

