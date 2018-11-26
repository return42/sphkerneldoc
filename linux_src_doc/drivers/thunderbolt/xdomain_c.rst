.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/thunderbolt/xdomain.c

.. _`tb_xdomain_response`:

tb_xdomain_response
===================

.. c:function:: int tb_xdomain_response(struct tb_xdomain *xd, const void *response, size_t size, enum tb_cfg_pkg_type type)

    Send a XDomain response message

    :param xd:
        XDomain to send the message
    :type xd: struct tb_xdomain \*

    :param response:
        Response to send
    :type response: const void \*

    :param size:
        Size of the response
    :type size: size_t

    :param type:
        PDF type of the response
    :type type: enum tb_cfg_pkg_type

.. _`tb_xdomain_response.description`:

Description
-----------

This can be used to send a XDomain response message to the other
domain. No response for the message is expected.

.. _`tb_xdomain_response.return`:

Return
------

\ ``0``\  in case of success and negative errno in case of failure

.. _`tb_xdomain_request`:

tb_xdomain_request
==================

.. c:function:: int tb_xdomain_request(struct tb_xdomain *xd, const void *request, size_t request_size, enum tb_cfg_pkg_type request_type, void *response, size_t response_size, enum tb_cfg_pkg_type response_type, unsigned int timeout_msec)

    Send a XDomain request

    :param xd:
        XDomain to send the request
    :type xd: struct tb_xdomain \*

    :param request:
        Request to send
    :type request: const void \*

    :param request_size:
        Size of the request in bytes
    :type request_size: size_t

    :param request_type:
        PDF type of the request
    :type request_type: enum tb_cfg_pkg_type

    :param response:
        Response is copied here
    :type response: void \*

    :param response_size:
        Expected size of the response in bytes
    :type response_size: size_t

    :param response_type:
        Expected PDF type of the response
    :type response_type: enum tb_cfg_pkg_type

    :param timeout_msec:
        Timeout in milliseconds to wait for the response
    :type timeout_msec: unsigned int

.. _`tb_xdomain_request.description`:

Description
-----------

This function can be used to send XDomain control channel messages to
the other domain. The function waits until the response is received
or when timeout triggers. Whichever comes first.

.. _`tb_xdomain_request.return`:

Return
------

\ ``0``\  in case of success and negative errno in case of failure

.. _`tb_register_protocol_handler`:

tb_register_protocol_handler
============================

.. c:function:: int tb_register_protocol_handler(struct tb_protocol_handler *handler)

    Register protocol handler

    :param handler:
        Handler to register
    :type handler: struct tb_protocol_handler \*

.. _`tb_register_protocol_handler.description`:

Description
-----------

This allows XDomain service drivers to hook into incoming XDomain
messages. After this function is called the service driver needs to
be able to handle calls to callback whenever a package with the
registered protocol is received.

.. _`tb_unregister_protocol_handler`:

tb_unregister_protocol_handler
==============================

.. c:function:: void tb_unregister_protocol_handler(struct tb_protocol_handler *handler)

    Unregister protocol handler

    :param handler:
        Handler to unregister
    :type handler: struct tb_protocol_handler \*

.. _`tb_unregister_protocol_handler.description`:

Description
-----------

Removes the previously registered protocol handler.

.. _`tb_register_service_driver`:

tb_register_service_driver
==========================

.. c:function:: int tb_register_service_driver(struct tb_service_driver *drv)

    Register XDomain service driver

    :param drv:
        Driver to register
    :type drv: struct tb_service_driver \*

.. _`tb_register_service_driver.description`:

Description
-----------

Registers new service driver from \ ``drv``\  to the bus.

.. _`tb_unregister_service_driver`:

tb_unregister_service_driver
============================

.. c:function:: void tb_unregister_service_driver(struct tb_service_driver *drv)

    Unregister XDomain service driver

    :param drv:
        *undescribed*
    :type drv: struct tb_service_driver \*

