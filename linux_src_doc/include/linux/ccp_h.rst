.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/ccp.h

.. _`ccp_present`:

ccp_present
===========

.. c:function:: int ccp_present( void)

    check if a CCP device is present

    :param  void:
        no arguments

.. _`ccp_present.description`:

Description
-----------

Returns zero if a CCP device is present, -ENODEV otherwise.

.. _`ccp_version`:

ccp_version
===========

.. c:function:: unsigned int ccp_version( void)

    get the version of the CCP

    :param  void:
        no arguments

.. _`ccp_version.description`:

Description
-----------

Returns a positive version number, or zero if no CCP

.. _`ccp_enqueue_cmd`:

ccp_enqueue_cmd
===============

.. c:function:: int ccp_enqueue_cmd(struct ccp_cmd *cmd)

    queue an operation for processing by the CCP

    :param struct ccp_cmd \*cmd:
        ccp_cmd struct to be processed

.. _`ccp_enqueue_cmd.description`:

Description
-----------

Refer to the ccp_cmd struct below for required fields.

Queue a cmd to be processed by the CCP. If queueing the cmd
would exceed the defined length of the cmd queue the cmd will
only be queued if the CCP_CMD_MAY_BACKLOG flag is set and will
result in a return code of -EBUSY.

The callback routine specified in the ccp_cmd struct will be
called to notify the caller of completion (if the cmd was not
backlogged) or advancement out of the backlog. If the cmd has
advanced out of the backlog the "err" value of the callback
will be -EINPROGRESS. Any other "err" value during callback is
the result of the operation.

.. _`ccp_enqueue_cmd.the-cmd-has-been-successfully-queued-if`:

The cmd has been successfully queued if
---------------------------------------

the return code is -EINPROGRESS or
the return code is -EBUSY and CCP_CMD_MAY_BACKLOG flag is set

.. _`ccp_aes_engine`:

struct ccp_aes_engine
=====================

.. c:type:: struct ccp_aes_engine

    CCP AES operation

.. _`ccp_aes_engine.definition`:

Definition
----------

.. code-block:: c

    struct ccp_aes_engine {
        enum ccp_aes_type type;
        enum ccp_aes_mode mode;
        enum ccp_aes_action action;
        struct scatterlist *key;
        u32 key_len;
        struct scatterlist *iv;
        u32 iv_len;
        struct scatterlist *src;
        struct scatterlist * *dst;
        u64 src_len;
        u32 cmac_final;
        struct scatterlist *cmac_key;
        u32 cmac_key_len;
        u32 aad_len;
    }

.. _`ccp_aes_engine.members`:

Members
-------

type
    AES operation key size

mode
    AES operation mode

action
    AES operation (decrypt/encrypt)

key
    key to be used for this AES operation

key_len
    length in bytes of key

iv
    IV to be used for this AES operation

iv_len
    length in bytes of iv

src
    data to be used for this operation

dst
    data produced by this operation

src_len
    length in bytes of data used for this operation

cmac_final
    indicates final operation when running in CMAC mode

cmac_key
    K1/K2 key used in final CMAC operation

cmac_key_len
    length in bytes of cmac_key

aad_len
    *undescribed*

.. _`ccp_aes_engine.description`:

Description
-----------

Variables required to be set when calling \ :c:func:`ccp_enqueue_cmd`\ :
- type, mode, action, key, key_len, src, dst, src_len
- iv, iv_len for any mode other than ECB
- cmac_final for CMAC mode
- cmac_key, cmac_key_len for CMAC mode if cmac_final is non-zero

The iv variable is used as both input and output. On completion of the
AES operation the new IV overwrites the old IV.

.. _`ccp_xts_aes_engine`:

struct ccp_xts_aes_engine
=========================

.. c:type:: struct ccp_xts_aes_engine

    CCP XTS AES operation

.. _`ccp_xts_aes_engine.definition`:

Definition
----------

.. code-block:: c

    struct ccp_xts_aes_engine {
        enum ccp_aes_action action;
        enum ccp_xts_aes_unit_size unit_size;
        struct scatterlist *key;
        u32 key_len;
        struct scatterlist *iv;
        u32 iv_len;
        struct scatterlist *src;
        struct scatterlist * *dst;
        u64 src_len;
        u32 final;
    }

