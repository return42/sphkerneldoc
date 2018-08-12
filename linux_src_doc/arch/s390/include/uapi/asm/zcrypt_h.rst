.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/s390/include/uapi/asm/zcrypt.h

.. _`ica_rsa_modexpo`:

struct ica_rsa_modexpo
======================

.. c:type:: struct ica_rsa_modexpo


.. _`ica_rsa_modexpo.definition`:

Definition
----------

.. code-block:: c

    struct ica_rsa_modexpo {
        char __user * inputdata;
        unsigned int inputdatalength;
        char __user * outputdata;
        unsigned int outputdatalength;
        char __user * b_key;
        char __user * n_modulus;
    }

.. _`ica_rsa_modexpo.members`:

Members
-------

inputdata
    *undescribed*

inputdatalength
    *undescribed*

outputdata
    *undescribed*

outputdatalength
    *undescribed*

b_key
    *undescribed*

n_modulus
    *undescribed*

.. _`ica_rsa_modexpo.requirements`:

Requirements
------------

- outputdatalength is at least as large as inputdatalength.
- All key parts are right justified in their fields, padded on
the left with zeroes.
- length(b_key) = inputdatalength
- length(n_modulus) = inputdatalength

.. _`ica_rsa_modexpo_crt`:

struct ica_rsa_modexpo_crt
==========================

.. c:type:: struct ica_rsa_modexpo_crt


.. _`ica_rsa_modexpo_crt.definition`:

Definition
----------

.. code-block:: c

    struct ica_rsa_modexpo_crt {
        char __user * inputdata;
        unsigned int inputdatalength;
        char __user * outputdata;
        unsigned int outputdatalength;
        char __user * bp_key;
        char __user * bq_key;
        char __user * np_prime;
        char __user * nq_prime;
        char __user * u_mult_inv;
    }

.. _`ica_rsa_modexpo_crt.members`:

Members
-------

inputdata
    *undescribed*

inputdatalength
    *undescribed*

outputdata
    *undescribed*

outputdatalength
    *undescribed*

bp_key
    *undescribed*

bq_key
    *undescribed*

np_prime
    *undescribed*

nq_prime
    *undescribed*

u_mult_inv
    *undescribed*

.. _`ica_rsa_modexpo_crt.requirements`:

Requirements
------------

- inputdatalength is even.
- outputdatalength is at least as large as inputdatalength.
- All key parts are right justified in their fields, padded on
the left with zeroes.
- length(bp_key)     = inputdatalength/2 + 8
- length(bq_key)     = inputdatalength/2
- length(np_key)     = inputdatalength/2 + 8
- length(nq_key)     = inputdatalength/2
- length(u_mult_inv) = inputdatalength/2 + 8

.. _`ep11_cprb`:

struct ep11_cprb
================

.. c:type:: struct ep11_cprb

    EP11 connectivity programming request block

.. _`ep11_cprb.definition`:

Definition
----------

.. code-block:: c

    struct ep11_cprb {
        uint16_t cprb_len;
        unsigned char cprb_ver_id;
        unsigned char pad_000[2];
        unsigned char flags;
        unsigned char func_id[2];
        uint32_t source_id;
        uint32_t target_id;
        uint32_t ret_code;
        uint32_t reserved1;
        uint32_t reserved2;
        uint32_t payload_len;
    }

.. _`ep11_cprb.members`:

Members
-------

cprb_len
    CPRB header length [0x0020]

cprb_ver_id
    CPRB version id.   [0x04]

pad_000
    Alignment pad bytes

flags
    Admin cmd [0x80] or functional cmd [0x00]

func_id
    Function id / subtype [0x5434]

source_id
    Source id [originator id]

target_id
    Target id [usage/ctrl domain id]

ret_code
    Return code

reserved1
    Reserved

reserved2
    Reserved

payload_len
    Payload length

.. _`ep11_target_dev`:

struct ep11_target_dev
======================

.. c:type:: struct ep11_target_dev

    EP11 target device list

.. _`ep11_target_dev.definition`:

Definition
----------

.. code-block:: c

    struct ep11_target_dev {
        uint16_t ap_id;
        uint16_t dom_id;
    }

.. _`ep11_target_dev.members`:

Members
-------

ap_id
    AP device id

dom_id
    Usage domain id