.. _`tb_unregister_service_driver.description`:

Description
-----------

Unregisters XDomain service driver from the bus.

.. _`tb_xdomain_alloc`:

tb_xdomain_alloc
================

.. c:function:: struct tb_xdomain *tb_xdomain_alloc(struct tb *tb, struct device *parent, u64 route, const uuid_t *local_uuid, const uuid_t *remote_uuid)

    Allocate new XDomain object

    :param tb:
        Domain where the XDomain belongs
    :type tb: struct tb \*

    :param parent:
        Parent device (the switch through the connection to the
        other domain is reached).
    :type parent: struct device \*

    :param route:
        Route string used to reach the other domain
    :type route: u64

    :param local_uuid:
        Our local domain UUID
    :type local_uuid: const uuid_t \*

    :param remote_uuid:
        UUID of the other domain
    :type remote_uuid: const uuid_t \*

.. _`tb_xdomain_alloc.description`:

Description
-----------

Allocates new XDomain structure and returns pointer to that. The
object must be released by calling \ :c:func:`tb_xdomain_put`\ .

.. _`tb_xdomain_add`:

tb_xdomain_add
==============

.. c:function:: void tb_xdomain_add(struct tb_xdomain *xd)

    Add XDomain to the bus

    :param xd:
        XDomain to add
    :type xd: struct tb_xdomain \*

.. _`tb_xdomain_add.description`:

Description
-----------

This function starts XDomain discovery protocol handshake and
eventually adds the XDomain to the bus. After calling this function
the caller needs to call \ :c:func:`tb_xdomain_remove`\  in order to remove and
release the object regardless whether the handshake succeeded or not.

.. _`tb_xdomain_remove`:

tb_xdomain_remove
=================

.. c:function:: void tb_xdomain_remove(struct tb_xdomain *xd)

    Remove XDomain from the bus

    :param xd:
        XDomain to remove
    :type xd: struct tb_xdomain \*

.. _`tb_xdomain_remove.description`:

Description
-----------

This will stop all ongoing configuration work and remove the XDomain
along with any services from the bus. When the last reference to \ ``xd``\ 
is released the object will be released as well.

.. _`tb_xdomain_enable_paths`:

tb_xdomain_enable_paths
=======================

.. c:function:: int tb_xdomain_enable_paths(struct tb_xdomain *xd, u16 transmit_path, u16 transmit_ring, u16 receive_path, u16 receive_ring)

    Enable DMA paths for XDomain connection

    :param xd:
        XDomain connection
    :type xd: struct tb_xdomain \*

    :param transmit_path:
        HopID of the transmit path the other end is using to
        send packets
    :type transmit_path: u16

    :param transmit_ring:
        DMA ring used to receive packets from the other end
    :type transmit_ring: u16

    :param receive_path:
        HopID of the receive path the other end is using to
        receive packets
    :type receive_path: u16

    :param receive_ring:
        DMA ring used to send packets to the other end
    :type receive_ring: u16

.. _`tb_xdomain_enable_paths.description`:

Description
-----------

The function enables DMA paths accordingly so that after successful
return the caller can send and receive packets using high-speed DMA
path.

.. _`tb_xdomain_enable_paths.return`:

Return
------

\ ``0``\  in case of success and negative errno in case of error

.. _`tb_xdomain_disable_paths`:

tb_xdomain_disable_paths
========================

.. c:function:: int tb_xdomain_disable_paths(struct tb_xdomain *xd)

    Disable DMA paths for XDomain connection

    :param xd:
        XDomain connection
    :type xd: struct tb_xdomain \*

.. _`tb_xdomain_disable_paths.description`:

Description
-----------

This does the opposite of \ :c:func:`tb_xdomain_enable_paths`\ . After call to
this the caller is not expected to use the rings anymore.

.. _`tb_xdomain_disable_paths.return`:

