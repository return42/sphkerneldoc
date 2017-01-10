.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/zcrypt_cex2a.c

.. _`zcrypt_cex2a_card_probe`:

zcrypt_cex2a_card_probe
=======================

.. c:function:: int zcrypt_cex2a_card_probe(struct ap_device *ap_dev)

    since the bus_match already checked the card type.

    :param struct ap_device \*ap_dev:
        pointer to the AP device.

.. _`zcrypt_cex2a_card_remove`:

zcrypt_cex2a_card_remove
========================

.. c:function:: void zcrypt_cex2a_card_remove(struct ap_device *ap_dev)

    if an AP card device is removed.

    :param struct ap_device \*ap_dev:
        *undescribed*

.. _`zcrypt_cex2a_queue_probe`:

zcrypt_cex2a_queue_probe
========================

.. c:function:: int zcrypt_cex2a_queue_probe(struct ap_device *ap_dev)

    since the bus_match already checked the queue type.

    :param struct ap_device \*ap_dev:
        pointer to the AP device.

.. _`zcrypt_cex2a_queue_remove`:

zcrypt_cex2a_queue_remove
=========================

.. c:function:: void zcrypt_cex2a_queue_remove(struct ap_device *ap_dev)

    if an AP queue device is removed.

    :param struct ap_device \*ap_dev:
        *undescribed*

.. This file was automatic generated / don't edit.

