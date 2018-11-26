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

    :param dev:
        *undescribed*
    :type dev: struct crypto4xx_device \*

.. _`crypto4xx_build_pdr`:

crypto4xx_build_pdr
===================

.. c:function:: u32 crypto4xx_build_pdr(struct crypto4xx_device *dev)

    no need to alloc buf for the ring gdr_tail, gdr_head and gdr_count are initialized by this function

    :param dev:
        *undescribed*
    :type dev: struct crypto4xx_device \*

.. _`crypto4xx_build_gdr`:

crypto4xx_build_gdr
===================

.. c:function:: u32 crypto4xx_build_gdr(struct crypto4xx_device *dev)

    no need to alloc buf for the ring gdr_tail, gdr_head and gdr_count are initialized by this function

    :param dev:
        *undescribed*
    :type dev: struct crypto4xx_device \*

.. _`crypto4xx_build_sdr`:

crypto4xx_build_sdr
===================

.. c:function:: u32 crypto4xx_build_sdr(struct crypto4xx_device *dev)

    need to alloc buf for the ring sdr_tail, sdr_head and sdr_count are initialized by this function

    :param dev:
        *undescribed*
    :type dev: struct crypto4xx_device \*

.. _`crypto4xx_ctx_init`:

crypto4xx_ctx_init
==================

.. c:function:: void crypto4xx_ctx_init(struct crypto4xx_alg *amcc_alg, struct crypto4xx_ctx *ctx)

    :param amcc_alg:
        *undescribed*
    :type amcc_alg: struct crypto4xx_alg \*

    :param ctx:
        *undescribed*
    :type ctx: struct crypto4xx_ctx \*

.. _`crypto4xx_interrupt_handler`:

crypto4xx_interrupt_handler
===========================

.. c:function:: irqreturn_t crypto4xx_interrupt_handler(int irq, void *data, u32 clr_val)

    :param irq:
        *undescribed*
    :type irq: int

    :param data:
        *undescribed*
    :type data: void \*

    :param clr_val:
        *undescribed*
    :type clr_val: u32

.. _`crypto4xx_probe`:

crypto4xx_probe
===============

.. c:function:: int crypto4xx_probe(struct platform_device *ofdev)

    :param ofdev:
        *undescribed*
    :type ofdev: struct platform_device \*

.. This file was automatic generated / don't edit.

