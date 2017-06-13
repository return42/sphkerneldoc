.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_cpp.h

.. _`nfp_cpp_id`:

NFP_CPP_ID
==========

.. c:function::  NFP_CPP_ID( target,  action,  token)

    pack target, token, and action into a CPP ID.

    :param  target:
        NFP CPP target id

    :param  action:
        NFP CPP action id

    :param  token:
        NFP CPP token id

.. _`nfp_cpp_id.description`:

Description
-----------

Create a 32-bit CPP identifier representing the access to be made.
These identifiers are used as parameters to other NFP CPP
functions.  Some CPP devices may allow wildcard identifiers to be
specified.

.. _`nfp_cpp_id.return`:

Return
------

NFP CPP ID

.. _`nfp_cpp_island_id`:

NFP_CPP_ISLAND_ID
=================

.. c:function::  NFP_CPP_ISLAND_ID( target,  action,  token,  island)

    pack target, token, action, and island into a CPP ID.

    :param  target:
        NFP CPP target id

    :param  action:
        NFP CPP action id

    :param  token:
        NFP CPP token id

    :param  island:
        NFP CPP island id

.. _`nfp_cpp_island_id.description`:

Description
-----------

Create a 32-bit CPP identifier representing the access to be made.
These identifiers are used as parameters to other NFP CPP
functions.  Some CPP devices may allow wildcard identifiers to be
specified.

.. _`nfp_cpp_island_id.return`:

Return
------

NFP CPP ID

.. _`nfp_cpp_id_target_of`:

NFP_CPP_ID_TARGET_of
====================

.. c:function:: u8 NFP_CPP_ID_TARGET_of(u32 id)

    Return the NFP CPP target of a NFP CPP ID

    :param u32 id:
        NFP CPP ID

.. _`nfp_cpp_id_target_of.return`:

Return
------

NFP CPP target

.. _`nfp_cpp_id_token_of`:

NFP_CPP_ID_TOKEN_of
===================

.. c:function:: u8 NFP_CPP_ID_TOKEN_of(u32 id)

    Return the NFP CPP token of a NFP CPP ID

    :param u32 id:
        NFP CPP ID

.. _`nfp_cpp_id_token_of.return`:

Return
------

NFP CPP token

.. _`nfp_cpp_id_action_of`:

NFP_CPP_ID_ACTION_of
====================

.. c:function:: u8 NFP_CPP_ID_ACTION_of(u32 id)

    Return the NFP CPP action of a NFP CPP ID

    :param u32 id:
        NFP CPP ID

.. _`nfp_cpp_id_action_of.return`:

Return
------

NFP CPP action

.. _`nfp_cpp_id_island_of`:

NFP_CPP_ID_ISLAND_of
====================

.. c:function:: u8 NFP_CPP_ID_ISLAND_of(u32 id)

    Return the NFP CPP island of a NFP CPP ID

    :param u32 id:
        NFP CPP ID

.. _`nfp_cpp_id_island_of.return`:

Return
------

NFP CPP island

.. _`nfp_cpp_interface`:

NFP_CPP_INTERFACE
=================

.. c:function::  NFP_CPP_INTERFACE( type,  unit,  channel)

    Construct a 16-bit NFP Interface ID

    :param  type:
        NFP Interface Type

    :param  unit:
        Unit identifier for the interface type

    :param  channel:
        Channel identifier for the interface unit

.. _`nfp_cpp_interface.description`:

Description
-----------

Interface IDs consists of 4 bits of interface type,
4 bits of unit identifier, and 8 bits of channel identifier.

The NFP Interface ID is used in the implementation of
NFP CPP API mutexes, which use the MU Atomic CompareAndWrite
operation - hence the limit to 16 bits to be able to
use the NFP Interface ID as a lock owner.

.. _`nfp_cpp_interface.return`:

Return
------

Interface ID

.. _`nfp_cpp_interface_type_of`:

NFP_CPP_INTERFACE_TYPE_of
=========================