.. _`ep11_urb`:

struct ep11_urb
===============

.. c:type:: struct ep11_urb

    EP11 user request block

.. _`ep11_urb.definition`:

Definition
----------

.. code-block:: c

    struct ep11_urb {
        uint16_t targets_num;
        uint64_t targets;
        uint64_t weight;
        uint64_t req_no;
        uint64_t req_len;
        uint64_t req;
        uint64_t resp_len;
        uint64_t resp;
    }

.. _`ep11_urb.members`:

Members
-------

targets_num
    Number of target adapters

targets
    Addr to target adapter list

weight
    Level of request priority

req_no
    Request id/number

req_len
    Request length

req
    Addr to request block

resp_len
    Response length

resp
    Addr to response block

.. _`zcrypt_device_status_ext`:

struct zcrypt_device_status_ext
===============================

.. c:type:: struct zcrypt_device_status_ext


.. _`zcrypt_device_status_ext.definition`:

Definition
----------

.. code-block:: c

    struct zcrypt_device_status_ext {
        unsigned int hwtype:8;
        unsigned int qid:16;
        unsigned int online:1;
        unsigned int functions:6;
        unsigned int reserved:1;
    }

.. _`zcrypt_device_status_ext.members`:

Members
-------

hwtype
    raw hardware type

qid
    8 bit device index, 8 bit domain

online
    *undescribed*

functions
    AP device function bit field 'abcdef'
    a, b, c = reserved
    d = CCA coprocessor
    e = Accelerator
    f = EP11 coprocessor
    \ ``online``\               online status
    \ ``reserved``\             reserved

reserved
    *undescribed*

.. _`icarsamodexpo`:

ICARSAMODEXPO
=============

.. c:function::  ICARSAMODEXPO()

.. _`icarsamodexpo.description`:

Description
-----------

The \ :c:func:`ioctl`\ s which are implemented (along with relevant details)

.. _`icarsamodexpo.are`:

are
---


ICARSAMODEXPO
Perform an RSA operation using a Modulus-Exponent pair
This takes an ica_rsa_modexpo struct as its arg.

.. _`icarsamodexpo.note`:

NOTE
----

please refer to the comments preceding this structure
for the implementation details for the contents of the
block

ICARSACRT
Perform an RSA operation using a Chinese-Remainder Theorem key
This takes an ica_rsa_modexpo_crt struct as its arg.

please refer to the comments preceding this structure
for the implementation details for the contents of the
block

ZSECSENDCPRB
Send an arbitrary CPRB to a crypto card.

ZSENDEP11CPRB
Send an arbitrary EP11 CPRB to an EP11 coprocessor crypto card.

ZCRYPT_DEVICE_STATUS
The given struct zcrypt_device_matrix_ext is updated with
status information for each currently known apqn.

ZCRYPT_STATUS_MASK
Return an MAX_ZDEV_CARDIDS_EXT element array of unsigned chars for the
status of all devices.

.. _`icarsamodexpo.0x01`:

0x01
----

PCICA

.. _`icarsamodexpo.0x02`:

0x02
----

PCICC

.. _`icarsamodexpo.0x03`:

0x03
----

PCIXCC_MCL2

.. _`icarsamodexpo.0x04`:

0x04
----

PCIXCC_MCL3

.. _`icarsamodexpo.0x05`:

0x05
----

CEX2C

.. _`icarsamodexpo.0x06`:

0x06
----

CEX2A

.. _`icarsamodexpo.0x07`:

0x07
----

CEX3C

.. _`icarsamodexpo.0x08`:

0x08
----

CEX3A

.. _`icarsamodexpo.0x0a`:

0x0a
----

CEX4

.. _`icarsamodexpo.0x0b`:

0x0b
----

CEX5

.. _`icarsamodexpo.0x0c`:

0x0c
----

CEX6

.. _`icarsamodexpo.0x0d`:

0x0d
----

device is disabled

ZCRYPT_QDEPTH_MASK
Return an MAX_ZDEV_CARDIDS_EXT element array of unsigned chars for the
queue depth of all devices.

ZCRYPT_PERDEV_REQCNT
Return an MAX_ZDEV_CARDIDS_EXT element array of unsigned integers for
the number of successfully completed requests per device since the
device was detected and made available.

.. This file was automatic generated / don't edit.

