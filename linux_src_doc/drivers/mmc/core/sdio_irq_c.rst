.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mmc/core/sdio_irq.c

.. _`sdio_claim_irq`:

sdio_claim_irq
==============

.. c:function:: int sdio_claim_irq(struct sdio_func *func, sdio_irq_handler_t *handler)

    claim the IRQ for a SDIO function

    :param struct sdio_func \*func:
        SDIO function

    :param sdio_irq_handler_t \*handler:
        IRQ handler callback

.. _`sdio_claim_irq.description`:

Description
-----------

Claim and activate the IRQ for the given SDIO function. The provided
handler will be called when that IRQ is asserted.  The host is always
claimed already when the handler is called so the handler should not
call \ :c:func:`sdio_claim_host`\  or \ :c:func:`sdio_release_host`\ .

.. _`sdio_release_irq`:

sdio_release_irq
================

.. c:function:: int sdio_release_irq(struct sdio_func *func)

    release the IRQ for a SDIO function

    :param struct sdio_func \*func:
        SDIO function

.. _`sdio_release_irq.description`:

Description
-----------

Disable and release the IRQ for the given SDIO function.

.. This file was automatic generated / don't edit.

