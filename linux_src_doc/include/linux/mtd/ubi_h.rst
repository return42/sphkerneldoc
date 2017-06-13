.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/mtd/ubi.h

.. _`ubi_volume_info`:

struct ubi_volume_info
======================

.. c:type:: struct ubi_volume_info

    UBI volume description data structure.

.. _`ubi_volume_info.definition`:

Definition
----------

.. code-block:: c

    struct ubi_volume_info {
        int ubi_num;
        int vol_id;
        int size;
        long long used_bytes;
        int used_ebs;
        int vol_type;
        int corrupted;
        int upd_marker;
        int alignment;
        int usable_leb_size;
        int name_len;
        const char *name;
        dev_t cdev;
    }

.. _`ubi_volume_info.members`:

Members
-------

ubi_num
    UBI device number this volume belongs to

vol_id
    volume ID

size
    how many physical eraseblocks are reserved for this volume

used_bytes
    how many bytes of data this volume contains

used_ebs
    how many physical eraseblocks of this volume actually contain any
    data

vol_type
    volume type (%UBI_DYNAMIC_VOLUME or \ ``UBI_STATIC_VOLUME``\ )

corrupted
    non-zero if the volume is corrupted (static volumes only)

upd_marker
    non-zero if the volume has update marker set

alignment
    volume alignment

usable_leb_size
    how many bytes are available in logical eraseblocks of
    this volume

name_len
    volume name length

name
    volume name

cdev
    UBI volume character device major and minor numbers

.. _`ubi_volume_info.description`:

Description
-----------

The \ ``corrupted``\  flag is only relevant to static volumes and is always zero
for dynamic ones. This is because UBI does not care about dynamic volume
data protection and only cares about protecting static volume data.

The \ ``upd_marker``\  flag is set if the volume update operation was interrupted.
Before touching the volume data during the update operation, UBI first sets
the update marker flag for this volume. If the volume update operation was
further interrupted, the update marker indicates this. If the update marker
is set, the contents of the volume is certainly damaged and a new volume
update operation has to be started.

To put it differently, \ ``corrupted``\  and \ ``upd_marker``\  fields have different

.. _`ubi_volume_info.semantics`:

semantics
---------

o the \ ``corrupted``\  flag means that this static volume is corrupted for some
reasons, but not because an interrupted volume update
o the \ ``upd_marker``\  field means that the volume is damaged because of an
interrupted update operation.

I.e., the \ ``corrupted``\  flag is never set if the \ ``upd_marker``\  flag is set.

The \ ``used_bytes``\  and \ ``used_ebs``\  fields are only really needed for static
volumes and contain the number of bytes stored in this static volume and how
many eraseblock this data occupies. In case of dynamic volumes, the
\ ``used_bytes``\  field is equivalent to \ ``size``\ \*@usable_leb_size, and the \ ``used_ebs``\ 
field is equivalent to \ ``size``\ .

In general, logical eraseblock size is a property of the UBI device, not
of the UBI volume. Indeed, the logical eraseblock size depends on the
physical eraseblock size and on how much bytes UBI headers consume. But
because of the volume alignment (@alignment), the usable size of logical
eraseblocks if a volume may be less. The following equation is true:
\ ``usable_leb_size``\  = LEB size - (LEB size mod \ ``alignment``\ ),
where LEB size is the logical eraseblock size defined by the UBI device.

The alignment is multiple to the minimal flash input/output unit size or \ ``1``\ 
if all the available space is used.

To put this differently, alignment may be considered is a way to change
volume logical eraseblock sizes.

.. _`ubi_sgl`:

struct ubi_sgl
==============

.. c:type:: struct ubi_sgl

    UBI scatter gather list data structure.

.. _`ubi_sgl.definition`:

Definition
----------

.. code-block:: c

    struct ubi_sgl {
        int list_pos;
        int page_pos;
        struct scatterlist sg;
    }

.. _`ubi_sgl.members`:

Members
-------

list_pos
    current position in \ ``sg``\ []

page_pos
    current position in \ ``sg``\ [@list_pos]

sg
    the scatter gather list itself

.. _`ubi_sgl.description`:

Description
-----------

ubi_sgl is a wrapper around a scatter list which keeps track of the
current position in the list and the current list item such that
it can be used across multiple \ :c:func:`ubi_leb_read_sg`\  calls.

.. _`ubi_sgl_init`:

ubi_sgl_init
============

.. c:function:: void ubi_sgl_init(struct ubi_sgl *usgl)

    initialize an UBI scatter gather list data structure.

    :param struct ubi_sgl \*usgl:
        the UBI scatter gather struct itself

.. _`ubi_sgl_init.description`:

Description
-----------

Please note that you still have to use \ :c:func:`sg_init_table`\  or any adequate
function to initialize the unterlaying struct scatterlist.

.. _`ubi_device_info`:

struct ubi_device_info
======================

.. c:type:: struct ubi_device_info

    UBI device description data structure.

.. _`ubi_device_info.definition`:

Definition
----------

.. code-block:: c

    struct ubi_device_info {
        int ubi_num;
        int leb_size;
        int leb_start;
        int min_io_size;
        int max_write_size;
        int ro_mode;
        dev_t cdev;
    }

.. _`ubi_device_info.members`:

Members
-------

ubi_num
    ubi device number

leb_size
    logical eraseblock size on this UBI device

leb_start
    starting offset of logical eraseblocks within physical
    eraseblocks

min_io_size
    minimal I/O unit size

max_write_size
    maximum amount of bytes the underlying flash can write at a
    time (MTD write buffer size)

ro_mode
    if this device is in read-only mode

cdev
    UBI character device major and minor numbers

.. _`ubi_device_info.description`:

Description
-----------

Note, \ ``leb_size``\  is the logical eraseblock size offered by the UBI device.
Volumes of this UBI device may have smaller logical eraseblock size if their
alignment is not equivalent to \ ``1``\ .

The \ ``max_write_size``\  field describes flash write maximum write unit. For
example, NOR flash allows for changing individual bytes, so \ ``min_io_size``\  is
\ ``1``\ . However, it does not mean than NOR flash has to write data byte-by-byte.
Instead, CFI NOR flashes have a write-buffer of, e.g., 64 bytes, and when
writing large chunks of data, they write 64-bytes at a time. Obviously, this
improves write throughput.

Also, the MTD device may have N interleaved (striped) flash chips
underneath, in which case \ ``min_io_size``\  can be physical min. I/O size of
single flash chip, while \ ``max_write_size``\  can be N \* \ ``min_io_size``\ .

The \ ``max_write_size``\  field is always greater or equivalent to \ ``min_io_size``\ .
E.g., some NOR flashes may have (@min_io_size = 1, \ ``max_write_size``\  = 64). In
contrast, NAND flashes usually have \ ``min_io_size``\  = \ ``max_write_size``\  = NAND
page size.

.. This file was automatic generated / don't edit.

