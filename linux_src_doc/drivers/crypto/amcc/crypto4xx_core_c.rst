.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/amcc/crypto4xx_core.c

.. _`ppc4xx_sec_version_str`:

PPC4XX_SEC_VERSION_STR
======================

.. c:function::  PPC4XX_SEC_VERSION_STR()

.. _`ppc4xx_sec_version_str.description`:

Description
-----------

Copyright (c) 2008 Applied Micro Circuits Corporation.
All rights reserved. James Hsiao <jhsiao@amcc.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

This file implements AMCC crypto offload Linux device driver for use with
Linux CryptoAPI.

.. _`crypto4xx_hw_init`:

crypto4xx_hw_init
=================

.. c:function:: void crypto4xx_hw_init(struct crypto4xx_device *dev)

    :param struct crypto4xx_device \*dev:
        *undescribed*

.. _`crypto4xx_build_pdr`:

crypto4xx_build_pdr
===================

.. c:function:: u32 crypto4xx_build_pdr(struct crypto4xx_device *dev)

    no need to alloc buf for the ring gdr_tail, gdr_head and gdr_count are initialized by this function

    :param struct crypto4xx_device \*dev:
        *undescribed*

.. _`crypto4xx_build_gdr`:

crypto4xx_build_gdr
===================

.. c:function:: u32 crypto4xx_build_gdr(struct crypto4xx_device *dev)

    no need to alloc buf for the ring gdr_tail, gdr_head and gdr_count are initialized by this function

    :param struct crypto4xx_device \*dev:
        *undescribed*

.. _`crypto4xx_build_sdr`:

crypto4xx_build_sdr
===================

.. c:function:: u32 crypto4xx_build_sdr(struct crypto4xx_device *dev)

    need to alloc buf for the ring sdr_tail, sdr_head and sdr_count are initialized by this function

    :param struct crypto4xx_device \*dev:
        *undescribed*

.. _`crypto4xx_memcpy_le`:

crypto4xx_memcpy_le
===================

.. c:function:: void crypto4xx_memcpy_le(unsigned int *dst, const unsigned char *buf, int len)

    Only use this function to copy items that is word aligned.

    :param unsigned int \*dst:
        *undescribed*

    :param const unsigned char \*buf:
        *undescribed*

    :param int len:
        *undescribed*

.. _`crypto4xx_alg_init`:

crypto4xx_alg_init
==================

.. c:function:: int crypto4xx_alg_init(struct crypto_tfm *tfm)

    :param struct crypto_tfm \*tfm:
        *undescribed*

.. _`crypto4xx_ce_interrupt_handler`:

crypto4xx_ce_interrupt_handler
==============================

.. c:function:: irqreturn_t crypto4xx_ce_interrupt_handler(int irq, void *data)

    :param int irq:
        *undescribed*

    :param void \*data:
        *undescribed*

.. _`crypto4xx_probe`:

crypto4xx_probe
===============

.. c:function:: int crypto4xx_probe(struct platform_device *ofdev)

    :param struct platform_device \*ofdev:
        *undescribed*

.. This file was automatic generated / don't edit.

