.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/nouveau/nvkm/falcon/msgqueue.h

.. _`nvkm_msgqueue_hdr`:

struct nvkm_msgqueue_hdr
========================

.. c:type:: struct nvkm_msgqueue_hdr

    header for all commands/messages

.. _`nvkm_msgqueue_hdr.definition`:

Definition
----------

.. code-block:: c

    struct nvkm_msgqueue_hdr {
        u8 unit_id;
        u8 size;
        u8 ctrl_flags;
        u8 seq_id;
    }

.. _`nvkm_msgqueue_hdr.members`:

Members
-------

unit_id
    id of firmware using receiving the command/sending the message

size
    total size of command/message

ctrl_flags
    type of command/message

seq_id
    used to match a message from its corresponding command

.. _`nvkm_msgqueue_msg`:

struct nvkm_msgqueue_msg
========================

.. c:type:: struct nvkm_msgqueue_msg

    base message.

.. _`nvkm_msgqueue_msg.definition`:

Definition
----------

.. code-block:: c

    struct nvkm_msgqueue_msg {
        struct nvkm_msgqueue_hdr hdr;
        u8 msg_type;
    }

.. _`nvkm_msgqueue_msg.members`:

Members
-------

hdr
    *undescribed*

msg_type
    *undescribed*

.. _`nvkm_msgqueue_msg.description`:

Description
-----------

This is just a header and a message (or command) type. Useful when
building command-specific structures.

.. _`nvkm_msgqueue_init_func`:

struct nvkm_msgqueue_init_func
==============================

.. c:type:: struct nvkm_msgqueue_init_func

    msgqueue functions related to initialization

.. _`nvkm_msgqueue_init_func.definition`:

Definition
----------

.. code-block:: c

    struct nvkm_msgqueue_init_func {
        void (*gen_cmdline)(struct nvkm_msgqueue *, void *);
        int (*init_callback)(struct nvkm_msgqueue *, struct nvkm_msgqueue_hdr *);
    }

.. _`nvkm_msgqueue_init_func.members`:

Members
-------

gen_cmdline
    build the commandline into a pre-allocated buffer

init_callback
    called to process the init message

.. _`nvkm_msgqueue_acr_func`:

struct nvkm_msgqueue_acr_func
=============================

.. c:type:: struct nvkm_msgqueue_acr_func

    msgqueue functions related to ACR

.. _`nvkm_msgqueue_acr_func.definition`:

Definition
----------

.. code-block:: c

    struct nvkm_msgqueue_acr_func {
        int (*boot_falcon)(struct nvkm_msgqueue *, enum nvkm_secboot_falcon);
        int (*boot_multiple_falcons)(struct nvkm_msgqueue *, unsigned long);
    }

.. _`nvkm_msgqueue_acr_func.members`:

Members
-------

boot_falcon
    build and send the command to reset a given falcon

boot_multiple_falcons
    build and send the command to reset several falcons

.. _`nvkm_msgqueue_queue`:

struct nvkm_msgqueue_queue
==========================

.. c:type:: struct nvkm_msgqueue_queue

    information about a command or message queue

.. _`nvkm_msgqueue_queue.definition`:

Definition
----------

.. code-block:: c

    struct nvkm_msgqueue_queue {
        struct mutex mutex;
        u32 index;
        u32 offset;
        u32 size;
        u32 position;
        u32 head_reg;
        u32 tail_reg;
    }

.. _`nvkm_msgqueue_queue.members`:

Members
-------

mutex
    *undescribed*

index
    physical queue index

offset
    DMEM offset where this queue begins

size
    size allocated to this queue in DMEM (in bytes)

position
    current write position

head_reg
    address of the HEAD register for this queue

tail_reg
    address of the TAIL register for this queue

.. _`nvkm_msgqueue_queue.description`:

Description
-----------

The number of queues is firmware-dependent. All queues must have their
information filled by the init message handler.

.. _`nvkm_msgqueue_seq`:

struct nvkm_msgqueue_seq
========================

.. c:type:: struct nvkm_msgqueue_seq

    keep track of ongoing commands

.. _`nvkm_msgqueue_seq.definition`:

Definition
----------

.. code-block:: c

    struct nvkm_msgqueue_seq {
        u16 id;
        enum state;
        nvkm_msgqueue_callback callback;
        struct completion *completion;
    }

.. _`nvkm_msgqueue_seq.members`:

Members
-------

id
    sequence ID

state
    current state

callback
    callback to call upon receiving matching message

completion
    completion to signal after callback is called

.. _`nvkm_msgqueue_seq.description`:

Description
-----------

Every time a command is sent, a sequence is assigned to it so the
corresponding message can be matched. Upon receiving the message, a callback
can be called and/or a completion signaled.

.. _`nvkm_msgqueue`:

struct nvkm_msgqueue
====================

.. c:type:: struct nvkm_msgqueue

    manage a command/message based FW on a falcon

.. _`nvkm_msgqueue.definition`:

Definition
----------

.. code-block:: c

    struct nvkm_msgqueue {
        struct nvkm_falcon *falcon;
        const struct nvkm_msgqueue_func *func;
        u32 fw_version;
        bool init_msg_received;
        struct completion init_done;
        struct mutex seq_lock;
        struct nvkm_msgqueue_seq seq;
        unsigned long seq_tbl;
    }

.. _`nvkm_msgqueue.members`:

Members
-------

falcon
    falcon to be managed

func
    implementation of the firmware to use

fw_version
    *undescribed*

init_msg_received
    whether the init message has already been received

init_done
    whether all init is complete and commands can be processed

seq_lock
    protects seq and seq_tbl

seq
    sequences to match commands and messages

seq_tbl
    bitmap of sequences currently in use

.. This file was automatic generated / don't edit.

