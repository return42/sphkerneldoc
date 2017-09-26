.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/cavium/nitrox/nitrox_req.h

.. _`gphdr`:

struct gphdr
============

.. c:type:: struct gphdr

    General purpose Header

.. _`gphdr.definition`:

Definition
----------

.. code-block:: c

    struct gphdr {
        __be16 param0;
        __be16 param1;
        __be16 param2;
        __be16 param3;
    }

.. _`gphdr.members`:

Members
-------

param0
    first parameter.

param1
    second parameter.

param2
    third parameter.

param3
    fourth parameter.

.. _`gphdr.description`:

Description
-----------

Params tell the iv and enc/dec data offsets.

.. _`se_crypto_request`:

struct se_crypto_request
========================

.. c:type:: struct se_crypto_request

    SE crypto request structure.

.. _`se_crypto_request.definition`:

Definition
----------

.. code-block:: c

    struct se_crypto_request {
        u8 opcode;
        gfp_t gfp;
        u32 flags;
        u64 ctx_handle;
        struct gphdr gph;
        union se_req_ctrl ctrl;
        u8 iv[MAX_IV_LEN];
        u16 ivsize;
        struct scatterlist *src;
        struct scatterlist *dst;
    }

.. _`se_crypto_request.members`:

Members
-------

opcode
    Request opcode (enc/dec)

gfp
    *undescribed*

flags
    flags from crypto subsystem

ctx_handle
    Crypto context handle.

gph
    GP Header

ctrl
    Request Information.

iv
    *undescribed*

ivsize
    *undescribed*

src
    *undescribed*

dst
    *undescribed*

.. _`crypto_keys`:

struct crypto_keys
==================

.. c:type:: struct crypto_keys

    Crypto keys

.. _`crypto_keys.definition`:

Definition
----------

.. code-block:: c

    struct crypto_keys {
        union {
            u8 key[AES_MAX_KEY_SIZE];
            u8 key1[AES_MAX_KEY_SIZE];
        } u;
        u8 iv[AES_BLOCK_SIZE];
    }

.. _`crypto_keys.members`:

Members
-------

u
    *undescribed*

iv
    Encryption IV or Tweak for AES-XTS

.. _`auth_keys`:

struct auth_keys
================

.. c:type:: struct auth_keys

    Authentication keys

.. _`auth_keys.definition`:

Definition
----------

.. code-block:: c

    struct auth_keys {
        union {
            u8 ipad[64];
            u8 key2[64];
        } u;
        u8 opad[64];
    }

.. _`auth_keys.members`:

Members
-------

u
    *undescribed*

opad
    OPAD or AUTH KEY if auth_input_type = 1

.. _`flexi_crypto_context`:

struct flexi_crypto_context
===========================

.. c:type:: struct flexi_crypto_context

    Crypto context

.. _`flexi_crypto_context.definition`:

Definition
----------

.. code-block:: c

    struct flexi_crypto_context {
        union {
            __be64 flags;
            struct {
    #if defined(__BIG_ENDIAN_BITFIELD)
                u64 cipher_type : 4;
                u64 reserved_59 : 1;
                u64 aes_keylen : 2;
                u64 iv_source : 1;
                u64 hash_type : 4;
                u64 reserved_49_51 : 3;
                u64 auth_input_type: 1;
                u64 mac_len : 8;
                u64 reserved_0_39 : 40;
    #else
                u64 reserved_0_39 : 40;
                u64 mac_len : 8;
                u64 auth_input_type: 1;
                u64 reserved_49_51 : 3;
                u64 hash_type : 4;
                u64 iv_source : 1;
                u64 aes_keylen : 2;
                u64 reserved_59 : 1;
                u64 cipher_type : 4;
    #endif
            } w0;
        } ;
        struct crypto_keys crypto;
        struct auth_keys auth;
    }

.. _`flexi_crypto_context.members`:

Members
-------

{unnamed_union}
    anonymous

flags
    *undescribed*

w0
    *undescribed*

crypto
    Crypto keys

auth
    Authentication keys

.. _`nps_pkt_instr`:

struct nps_pkt_instr
====================

.. c:type:: struct nps_pkt_instr

    NPS Packet Instruction of SE cores.

.. _`nps_pkt_instr.definition`:

Definition
----------

.. code-block:: c

    struct nps_pkt_instr {
        __be64 dptr0;
        union pkt_instr_hdr ih;
        union pkt_hdr irh;
        union slc_store_info slc;
        u64 fdata[2];
    }

.. _`nps_pkt_instr.members`:

Members
-------

dptr0
    Input pointer points to buffer in remote host.

ih
    Packet Instruction Header (8 bytes)

irh
    Packet Input Header (16 bytes)

slc
    Solicited Packet Output Store Information (16 bytes)

fdata
    Front data

.. _`nps_pkt_instr.description`:

Description
-----------

64-Byte Instruction Format

.. _`ctx_hdr`:

struct ctx_hdr
==============

.. c:type:: struct ctx_hdr

    Book keeping data about the crypto context

.. _`ctx_hdr.definition`:

Definition
----------

.. code-block:: c

    struct ctx_hdr {
        struct dma_pool *pool;
        dma_addr_t dma;
        dma_addr_t ctx_dma;
    }

.. _`ctx_hdr.members`:

Members
-------

pool
    Pool used to allocate crypto context

dma
    Base DMA address of the cypto context

ctx_dma
    Actual usable crypto context for NITROX

.. _`nitrox_softreq`:

struct nitrox_softreq
=====================

.. c:type:: struct nitrox_softreq

    Represents the NIROX Request.

.. _`nitrox_softreq.definition`:

Definition
----------

.. code-block:: c

    struct nitrox_softreq {
        struct list_head response;
        struct list_head backlog;
        u32 flags;
        gfp_t gfp;
        atomic_t status;
        bool inplace;
        struct nitrox_device *ndev;
        struct nitrox_cmdq *cmdq;
        struct nps_pkt_instr instr;
        struct resp_hdr resp;
        struct nitrox_sgtable in;
        struct nitrox_sgtable out;
        unsigned long tstamp;
        completion_t callback;
        struct skcipher_request *skreq;
    }

.. _`nitrox_softreq.members`:

Members
-------

response
    response list entry

backlog
    Backlog list entry

flags
    *undescribed*

gfp
    *undescribed*

status
    *undescribed*

inplace
    *undescribed*

ndev
    Device used to submit the request

cmdq
    Command queue for submission

instr
    64B instruction

resp
    Response headers

in
    SG table for input
    \ ``out``\  SG table for output

out
    *undescribed*

tstamp
    Request submitted time in jiffies

callback
    callback after request completion/timeout

skreq
    *undescribed*

.. This file was automatic generated / don't edit.

