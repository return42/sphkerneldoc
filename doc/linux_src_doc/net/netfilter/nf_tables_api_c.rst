.. -*- coding: utf-8; mode: rst -*-

===============
nf_tables_api.c
===============


.. _`nft_register_afinfo`:

nft_register_afinfo
===================

.. c:function:: int nft_register_afinfo (struct net *net, struct nft_af_info *afi)

    register nf_tables address family info

    :param struct net \*net:

        *undescribed*

    :param struct nft_af_info \*afi:
        address family info to register



.. _`nft_register_afinfo.description`:

Description
-----------

Register the address family for use with nf_tables. Returns zero on
success or a negative errno code otherwise.



.. _`nft_unregister_afinfo`:

nft_unregister_afinfo
=====================

.. c:function:: void nft_unregister_afinfo (struct net *net, struct nft_af_info *afi)

    unregister nf_tables address family info

    :param struct net \*net:

        *undescribed*

    :param struct nft_af_info \*afi:
        address family info to unregister



.. _`nft_unregister_afinfo.description`:

Description
-----------

Unregister the address family for use with nf_tables.



.. _`nft_register_expr`:

nft_register_expr
=================

.. c:function:: int nft_register_expr (struct nft_expr_type *type)

    register nf_tables expr type

    :param struct nft_expr_type \*type:

        *undescribed*



.. _`nft_register_expr.description`:

Description
-----------

Registers the expr type for use with nf_tables. Returns zero on
success or a negative errno code otherwise.



.. _`nft_unregister_expr`:

nft_unregister_expr
===================

.. c:function:: void nft_unregister_expr (struct nft_expr_type *type)

    unregister nf_tables expr type

    :param struct nft_expr_type \*type:

        *undescribed*



.. _`nft_unregister_expr.description`:

Description
-----------

Unregisters the expr typefor use with nf_tables.



.. _`nft_parse_register`:

nft_parse_register
==================

.. c:function:: unsigned int nft_parse_register (const struct nlattr *attr)

    parse a register value from a netlink attribute

    :param const struct nlattr \*attr:
        netlink attribute



.. _`nft_parse_register.description`:

Description
-----------

Parse and translate a register value from a netlink attribute.
Registers used to be 128 bit wide, these register numbers will be
mapped to the corresponding 32 bit register numbers.



.. _`nft_dump_register`:

nft_dump_register
=================

.. c:function:: int nft_dump_register (struct sk_buff *skb, unsigned int attr, unsigned int reg)

    dump a register value to a netlink attribute

    :param struct sk_buff \*skb:
        socket buffer

    :param unsigned int attr:
        attribute number

    :param unsigned int reg:
        register number



.. _`nft_dump_register.description`:

Description
-----------

Construct a netlink attribute containing the register number. For
compatibility reasons, register numbers being a multiple of 4 are
translated to the corresponding 128 bit register numbers.



.. _`nft_validate_register_load`:

nft_validate_register_load
==========================

.. c:function:: int nft_validate_register_load (enum nft_registers reg, unsigned int len)

    validate a load from a register

    :param enum nft_registers reg:
        the register number

    :param unsigned int len:
        the length of the data



.. _`nft_validate_register_load.description`:

Description
-----------

Validate that the input register is one of the general purpose
registers and that the length of the load is within the bounds.



.. _`nft_validate_register_store`:

nft_validate_register_store
===========================

.. c:function:: int nft_validate_register_store (const struct nft_ctx *ctx, enum nft_registers reg, const struct nft_data *data, enum nft_data_types type, unsigned int len)

    validate an expressions' register store

    :param const struct nft_ctx \*ctx:
        context of the expression performing the load

    :param enum nft_registers reg:
        the destination register number

    :param const struct nft_data \*data:
        the data to load

    :param enum nft_data_types type:
        the data type

    :param unsigned int len:
        the length of the data



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

.. c:function:: int nft_data_init (const struct nft_ctx *ctx, struct nft_data *data, unsigned int size, struct nft_data_desc *desc, const struct nlattr *nla)

    parse nf_tables data netlink attributes

    :param const struct nft_ctx \*ctx:
        context of the expression using the data

    :param struct nft_data \*data:
        destination struct nft_data

    :param unsigned int size:
        maximum data length

    :param struct nft_data_desc \*desc:
        data description

    :param const struct nlattr \*nla:
        netlink attribute containing data



.. _`nft_data_init.description`:

Description
-----------

Parse the netlink data attributes and initialize a struct nft_data.
The type and length of data are returned in the data description.

The caller can indicate that it only wants to accept data of type
NFT_DATA_VALUE by passing NULL for the ctx argument.



.. _`nft_data_uninit`:

nft_data_uninit
===============

.. c:function:: void nft_data_uninit (const struct nft_data *data, enum nft_data_types type)

    release a nft_data item

    :param const struct nft_data \*data:
        struct nft_data to release

    :param enum nft_data_types type:
        type of data



.. _`nft_data_uninit.description`:

Description
-----------

Release a nft_data item. NFT_DATA_VALUE types can be silently discarded,
all others need to be released by calling this function.

