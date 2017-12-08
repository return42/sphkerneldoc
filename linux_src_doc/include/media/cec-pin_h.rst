.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/cec-pin.h

.. _`cec_pin_ops`:

struct cec_pin_ops
==================

.. c:type:: struct cec_pin_ops

    low-level CEC pin operations

.. _`cec_pin_ops.definition`:

Definition
----------

.. code-block:: c

    struct cec_pin_ops {
        bool (*read)(struct cec_adapter *adap);
        void (*low)(struct cec_adapter *adap);
        void (*high)(struct cec_adapter *adap);
        bool (*enable_irq)(struct cec_adapter *adap);
        void (*disable_irq)(struct cec_adapter *adap);
        void (*free)(struct cec_adapter *adap);
        void (*status)(struct cec_adapter *adap, struct seq_file *file);
        int (*read_hpd)(struct cec_adapter *adap);
    }

.. _`cec_pin_ops.members`:

Members
-------

read
    read the CEC pin. Return true if high, false if low.

low
    drive the CEC pin low.

high
    stop driving the CEC pin. The pull-up will drive the pin
    high, unless someone else is driving the pin low.

enable_irq
    optional, enable the interrupt to detect pin voltage changes.

disable_irq
    optional, disable the interrupt.

free
    optional. Free any allocated resources. Called when the
    adapter is deleted.

status
    optional, log status information.

read_hpd
    read the HPD pin. Return true if high, false if low or
    an error if negative. If NULL or -ENOTTY is returned,
    then this is not supported.

.. _`cec_pin_ops.description`:

Description
-----------

These operations are used by the cec pin framework to manipulate
the CEC pin.

.. _`cec_pin_changed`:

cec_pin_changed
===============

.. c:function:: void cec_pin_changed(struct cec_adapter *adap, bool value)

    update pin state from interrupt

    :param struct cec_adapter \*adap:
        pointer to the cec adapter

    :param bool value:
        when true the pin is high, otherwise it is low

.. _`cec_pin_changed.description`:

Description
-----------

If changes of the CEC voltage are detected via an interrupt, then
cec_pin_changed is called from the interrupt with the new value.

.. _`cec_pin_allocate_adapter`:

cec_pin_allocate_adapter
========================

.. c:function:: struct cec_adapter *cec_pin_allocate_adapter(const struct cec_pin_ops *pin_ops, void *priv, const char *name, u32 caps)

    allocate a pin-based cec adapter

    :param const struct cec_pin_ops \*pin_ops:
        low-level pin operations

    :param void \*priv:
        will be stored in adap->priv and can be used by the adapter ops.
        Use cec_get_drvdata(adap) to get the priv pointer.

    :param const char \*name:
        the name of the CEC adapter. Note: this name will be copied.

    :param u32 caps:
        capabilities of the CEC adapter. This will be ORed with
        CEC_CAP_MONITOR_ALL and CEC_CAP_MONITOR_PIN.

.. _`cec_pin_allocate_adapter.description`:

Description
-----------

Allocate a cec adapter using the cec pin framework.

.. _`cec_pin_allocate_adapter.return`:

Return
------

a pointer to the cec adapter or an error pointer

.. This file was automatic generated / don't edit.

