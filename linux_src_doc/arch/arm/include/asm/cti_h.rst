.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/arm/include/asm/cti.h

.. _`cti`:

struct cti
==========

.. c:type:: struct cti

    cross trigger interface struct

.. _`cti.definition`:

Definition
----------

.. code-block:: c

    struct cti {
        void __iomem *base;
        int irq;
        int trig_out_for_irq;
    }

.. _`cti.members`:

Members
-------

base
    mapped virtual address for the cti base

irq
    irq number for the cti

trig_out_for_irq
    triger out number which will cause
    the \ ``irq``\  happen

.. _`cti.description`:

Description
-----------

cti struct used to operate cti registers.

.. _`cti_init`:

cti_init
========

.. c:function:: void cti_init(struct cti *cti, void __iomem *base, int irq, int trig_out)

    initialize the cti instance

    :param cti:
        cti instance
    :type cti: struct cti \*

    :param base:
        mapped virtual address for the cti base
    :type base: void __iomem \*

    :param irq:
        irq number for the cti
    :type irq: int

    :param trig_out:
        triger out number which will cause
        the \ ``irq``\  happen
    :type trig_out: int

.. _`cti_init.description`:

Description
-----------

called by machine code to pass the board dependent
\ ``base``\ , \ ``irq``\  and \ ``trig_out``\  to cti.

.. _`cti_map_trigger`:

cti_map_trigger
===============

.. c:function:: void cti_map_trigger(struct cti *cti, int trig_in, int trig_out, int chan)

    use the \ ``chan``\  to map \ ``trig_in``\  to \ ``trig_out``\ 

    :param cti:
        cti instance
    :type cti: struct cti \*

    :param trig_in:
        trigger in number
    :type trig_in: int

    :param trig_out:
        trigger out number
    :type trig_out: int

    :param chan:
        *undescribed*
    :type chan: int

.. _`cti_map_trigger.description`:

Description
-----------

This function maps one trigger in of \ ``trig_in``\  to one trigger
out of \ ``trig_out``\  using the channel \ ``chan``\ .

.. _`cti_enable`:

cti_enable
==========

.. c:function:: void cti_enable(struct cti *cti)

    enable the cti module

    :param cti:
        cti instance
    :type cti: struct cti \*

.. _`cti_enable.description`:

Description
-----------

enable the cti module

.. _`cti_disable`:

cti_disable
===========

.. c:function:: void cti_disable(struct cti *cti)

    disable the cti module

    :param cti:
        cti instance
    :type cti: struct cti \*

.. _`cti_disable.description`:

Description
-----------

enable the cti module

.. _`cti_irq_ack`:

cti_irq_ack
===========

.. c:function:: void cti_irq_ack(struct cti *cti)

    clear the cti irq

    :param cti:
        cti instance
    :type cti: struct cti \*

.. _`cti_irq_ack.description`:

Description
-----------

clear the cti irq

.. _`cti_unlock`:

cti_unlock
==========

.. c:function:: void cti_unlock(struct cti *cti)

    unlock cti module

    :param cti:
        cti instance
    :type cti: struct cti \*

.. _`cti_unlock.description`:

Description
-----------

unlock the cti module, or else any writes to the cti
module is not allowed.

.. _`cti_lock`:

cti_lock
========

.. c:function:: void cti_lock(struct cti *cti)

    lock cti module

    :param cti:
        cti instance
    :type cti: struct cti \*

.. _`cti_lock.description`:

Description
-----------

lock the cti module, so any writes to the cti
module will be not allowed.

.. This file was automatic generated / don't edit.

