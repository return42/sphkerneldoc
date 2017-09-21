.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/nvdimm/label.h

.. _`nd_namespace_index`:

struct nd_namespace_index
=========================

.. c:type:: struct nd_namespace_index

    label set superblock

.. _`nd_namespace_index.definition`:

Definition
----------

.. code-block:: c

    struct nd_namespace_index {
        u8 sig;
        u8 flags;
        u8 labelsize;
        __le32 seq;
        __le64 myoff;
        __le64 mysize;
        __le64 otheroff;
        __le64 labeloff;
        __le32 nslot;
        __le16 major;
        __le16 minor;
        __le64 checksum;
        u8 free;
    }

.. _`nd_namespace_index.members`:

Members
-------

sig
    NAMESPACE_INDEX\0

flags
    placeholder

labelsize
    *undescribed*

seq
    sequence number for this index

myoff
    offset of this index in label area

mysize
    size of this index struct

otheroff
    offset of other index

labeloff
    offset of first label slot

nslot
    total number of label slots

major
    label area major version

minor
    label area minor version

checksum
    fletcher64 of all fields

free
    bitmap, nlabel bits

.. _`nd_namespace_index.description`:

Description
-----------

The size of free[] is rounded up so the total struct size is a
multiple of NSINDEX_ALIGN bytes.  Any bits this allocates beyond
nlabel bits must be zero.

.. _`nd_namespace_label`:

struct nd_namespace_label
=========================

.. c:type:: struct nd_namespace_label

    namespace superblock

.. _`nd_namespace_label.definition`:

Definition
----------

.. code-block:: c

    struct nd_namespace_label {
        u8 uuid;
        u8 name;
        __le32 flags;
        __le16 nlabel;
        __le16 position;
        __le64 isetcookie;
        __le64 lbasize;
        __le64 dpa;
        __le64 rawsize;
        __le32 slot;
        u8 align;
        u8 reserved;
        guid_t type_guid;
        guid_t abstraction_guid;
        u8 reserved2;
        __le64 checksum;
    }

.. _`nd_namespace_label.members`:

Members
-------

uuid
    UUID per RFC 4122

name
    optional name (NULL-terminated)

flags
    see NSLABEL_FLAG\_\*

nlabel
    num labels to describe this ns

position
    labels position in set

isetcookie
    interleave set cookie

lbasize
    LBA size in bytes or 0 for pmem

dpa
    DPA of NVM range on this DIMM

rawsize
    size of namespace

slot
    slot of this label in label area

align
    *undescribed*

reserved
    *undescribed*

type_guid
    *undescribed*

abstraction_guid
    *undescribed*

reserved2
    *undescribed*

checksum
    *undescribed*

.. _`nd_label_id`:

struct nd_label_id
==================

.. c:type:: struct nd_label_id

    identifier string for dpa allocation

.. _`nd_label_id.definition`:

Definition
----------

.. code-block:: c

    struct nd_label_id {
        char id;
    }

.. _`nd_label_id.members`:

Members
-------

id
    "{blk\|pmem}-<namespace uuid>"

.. This file was automatic generated / don't edit.