.. _`ccp_xts_aes_engine.members`:

Members
-------

action
    AES operation (decrypt/encrypt)

unit_size
    unit size of the XTS operation

key
    key to be used for this XTS AES operation

key_len
    length in bytes of key

iv
    IV to be used for this XTS AES operation

iv_len
    length in bytes of iv

src
    data to be used for this operation

dst
    data produced by this operation

src_len
    length in bytes of data used for this operation

final
    indicates final XTS operation

.. _`ccp_xts_aes_engine.description`:

Description
-----------

Variables required to be set when calling \ :c:func:`ccp_enqueue_cmd`\ :
- action, unit_size, key, key_len, iv, iv_len, src, dst, src_len, final

The iv variable is used as both input and output. On completion of the
AES operation the new IV overwrites the old IV.

.. _`ccp_sha_engine`:

struct ccp_sha_engine
=====================

.. c:type:: struct ccp_sha_engine

    CCP SHA operation

.. _`ccp_sha_engine.definition`:

Definition
----------

.. code-block:: c

    struct ccp_sha_engine {
        enum ccp_sha_type type;
        struct scatterlist *ctx;
        u32 ctx_len;
        struct scatterlist *src;
        u64 src_len;
        struct scatterlist *opad;
        u32 opad_len;
        u32 first;
        u32 final;
        u64 msg_bits;
    }

.. _`ccp_sha_engine.members`:

Members
-------

type
    Type of SHA operation

ctx
    current hash value

ctx_len
    length in bytes of hash value

src
    data to be used for this operation

src_len
    length in bytes of data used for this operation

opad
    data to be used for final HMAC operation

opad_len
    length in bytes of data used for final HMAC operation

first
    indicates first SHA operation

final
    indicates final SHA operation

msg_bits
    total length of the message in bits used in final SHA operation

.. _`ccp_sha_engine.description`:

Description
-----------

Variables required to be set when calling \ :c:func:`ccp_enqueue_cmd`\ :
- type, ctx, ctx_len, src, src_len, final
- msg_bits if final is non-zero

The ctx variable is used as both input and output. On completion of the
SHA operation the new hash value overwrites the old hash value.

.. _`ccp_des3_engine`:

struct ccp_des3_engine
======================

.. c:type:: struct ccp_des3_engine

    CCP SHA operation

.. _`ccp_des3_engine.definition`:

Definition
----------

.. code-block:: c

    struct ccp_des3_engine {
        enum ccp_des3_type type;
        enum ccp_des3_mode mode;
        enum ccp_des3_action action;
        struct scatterlist *key;
        u32 key_len;
        struct scatterlist *iv;
        u32 iv_len;
        struct scatterlist *src;
        struct scatterlist * *dst;
        u64 src_len;
    }

.. _`ccp_des3_engine.members`:

Members
-------

type
    Type of 3DES operation

mode
    cipher mode

action
    3DES operation (decrypt/encrypt)

key
    key to be used for this 3DES operation

key_len
    length of key (in bytes)

iv
    IV to be used for this AES operation

iv_len
    length in bytes of iv

src
    input data to be used for this operation

dst
    output data produced by this operation

src_len
    length of input data used for this operation (in bytes)

.. _`ccp_des3_engine.description`:

Description
-----------

Variables required to be set when calling \ :c:func:`ccp_enqueue_cmd`\ :
- type, mode, action, key, key_len, src, dst, src_len
- iv, iv_len for any mode other than ECB

The iv variable is used as both input and output. On completion of the
3DES operation the new IV overwrites the old IV.

.. _`ccp_rsa_engine`:

struct ccp_rsa_engine
=====================

.. c:type:: struct ccp_rsa_engine

    CCP RSA operation

.. _`ccp_rsa_engine.definition`:

Definition
----------

.. code-block:: c

    struct ccp_rsa_engine {
        u32 key_size;
        struct scatterlist *exp;
        u32 exp_len;
        struct scatterlist *mod;
        u32 mod_len;
        struct scatterlist *src;
        struct scatterlist * *dst;
        u32 src_len;
    }

