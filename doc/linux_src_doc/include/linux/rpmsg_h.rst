.. -*- coding: utf-8; mode: rst -*-

=======
rpmsg.h
=======


.. _`rpmsg_hdr`:

struct rpmsg_hdr
================

.. c:type:: rpmsg_hdr

    common header for all rpmsg messages


.. _`rpmsg_hdr.definition`:

Definition
----------

.. code-block:: c

  struct rpmsg_hdr {
    u32 src;
    u32 dst;
    u32 reserved;
    u16 len;
    u16 flags;
    u8 data[0];
  };


.. _`rpmsg_hdr.members`:

Members
-------

:``src``:
    source address

:``dst``:
    destination address

:``reserved``:
    reserved for future use

:``len``:
    length of payload (in bytes)

:``flags``:
    message flags

:``data[0]``:
    ``len`` bytes of message payload data




.. _`rpmsg_hdr.description`:

Description
-----------

Every message sent(/received) on the rpmsg bus begins with this header.



.. _`rpmsg_ns_msg`:

struct rpmsg_ns_msg
===================

.. c:type:: rpmsg_ns_msg

    dynamic name service announcement message


.. _`rpmsg_ns_msg.definition`:

Definition
----------

.. code-block:: c

  struct rpmsg_ns_msg {
    char name[RPMSG_NAME_SIZE];
    u32 addr;
    u32 flags;
  };


.. _`rpmsg_ns_msg.members`:

Members
-------

:``name[RPMSG_NAME_SIZE]``:
    name of remote service that is published

:``addr``:
    address of remote service that is published

:``flags``:
    indicates whether service is created or destroyed




.. _`rpmsg_ns_msg.description`:

Description
-----------

This message is sent across to publish a new service, or announce
about its removal. When we receive these messages, an appropriate
rpmsg channel (i.e device) is created/destroyed. In turn, the ->:c:func:`probe`
or ->:c:func:`remove` handler of the appropriate rpmsg driver will be invoked
(if/as-soon-as one is registered).



.. _`rpmsg_ns_flags`:

enum rpmsg_ns_flags
===================

.. c:type:: rpmsg_ns_flags

    dynamic name service announcement flags


.. _`rpmsg_ns_flags.definition`:

Definition
----------

.. code-block:: c

    enum rpmsg_ns_flags {
      RPMSG_NS_CREATE,
      RPMSG_NS_DESTROY
    };


.. _`rpmsg_ns_flags.constants`:

Constants
---------

:``RPMSG_NS_CREATE``:
    a new remote service was just created

:``RPMSG_NS_DESTROY``:
    a known remote service was just destroyed


.. _`rpmsg_endpoint`:

struct rpmsg_endpoint
=====================

.. c:type:: rpmsg_endpoint

    binds a local rpmsg address to its user


.. _`rpmsg_endpoint.definition`:

Definition
----------

.. code-block:: c

  struct rpmsg_endpoint {
    struct rpmsg_channel * rpdev;
    struct kref refcount;
    rpmsg_rx_cb_t cb;
    struct mutex cb_lock;
    u32 addr;
    void * priv;
  };


.. _`rpmsg_endpoint.members`:

Members
-------

:``rpdev``:
    rpmsg channel device

:``refcount``:
    when this drops to zero, the ept is deallocated

:``cb``:
    rx callback handler

:``cb_lock``:
    must be taken before accessing/changing ``cb``

:``addr``:
    local rpmsg address

:``priv``:
    private data for the driver's use




.. _`rpmsg_endpoint.description`:

Description
-----------

In essence, an rpmsg endpoint represents a listener on the rpmsg bus, as
it binds an rpmsg address with an rx callback handler.

Simple rpmsg drivers shouldn't use this struct directly, because



.. _`rpmsg_endpoint.things-just-work`:

things just work
----------------

every rpmsg driver provides an rx callback upon
registering to the bus, and that callback is then bound to its rpmsg
address when the driver is probed. When relevant inbound messages arrive
(i.e. messages which their dst address equals to the src address of
the rpmsg channel), the driver's handler is invoked to process it.

More complicated drivers though, that do need to allocate additional rpmsg
addresses, and bind them to different rx callbacks, must explicitly
create additional endpoints by themselves (see :c:func:`rpmsg_create_ept`).



.. _`rpmsg_driver`:

struct rpmsg_driver
===================

.. c:type:: rpmsg_driver

    rpmsg driver struct


.. _`rpmsg_driver.definition`:

Definition
----------

.. code-block:: c

  struct rpmsg_driver {
    struct device_driver drv;
    const struct rpmsg_device_id * id_table;
    int (* probe) (struct rpmsg_channel *dev);
    void (* remove) (struct rpmsg_channel *dev);
    void (* callback) (struct rpmsg_channel *, void *, int, void *, u32);
  };


.. _`rpmsg_driver.members`:

Members
-------

:``drv``:
    underlying device driver

:``id_table``:
    rpmsg ids serviced by this driver

:``probe``:
    invoked when a matching rpmsg channel (i.e. device) is found

:``remove``:
    invoked when the rpmsg channel is removed

:``callback``:
    invoked when an inbound message is received on the channel




.. _`rpmsg_send`:

rpmsg_send
==========

