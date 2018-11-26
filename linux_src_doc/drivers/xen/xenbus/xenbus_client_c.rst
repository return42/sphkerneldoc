.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/xen/xenbus/xenbus_client.c

.. _`xenbus_watch_path`:

xenbus_watch_path
=================

.. c:function:: int xenbus_watch_path(struct xenbus_device *dev, const char *path, struct xenbus_watch *watch, void (*callback)(struct xenbus_watch *, const char *, const char *))

    register a watch

    :param dev:
        xenbus device
    :type dev: struct xenbus_device \*

    :param path:
        path to watch
    :type path: const char \*

    :param watch:
        watch to register
    :type watch: struct xenbus_watch \*

    :param void (\*callback)(struct xenbus_watch \*, const char \*, const char \*):
        callback to register

.. _`xenbus_watch_path.description`:

Description
-----------

Register a \ ``watch``\  on the given path, using the given xenbus_watch structure
for storage, and the given \ ``callback``\  function as the callback.  Return 0 on
success, or -errno on error.  On success, the given \ ``path``\  will be saved as
\ ``watch->node``\ , and remains the caller's to free.  On error, \ ``watch->node``\  will
be NULL, the device will switch to \ ``XenbusStateClosing``\ , and the error will
be saved in the store.

.. _`xenbus_watch_pathfmt`:

xenbus_watch_pathfmt
====================

.. c:function:: int xenbus_watch_pathfmt(struct xenbus_device *dev, struct xenbus_watch *watch, void (*callback)(struct xenbus_watch *, const char *, const char *), const char *pathfmt,  ...)

    register a watch on a sprintf-formatted path

    :param dev:
        xenbus device
    :type dev: struct xenbus_device \*

    :param watch:
        watch to register
    :type watch: struct xenbus_watch \*

    :param void (\*callback)(struct xenbus_watch \*, const char \*, const char \*):
        callback to register

    :param pathfmt:
        format of path to watch
    :type pathfmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`xenbus_watch_pathfmt.description`:

Description
-----------

Register a watch on the given \ ``path``\ , using the given xenbus_watch
structure for storage, and the given \ ``callback``\  function as the callback.
Return 0 on success, or -errno on error.  On success, the watched path
(@path/@path2) will be saved as \ ``watch->node``\ , and becomes the caller's to
\ :c:func:`kfree`\ .  On error, watch->node will be NULL, so the caller has nothing to
free, the device will switch to \ ``XenbusStateClosing``\ , and the error will be
saved in the store.

.. _`xenbus_switch_state`:

xenbus_switch_state
===================

.. c:function:: int xenbus_switch_state(struct xenbus_device *dev, enum xenbus_state state)

    :param dev:
        xenbus device
    :type dev: struct xenbus_device \*

    :param state:
        new state
    :type state: enum xenbus_state

.. _`xenbus_switch_state.description`:

Description
-----------

Advertise in the store a change of the given driver to the given new_state.
Return 0 on success, or -errno on error.  On error, the device will switch
to XenbusStateClosing, and the error will be saved in the store.

.. _`xenbus_dev_error`:

xenbus_dev_error
================

.. c:function:: void xenbus_dev_error(struct xenbus_device *dev, int err, const char *fmt,  ...)

    :param dev:
        xenbus device
    :type dev: struct xenbus_device \*

    :param err:
        error to report
    :type err: int

    :param fmt:
        error message format
    :type fmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`xenbus_dev_error.description`:

Description
-----------

Report the given negative errno into the store, along with the given
formatted message.

.. _`xenbus_dev_fatal`:

xenbus_dev_fatal
================

.. c:function:: void xenbus_dev_fatal(struct xenbus_device *dev, int err, const char *fmt,  ...)

    :param dev:
        xenbus device
    :type dev: struct xenbus_device \*

    :param err:
        error to report
    :type err: int

    :param fmt:
        error message format
    :type fmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`xenbus_dev_fatal.description`:

Description
-----------

Equivalent to xenbus_dev_error(dev, err, fmt, args), followed by
xenbus_switch_state(dev, XenbusStateClosing) to schedule an orderly
closedown of this driver and its peer.

.. _`xenbus_switch_fatal`:

xenbus_switch_fatal
===================

.. c:function:: void xenbus_switch_fatal(struct xenbus_device *dev, int depth, int err, const char *fmt,  ...)

    avoiding recursion within xenbus_switch_state.

    :param dev:
        *undescribed*
    :type dev: struct xenbus_device \*

    :param depth:
        *undescribed*
    :type depth: int

    :param err:
        *undescribed*
    :type err: int

    :param fmt:
        *undescribed*
    :type fmt: const char \*

    :param ellipsis ellipsis:
        variable arguments

.. _`xenbus_grant_ring`:

xenbus_grant_ring
=================

.. c:function:: int xenbus_grant_ring(struct xenbus_device *dev, void *vaddr, unsigned int nr_pages, grant_ref_t *grefs)

    :param dev:
        xenbus device
    :type dev: struct xenbus_device \*

    :param vaddr:
        starting virtual address of the ring
    :type vaddr: void \*

    :param nr_pages:
        number of pages to be granted
    :type nr_pages: unsigned int

    :param grefs:
        grant reference array to be filled in
    :type grefs: grant_ref_t \*

.. _`xenbus_grant_ring.description`:

Description
-----------

Grant access to the given \ ``vaddr``\  to the peer of the given device.
Then fill in \ ``grefs``\  with grant references.  Return 0 on success, or
-errno on error.  On error, the device will switch to
XenbusStateClosing, and the error will be saved in the store.

