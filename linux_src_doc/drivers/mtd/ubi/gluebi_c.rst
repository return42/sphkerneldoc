.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mtd/ubi/gluebi.c

.. _`gluebi_device`:

struct gluebi_device
====================

.. c:type:: struct gluebi_device

    a gluebi device description data structure.

.. _`gluebi_device.definition`:

Definition
----------

.. code-block:: c

    struct gluebi_device {
        struct mtd_info mtd;
        int refcnt;
        struct ubi_volume_desc *desc;
        int ubi_num;
        int vol_id;
        struct list_head list;
    }

.. _`gluebi_device.members`:

Members
-------

mtd
    emulated MTD device description object

refcnt
    gluebi device reference count

desc
    UBI volume descriptor

ubi_num
    UBI device number this gluebi device works on

vol_id
    ID of UBI volume this gluebi device works on

list
    link in a list of gluebi devices

.. _`find_gluebi_nolock`:

find_gluebi_nolock
==================

.. c:function:: struct gluebi_device *find_gluebi_nolock(int ubi_num, int vol_id)

    find a gluebi device.

    :param ubi_num:
        UBI device number
    :type ubi_num: int

    :param vol_id:
        volume ID
    :type vol_id: int

.. _`find_gluebi_nolock.description`:

Description
-----------

This function seraches for gluebi device corresponding to UBI device
\ ``ubi_num``\  and UBI volume \ ``vol_id``\ . Returns the gluebi device description
object in case of success and \ ``NULL``\  in case of failure. The caller has to
have the \ :c:type:`struct devices_mutex <devices_mutex>`\  locked.

.. _`gluebi_get_device`:

gluebi_get_device
=================

.. c:function:: int gluebi_get_device(struct mtd_info *mtd)

    get MTD device reference.

    :param mtd:
        the MTD device description object
    :type mtd: struct mtd_info \*

.. _`gluebi_get_device.description`:

Description
-----------

This function is called every time the MTD device is being opened and
implements the MTD \ :c:func:`get_device`\  operation. Returns zero in case of success
and a negative error code in case of failure.

.. _`gluebi_put_device`:

gluebi_put_device
=================

.. c:function:: void gluebi_put_device(struct mtd_info *mtd)

    put MTD device reference.

    :param mtd:
        the MTD device description object
    :type mtd: struct mtd_info \*

.. _`gluebi_put_device.description`:

Description
-----------

This function is called every time the MTD device is being put. Returns
zero in case of success and a negative error code in case of failure.

.. _`gluebi_read`:

gluebi_read
===========

.. c:function:: int gluebi_read(struct mtd_info *mtd, loff_t from, size_t len, size_t *retlen, unsigned char *buf)

    read operation of emulated MTD devices.

    :param mtd:
        MTD device description object
    :type mtd: struct mtd_info \*

    :param from:
        absolute offset from where to read
    :type from: loff_t

    :param len:
        how many bytes to read
    :type len: size_t

    :param retlen:
        count of read bytes is returned here
    :type retlen: size_t \*

    :param buf:
        buffer to store the read data
    :type buf: unsigned char \*

.. _`gluebi_read.description`:

Description
-----------

This function returns zero in case of success and a negative error code in
case of failure.

.. _`gluebi_write`:

gluebi_write
============

.. c:function:: int gluebi_write(struct mtd_info *mtd, loff_t to, size_t len, size_t *retlen, const u_char *buf)

    write operation of emulated MTD devices.

    :param mtd:
        MTD device description object
    :type mtd: struct mtd_info \*

    :param to:
        absolute offset where to write
    :type to: loff_t

    :param len:
        how many bytes to write
    :type len: size_t

    :param retlen:
        count of written bytes is returned here
    :type retlen: size_t \*

    :param buf:
        buffer with data to write
    :type buf: const u_char \*

.. _`gluebi_write.description`:

Description
-----------

This function returns zero in case of success and a negative error code in
case of failure.

.. _`gluebi_erase`:

gluebi_erase
============

.. c:function:: int gluebi_erase(struct mtd_info *mtd, struct erase_info *instr)

    erase operation of emulated MTD devices.

    :param mtd:
        the MTD device description object
    :type mtd: struct mtd_info \*

    :param instr:
        the erase operation description
    :type instr: struct erase_info \*

.. _`gluebi_erase.description`:

Description
-----------

This function calls the erase callback when finishes. Returns zero in case
of success and a negative error code in case of failure.

.. _`gluebi_create`:

gluebi_create
=============

.. c:function:: int gluebi_create(struct ubi_device_info *di, struct ubi_volume_info *vi)

    create a gluebi device for an UBI volume.

    :param di:
        UBI device description object
    :type di: struct ubi_device_info \*

    :param vi:
        UBI volume description object
    :type vi: struct ubi_volume_info \*

.. _`gluebi_create.description`:

Description
-----------

This function is called when a new UBI volume is created in order to create
corresponding fake MTD device. Returns zero in case of success and a
negative error code in case of failure.

.. _`gluebi_remove`:

gluebi_remove
=============

.. c:function:: int gluebi_remove(struct ubi_volume_info *vi)

    remove a gluebi device.

    :param vi:
        UBI volume description object
    :type vi: struct ubi_volume_info \*

.. _`gluebi_remove.description`:

Description
-----------

This function is called when an UBI volume is removed and it removes
corresponding fake MTD device. Returns zero in case of success and a
negative error code in case of failure.

.. _`gluebi_updated`:

gluebi_updated
==============

.. c:function:: int gluebi_updated(struct ubi_volume_info *vi)

    UBI volume was updated notifier.

    :param vi:
        volume info structure
    :type vi: struct ubi_volume_info \*

.. _`gluebi_updated.description`:

Description
-----------

This function is called every time an UBI volume is updated. It does nothing
if te volume \ ``vol``\  is dynamic, and changes MTD device size if the
volume is static. This is needed because static volumes cannot be read past
data they contain. This function returns zero in case of success and a
negative error code in case of error.

.. _`gluebi_resized`:

gluebi_resized
==============

.. c:function:: int gluebi_resized(struct ubi_volume_info *vi)

    UBI volume was re-sized notifier.

    :param vi:
        volume info structure
    :type vi: struct ubi_volume_info \*

.. _`gluebi_resized.description`:

Description
-----------

This function is called every time an UBI volume is re-size. It changes the
corresponding fake MTD device size. This function returns zero in case of
success and a negative error code in case of error.

.. _`gluebi_notify`:

gluebi_notify
=============

.. c:function:: int gluebi_notify(struct notifier_block *nb, unsigned long l, void *ns_ptr)

    UBI notification handler.

    :param nb:
        registered notifier block
    :type nb: struct notifier_block \*

    :param l:
        notification type
    :type l: unsigned long

    :param ns_ptr:
        *undescribed*
    :type ns_ptr: void \*

.. This file was automatic generated / don't edit.