.. c:function:: int rpmsg_send (struct rpmsg_channel *rpdev, void *data, int len)

    send a message across to the remote processor

    :param struct rpmsg_channel \*rpdev:
        the rpmsg channel

    :param void \*data:
        payload of message

    :param int len:
        length of payload



.. _`rpmsg_send.description`:

Description
-----------

This function sends ``data`` of length ``len`` on the ``rpdev`` channel.
The message will be sent to the remote processor which the ``rpdev``
channel belongs to, using ``rpdev``\ 's source and destination addresses.
In case there are no TX buffers available, the function will block until
one becomes available, or a timeout of 15 seconds elapses. When the latter
happens, -ERESTARTSYS is returned.

Can only be called from process context (for now).

Returns 0 on success and an appropriate error value on failure.



.. _`rpmsg_sendto`:

rpmsg_sendto
============

.. c:function:: int rpmsg_sendto (struct rpmsg_channel *rpdev, void *data, int len, u32 dst)

    send a message across to the remote processor, specify dst

    :param struct rpmsg_channel \*rpdev:
        the rpmsg channel

    :param void \*data:
        payload of message

    :param int len:
        length of payload

    :param u32 dst:
        destination address



.. _`rpmsg_sendto.description`:

Description
-----------

This function sends ``data`` of length ``len`` to the remote ``dst`` address.
The message will be sent to the remote processor which the ``rpdev``
channel belongs to, using ``rpdev``\ 's source address.
In case there are no TX buffers available, the function will block until
one becomes available, or a timeout of 15 seconds elapses. When the latter
happens, -ERESTARTSYS is returned.

Can only be called from process context (for now).

Returns 0 on success and an appropriate error value on failure.



.. _`rpmsg_send_offchannel`:

rpmsg_send_offchannel
=====================

.. c:function:: int rpmsg_send_offchannel (struct rpmsg_channel *rpdev, u32 src, u32 dst, void *data, int len)

    send a message using explicit src/dst addresses

    :param struct rpmsg_channel \*rpdev:
        the rpmsg channel

    :param u32 src:
        source address

    :param u32 dst:
        destination address

    :param void \*data:
        payload of message

    :param int len:
        length of payload



.. _`rpmsg_send_offchannel.description`:

Description
-----------

This function sends ``data`` of length ``len`` to the remote ``dst`` address,
and uses ``src`` as the source address.
The message will be sent to the remote processor which the ``rpdev``
channel belongs to.
In case there are no TX buffers available, the function will block until
one becomes available, or a timeout of 15 seconds elapses. When the latter
happens, -ERESTARTSYS is returned.

Can only be called from process context (for now).

Returns 0 on success and an appropriate error value on failure.



.. _`rpmsg_trysend`:

rpmsg_trysend
=============

.. c:function:: int rpmsg_trysend (struct rpmsg_channel *rpdev, void *data, int len)

    send a message across to the remote processor

    :param struct rpmsg_channel \*rpdev:
        the rpmsg channel

    :param void \*data:
        payload of message

    :param int len:
        length of payload



.. _`rpmsg_trysend.description`:

Description
-----------

This function sends ``data`` of length ``len`` on the ``rpdev`` channel.
The message will be sent to the remote processor which the ``rpdev``
channel belongs to, using ``rpdev``\ 's source and destination addresses.
In case there are no TX buffers available, the function will immediately
return -ENOMEM without waiting until one becomes available.

Can only be called from process context (for now).

Returns 0 on success and an appropriate error value on failure.



.. _`rpmsg_trysendto`:

rpmsg_trysendto
===============

.. c:function:: int rpmsg_trysendto (struct rpmsg_channel *rpdev, void *data, int len, u32 dst)

    send a message across to the remote processor, specify dst

    :param struct rpmsg_channel \*rpdev:
        the rpmsg channel

    :param void \*data:
        payload of message

    :param int len:
        length of payload

    :param u32 dst:
        destination address



.. _`rpmsg_trysendto.description`:

Description
-----------

This function sends ``data`` of length ``len`` to the remote ``dst`` address.
The message will be sent to the remote processor which the ``rpdev``
channel belongs to, using ``rpdev``\ 's source address.
In case there are no TX buffers available, the function will immediately
return -ENOMEM without waiting until one becomes available.

Can only be called from process context (for now).

Returns 0 on success and an appropriate error value on failure.



.. _`rpmsg_trysend_offchannel`:

rpmsg_trysend_offchannel
========================

.. c:function:: int rpmsg_trysend_offchannel (struct rpmsg_channel *rpdev, u32 src, u32 dst, void *data, int len)

    send a message using explicit src/dst addresses

    :param struct rpmsg_channel \*rpdev:
        the rpmsg channel

    :param u32 src:
        source address

    :param u32 dst:
        destination address

    :param void \*data:
        payload of message

    :param int len:
        length of payload



.. _`rpmsg_trysend_offchannel.description`:

Description
-----------

This function sends ``data`` of length ``len`` to the remote ``dst`` address,
and uses ``src`` as the source address.
The message will be sent to the remote processor which the ``rpdev``
channel belongs to.
In case there are no TX buffers available, the function will immediately
return -ENOMEM without waiting until one becomes available.

Can only be called from process context (for now).

Returns 0 on success and an appropriate error value on failure.

