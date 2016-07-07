.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mmc/host.h

.. _`mmc_slot`:

struct mmc_slot
===============

.. c:type:: struct mmc_slot

    MMC slot functions

.. _`mmc_slot.definition`:

Definition
----------

.. code-block:: c

    struct mmc_slot {
        int cd_irq;
        void *handler_priv;
    }

.. _`mmc_slot.members`:

Members
-------

cd_irq
    MMC/SD-card slot hotplug detection IRQ or -EINVAL

handler_priv
    MMC/SD-card slot context

.. _`mmc_slot.description`:

Description
-----------

Some MMC/SD host controllers implement slot-functions like card and
write-protect detection natively. However, a large number of controllers
leave these functions to the CPU. This struct provides a hook to attach
such slot-function drivers.

.. This file was automatic generated / don't edit.