.. _`ccp_rsa_engine.members`:

Members
-------

key_size
    length in bits of RSA key

exp
    RSA exponent

exp_len
    length in bytes of exponent

mod
    RSA modulus

mod_len
    length in bytes of modulus

src
    data to be used for this operation

dst
    data produced by this operation

src_len
    length in bytes of data used for this operation

.. _`ccp_rsa_engine.description`:

Description
-----------

Variables required to be set when calling \ :c:func:`ccp_enqueue_cmd`\ :
- key_size, exp, exp_len, mod, mod_len, src, dst, src_len

.. _`ccp_passthru_engine`:

struct ccp_passthru_engine
==========================

.. c:type:: struct ccp_passthru_engine

    CCP pass-through operation

.. _`ccp_passthru_engine.definition`:

Definition
----------

.. code-block:: c

    struct ccp_passthru_engine {
        enum ccp_passthru_bitwise bit_mod;
        enum ccp_passthru_byteswap byte_swap;
        struct scatterlist *mask;
        u32 mask_len;
        struct scatterlist *src;
        struct scatterlist * *dst;
        u64 src_len;
        u32 final;
    }

.. _`ccp_passthru_engine.members`:

Members
-------

bit_mod
    bitwise operation to perform

byte_swap
    byteswap operation to perform

mask
    mask to be applied to data

mask_len
    length in bytes of mask

src
    data to be used for this operation

dst
    data produced by this operation

src_len
    length in bytes of data used for this operation

final
    indicate final pass-through operation

.. _`ccp_passthru_engine.description`:

Description
-----------

Variables required to be set when calling \ :c:func:`ccp_enqueue_cmd`\ :
- bit_mod, byte_swap, src, dst, src_len
- mask, mask_len if bit_mod is not CCP_PASSTHRU_BITWISE_NOOP

.. _`ccp_passthru_nomap_engine`:

struct ccp_passthru_nomap_engine
================================

.. c:type:: struct ccp_passthru_nomap_engine

    CCP pass-through operation without performing DMA mapping

.. _`ccp_passthru_nomap_engine.definition`:

Definition
----------

.. code-block:: c

    struct ccp_passthru_nomap_engine {
        enum ccp_passthru_bitwise bit_mod;
        enum ccp_passthru_byteswap byte_swap;
        dma_addr_t mask;
        u32 mask_len;
        dma_addr_t src_dma;
        dma_addr_t dst_dma;
        u64 src_len;
        u32 final;
    }

.. _`ccp_passthru_nomap_engine.members`:

Members
-------

bit_mod
    bitwise operation to perform

byte_swap
    byteswap operation to perform

mask
    mask to be applied to data

mask_len
    length in bytes of mask

src_dma
    *undescribed*

dst_dma
    *undescribed*

src_len
    length in bytes of data used for this operation

final
    indicate final pass-through operation

.. _`ccp_passthru_nomap_engine.description`:

Description
-----------

Variables required to be set when calling \ :c:func:`ccp_enqueue_cmd`\ :
- bit_mod, byte_swap, src, dst, src_len
- mask, mask_len if bit_mod is not CCP_PASSTHRU_BITWISE_NOOP

.. _`ccp_ecc_modular_math`:

struct ccp_ecc_modular_math
===========================

.. c:type:: struct ccp_ecc_modular_math

    CCP ECC modular math parameters

.. _`ccp_ecc_modular_math.definition`:

Definition
----------

.. code-block:: c

    struct ccp_ecc_modular_math {
        struct scatterlist *operand_1;
        unsigned int operand_1_len;
        struct scatterlist *operand_2;
        unsigned int operand_2_len;
        struct scatterlist *result;
        unsigned int result_len;
    }

.. _`ccp_ecc_modular_math.members`:

Members
-------

operand_1
    first operand for the modular math operation

operand_1_len
    length of the first operand

operand_2
    second operand for the modular math operation
    (not used for CCP_ECC_FUNCTION_MINV_384BIT)

