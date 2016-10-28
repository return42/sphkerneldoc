.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rapidio/rio-scan.c

.. _`rio_destid_alloc`:

rio_destid_alloc
================

.. c:function:: u16 rio_destid_alloc(struct rio_net *net)

    Allocate next available destID for given network

    :param struct rio_net \*net:
        RIO network

.. _`rio_destid_alloc.description`:

Description
-----------

Returns next available device destination ID for the specified RIO network.
Marks allocated ID as one in use.
Returns RIO_INVALID_DESTID if new destID is not available.

.. _`rio_destid_reserve`:

rio_destid_reserve
==================

.. c:function:: int rio_destid_reserve(struct rio_net *net, u16 destid)

    Reserve the specivied destID

    :param struct rio_net \*net:
        RIO network

    :param u16 destid:
        destID to reserve

.. _`rio_destid_reserve.description`:

Description
-----------

Tries to reserve the specified destID.
Returns 0 if successful.

.. _`rio_destid_free`:

rio_destid_free
===============

.. c:function:: void rio_destid_free(struct rio_net *net, u16 destid)

    free a previously allocated destID

    :param struct rio_net \*net:
        RIO network

    :param u16 destid:
        destID to free

.. _`rio_destid_free.description`:

Description
-----------

Makes the specified destID available for use.

.. _`rio_destid_first`:

rio_destid_first
================

.. c:function:: u16 rio_destid_first(struct rio_net *net)

    return first destID in use

    :param struct rio_net \*net:
        RIO network

.. _`rio_destid_next`:

rio_destid_next
===============

.. c:function:: u16 rio_destid_next(struct rio_net *net, u16 from)

    return next destID in use

    :param struct rio_net \*net:
        RIO network

    :param u16 from:
        destination ID from which search shall continue

.. _`rio_get_device_id`:

rio_get_device_id
=================

.. c:function:: u16 rio_get_device_id(struct rio_mport *port, u16 destid, u8 hopcount)

    Get the base/extended device id for a device

    :param struct rio_mport \*port:
        RIO master port

    :param u16 destid:
        Destination ID of device

    :param u8 hopcount:
        Hopcount to device

.. _`rio_get_device_id.description`:

Description
-----------

Reads the base/extended device id from a device. Returns the
8/16-bit device ID.

.. _`rio_set_device_id`:

rio_set_device_id
=================

.. c:function:: void rio_set_device_id(struct rio_mport *port, u16 destid, u8 hopcount, u16 did)

    Set the base/extended device id for a device

    :param struct rio_mport \*port:
        RIO master port

    :param u16 destid:
        Destination ID of device

    :param u8 hopcount:
        Hopcount to device

    :param u16 did:
        Device ID value to be written

.. _`rio_set_device_id.description`:

Description
-----------

Writes the base/extended device id from a device.

.. _`rio_clear_locks`:

rio_clear_locks
===============

.. c:function:: int rio_clear_locks(struct rio_net *net)

    Release all host locks and signal enumeration complete

    :param struct rio_net \*net:
        RIO network to run on

.. _`rio_clear_locks.description`:

Description
-----------

Marks the component tag CSR on each device with the enumeration
complete flag. When complete, it then release the host locks on
each device. Returns 0 on success or \ ``-EINVAL``\  on failure.

.. _`rio_enum_host`:

rio_enum_host
=============

.. c:function:: int rio_enum_host(struct rio_mport *port)

    Set host lock and initialize host destination ID

    :param struct rio_mport \*port:
        Master port to issue transaction

.. _`rio_enum_host.description`:

Description
-----------

Sets the local host master port lock and destination ID register
with the host device ID value. The host device ID value is provided
by the platform. Returns \ ``0``\  on success or \ ``-1``\  on failure.

.. _`rio_device_has_destid`:

rio_device_has_destid
=====================

.. c:function:: int rio_device_has_destid(struct rio_mport *port, int src_ops, int dst_ops)

    Test if a device contains a destination ID register

    :param struct rio_mport \*port:
        Master port to issue transaction

    :param int src_ops:
        RIO device source operations

    :param int dst_ops:
        RIO device destination operations

.. _`rio_device_has_destid.description`:

Description
-----------

Checks the provided \ ``src_ops``\  and \ ``dst_ops``\  for the necessary transaction
capabilities that indicate whether or not a device will implement a
destination ID register. Returns 1 if true or 0 if false.

