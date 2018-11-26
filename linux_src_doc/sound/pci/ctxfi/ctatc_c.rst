.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/pci/ctxfi/ctatc.c

.. _`mono_sum_scale`:

MONO_SUM_SCALE
==============

.. c:function::  MONO_SUM_SCALE()

.. _`mono_sum_scale.description`:

Description
-----------

This source file is released under GPL v2 license (no other versions).
See the COPYING file included in the main directory of this source
distribution for the license terms and conditions.

\ ``File``\     ctatc.c

\ ``Brief``\ 
This file contains the implementation of the device resource management
object.

\ ``Author``\  Liu Chun
\ ``Date``\  Mar 28 2008

.. _`ct_atc_create`:

ct_atc_create
=============

.. c:function:: int ct_atc_create(struct snd_card *card, struct pci_dev *pci, unsigned int rsr, unsigned int msr, int chip_type, unsigned int ssid, struct ct_atc **ratc)

    create and initialize a hardware manager

    :param card:
        corresponding alsa card object
    :type card: struct snd_card \*

    :param pci:
        corresponding kernel pci device object
    :type pci: struct pci_dev \*

    :param rsr:
        *undescribed*
    :type rsr: unsigned int

    :param msr:
        *undescribed*
    :type msr: unsigned int

    :param chip_type:
        *undescribed*
    :type chip_type: int

    :param ssid:
        *undescribed*
    :type ssid: unsigned int

    :param ratc:
        return created object address in it
    :type ratc: struct ct_atc \*\*

.. _`ct_atc_create.description`:

Description
-----------

Creates and initializes a hardware manager.

Creates kmallocated ct_atc structure. Initializes hardware.
Returns 0 if succeeds, or negative error code if fails.

.. This file was automatic generated / don't edit.

