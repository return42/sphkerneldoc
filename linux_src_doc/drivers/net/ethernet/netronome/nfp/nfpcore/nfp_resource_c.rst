.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/net/ethernet/netronome/nfp/nfpcore/nfp_resource.c

.. _`nfp_resource_entry`:

struct nfp_resource_entry
=========================

.. c:type:: struct nfp_resource_entry

    Resource table entry

.. _`nfp_resource_entry.definition`:

Definition
----------

.. code-block:: c

    struct nfp_resource_entry {
        struct nfp_resource_entry_mutex {
            u32 owner;
            u32 key;
        } mutex;
        struct nfp_resource_entry_region {
            u8 name[NFP_RESOURCE_ENTRY_NAME_SZ];
            u8 reserved[5];
            u8 cpp_action;
            u8 cpp_token;
            u8 cpp_target;
            u32 page_offset;
            u32 page_size;
        } region;
    }

.. _`nfp_resource_entry.members`:

Members
-------

mutex
    *undescribed*

region
    Memory region descriptor

.. _`nfp_resource_acquire`:

nfp_resource_acquire
====================

.. c:function:: struct nfp_resource *nfp_resource_acquire(struct nfp_cpp *cpp, const char *name)

    Acquire a resource handle

    :param struct nfp_cpp \*cpp:
        NFP CPP handle

    :param const char \*name:
        Name of the resource

.. _`nfp_resource_acquire.note`:

NOTE
----

This function locks the acquired resource

.. _`nfp_resource_acquire.return`:

Return
------

NFP Resource handle, or \ :c:func:`ERR_PTR`\ 

.. _`nfp_resource_release`:

nfp_resource_release
====================

.. c:function:: void nfp_resource_release(struct nfp_resource *res)

    Release a NFP Resource handle

    :param struct nfp_resource \*res:
        NFP Resource handle

.. _`nfp_resource_release.note`:

NOTE
----

This function implictly unlocks the resource handle

.. _`nfp_resource_cpp_id`:

nfp_resource_cpp_id
===================

.. c:function:: u32 nfp_resource_cpp_id(struct nfp_resource *res)

    Return the cpp_id of a resource handle

    :param struct nfp_resource \*res:
        NFP Resource handle

.. _`nfp_resource_cpp_id.return`:

Return
------

NFP CPP ID

.. _`nfp_resource_name`:

nfp_resource_name
=================

.. c:function:: const char *nfp_resource_name(struct nfp_resource *res)

    Return the name of a resource handle

    :param struct nfp_resource \*res:
        NFP Resource handle

.. _`nfp_resource_name.return`:

Return
------

const char pointer to the name of the resource

.. _`nfp_resource_address`:

nfp_resource_address
====================

.. c:function:: u64 nfp_resource_address(struct nfp_resource *res)

    Return the address of a resource handle

    :param struct nfp_resource \*res:
        NFP Resource handle

.. _`nfp_resource_address.return`:

Return
------

Address of the resource

.. _`nfp_resource_size`:

nfp_resource_size
=================

.. c:function:: u64 nfp_resource_size(struct nfp_resource *res)

    Return the size in bytes of a resource handle

    :param struct nfp_resource \*res:
        NFP Resource handle

.. _`nfp_resource_size.return`:

Return
------

Size of the resource in bytes

.. This file was automatic generated / don't edit.

