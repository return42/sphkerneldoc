.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/crypto/zcrypt_pcixcc.c

.. _`zcrypt_pcixcc_mcl`:

zcrypt_pcixcc_mcl
=================

.. c:function:: int zcrypt_pcixcc_mcl(struct ap_device *ap_dev)

    code detection function. Its sends a message to a pcixcc card to find out the microcode level.

    :param struct ap_device \*ap_dev:
        pointer to the AP device.

.. _`zcrypt_pcixcc_rng_supported`:

zcrypt_pcixcc_rng_supported
===========================

.. c:function:: int zcrypt_pcixcc_rng_supported(struct ap_device *ap_dev)

    card to find out if large random numbers are supported.

    :param struct ap_device \*ap_dev:
        pointer to the AP device.

.. _`zcrypt_pcixcc_rng_supported.description`:

Description
-----------

Returns 1 if large random numbers are supported, 0 if not and < 0 on error.

.. _`zcrypt_pcixcc_probe`:

zcrypt_pcixcc_probe
===================

.. c:function:: int zcrypt_pcixcc_probe(struct ap_device *ap_dev)

    since the bus_match already checked the hardware type. The PCIXCC

    :param struct ap_device \*ap_dev:
        pointer to the AP device.

.. _`zcrypt_pcixcc_probe.cards-come-in-two-flavours`:

cards come in two flavours
--------------------------

micro code level 2 and micro code level 3.
This is checked by sending a test message to the device.

.. _`zcrypt_pcixcc_remove`:

zcrypt_pcixcc_remove
====================

.. c:function:: void zcrypt_pcixcc_remove(struct ap_device *ap_dev)

    if an AP device is removed.

    :param struct ap_device \*ap_dev:
        *undescribed*

.. This file was automatic generated / don't edit.