.. _`xenbus_alloc_evtchn`:

xenbus_alloc_evtchn
===================

.. c:function:: int xenbus_alloc_evtchn(struct xenbus_device *dev, int *port)

    created local port to \*port.  Return 0 on success, or -errno on error.  On error, the device will switch to XenbusStateClosing, and the error will be saved in the store.

    :param dev:
        *undescribed*
    :type dev: struct xenbus_device \*

    :param port:
        *undescribed*
    :type port: int \*

.. _`xenbus_free_evtchn`:

xenbus_free_evtchn
==================

.. c:function:: int xenbus_free_evtchn(struct xenbus_device *dev, int port)

    errno on error.

    :param dev:
        *undescribed*
    :type dev: struct xenbus_device \*

    :param port:
        *undescribed*
    :type port: int

.. _`xenbus_map_ring_valloc`:

xenbus_map_ring_valloc
======================

.. c:function:: int xenbus_map_ring_valloc(struct xenbus_device *dev, grant_ref_t *gnt_refs, unsigned int nr_grefs, void **vaddr)

    :param dev:
        xenbus device
    :type dev: struct xenbus_device \*

    :param gnt_refs:
        grant reference array
    :type gnt_refs: grant_ref_t \*

    :param nr_grefs:
        number of grant references
    :type nr_grefs: unsigned int

    :param vaddr:
        pointer to address to be filled out by mapping
    :type vaddr: void \*\*

.. _`xenbus_map_ring_valloc.description`:

Description
-----------

Map \ ``nr_grefs``\  pages of memory into this domain from another
domain's grant table.  xenbus_map_ring_valloc allocates \ ``nr_grefs``\ 
pages of virtual address space, maps the pages to that address, and
sets \*vaddr to that address.  Returns 0 on success, and GNTST\_\*
(see xen/include/interface/grant_table.h) or -ENOMEM / -EINVAL on
error. If an error is returned, device will switch to
XenbusStateClosing and the error message will be saved in XenStore.

.. _`xenbus_map_ring`:

xenbus_map_ring
===============

.. c:function:: int xenbus_map_ring(struct xenbus_device *dev, grant_ref_t *gnt_refs, unsigned int nr_grefs, grant_handle_t *handles, unsigned long *vaddrs, bool *leaked)

    :param dev:
        xenbus device
    :type dev: struct xenbus_device \*

    :param gnt_refs:
        grant reference array
    :type gnt_refs: grant_ref_t \*

    :param nr_grefs:
        number of grant reference
    :type nr_grefs: unsigned int

    :param handles:
        pointer to grant handle to be filled
    :type handles: grant_handle_t \*

    :param vaddrs:
        addresses to be mapped to
    :type vaddrs: unsigned long \*

    :param leaked:
        fail to clean up a failed map, caller should not free vaddr
    :type leaked: bool \*

.. _`xenbus_map_ring.description`:

Description
-----------

Map pages of memory into this domain from another domain's grant table.
xenbus_map_ring does not allocate the virtual address space (you must do
this yourself!). It only maps in the pages to the specified address.
Returns 0 on success, and GNTST\_\* (see xen/include/interface/grant_table.h)
or -ENOMEM / -EINVAL on error. If an error is returned, device will switch to
XenbusStateClosing and the first error message will be saved in XenStore.
Further more if we fail to map the ring, caller should check \ ``leaked``\ .
If \ ``leaked``\  is not zero it means xenbus_map_ring fails to clean up, caller
should not free the address space of \ ``vaddr``\ .

.. _`xenbus_unmap_ring_vfree`:

xenbus_unmap_ring_vfree
=======================

.. c:function:: int xenbus_unmap_ring_vfree(struct xenbus_device *dev, void *vaddr)

    :param dev:
        xenbus device
    :type dev: struct xenbus_device \*

    :param vaddr:
        addr to unmap
    :type vaddr: void \*

.. _`xenbus_unmap_ring_vfree.description`:

Description
-----------

Based on Rusty Russell's skeleton driver's unmap_page.
Unmap a page of memory in this domain that was imported from another domain.
Use xenbus_unmap_ring_vfree if you mapped in your memory with
xenbus_map_ring_valloc (it will free the virtual address space).
Returns 0 on success and returns GNTST\_\* on error
(see xen/include/interface/grant_table.h).

.. _`xenbus_unmap_ring`:

xenbus_unmap_ring
=================

.. c:function:: int xenbus_unmap_ring(struct xenbus_device *dev, grant_handle_t *handles, unsigned int nr_handles, unsigned long *vaddrs)

    :param dev:
        xenbus device
    :type dev: struct xenbus_device \*

    :param handles:
        grant handle array
    :type handles: grant_handle_t \*

    :param nr_handles:
        number of handles in the array
    :type nr_handles: unsigned int

    :param vaddrs:
        addresses to unmap
    :type vaddrs: unsigned long \*

.. _`xenbus_unmap_ring.description`:

Description
-----------

Unmap memory in this domain that was imported from another domain.
Returns 0 on success and returns GNTST\_\* on error
(see xen/include/interface/grant_table.h).

.. _`xenbus_read_driver_state`:

xenbus_read_driver_state
========================

.. c:function:: enum xenbus_state xenbus_read_driver_state(const char *path)

    :param path:
        path for driver
    :type path: const char \*

.. _`xenbus_read_driver_state.description`:

Description
-----------

Return the state of the driver rooted at the given store path, or
XenbusStateUnknown if no state can be read.

.. This file was automatic generated / don't edit.

