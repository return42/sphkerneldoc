.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/rave-sp.c

.. _`rave_sp_deframer_state`:

enum rave_sp_deframer_state
===========================

.. c:type:: enum rave_sp_deframer_state

    Possible state for de-framer

.. _`rave_sp_deframer_state.definition`:

Definition
----------

.. code-block:: c

    enum rave_sp_deframer_state {
        RAVE_SP_EXPECT_SOF,
        RAVE_SP_EXPECT_DATA,
        RAVE_SP_EXPECT_ESCAPED_DATA
    };

.. _`rave_sp_deframer_state.constants`:

Constants
---------

RAVE_SP_EXPECT_SOF
    Scanning input for start-of-frame marker

RAVE_SP_EXPECT_DATA
    Got start of frame marker, collecting frame

RAVE_SP_EXPECT_ESCAPED_DATA
    Got escape character, collecting escaped byte

.. _`rave_sp_deframer`:

struct rave_sp_deframer
=======================

.. c:type:: struct rave_sp_deframer

    Device protocol deframer

.. _`rave_sp_deframer.definition`:

Definition
----------

.. code-block:: c

    struct rave_sp_deframer {
        enum rave_sp_deframer_state state;
        unsigned char data[RAVE_SP_RX_BUFFER_SIZE];
        size_t length;
    }

.. _`rave_sp_deframer.members`:

Members
-------

state
    Current state of the deframer

data
    Buffer used to collect deframed data

length
    Number of bytes de-framed so far

.. _`rave_sp_reply`:

struct rave_sp_reply
====================

.. c:type:: struct rave_sp_reply

    Reply as per RAVE device protocol

.. _`rave_sp_reply.definition`:

Definition
----------

.. code-block:: c

    struct rave_sp_reply {
        size_t length;
        void *data;
        u8 code;
        u8 ackid;
        struct completion received;
    }

.. _`rave_sp_reply.members`:

Members
-------

length
    Expected reply length

data
    Buffer to store reply payload in

code
    Expected reply code

ackid
    Expected reply ACK ID

received
    *undescribed*

.. _`rave_sp_checksum`:

struct rave_sp_checksum
=======================

.. c:type:: struct rave_sp_checksum

    Variant specific checksum implementation details

.. _`rave_sp_checksum.definition`:

Definition
----------

.. code-block:: c

    struct rave_sp_checksum {
        size_t length;
        void (*subroutine)(const u8 *, size_t, u8 *);
    }

.. _`rave_sp_checksum.members`:

Members
-------

length
    Caculated checksum length

subroutine
    Utilized checksum algorithm implementation

.. _`rave_sp_variant_cmds`:

struct rave_sp_variant_cmds
===========================

.. c:type:: struct rave_sp_variant_cmds

    Variant specific command routines

.. _`rave_sp_variant_cmds.definition`:

Definition
----------

.. code-block:: c

    struct rave_sp_variant_cmds {
        int (*translate)(enum rave_sp_command);
    }

.. _`rave_sp_variant_cmds.members`:

Members
-------

translate
    Generic to variant specific command mapping routine

.. _`rave_sp_variant`:

struct rave_sp_variant
======================

.. c:type:: struct rave_sp_variant

    RAVE supervisory processor core variant

.. _`rave_sp_variant.definition`:

Definition
----------

.. code-block:: c

    struct rave_sp_variant {
        const struct rave_sp_checksum *checksum;
        struct rave_sp_variant_cmds cmd;
    }

.. _`rave_sp_variant.members`:

Members
-------

checksum
    Variant specific checksum implementation

cmd
    Variant specific command pointer table

.. _`rave_sp`:

struct rave_sp
==============

.. c:type:: struct rave_sp

    RAVE supervisory processor core

.. _`rave_sp.definition`:

Definition
----------

.. code-block:: c

    struct rave_sp {
        struct serdev_device *serdev;
        struct rave_sp_deframer deframer;
        atomic_t ackid;
        struct mutex bus_lock;
        struct mutex reply_lock;
        struct rave_sp_reply *reply;
        const struct rave_sp_variant *variant;
        struct blocking_notifier_head event_notifier_list;
        const char *part_number_firmware;
        const char *part_number_bootloader;
    }

.. _`rave_sp.members`:

Members
-------

serdev
    Pointer to underlying serdev

deframer
    Stored state of the protocol deframer

ackid
    ACK ID used in last reply sent to the device

bus_lock
    Lock to serialize access to the device

reply_lock
    Lock protecting \ ``reply``\ 

reply
    Pointer to memory to store reply payload

variant
    Device variant specific information

event_notifier_list
    Input event notification chain

part_number_firmware
    Firmware version

part_number_bootloader
    Bootloader version

.. This file was automatic generated / don't edit.

