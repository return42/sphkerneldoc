.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/plat-samsung/include/plat/wakeup-mask.h

.. _`samsung_wakeup_mask`:

struct samsung_wakeup_mask
==========================

.. c:type:: struct samsung_wakeup_mask

    wakeup mask information

.. _`samsung_wakeup_mask.definition`:

Definition
----------

.. code-block:: c

    struct samsung_wakeup_mask {
        unsigned int irq;
        u32 bit;
    }

.. _`samsung_wakeup_mask.members`:

Members
-------

irq
    The interrupt associated with this wakeup.

bit
    The bit, as a (1 << bitno) controlling this source.

.. _`samsung_sync_wakemask`:

samsung_sync_wakemask
=====================

.. c:function:: void samsung_sync_wakemask(void __iomem *reg, const struct samsung_wakeup_mask *masks, int nr_masks)

    sync wakeup mask information for pm

    :param void __iomem \*reg:
        The register that is used.

    :param const struct samsung_wakeup_mask \*masks:
        The list of masks to use.

    :param int nr_masks:
        The number of entries pointed to buy \ ``masks``\ .

.. _`samsung_sync_wakemask.description`:

Description
-----------

Synchronise the wakeup mask information at suspend time from the list
of interrupts and control bits in \ ``masks``\ . We do this at suspend time
as overriding the relevant irq chips is harder and the register is only
required to be correct before we enter sleep.

.. This file was automatic generated / don't edit.