.. _`rio_release_dev`:

rio_release_dev
===============

.. c:function:: void rio_release_dev(struct device *dev)

    Frees a RIO device struct

    :param struct device \*dev:
        LDM device associated with a RIO device struct

.. _`rio_release_dev.description`:

Description
-----------

Gets the RIO device struct associated a RIO device struct.
The RIO device struct is freed.

.. _`rio_is_switch`:

rio_is_switch
=============

.. c:function:: int rio_is_switch(struct rio_dev *rdev)

    Tests if a RIO device has switch capabilities

    :param struct rio_dev \*rdev:
        RIO device

.. _`rio_is_switch.description`:

Description
-----------

Gets the RIO device Processing Element Features register
contents and tests for switch capabilities. Returns 1 if
the device is a switch or 0 if it is not a switch.
The RIO device struct is freed.

.. _`rio_setup_device`:

rio_setup_device
================

.. c:function:: struct rio_dev *rio_setup_device(struct rio_net *net, struct rio_mport *port, u16 destid, u8 hopcount, int do_enum)

    Allocates and sets up a RIO device

    :param struct rio_net \*net:
        RIO network

    :param struct rio_mport \*port:
        Master port to send transactions

    :param u16 destid:
        Current destination ID

    :param u8 hopcount:
        Current hopcount

    :param int do_enum:
        Enumeration/Discovery mode flag

.. _`rio_setup_device.description`:

Description
-----------

Allocates a RIO device and configures fields based on configuration
space contents. If device has a destination ID register, a destination
ID is either assigned in enumeration mode or read from configuration
space in discovery mode.  If the device has switch capabilities, then
a switch is allocated and configured appropriately. Returns a pointer
to a RIO device on success or NULL on failure.

.. _`rio_sport_is_active`:

rio_sport_is_active
===================

.. c:function:: int rio_sport_is_active(struct rio_mport *port, u16 destid, u8 hopcount, int sport)

    Tests if a switch port has an active connection.

    :param struct rio_mport \*port:
        Master port to send transaction

    :param u16 destid:
        Associated destination ID for switch

    :param u8 hopcount:
        Hopcount to reach switch

    :param int sport:
        Switch port number

.. _`rio_sport_is_active.description`:

Description
-----------

Reads the port error status CSR for a particular switch port to
determine if the port has an active link.  Returns
\ ``RIO_PORT_N_ERR_STS_PORT_OK``\  if the port is active or \ ``0``\  if it is
inactive.

.. _`rio_get_host_deviceid_lock`:

rio_get_host_deviceid_lock
==========================

.. c:function:: u16 rio_get_host_deviceid_lock(struct rio_mport *port, u8 hopcount)

    Reads the Host Device ID Lock CSR on a device

    :param struct rio_mport \*port:
        Master port to send transaction

    :param u8 hopcount:
        Number of hops to the device

.. _`rio_get_host_deviceid_lock.description`:

Description
-----------

Used during enumeration to read the Host Device ID Lock CSR on a
RIO device. Returns the value of the lock register.

.. _`rio_enum_peer`:

rio_enum_peer
=============

.. c:function:: int rio_enum_peer(struct rio_net *net, struct rio_mport *port, u8 hopcount, struct rio_dev *prev, int prev_port)

    Recursively enumerate a RIO network through a master port

    :param struct rio_net \*net:
        RIO network being enumerated

    :param struct rio_mport \*port:
        Master port to send transactions

    :param u8 hopcount:
        Number of hops into the network

    :param struct rio_dev \*prev:
        Previous RIO device connected to the enumerated one

    :param int prev_port:
        Port on previous RIO device

.. _`rio_enum_peer.description`:

Description
-----------

Recursively enumerates a RIO network.  Transactions are sent via the
master port passed in \ ``port``\ .

.. _`rio_enum_complete`:

rio_enum_complete
=================

.. c:function:: int rio_enum_complete(struct rio_mport *port)

    Tests if enumeration of a network is complete

    :param struct rio_mport \*port:
        Master port to send transaction

.. _`rio_enum_complete.description`:

Description
-----------

Tests the PGCCSR discovered bit for non-zero value (enumeration
complete flag). Return \ ``1``\  if enumeration is complete or \ ``0``\  if
enumeration is incomplete.