operand_2_len
    length of the second operand
    (not used for CCP_ECC_FUNCTION_MINV_384BIT)

result
    result of the modular math operation

result_len
    length of the supplied result buffer

.. _`ccp_ecc_point`:

struct ccp_ecc_point
====================

.. c:type:: struct ccp_ecc_point

    CCP ECC point definition

.. _`ccp_ecc_point.definition`:

Definition
----------

.. code-block:: c

    struct ccp_ecc_point {
        struct scatterlist *x;
        unsigned int x_len;
        struct scatterlist *y;
        unsigned int y_len;
    }

.. _`ccp_ecc_point.members`:

Members
-------

x
    the x coordinate of the ECC point

x_len
    the length of the x coordinate

y
    the y coordinate of the ECC point

y_len
    the length of the y coordinate

.. _`ccp_ecc_point_math`:

struct ccp_ecc_point_math
=========================

.. c:type:: struct ccp_ecc_point_math

    CCP ECC point math parameters

.. _`ccp_ecc_point_math.definition`:

Definition
----------

.. code-block:: c

    struct ccp_ecc_point_math {
        struct ccp_ecc_point point_1;
        struct ccp_ecc_point point_2;
        struct scatterlist *domain_a;
        unsigned int domain_a_len;
        struct scatterlist *scalar;
        unsigned int scalar_len;
        struct ccp_ecc_point result;
    }

.. _`ccp_ecc_point_math.members`:

Members
-------

point_1
    the first point of the ECC point math operation

point_2
    the second point of the ECC point math operation
    (only used for CCP_ECC_FUNCTION_PADD_384BIT)

domain_a
    the a parameter of the ECC curve

domain_a_len
    the length of the a parameter

scalar
    the scalar parameter for the point match operation
    (only used for CCP_ECC_FUNCTION_PMUL_384BIT)

scalar_len
    the length of the scalar parameter
    (only used for CCP_ECC_FUNCTION_PMUL_384BIT)

result
    the point resulting from the point math operation

.. _`ccp_ecc_engine`:

struct ccp_ecc_engine
=====================

.. c:type:: struct ccp_ecc_engine

    CCP ECC operation

.. _`ccp_ecc_engine.definition`:

Definition
----------

.. code-block:: c

    struct ccp_ecc_engine {
        enum ccp_ecc_function function;
        struct scatterlist *mod;
        u32 mod_len;
        union u;
        u16 ecc_result;
    }

.. _`ccp_ecc_engine.members`:

Members
-------

function
    ECC function to perform

mod
    ECC modulus

mod_len
    length in bytes of modulus

u
    *undescribed*

ecc_result
    result of the ECC operation

.. _`ccp_ecc_engine.description`:

Description
-----------

Variables required to be set when calling \ :c:func:`ccp_enqueue_cmd`\ :
- function, mod, mod_len
- operand, operand_len, operand_count, output, output_len, output_count
- ecc_result

.. _`ccp_cmd`:

struct ccp_cmd
==============

.. c:type:: struct ccp_cmd

    CCP operation request

.. _`ccp_cmd.definition`:

Definition
----------

.. code-block:: c

    struct ccp_cmd {
        struct list_head entry;
        struct work_struct work;
        struct ccp_device *ccp;
        int ret;
        u32 flags;
        enum ccp_engine engine;
        u32 engine_error;
        union u;
        void (*callback)(void *data, int err);
        void *data;
    }

.. _`ccp_cmd.members`:

Members
-------

entry
    list element (ccp driver use only)

work
    work element used for callbacks (ccp driver use only)

ccp
    CCP device to be run on

ret
    operation return code (ccp driver use only)

flags
    cmd processing flags

engine
    CCP operation to perform

engine_error
    CCP engine return code

u
    engine specific structures, refer to specific engine struct below

callback
    operation completion callback function

data
    parameter value to be supplied to the callback function

.. _`ccp_cmd.description`:

Description
-----------

Variables required to be set when calling \ :c:func:`ccp_enqueue_cmd`\ :
- engine, callback
- See the operation structures below for what is required for each
operation.

.. This file was automatic generated / don't edit.

