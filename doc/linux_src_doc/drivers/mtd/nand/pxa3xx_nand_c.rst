.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/nand/pxa3xx_nand.c

.. _`pxa3xx_nand_start`:

pxa3xx_nand_start
=================

.. c:function:: void pxa3xx_nand_start(struct pxa3xx_nand_info *info)

    it is a must to set ND_RUN firstly, then write command buffer, otherwise, it does not work. We enable all the interrupt at the same time, and let pxa3xx_nand_irq to handle all logic.

    :param struct pxa3xx_nand_info \*info:
        *undescribed*

.. This file was automatic generated / don't edit.