.. _`rio_disc_peer`:

rio_disc_peer
=============

.. c:function:: int rio_disc_peer(struct rio_net *net, struct rio_mport *port, u16 destid, u8 hopcount, struct rio_dev *prev, int prev_port)

    Recursively discovers a RIO network through a master port

    :param struct rio_net \*net:
        RIO network being discovered

    :param struct rio_mport \*port:
        Master port to send transactions

    :param u16 destid:
        Current destination ID in network

    :param u8 hopcount:
        Number of hops into the network

    :param struct rio_dev \*prev:
        previous rio_dev

    :param int prev_port:
        previous port number

.. _`rio_disc_peer.description`:

Description
-----------

Recursively discovers a RIO network.  Transactions are sent via the
master port passed in \ ``port``\ .

.. _`rio_mport_is_active`:

rio_mport_is_active
===================

.. c:function:: int rio_mport_is_active(struct rio_mport *port)

    Tests if master port link is active

    :param struct rio_mport \*port:
        Master port to test

.. _`rio_mport_is_active.description`:

Description
-----------

Reads the port error status CSR for the master port to
determine if the port has an active link.  Returns
\ ``RIO_PORT_N_ERR_STS_PORT_OK``\  if the  master port is active
or \ ``0``\  if it is inactive.

.. _`rio_update_route_tables`:

rio_update_route_tables
=======================

.. c:function:: void rio_update_route_tables(struct rio_net *net)

    Updates route tables in switches

    :param struct rio_net \*net:
        RIO network to run update on

.. _`rio_update_route_tables.description`:

Description
-----------

For each enumerated device, ensure that each switch in a system
has correct routing entries. Add routes for devices that where
unknown dirung the first enumeration pass through the switch.

.. _`rio_init_em`:

rio_init_em
===========

.. c:function:: void rio_init_em(struct rio_dev *rdev)

    Initializes RIO Error Management (for switches)

    :param struct rio_dev \*rdev:
        RIO device

.. _`rio_init_em.description`:

Description
-----------

For each enumerated switch, call device-specific error management
initialization routine (if supplied by the switch driver).

.. _`rio_enum_mport`:

rio_enum_mport
==============

.. c:function:: int rio_enum_mport(struct rio_mport *mport, u32 flags)

    Start enumeration through a master port

    :param struct rio_mport \*mport:
        Master port to send transactions

    :param u32 flags:
        Enumeration control flags

.. _`rio_enum_mport.description`:

Description
-----------

Starts the enumeration process. If somebody has enumerated our
master port device, then give up. If not and we have an active
link, then start recursive peer enumeration. Returns \ ``0``\  if
enumeration succeeds or \ ``-EBUSY``\  if enumeration fails.

.. _`rio_build_route_tables`:

rio_build_route_tables
======================

.. c:function:: void rio_build_route_tables(struct rio_net *net)

    Generate route tables from switch route entries

    :param struct rio_net \*net:
        RIO network to run route tables scan on

.. _`rio_build_route_tables.description`:

Description
-----------

For each switch device, generate a route table by copying existing
route entries from the switch.

.. _`rio_disc_mport`:

rio_disc_mport
==============

.. c:function:: int rio_disc_mport(struct rio_mport *mport, u32 flags)

    Start discovery through a master port

    :param struct rio_mport \*mport:
        Master port to send transactions

    :param u32 flags:
        discovery control flags

.. _`rio_disc_mport.description`:

Description
-----------

Starts the discovery process. If we have an active link,
then wait for the signal that enumeration is complete (if wait
is allowed).
When enumeration completion is signaled, start recursive
peer discovery. Returns \ ``0``\  if discovery succeeds or \ ``-EBUSY``\ 
on failure.

.. _`rio_basic_attach`:

rio_basic_attach
================

.. c:function:: int rio_basic_attach( void)

    :param  void:
        no arguments

.. _`rio_basic_attach.description`:

Description
-----------

When this enumeration/discovery method is loaded as a module this function
registers its specific enumeration and discover routines for all available
RapidIO mport devices. The "scan" command line parameter controls ability of
the module to start RapidIO enumeration/discovery automatically.

Returns 0 for success or -EIO if unable to register itself.

This enumeration/discovery method cannot be unloaded and therefore does not
provide a matching cleanup_module routine.

.. This file was automatic generated / don't edit.

