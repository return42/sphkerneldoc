.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/soc/qcom/smp2p.c

.. _`smp2p_smem_item`:

struct smp2p_smem_item
======================

.. c:type:: struct smp2p_smem_item

    in memory communication structure

.. _`smp2p_smem_item.definition`:

Definition
----------

.. code-block:: c

    struct smp2p_smem_item {
        u32 magic;
        u8 version;
        unsigned features:24;
        u16 local_pid;
        u16 remote_pid;
        u16 total_entries;
        u16 valid_entries;
        u32 flags;
        struct {
            u8 name[SMP2P_MAX_ENTRY_NAME];
            u32 value;
        } entries[SMP2P_MAX_ENTRY];
    }

.. _`smp2p_smem_item.members`:

Members
-------

magic
    magic number

version
    version - must be 1

features
    features flag - currently unused

local_pid
    processor id of sending end

remote_pid
    processor id of receiving end

total_entries
    number of entries - always SMP2P_MAX_ENTRY

valid_entries
    number of allocated entries

flags
    *undescribed*

entries
    individual communication entries

name
    name of the entry

value
    content of the entry

.. _`smp2p_entry`:

struct smp2p_entry
==================

.. c:type:: struct smp2p_entry

    driver context matching one entry

.. _`smp2p_entry.definition`:

Definition
----------

.. code-block:: c

    struct smp2p_entry {
        struct list_head node;
        struct qcom_smp2p *smp2p;
        const char *name;
        u32 *value;
        u32 last_value;
        struct irq_domain *domain;
        DECLARE_BITMAP(irq_enabled, 32);
        DECLARE_BITMAP(irq_rising, 32);
        DECLARE_BITMAP(irq_falling, 32);
        struct qcom_smem_state *state;
        spinlock_t lock;
    }

.. _`smp2p_entry.members`:

Members
-------

node
    list entry to keep track of allocated entries

smp2p
    reference to the device driver context

name
    name of the entry, to match against smp2p_smem_item

value
    pointer to smp2p_smem_item entry value

last_value
    last handled value

domain
    irq_domain for inbound entries

irq_enabled
    bitmap to track enabled irq bits

irq_rising
    bitmap to mark irq bits for rising detection

irq_falling
    bitmap to mark irq bits for falling detection

state
    smem state handle

lock
    spinlock to protect read-modify-write of the value

.. _`qcom_smp2p`:

struct qcom_smp2p
=================

.. c:type:: struct qcom_smp2p

    device driver context

.. _`qcom_smp2p.definition`:

Definition
----------

.. code-block:: c

    struct qcom_smp2p {
        struct device *dev;
        struct smp2p_smem_item *in;
        struct smp2p_smem_item *out;
        unsigned smem_items[SMP2P_OUTBOUND + 1];
        unsigned valid_entries;
        unsigned local_pid;
        unsigned remote_pid;
        struct regmap *ipc_regmap;
        int ipc_offset;
        int ipc_bit;
        struct list_head inbound;
        struct list_head outbound;
    }

.. _`qcom_smp2p.members`:

Members
-------

dev
    device driver handle

in
    pointer to the inbound smem item

out
    *undescribed*

smem_items
    ids of the two smem items

valid_entries
    already scanned inbound entries

local_pid
    processor id of the inbound edge

remote_pid
    processor id of the outbound edge

ipc_regmap
    regmap for the outbound ipc

ipc_offset
    offset within the regmap

ipc_bit
    bit in regmap@offset to kick to signal remote processor

inbound
    list of inbound entries

outbound
    list of outbound entries

.. _`qcom_smp2p_intr`:

qcom_smp2p_intr
===============

.. c:function:: irqreturn_t qcom_smp2p_intr(int irq, void *data)

    interrupt handler for incoming notifications

    :param int irq:
        unused

    :param void \*data:
        smp2p driver context

.. _`qcom_smp2p_intr.description`:

Description
-----------

Handle notifications from the remote side to handle newly allocated entries
or any changes to the state bits of existing entries.

.. This file was automatic generated / don't edit.

