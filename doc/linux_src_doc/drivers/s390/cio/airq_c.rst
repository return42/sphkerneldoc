.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/cio/airq.c

.. _`register_adapter_interrupt`:

register_adapter_interrupt
==========================

.. c:function:: int register_adapter_interrupt(struct airq_struct *airq)

    register adapter interrupt handler

    :param struct airq_struct \*airq:
        pointer to adapter interrupt descriptor

.. _`register_adapter_interrupt.description`:

Description
-----------

Returns 0 on success, or -EINVAL.

.. _`unregister_adapter_interrupt`:

unregister_adapter_interrupt
============================

.. c:function:: void unregister_adapter_interrupt(struct airq_struct *airq)

    unregister adapter interrupt handler

    :param struct airq_struct \*airq:
        pointer to adapter interrupt descriptor

.. _`airq_iv_create`:

airq_iv_create
==============

.. c:function:: struct airq_iv *airq_iv_create(unsigned long bits, unsigned long flags)

    create an interrupt vector

    :param unsigned long bits:
        number of bits in the interrupt vector

    :param unsigned long flags:
        allocation flags

.. _`airq_iv_create.description`:

Description
-----------

Returns a pointer to an interrupt vector structure

.. _`airq_iv_release`:

airq_iv_release
===============

.. c:function:: void airq_iv_release(struct airq_iv *iv)

    release an interrupt vector

    :param struct airq_iv \*iv:
        pointer to interrupt vector structure

.. _`airq_iv_alloc`:

airq_iv_alloc
=============

.. c:function:: unsigned long airq_iv_alloc(struct airq_iv *iv, unsigned long num)

    allocate irq bits from an interrupt vector

    :param struct airq_iv \*iv:
        pointer to an interrupt vector structure

    :param unsigned long num:
        number of consecutive irq bits to allocate

.. _`airq_iv_alloc.description`:

Description
-----------

Returns the bit number of the first irq in the allocated block of irqs,
or -1UL if no bit is available or the AIRQ_IV_ALLOC flag has not been
specified

.. _`airq_iv_free`:

airq_iv_free
============

.. c:function:: void airq_iv_free(struct airq_iv *iv, unsigned long bit, unsigned long num)

    free irq bits of an interrupt vector

    :param struct airq_iv \*iv:
        pointer to interrupt vector structure

    :param unsigned long bit:
        number of the first irq bit to free

    :param unsigned long num:
        number of consecutive irq bits to free

.. _`airq_iv_scan`:

airq_iv_scan
============

.. c:function:: unsigned long airq_iv_scan(struct airq_iv *iv, unsigned long start, unsigned long end)

    scan interrupt vector for non-zero bits

    :param struct airq_iv \*iv:
        pointer to interrupt vector structure

    :param unsigned long start:
        bit number to start the search

    :param unsigned long end:
        bit number to end the search

.. _`airq_iv_scan.description`:

Description
-----------

Returns the bit number of the next non-zero interrupt bit, or
-1UL if the scan completed without finding any more any non-zero bits.

.. This file was automatic generated / don't edit.

