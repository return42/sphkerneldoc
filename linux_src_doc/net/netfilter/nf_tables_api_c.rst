.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/netfilter/nf_tables_api.c

.. _`nft_register_expr`:

nft_register_expr
=================

.. c:function:: int nft_register_expr(struct nft_expr_type *type)

    register nf_tables expr type

    :param type:
        *undescribed*
    :type type: struct nft_expr_type \*

.. _`nft_register_expr.description`:

Description
-----------

Registers the expr type for use with nf_tables. Returns zero on
success or a negative errno code otherwise.

.. _`nft_unregister_expr`:

nft_unregister_expr
===================

.. c:function:: void nft_unregister_expr(struct nft_expr_type *type)

    unregister nf_tables expr type

    :param type:
        *undescribed*
    :type type: struct nft_expr_type \*

.. _`nft_unregister_expr.description`:

Description
-----------

Unregisters the expr typefor use with nf_tables.

.. _`nft_data_hold`:

nft_data_hold
=============

.. c:function:: void nft_data_hold(const struct nft_data *data, enum nft_data_types type)

    hold a nft_data item

    :param data:
        struct nft_data to release
    :type data: const struct nft_data \*

    :param type:
        type of data
    :type type: enum nft_data_types

.. _`nft_data_hold.description`:

Description
-----------

Hold a nft_data item. NFT_DATA_VALUE types can be silently discarded,
NFT_DATA_VERDICT bumps the reference to chains in case of NFT_JUMP and
NFT_GOTO verdicts. This function must be called on active data objects
from the second phase of the commit protocol.

.. _`nft_register_obj`:

nft_register_obj
================

.. c:function:: int nft_register_obj(struct nft_object_type *obj_type)

    register nf_tables stateful object type

    :param obj_type:
        *undescribed*
    :type obj_type: struct nft_object_type \*

.. _`nft_register_obj.description`:

Description
-----------

Registers the object type for use with nf_tables. Returns zero on
success or a negative errno code otherwise.

.. _`nft_unregister_obj`:

nft_unregister_obj
==================

.. c:function:: void nft_unregister_obj(struct nft_object_type *obj_type)

    unregister nf_tables object type

    :param obj_type:
        *undescribed*
    :type obj_type: struct nft_object_type \*

.. _`nft_unregister_obj.description`:

Description
-----------

Unregisters the object type for use with nf_tables.

.. _`nft_parse_u32_check`:

nft_parse_u32_check
===================

.. c:function:: int nft_parse_u32_check(const struct nlattr *attr, int max, u32 *dest)

    fetch u32 attribute and check for maximum value

    :param attr:
        netlink attribute to fetch value from
    :type attr: const struct nlattr \*

    :param max:
        maximum value to be stored in dest
    :type max: int

    :param dest:
        pointer to the variable
    :type dest: u32 \*

.. _`nft_parse_u32_check.description`:

Description
-----------

Parse, check and store a given u32 netlink attribute into variable.
This function returns -ERANGE if the value goes over maximum value.
Otherwise a 0 is returned and the attribute value is stored in the
destination variable.

.. _`nft_parse_register`:

nft_parse_register
==================

.. c:function:: unsigned int nft_parse_register(const struct nlattr *attr)

    parse a register value from a netlink attribute

    :param attr:
        netlink attribute
    :type attr: const struct nlattr \*

.. _`nft_parse_register.description`:

Description
-----------

Parse and translate a register value from a netlink attribute.
Registers used to be 128 bit wide, these register numbers will be
mapped to the corresponding 32 bit register numbers.

.. _`nft_dump_register`:

nft_dump_register
=================

.. c:function:: int nft_dump_register(struct sk_buff *skb, unsigned int attr, unsigned int reg)

    dump a register value to a netlink attribute

    :param skb:
        socket buffer
    :type skb: struct sk_buff \*

    :param attr:
        attribute number
    :type attr: unsigned int

    :param reg:
        register number
    :type reg: unsigned int

.. _`nft_dump_register.description`:

Description
-----------

Construct a netlink attribute containing the register number. For
compatibility reasons, register numbers being a multiple of 4 are
translated to the corresponding 128 bit register numbers.

.. _`nft_validate_register_load`:

nft_validate_register_load
==========================

.. c:function:: int nft_validate_register_load(enum nft_registers reg, unsigned int len)

    validate a load from a register

    :param reg:
        the register number
    :type reg: enum nft_registers

    :param len:
        the length of the data
    :type len: unsigned int

.. _`nft_validate_register_load.description`:

Description
-----------

Validate that the input register is one of the general purpose
registers and that the length of the load is within the bounds.

.. _`nft_validate_register_store`:

nft_validate_register_store
===========================

.. c:function:: int nft_validate_register_store(const struct nft_ctx *ctx, enum nft_registers reg, const struct nft_data *data, enum nft_data_types type, unsigned int len)

    validate an expressions' register store

    :param ctx:
        context of the expression performing the load
    :type ctx: const struct nft_ctx \*

    :param reg:
        the destination register number
    :type reg: enum nft_registers

    :param data:
        the data to load
    :type data: const struct nft_data \*

    :param type:
        the data type
    :type type: enum nft_data_types

    :param len:
        the length of the data
    :type len: unsigned int

.. _`nft_validate_register_store.description`:

Description
-----------

Validate that a data load uses the appropriate data type for
the destination register and the length is within the bounds.
A value of NULL for the data means that its runtime gathered
data.

.. _`nft_data_init`:

nft_data_init
=============

.. c:function:: int nft_data_init(const struct nft_ctx *ctx, struct nft_data *data, unsigned int size, struct nft_data_desc *desc, const struct nlattr *nla)

    parse nf_tables data netlink attributes

    :param ctx:
        context of the expression using the data
    :type ctx: const struct nft_ctx \*

    :param data:
        destination struct nft_data
    :type data: struct nft_data \*

    :param size:
        maximum data length
    :type size: unsigned int

    :param desc:
        data description
    :type desc: struct nft_data_desc \*

    :param nla:
        netlink attribute containing data
    :type nla: const struct nlattr \*

.. _`nft_data_init.description`:

Description
-----------

Parse the netlink data attributes and initialize a struct nft_data.
The type and length of data are returned in the data description.

The caller can indicate that it only wants to accept data of type
NFT_DATA_VALUE by passing NULL for the ctx argument.

.. _`nft_data_release`:

nft_data_release
================

.. c:function:: void nft_data_release(const struct nft_data *data, enum nft_data_types type)

    release a nft_data item

    :param data:
        struct nft_data to release
    :type data: const struct nft_data \*

    :param type:
        type of data
    :type type: enum nft_data_types

.. _`nft_data_release.description`:

Description
-----------

Release a nft_data item. NFT_DATA_VALUE types can be silently discarded,
all others need to be released by calling this function.

.. This file was automatic generated / don't edit.

