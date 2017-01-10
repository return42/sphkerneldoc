.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/zcrypt_pcixcc.c

.. _`zcrypt_pcixcc_rng_supported`:

zcrypt_pcixcc_rng_supported
===========================

.. c:function:: int zcrypt_pcixcc_rng_supported(struct ap_queue *aq)

    card to find out if large random numbers are supported.

    :param struct ap_queue \*aq:
        *undescribed*

.. _`zcrypt_pcixcc_rng_supported.description`:

Description
-----------

Returns 1 if large random numbers are supported, 0 if not and < 0 on error.

.. _`zcrypt_pcixcc_card_probe`:

zcrypt_pcixcc_card_probe
========================

.. c:function:: int zcrypt_pcixcc_card_probe(struct ap_device *ap_dev)

    AP device since the bus_match already checked the hardware type. The

    :param struct ap_device \*ap_dev:
        pointer to the AP card device.

.. _`zcrypt_pcixcc_card_probe.pcixcc-cards-come-in-two-flavours`:

PCIXCC cards come in two flavours
---------------------------------

micro code level 2 and micro code
level 3. This is checked by sending a test message to the device.

.. _`zcrypt_pcixcc_card_remove`:

zcrypt_pcixcc_card_remove
=========================

.. c:function:: void zcrypt_pcixcc_card_remove(struct ap_device *ap_dev)

    if an AP card device is removed.

    :param struct ap_device \*ap_dev:
        *undescribed*

.. _`zcrypt_pcixcc_queue_probe`:

zcrypt_pcixcc_queue_probe
=========================

.. c:function:: int zcrypt_pcixcc_queue_probe(struct ap_device *ap_dev)

    AP device since the bus_match already checked the hardware type. The

    :param struct ap_device \*ap_dev:
        pointer to the AP card device.

.. _`zcrypt_pcixcc_queue_probe.pcixcc-cards-come-in-two-flavours`:

PCIXCC cards come in two flavours
---------------------------------

micro code level 2 and micro code
level 3. This is checked by sending a test message to the device.

.. _`zcrypt_pcixcc_queue_remove`:

zcrypt_pcixcc_queue_remove
==========================

.. c:function:: void zcrypt_pcixcc_queue_remove(struct ap_device *ap_dev)

    if an AP queue device is removed.

    :param struct ap_device \*ap_dev:
        *undescribed*

.. This file was automatic generated / don't edit.

