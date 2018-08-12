.. -*- coding: utf-8; mode: rst -*-
.. src-file: tools/include/uapi/linux/lirc.h

.. _`rc_proto`:

enum rc_proto
=============

.. c:type:: enum rc_proto

    the Remote Controller protocol

.. _`rc_proto.definition`:

Definition
----------

.. code-block:: c

    enum rc_proto {
        RC_PROTO_UNKNOWN,
        RC_PROTO_OTHER,
        RC_PROTO_RC5,
        RC_PROTO_RC5X_20,
        RC_PROTO_RC5_SZ,
        RC_PROTO_JVC,
        RC_PROTO_SONY12,
        RC_PROTO_SONY15,
        RC_PROTO_SONY20,
        RC_PROTO_NEC,
        RC_PROTO_NECX,
        RC_PROTO_NEC32,
        RC_PROTO_SANYO,
        RC_PROTO_MCIR2_KBD,
        RC_PROTO_MCIR2_MSE,
        RC_PROTO_RC6_0,
        RC_PROTO_RC6_6A_20,
        RC_PROTO_RC6_6A_24,
        RC_PROTO_RC6_6A_32,
        RC_PROTO_RC6_MCE,
        RC_PROTO_SHARP,
        RC_PROTO_XMP,
        RC_PROTO_CEC,
        RC_PROTO_IMON
    };

.. _`rc_proto.constants`:

Constants
---------

RC_PROTO_UNKNOWN
    Protocol not known

RC_PROTO_OTHER
    Protocol known but proprietary

RC_PROTO_RC5
    Philips RC5 protocol

RC_PROTO_RC5X_20
    Philips RC5x 20 bit protocol

RC_PROTO_RC5_SZ
    StreamZap variant of RC5

RC_PROTO_JVC
    JVC protocol

RC_PROTO_SONY12
    Sony 12 bit protocol

RC_PROTO_SONY15
    Sony 15 bit protocol

RC_PROTO_SONY20
    Sony 20 bit protocol

RC_PROTO_NEC
    NEC protocol

RC_PROTO_NECX
    Extended NEC protocol

RC_PROTO_NEC32
    NEC 32 bit protocol

RC_PROTO_SANYO
    Sanyo protocol

RC_PROTO_MCIR2_KBD
    RC6-ish MCE keyboard

RC_PROTO_MCIR2_MSE
    RC6-ish MCE mouse

RC_PROTO_RC6_0
    Philips RC6-0-16 protocol

RC_PROTO_RC6_6A_20
    Philips RC6-6A-20 protocol

RC_PROTO_RC6_6A_24
    Philips RC6-6A-24 protocol

RC_PROTO_RC6_6A_32
    Philips RC6-6A-32 protocol

RC_PROTO_RC6_MCE
    MCE (Philips RC6-6A-32 subtype) protocol

RC_PROTO_SHARP
    Sharp protocol

RC_PROTO_XMP
    XMP protocol

RC_PROTO_CEC
    CEC protocol

RC_PROTO_IMON
    iMon Pad protocol

.. This file was automatic generated / don't edit.

