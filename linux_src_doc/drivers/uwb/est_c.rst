.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/uwb/est.c

.. _`uwb_est_create`:

uwb_est_create
==============

.. c:function:: int uwb_est_create( void)

    :param void:
        no arguments
    :type void: 

.. _`uwb_est_create.description`:

Description
-----------

Register the standard tables also.

.. _`uwb_est_create.fixme`:

FIXME
-----

tag init

.. _`uwb_est_grow`:

uwb_est_grow
============

.. c:function:: int uwb_est_grow( void)

    :param void:
        no arguments
    :type void: 

.. _`uwb_est_grow.description`:

Description
-----------

\ ``returns``\  0 if ok, < 0 errno no error.

.. _`uwb_est_register`:

uwb_est_register
================

.. c:function:: int uwb_est_register(u8 type, u8 event_high, u16 vendor, u16 product, const struct uwb_est_entry *entry, size_t entries)

    :param type:
        *undescribed*
    :type type: u8

    :param event_high:
        *undescribed*
    :type event_high: u8

    :param vendor:
        vendor code for matching against the device (0x0000 and
        0xffff mean any); use 0x0000 to force all to match without
        checking possible vendor specific ones, 0xfffff to match
        after checking vendor specific ones.
    :type vendor: u16

    :param product:
        product code from that vendor; same matching rules, use
        0x0000 for not allowing vendor specific matches, 0xffff
        for allowing.
    :type product: u16

    :param entry:
        *undescribed*
    :type entry: const struct uwb_est_entry \*

    :param entries:
        *undescribed*
    :type entries: size_t

.. _`uwb_est_register.description`:

Description
-----------

Makes room for it if the table is full, and then inserts  it in the
right position (entries are sorted by type, event_high, vendor and
then product).

This arragement just makes the tables sort differenty. Because the
table is sorted by growing type-event_high-vendor-product, a zero
vendor will match before than a 0x456a vendor, that will match
before a 0xfffff vendor.

\ ``returns``\  0 if ok, < 0 errno on error (-ENOENT if not found).

.. _`uwb_est_unregister`:

uwb_est_unregister
==================

.. c:function:: int uwb_est_unregister(u8 type, u8 event_high, u16 vendor, u16 product, const struct uwb_est_entry *entry, size_t entries)

    :param type:
        *undescribed*
    :type type: u8

    :param event_high:
        *undescribed*
    :type event_high: u8

    :param vendor:
        *undescribed*
    :type vendor: u16

    :param product:
        *undescribed*
    :type product: u16

    :param entry:
        *undescribed*
    :type entry: const struct uwb_est_entry \*

    :param entries:
        *undescribed*
    :type entries: size_t

.. _`uwb_est_unregister.description`:

Description
-----------

This just removes the specified entry and moves the ones after it
to fill in the gap. This is needed to keep the list sorted; no
reallocation is done to reduce the size of the table.

We unregister by all the data we used to register instead of by
pointer to the \ ``entry``\  array because we might have used the same
table for a bunch of IDs (for example).

\ ``returns``\  0 if ok, < 0 errno on error (-ENOENT if not found).

.. _`uwb_est_get_size`:

uwb_est_get_size
================

.. c:function:: ssize_t uwb_est_get_size(struct uwb_rc *uwb_rc, struct uwb_est *est, u8 event_low, const struct uwb_rceb *rceb, size_t rceb_size)

    :param uwb_rc:
        *undescribed*
    :type uwb_rc: struct uwb_rc \*

    :param est:
        *undescribed*
    :type est: struct uwb_est \*

    :param event_low:
        *undescribed*
    :type event_low: u8

    :param rceb:
        pointer to the buffer with the event
    :type rceb: const struct uwb_rceb \*

    :param rceb_size:
        size of the area pointed to by \ ``rceb``\  in bytes.
    :type rceb_size: size_t

.. _`uwb_est_get_size.description`:

Description
-----------

This will look at the received RCEB and guess what is the total
size. For variable sized events, it will look further ahead into
their length field to see how much data should be read.

Note this size is \*not\* final--the neh (Notification/Event Handle)
might specificy an extra size to add.

.. _`uwb_est_find_size`:

uwb_est_find_size
=================

.. c:function:: ssize_t uwb_est_find_size(struct uwb_rc *rc, const struct uwb_rceb *rceb, size_t rceb_size)

    :param rc:
        *undescribed*
    :type rc: struct uwb_rc \*

    :param rceb:
        pointer to the buffer with the event
    :type rceb: const struct uwb_rceb \*

    :param rceb_size:
        size of the area pointed to by \ ``rceb``\  in bytes.
    :type rceb_size: size_t

.. _`uwb_est_find_size.description`:

Description
-----------

This will look at the received RCEB and guess what is the total
size by checking all the tables registered with
\ :c:func:`uwb_est_register`\ . For variable sized events, it will look further
ahead into their length field to see how much data should be read.

Note this size is \*not\* final--the neh (Notification/Event Handle)
might specificy an extra size to add or replace.

.. This file was automatic generated / don't edit.