.. c:function::  NFP_CPP_INTERFACE_TYPE_of( interface)

    Get the interface type

    :param  interface:
        NFP Interface ID

.. _`nfp_cpp_interface_type_of.return`:

Return
------

NFP Interface ID's type

.. _`nfp_cpp_interface_unit_of`:

NFP_CPP_INTERFACE_UNIT_of
=========================

.. c:function::  NFP_CPP_INTERFACE_UNIT_of( interface)

    Get the interface unit

    :param  interface:
        NFP Interface ID

.. _`nfp_cpp_interface_unit_of.return`:

Return
------

NFP Interface ID's unit

.. _`nfp_cpp_interface_channel_of`:

NFP_CPP_INTERFACE_CHANNEL_of
============================

.. c:function::  NFP_CPP_INTERFACE_CHANNEL_of( interface)

    Get the interface channel

    :param  interface:
        NFP Interface ID

.. _`nfp_cpp_interface_channel_of.return`:

Return
------

NFP Interface ID's channel

.. _`nfp_cpp_operations`:

struct nfp_cpp_operations
=========================

.. c:type:: struct nfp_cpp_operations

    NFP CPP operations structure

.. _`nfp_cpp_operations.definition`:

Definition
----------

.. code-block:: c

    struct nfp_cpp_operations {
        size_t area_priv_size;
        struct module *owner;
        int (*init)(struct nfp_cpp *cpp);
        void (*free)(struct nfp_cpp *cpp);
        void (*read_serial)(struct device *dev, u8 *serial);
        u16 (*get_interface)(struct device *dev);
        int (*area_init)(struct nfp_cpp_area *area,u32 dest, unsigned long long address, unsigned long size);
        void (*area_cleanup)(struct nfp_cpp_area *area);
        int (*area_acquire)(struct nfp_cpp_area *area);
        void (*area_release)(struct nfp_cpp_area *area);
        struct resource *(*area_resource)(struct nfp_cpp_area *area);
        phys_addr_t (*area_phys)(struct nfp_cpp_area *area);
        void __iomem *(*area_iomem)(struct nfp_cpp_area *area);
        int (*area_read)(struct nfp_cpp_area *area, void *kernel_vaddr, unsigned long offset, unsigned int length);
        int (*area_write)(struct nfp_cpp_area *area, const void *kernel_vaddr, unsigned long offset, unsigned int length);
        size_t explicit_priv_size;
        int (*explicit_acquire)(struct nfp_cpp_explicit *expl);
        void (*explicit_release)(struct nfp_cpp_explicit *expl);
        int (*explicit_put)(struct nfp_cpp_explicit *expl, const void *buff, size_t len);
        int (*explicit_get)(struct nfp_cpp_explicit *expl, void *buff, size_t len);
        int (*explicit_do)(struct nfp_cpp_explicit *expl,const struct nfp_cpp_explicit_command *cmd, u64 address);
    }

.. _`nfp_cpp_operations.members`:

Members
-------

area_priv_size
    Size of the nfp_cpp_area private data

owner
    Owner module

init
    Initialize the NFP CPP bus

free
    Free the bus

read_serial
    Read serial number to memory provided

get_interface
    Return CPP interface

area_init
    Initialize a new NFP CPP area (not serialized)

area_cleanup
    Clean up a NFP CPP area (not serialized)

area_acquire
    Acquire the NFP CPP area (serialized)

area_release
    Release area (serialized)

area_resource
    Get resource range of area (not serialized)

area_phys
    Get physical address of area (not serialized)

area_iomem
    Get iomem of area (not serialized)

area_read
    Perform a read from a NFP CPP area (serialized)

area_write
    Perform a write to a NFP CPP area (serialized)

explicit_priv_size
    Size of an explicit's private area

explicit_acquire
    Acquire an explicit area

explicit_release
    Release an explicit area

explicit_put
    Write data to send

explicit_get
    Read data received

explicit_do
    Perform the transaction

.. This file was automatic generated / don't edit.

