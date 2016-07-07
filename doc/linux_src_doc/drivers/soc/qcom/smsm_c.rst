.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/smsm.c

.. _`qcom_smsm`:

struct qcom_smsm
================

.. c:type:: struct qcom_smsm

    smsm driver context

.. _`qcom_smsm.definition`:

Definition
----------

.. code-block:: c

    struct qcom_smsm {
        struct device *dev;
        u32 local_host;
        u32 num_hosts;
        u32 num_entries;
        u32 *local_state;
        u32 *subscription;
        struct qcom_smem_state *state;
        spinlock_t lock;
        struct smsm_entry *entries;
        struct smsm_host *hosts;
    }

.. _`qcom_smsm.members`:

Members
-------

dev
    smsm device pointer

local_host
    column in the subscription matrix representing this system

num_hosts
    number of columns in the subscription matrix

num_entries
    number of entries in the state map and rows in the subscription
    matrix

local_state
    pointer to the local processor's state bits

subscription
    pointer to local processor's row in subscription matrix

state
    smem state handle

lock
    spinlock for read-modify-write of the outgoing state

entries
    context for each of the entries

hosts
    context for each of the hosts

.. _`smsm_entry`:

struct smsm_entry
=================

.. c:type:: struct smsm_entry

    per remote processor entry context

.. _`smsm_entry.definition`:

Definition
----------

.. code-block:: c

    struct smsm_entry {
        struct qcom_smsm *smsm;
        struct irq_domain *domain;
        unsigned long irq_enabled\[BITS_TO_LONGS(32)\];
        unsigned long irq_rising\[BITS_TO_LONGS(32)\];
        unsigned long irq_falling\[BITS_TO_LONGS(32)\];
        u32 last_value;
        u32 *remote_state;
        u32 *subscription;
    }

.. _`smsm_entry.members`:

Members
-------

smsm
    back-reference to driver context

domain
    IRQ domain for this entry, if representing a remote system

last_value
    snapshot of state bits last time the interrupts where propagated

remote_state
    pointer to this entry's state bits

subscription
    pointer to a row in the subscription matrix representing this
    entry

.. _`smsm_host`:

struct smsm_host
================

.. c:type:: struct smsm_host

    representation of a remote host

.. _`smsm_host.definition`:

Definition
----------

.. code-block:: c

    struct smsm_host {
        struct regmap *ipc_regmap;
        int ipc_offset;
        int ipc_bit;
    }

.. _`smsm_host.members`:

Members
-------

ipc_regmap
    regmap for outgoing interrupt

ipc_offset
    offset in \ ``ipc_regmap``\  for outgoing interrupt

ipc_bit
    bit in \ ``ipc_regmap``\  + \ ``ipc_offset``\  for outgoing interrupt

.. _`smsm_update_bits`:

smsm_update_bits
================

.. c:function:: int smsm_update_bits(void *data, u32 mask, u32 value)

    change bit in outgoing entry and inform subscribers

    :param void \*data:
        smsm context pointer

    :param u32 mask:
        *undescribed*

    :param u32 value:
        new value

.. _`smsm_update_bits.description`:

Description
-----------

Used to set and clear the bits in the outgoing/local entry and inform
subscribers about the change.

.. _`smsm_intr`:

smsm_intr
=========

.. c:function:: irqreturn_t smsm_intr(int irq, void *data)

    cascading IRQ handler for SMSM

    :param int irq:
        unused

    :param void \*data:
        entry related to this IRQ

.. _`smsm_intr.description`:

Description
-----------

This function cascades an incoming interrupt from a remote system, based on
the state bits and configuration.

.. _`smsm_mask_irq`:

smsm_mask_irq
=============

.. c:function:: void smsm_mask_irq(struct irq_data *irqd)

    un-subscribe from cascades of IRQs of a certain staus bit

    :param struct irq_data \*irqd:
        IRQ handle to be masked

.. _`smsm_mask_irq.description`:

Description
-----------

This un-subscribes the local CPU from interrupts upon changes to the defines
status bit. The bit is also cleared from cascading.

.. _`smsm_unmask_irq`:

smsm_unmask_irq
===============

.. c:function:: void smsm_unmask_irq(struct irq_data *irqd)

    subscribe to cascades of IRQs of a certain status bit

    :param struct irq_data \*irqd:
        IRQ handle to be unmasked

.. _`smsm_unmask_irq.description`:

Description
-----------

This subscribes the local CPU to interrupts upon changes to the defined
status bit. The bit is also marked for cascading.

.. _`smsm_set_irq_type`:

smsm_set_irq_type
=================

.. c:function:: int smsm_set_irq_type(struct irq_data *irqd, unsigned int type)

    updates the requested IRQ type for the cascading

    :param struct irq_data \*irqd:
        consumer interrupt handle

    :param unsigned int type:
        requested flags

.. _`smsm_irq_map`:

smsm_irq_map
============

.. c:function:: int smsm_irq_map(struct irq_domain *d, unsigned int irq, irq_hw_number_t hw)

    sets up a mapping for a cascaded IRQ

    :param struct irq_domain \*d:
        IRQ domain representing an entry

    :param unsigned int irq:
        IRQ to set up

    :param irq_hw_number_t hw:
        unused

.. _`smsm_parse_ipc`:

smsm_parse_ipc
==============

.. c:function:: int smsm_parse_ipc(struct qcom_smsm *smsm, unsigned host_id)

    parses a qcom,ipc-\ ``d``\  device tree property

    :param struct qcom_smsm \*smsm:
        smsm driver context

    :param unsigned host_id:
        index of the remote host to be resolved

.. _`smsm_parse_ipc.description`:

Description
-----------

Parses device tree to acquire the information needed for sending the
outgoing interrupts to a remote host - identified by \ ``host_id``\ .

.. _`smsm_inbound_entry`:

smsm_inbound_entry
==================

.. c:function:: int smsm_inbound_entry(struct qcom_smsm *smsm, struct smsm_entry *entry, struct device_node *node)

    parse DT and set up an entry representing a remote system

    :param struct qcom_smsm \*smsm:
        smsm driver context

    :param struct smsm_entry \*entry:
        entry context to be set up

    :param struct device_node \*node:
        dt node containing the entry's properties

.. _`smsm_get_size_info`:

smsm_get_size_info
==================

.. c:function:: int smsm_get_size_info(struct qcom_smsm *smsm)

    parse the optional memory segment for sizes

    :param struct qcom_smsm \*smsm:
        smsm driver context

.. _`smsm_get_size_info.description`:

Description
-----------

Attempt to acquire the number of hosts and entries from the optional shared
memory location. Not being able to find this segment should indicate that
we're on a older system where these values was hard coded to
SMSM_DEFAULT_NUM_ENTRIES and SMSM_DEFAULT_NUM_HOSTS.

Returns 0 on success, negative errno on failure.

.. This file was automatic generated / don't edit.

