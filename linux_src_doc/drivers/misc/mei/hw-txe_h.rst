.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mei/hw-txe.h

.. _`mei_txe_hw`:

struct mei_txe_hw
=================

.. c:type:: struct mei_txe_hw

    txe hardware specifics

.. _`mei_txe_hw.definition`:

Definition
----------

.. code-block:: c

    struct mei_txe_hw {
        void __iomem * const *mem_addr;
        u32 aliveness;
        u32 readiness;
        u32 slots;
        wait_queue_head_t wait_aliveness_resp;
        unsigned long intr_cause;
    }

.. _`mei_txe_hw.members`:

Members
-------

mem_addr
    SeC and BRIDGE bars

aliveness
    aliveness (power gating) state of the hardware

readiness
    readiness state of the hardware

slots
    number of empty slots

wait_aliveness_resp
    aliveness wait queue

intr_cause
    translated interrupt cause

.. This file was automatic generated / don't edit.