Return
------

\ ``0``\  in case of success and negative errno in case of error

.. _`tb_xdomain_find_by_uuid`:

tb_xdomain_find_by_uuid
=======================

.. c:function:: struct tb_xdomain *tb_xdomain_find_by_uuid(struct tb *tb, const uuid_t *uuid)

    Find an XDomain by UUID

    :param tb:
        Domain where the XDomain belongs to
    :type tb: struct tb \*

    :param uuid:
        UUID to look for
    :type uuid: const uuid_t \*

.. _`tb_xdomain_find_by_uuid.description`:

Description
-----------

Finds XDomain by walking through the Thunderbolt topology below \ ``tb``\ .
The returned XDomain will have its reference count increased so the
caller needs to call \ :c:func:`tb_xdomain_put`\  when it is done with the
object.

This will find all XDomains including the ones that are not yet added
to the bus (handshake is still in progress).

The caller needs to hold \ ``tb->lock``\ .

.. _`tb_xdomain_find_by_link_depth`:

tb_xdomain_find_by_link_depth
=============================

.. c:function:: struct tb_xdomain *tb_xdomain_find_by_link_depth(struct tb *tb, u8 link, u8 depth)

    Find an XDomain by link and depth

    :param tb:
        Domain where the XDomain belongs to
    :type tb: struct tb \*

    :param link:
        Root switch link number
    :type link: u8

    :param depth:
        Depth in the link
    :type depth: u8

.. _`tb_xdomain_find_by_link_depth.description`:

Description
-----------

Finds XDomain by walking through the Thunderbolt topology below \ ``tb``\ .
The returned XDomain will have its reference count increased so the
caller needs to call \ :c:func:`tb_xdomain_put`\  when it is done with the
object.

This will find all XDomains including the ones that are not yet added
to the bus (handshake is still in progress).

The caller needs to hold \ ``tb->lock``\ .

.. _`tb_xdomain_find_by_route`:

tb_xdomain_find_by_route
========================

.. c:function:: struct tb_xdomain *tb_xdomain_find_by_route(struct tb *tb, u64 route)

    Find an XDomain by route string

    :param tb:
        Domain where the XDomain belongs to
    :type tb: struct tb \*

    :param route:
        XDomain route string
    :type route: u64

.. _`tb_xdomain_find_by_route.description`:

Description
-----------

Finds XDomain by walking through the Thunderbolt topology below \ ``tb``\ .
The returned XDomain will have its reference count increased so the
caller needs to call \ :c:func:`tb_xdomain_put`\  when it is done with the
object.

This will find all XDomains including the ones that are not yet added
to the bus (handshake is still in progress).

The caller needs to hold \ ``tb->lock``\ .

.. _`tb_register_property_dir`:

tb_register_property_dir
========================

.. c:function:: int tb_register_property_dir(const char *key, struct tb_property_dir *dir)

    Register property directory to the host

    :param key:
        Key (name) of the directory to add
    :type key: const char \*

    :param dir:
        Directory to add
    :type dir: struct tb_property_dir \*

.. _`tb_register_property_dir.description`:

Description
-----------

Service drivers can use this function to add new property directory
to the host available properties. The other connected hosts are
notified so they can re-read properties of this host if they are
interested.

.. _`tb_register_property_dir.return`:

Return
------

\ ``0``\  on success and negative errno on failure

.. _`tb_unregister_property_dir`:

tb_unregister_property_dir
==========================

.. c:function:: void tb_unregister_property_dir(const char *key, struct tb_property_dir *dir)

    Removes property directory from host

    :param key:
        Key (name) of the directory
    :type key: const char \*

    :param dir:
        Directory to remove
    :type dir: struct tb_property_dir \*

.. _`tb_unregister_property_dir.description`:

Description
-----------

This will remove the existing directory from this host and notify the
connected hosts about the change.

.. This file was automatic generated / don't edit.

