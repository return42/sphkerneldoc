.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/rapidio/rio.c

.. _`rio_local_get_device_id`:

rio_local_get_device_id
=======================

.. c:function:: u16 rio_local_get_device_id(struct rio_mport *port)

    Get the base/extended device id for a port

    :param port:
        RIO master port from which to get the deviceid
    :type port: struct rio_mport \*

.. _`rio_local_get_device_id.description`:

Description
-----------

Reads the base/extended device id from the local device
implementing the master port. Returns the 8/16-bit device
id.

.. _`rio_query_mport`:

rio_query_mport
===============

.. c:function:: int rio_query_mport(struct rio_mport *port, struct rio_mport_attr *mport_attr)

    Query mport device attributes

    :param port:
        mport device to query
    :type port: struct rio_mport \*

    :param mport_attr:
        mport attributes data structure
    :type mport_attr: struct rio_mport_attr \*

.. _`rio_query_mport.description`:

Description
-----------

Returns attributes of specified mport through the
pointer to attributes data structure.

.. _`rio_alloc_net`:

rio_alloc_net
=============

.. c:function:: struct rio_net *rio_alloc_net(struct rio_mport *mport)

    Allocate and initialize a new RIO network data structure

    :param mport:
        Master port associated with the RIO network
    :type mport: struct rio_mport \*

.. _`rio_alloc_net.description`:

Description
-----------

Allocates a RIO network structure, initializes per-network
list heads, and adds the associated master port to the
network list of associated master ports. Returns a
RIO network pointer on success or \ ``NULL``\  on failure.

.. _`rio_local_set_device_id`:

rio_local_set_device_id
=======================

.. c:function:: void rio_local_set_device_id(struct rio_mport *port, u16 did)

    Set the base/extended device id for a port

    :param port:
        RIO master port
    :type port: struct rio_mport \*

    :param did:
        Device ID value to be written
    :type did: u16

.. _`rio_local_set_device_id.description`:

Description
-----------

Writes the base/extended device id from a device.

.. _`rio_add_device`:

rio_add_device
==============

.. c:function:: int rio_add_device(struct rio_dev *rdev)

    Adds a RIO device to the device model

    :param rdev:
        RIO device
    :type rdev: struct rio_dev \*

.. _`rio_add_device.description`:

Description
-----------

Adds the RIO device to the global device list and adds the RIO
device to the RIO device list.  Creates the generic sysfs nodes
for an RIO device.

.. _`rio_request_inb_mbox`:

rio_request_inb_mbox
====================

.. c:function:: int rio_request_inb_mbox(struct rio_mport *mport, void *dev_id, int mbox, int entries, void (*minb)(struct rio_mport * mport, void *dev_id, int mbox, int slot))

    request inbound mailbox service

    :param mport:
        RIO master port from which to allocate the mailbox resource
    :type mport: struct rio_mport \*

    :param dev_id:
        Device specific pointer to pass on event
    :type dev_id: void \*

    :param mbox:
        Mailbox number to claim
    :type mbox: int

    :param entries:
        Number of entries in inbound mailbox queue
    :type entries: int

    :param void (\*minb)(struct rio_mport \* mport, void \*dev_id, int mbox, int slot):
        Callback to execute when inbound message is received

.. _`rio_request_inb_mbox.description`:

Description
-----------

Requests ownership of an inbound mailbox resource and binds
a callback function to the resource. Returns \ ``0``\  on success.

.. _`rio_release_inb_mbox`:

rio_release_inb_mbox
====================

.. c:function:: int rio_release_inb_mbox(struct rio_mport *mport, int mbox)

    release inbound mailbox message service

    :param mport:
        RIO master port from which to release the mailbox resource
    :type mport: struct rio_mport \*

    :param mbox:
        Mailbox number to release
    :type mbox: int

.. _`rio_release_inb_mbox.description`:

Description
-----------

Releases ownership of an inbound mailbox resource. Returns 0
if the request has been satisfied.

.. _`rio_request_outb_mbox`:

rio_request_outb_mbox
=====================

.. c:function:: int rio_request_outb_mbox(struct rio_mport *mport, void *dev_id, int mbox, int entries, void (*moutb)(struct rio_mport * mport, void *dev_id, int mbox, int slot))

    request outbound mailbox service

    :param mport:
        RIO master port from which to allocate the mailbox resource
    :type mport: struct rio_mport \*

    :param dev_id:
        Device specific pointer to pass on event
    :type dev_id: void \*

    :param mbox:
        Mailbox number to claim
    :type mbox: int

    :param entries:
        Number of entries in outbound mailbox queue
    :type entries: int

    :param void (\*moutb)(struct rio_mport \* mport, void \*dev_id, int mbox, int slot):
        Callback to execute when outbound message is sent

.. _`rio_request_outb_mbox.description`:

Description
-----------

Requests ownership of an outbound mailbox resource and binds
a callback function to the resource. Returns 0 on success.

.. _`rio_release_outb_mbox`:

rio_release_outb_mbox
=====================

.. c:function:: int rio_release_outb_mbox(struct rio_mport *mport, int mbox)

    release outbound mailbox message service

    :param mport:
        RIO master port from which to release the mailbox resource
    :type mport: struct rio_mport \*

    :param mbox:
        Mailbox number to release
    :type mbox: int

.. _`rio_release_outb_mbox.description`:

Description
-----------

Releases ownership of an inbound mailbox resource. Returns 0
if the request has been satisfied.

.. _`rio_setup_inb_dbell`:

rio_setup_inb_dbell
===================

.. c:function:: int rio_setup_inb_dbell(struct rio_mport *mport, void *dev_id, struct resource *res, void (*dinb)(struct rio_mport * mport, void *dev_id, u16 src, u16 dst, u16 info))

    bind inbound doorbell callback

    :param mport:
        RIO master port to bind the doorbell callback
    :type mport: struct rio_mport \*

    :param dev_id:
        Device specific pointer to pass on event
    :type dev_id: void \*

    :param res:
        Doorbell message resource
    :type res: struct resource \*

    :param void (\*dinb)(struct rio_mport \* mport, void \*dev_id, u16 src, u16 dst, u16 info):
        Callback to execute when doorbell is received

.. _`rio_setup_inb_dbell.description`:

Description
-----------

Adds a doorbell resource/callback pair into a port's
doorbell event list. Returns 0 if the request has been
satisfied.

.. _`rio_request_inb_dbell`:

rio_request_inb_dbell
=====================

.. c:function:: int rio_request_inb_dbell(struct rio_mport *mport, void *dev_id, u16 start, u16 end, void (*dinb)(struct rio_mport * mport, void *dev_id, u16 src, u16 dst, u16 info))

    request inbound doorbell message service

    :param mport:
        RIO master port from which to allocate the doorbell resource
    :type mport: struct rio_mport \*

    :param dev_id:
        Device specific pointer to pass on event
    :type dev_id: void \*

    :param start:
        Doorbell info range start
    :type start: u16

    :param end:
        Doorbell info range end
    :type end: u16

    :param void (\*dinb)(struct rio_mport \* mport, void \*dev_id, u16 src, u16 dst, u16 info):
        Callback to execute when doorbell is received

.. _`rio_request_inb_dbell.description`:

Description
-----------

Requests ownership of an inbound doorbell resource and binds
a callback function to the resource. Returns 0 if the request
has been satisfied.

.. _`rio_release_inb_dbell`:

rio_release_inb_dbell
=====================

.. c:function:: int rio_release_inb_dbell(struct rio_mport *mport, u16 start, u16 end)

    release inbound doorbell message service

    :param mport:
        RIO master port from which to release the doorbell resource
    :type mport: struct rio_mport \*

    :param start:
        Doorbell info range start
    :type start: u16

    :param end:
        Doorbell info range end
    :type end: u16

.. _`rio_release_inb_dbell.description`:

Description
-----------

Releases ownership of an inbound doorbell resource and removes
callback from the doorbell event list. Returns 0 if the request
has been satisfied.

.. _`rio_request_outb_dbell`:

rio_request_outb_dbell
======================

.. c:function:: struct resource *rio_request_outb_dbell(struct rio_dev *rdev, u16 start, u16 end)

    request outbound doorbell message range

    :param rdev:
        RIO device from which to allocate the doorbell resource
    :type rdev: struct rio_dev \*

    :param start:
        Doorbell message range start
    :type start: u16

    :param end:
        Doorbell message range end
    :type end: u16

.. _`rio_request_outb_dbell.description`:

Description
-----------

Requests ownership of a doorbell message range. Returns a resource
if the request has been satisfied or \ ``NULL``\  on failure.

.. _`rio_release_outb_dbell`:

rio_release_outb_dbell
======================

.. c:function:: int rio_release_outb_dbell(struct rio_dev *rdev, struct resource *res)

    release outbound doorbell message range

    :param rdev:
        RIO device from which to release the doorbell resource
    :type rdev: struct rio_dev \*

    :param res:
        Doorbell resource to be freed
    :type res: struct resource \*

.. _`rio_release_outb_dbell.description`:

Description
-----------

Releases ownership of a doorbell message range. Returns 0 if the
request has been satisfied.

.. _`rio_add_mport_pw_handler`:

rio_add_mport_pw_handler
========================

.. c:function:: int rio_add_mport_pw_handler(struct rio_mport *mport, void *context, int (*pwcback)(struct rio_mport *mport, void *context, union rio_pw_msg *msg, int step))

    add port-write message handler into the list of mport specific pw handlers

    :param mport:
        RIO master port to bind the portwrite callback
    :type mport: struct rio_mport \*

    :param context:
        Handler specific context to pass on event
    :type context: void \*

    :param int (\*pwcback)(struct rio_mport \*mport, void \*context, union rio_pw_msg \*msg, int step):
        Callback to execute when portwrite is received

.. _`rio_add_mport_pw_handler.description`:

Description
-----------

Returns 0 if the request has been satisfied.

.. _`rio_del_mport_pw_handler`:

rio_del_mport_pw_handler
========================

.. c:function:: int rio_del_mport_pw_handler(struct rio_mport *mport, void *context, int (*pwcback)(struct rio_mport *mport, void *context, union rio_pw_msg *msg, int step))

    remove port-write message handler from the list of mport specific pw handlers

    :param mport:
        RIO master port to bind the portwrite callback
    :type mport: struct rio_mport \*

    :param context:
        Registered handler specific context to pass on event
    :type context: void \*

    :param int (\*pwcback)(struct rio_mport \*mport, void \*context, union rio_pw_msg \*msg, int step):
        Registered callback function

.. _`rio_del_mport_pw_handler.description`:

Description
-----------

Returns 0 if the request has been satisfied.

.. _`rio_request_inb_pwrite`:

rio_request_inb_pwrite
======================

.. c:function:: int rio_request_inb_pwrite(struct rio_dev *rdev, int (*pwcback)(struct rio_dev *rdev, union rio_pw_msg *msg, int step))

    request inbound port-write message service for specific RapidIO device

    :param rdev:
        RIO device to which register inbound port-write callback routine
    :type rdev: struct rio_dev \*

    :param int (\*pwcback)(struct rio_dev \*rdev, union rio_pw_msg \*msg, int step):
        Callback routine to execute when port-write is received

.. _`rio_request_inb_pwrite.description`:

Description
-----------

Binds a port-write callback function to the RapidIO device.
Returns 0 if the request has been satisfied.

.. _`rio_release_inb_pwrite`:

rio_release_inb_pwrite
======================

.. c:function:: int rio_release_inb_pwrite(struct rio_dev *rdev)

    release inbound port-write message service associated with specific RapidIO device

    :param rdev:
        RIO device which registered for inbound port-write callback
    :type rdev: struct rio_dev \*

.. _`rio_release_inb_pwrite.description`:

Description
-----------

Removes callback from the rio_dev structure. Returns 0 if the request
has been satisfied.

.. _`rio_pw_enable`:

rio_pw_enable
=============

.. c:function:: void rio_pw_enable(struct rio_mport *mport, int enable)

    Enables/disables port-write handling by a master port

    :param mport:
        Master port associated with port-write handling
    :type mport: struct rio_mport \*

    :param enable:
        1=enable,  0=disable
    :type enable: int

.. _`rio_map_inb_region`:

rio_map_inb_region
==================

.. c:function:: int rio_map_inb_region(struct rio_mport *mport, dma_addr_t local, u64 rbase, u32 size, u32 rflags)

    - Map inbound memory region.

    :param mport:
        Master port.
    :type mport: struct rio_mport \*

    :param local:
        physical address of memory region to be mapped
    :type local: dma_addr_t

    :param rbase:
        RIO base address assigned to this window
    :type rbase: u64

    :param size:
        Size of the memory region
    :type size: u32

    :param rflags:
        Flags for mapping.
    :type rflags: u32

.. _`rio_map_inb_region.return`:

Return
------

0 -- Success.

This function will create the mapping from RIO space to local memory.

.. _`rio_unmap_inb_region`:

rio_unmap_inb_region
====================

.. c:function:: void rio_unmap_inb_region(struct rio_mport *mport, dma_addr_t lstart)

    - Unmap the inbound memory region

    :param mport:
        Master port
    :type mport: struct rio_mport \*

    :param lstart:
        physical address of memory region to be unmapped
    :type lstart: dma_addr_t

.. _`rio_map_outb_region`:

rio_map_outb_region
===================

.. c:function:: int rio_map_outb_region(struct rio_mport *mport, u16 destid, u64 rbase, u32 size, u32 rflags, dma_addr_t *local)

    - Map outbound memory region.

    :param mport:
        Master port.
    :type mport: struct rio_mport \*

    :param destid:
        destination id window points to
    :type destid: u16

    :param rbase:
        RIO base address window translates to
    :type rbase: u64

    :param size:
        Size of the memory region
    :type size: u32

    :param rflags:
        Flags for mapping.
    :type rflags: u32

    :param local:
        physical address of memory region mapped
    :type local: dma_addr_t \*

.. _`rio_map_outb_region.return`:

Return
------

0 -- Success.

This function will create the mapping from RIO space to local memory.

.. _`rio_unmap_outb_region`:

rio_unmap_outb_region
=====================

.. c:function:: void rio_unmap_outb_region(struct rio_mport *mport, u16 destid, u64 rstart)

    - Unmap the inbound memory region

    :param mport:
        Master port
    :type mport: struct rio_mport \*

    :param destid:
        destination id mapping points to
    :type destid: u16

    :param rstart:
        RIO base address window translates to
    :type rstart: u64

.. _`rio_mport_get_physefb`:

rio_mport_get_physefb
=====================

.. c:function:: u32 rio_mport_get_physefb(struct rio_mport *port, int local, u16 destid, u8 hopcount, u32 *rmap)

    Helper function that returns register offset for Physical Layer Extended Features Block.

    :param port:
        Master port to issue transaction
    :type port: struct rio_mport \*

    :param local:
        Indicate a local master port or remote device access
    :type local: int

    :param destid:
        Destination ID of the device
    :type destid: u16

    :param hopcount:
        Number of switch hops to the device
    :type hopcount: u8

    :param rmap:
        pointer to location to store register map type info
    :type rmap: u32 \*

.. _`rio_get_comptag`:

rio_get_comptag
===============

.. c:function:: struct rio_dev *rio_get_comptag(u32 comp_tag, struct rio_dev *from)

    Begin or continue searching for a RIO device by component tag

    :param comp_tag:
        RIO component tag to match
    :type comp_tag: u32

    :param from:
        Previous RIO device found in search, or \ ``NULL``\  for new search
    :type from: struct rio_dev \*

.. _`rio_get_comptag.description`:

Description
-----------

Iterates through the list of known RIO devices. If a RIO device is
found with a matching \ ``comp_tag``\ , a pointer to its device
structure is returned. Otherwise, \ ``NULL``\  is returned. A new search
is initiated by passing \ ``NULL``\  to the \ ``from``\  argument. Otherwise, if
\ ``from``\  is not \ ``NULL``\ , searches continue from next device on the global
list.

.. _`rio_set_port_lockout`:

rio_set_port_lockout
====================

.. c:function:: int rio_set_port_lockout(struct rio_dev *rdev, u32 pnum, int lock)

    Sets/clears LOCKOUT bit (RIO EM 1.3) for a switch port.

    :param rdev:
        Pointer to RIO device control structure
    :type rdev: struct rio_dev \*

    :param pnum:
        Switch port number to set LOCKOUT bit
    :type pnum: u32

    :param lock:
        Operation : set (=1) or clear (=0)
    :type lock: int

.. _`rio_enable_rx_tx_port`:

rio_enable_rx_tx_port
=====================

.. c:function:: int rio_enable_rx_tx_port(struct rio_mport *port, int local, u16 destid, u8 hopcount, u8 port_num)

    enable input receiver and output transmitter of given port

    :param port:
        Master port associated with the RIO network
    :type port: struct rio_mport \*

    :param local:
        local=1 select local port otherwise a far device is reached
    :type local: int

    :param destid:
        Destination ID of the device to check host bit
    :type destid: u16

    :param hopcount:
        Number of hops to reach the target
    :type hopcount: u8

    :param port_num:
        Port (-number on switch) to enable on a far end device
    :type port_num: u8

.. _`rio_enable_rx_tx_port.description`:

Description
-----------

Returns 0 or 1 from on General Control Command and Status Register
(EXT_PTR+0x3C)

.. _`rio_chk_dev_route`:

rio_chk_dev_route
=================

.. c:function:: int rio_chk_dev_route(struct rio_dev *rdev, struct rio_dev **nrdev, int *npnum)

    Validate route to the specified device.

    :param rdev:
        RIO device failed to respond
    :type rdev: struct rio_dev \*

    :param nrdev:
        Last active device on the route to rdev
    :type nrdev: struct rio_dev \*\*

    :param npnum:
        nrdev's port number on the route to rdev
    :type npnum: int \*

.. _`rio_chk_dev_route.description`:

Description
-----------

Follows a route to the specified RIO device to determine the last available
device (and corresponding RIO port) on the route.

.. _`rio_mport_chk_dev_access`:

rio_mport_chk_dev_access
========================

.. c:function:: int rio_mport_chk_dev_access(struct rio_mport *mport, u16 destid, u8 hopcount)

    Validate access to the specified device.

    :param mport:
        Master port to send transactions
    :type mport: struct rio_mport \*

    :param destid:
        Device destination ID in network
    :type destid: u16

    :param hopcount:
        Number of hops into the network
    :type hopcount: u8

.. _`rio_chk_dev_access`:

rio_chk_dev_access
==================

.. c:function:: int rio_chk_dev_access(struct rio_dev *rdev)

    Validate access to the specified device.

    :param rdev:
        Pointer to RIO device control structure
    :type rdev: struct rio_dev \*

.. _`rio_get_input_status`:

rio_get_input_status
====================

.. c:function:: int rio_get_input_status(struct rio_dev *rdev, int pnum, u32 *lnkresp)

    Sends a Link-Request/Input-Status control symbol and returns link-response (if requested).

    :param rdev:
        RIO devive to issue Input-status command
    :type rdev: struct rio_dev \*

    :param pnum:
        Device port number to issue the command
    :type pnum: int

    :param lnkresp:
        Response from a link partner
    :type lnkresp: u32 \*

.. _`rio_clr_err_stopped`:

rio_clr_err_stopped
===================

.. c:function:: int rio_clr_err_stopped(struct rio_dev *rdev, u32 pnum, u32 err_status)

    Clears port Error-stopped states.

    :param rdev:
        Pointer to RIO device control structure
    :type rdev: struct rio_dev \*

    :param pnum:
        Switch port number to clear errors
    :type pnum: u32

    :param err_status:
        port error status (if 0 reads register from device)
    :type err_status: u32

.. _`rio_clr_err_stopped.description`:

Description
-----------

TODO: Currently this routine is not compatible with recovery process
specified for idt_gen3 RapidIO switch devices. It has to be reviewed
to implement universal recovery process that is compatible full range
off available devices.
IDT gen3 switch driver now implements HW-specific error handler that
issues soft port reset to the port to reset ERR_STOP bits and ackIDs.

.. _`rio_inb_pwrite_handler`:

rio_inb_pwrite_handler
======================

.. c:function:: int rio_inb_pwrite_handler(struct rio_mport *mport, union rio_pw_msg *pw_msg)

    inbound port-write message handler

    :param mport:
        mport device associated with port-write
    :type mport: struct rio_mport \*

    :param pw_msg:
        pointer to inbound port-write message
    :type pw_msg: union rio_pw_msg \*

.. _`rio_inb_pwrite_handler.description`:

Description
-----------

Processes an inbound port-write message. Returns 0 if the request
has been satisfied.

.. _`rio_mport_get_efb`:

rio_mport_get_efb
=================

.. c:function:: u32 rio_mport_get_efb(struct rio_mport *port, int local, u16 destid, u8 hopcount, u32 from)

    get pointer to next extended features block

    :param port:
        Master port to issue transaction
    :type port: struct rio_mport \*

    :param local:
        Indicate a local master port or remote device access
    :type local: int

    :param destid:
        Destination ID of the device
    :type destid: u16

    :param hopcount:
        Number of switch hops to the device
    :type hopcount: u8

    :param from:
        Offset of  current Extended Feature block header (if 0 starts
        from ExtFeaturePtr)
    :type from: u32

.. _`rio_mport_get_feature`:

rio_mport_get_feature
=====================

.. c:function:: u32 rio_mport_get_feature(struct rio_mport *port, int local, u16 destid, u8 hopcount, int ftr)

    query for devices' extended features

    :param port:
        Master port to issue transaction
    :type port: struct rio_mport \*

    :param local:
        Indicate a local master port or remote device access
    :type local: int

    :param destid:
        Destination ID of the device
    :type destid: u16

    :param hopcount:
        Number of switch hops to the device
    :type hopcount: u8

    :param ftr:
        Extended feature code
    :type ftr: int

.. _`rio_mport_get_feature.description`:

Description
-----------

Tell if a device supports a given RapidIO capability.
Returns the offset of the requested extended feature
block within the device's RIO configuration space or
0 in case the device does not support it.

.. _`rio_get_asm`:

rio_get_asm
===========

.. c:function:: struct rio_dev *rio_get_asm(u16 vid, u16 did, u16 asm_vid, u16 asm_did, struct rio_dev *from)

    Begin or continue searching for a RIO device by vid/did/asm_vid/asm_did

    :param vid:
        RIO vid to match or \ ``RIO_ANY_ID``\  to match all vids
    :type vid: u16

    :param did:
        RIO did to match or \ ``RIO_ANY_ID``\  to match all dids
    :type did: u16

    :param asm_vid:
        RIO asm_vid to match or \ ``RIO_ANY_ID``\  to match all asm_vids
    :type asm_vid: u16

    :param asm_did:
        RIO asm_did to match or \ ``RIO_ANY_ID``\  to match all asm_dids
    :type asm_did: u16

    :param from:
        Previous RIO device found in search, or \ ``NULL``\  for new search
    :type from: struct rio_dev \*

.. _`rio_get_asm.description`:

Description
-----------

Iterates through the list of known RIO devices. If a RIO device is
found with a matching \ ``vid``\ , \ ``did``\ , \ ``asm_vid``\ , \ ``asm_did``\ , the reference
count to the device is incrememted and a pointer to its device
structure is returned. Otherwise, \ ``NULL``\  is returned. A new search
is initiated by passing \ ``NULL``\  to the \ ``from``\  argument. Otherwise, if
\ ``from``\  is not \ ``NULL``\ , searches continue from next device on the global
list. The reference count for \ ``from``\  is always decremented if it is
not \ ``NULL``\ .

.. _`rio_get_device`:

rio_get_device
==============

.. c:function:: struct rio_dev *rio_get_device(u16 vid, u16 did, struct rio_dev *from)

    Begin or continue searching for a RIO device by vid/did

    :param vid:
        RIO vid to match or \ ``RIO_ANY_ID``\  to match all vids
    :type vid: u16

    :param did:
        RIO did to match or \ ``RIO_ANY_ID``\  to match all dids
    :type did: u16

    :param from:
        Previous RIO device found in search, or \ ``NULL``\  for new search
    :type from: struct rio_dev \*

.. _`rio_get_device.description`:

Description
-----------

Iterates through the list of known RIO devices. If a RIO device is
found with a matching \ ``vid``\  and \ ``did``\ , the reference count to the
device is incrememted and a pointer to its device structure is returned.
Otherwise, \ ``NULL``\  is returned. A new search is initiated by passing \ ``NULL``\ 
to the \ ``from``\  argument. Otherwise, if \ ``from``\  is not \ ``NULL``\ , searches
continue from next device on the global list. The reference count for
\ ``from``\  is always decremented if it is not \ ``NULL``\ .

.. _`rio_std_route_add_entry`:

rio_std_route_add_entry
=======================

.. c:function:: int rio_std_route_add_entry(struct rio_mport *mport, u16 destid, u8 hopcount, u16 table, u16 route_destid, u8 route_port)

    Add switch route table entry using standard registers defined in RIO specification rev.1.3

    :param mport:
        Master port to issue transaction
    :type mport: struct rio_mport \*

    :param destid:
        Destination ID of the device
    :type destid: u16

    :param hopcount:
        Number of switch hops to the device
    :type hopcount: u8

    :param table:
        routing table ID (global or port-specific)
    :type table: u16

    :param route_destid:
        destID entry in the RT
    :type route_destid: u16

    :param route_port:
        destination port for specified destID
    :type route_port: u8

.. _`rio_std_route_get_entry`:

rio_std_route_get_entry
=======================

.. c:function:: int rio_std_route_get_entry(struct rio_mport *mport, u16 destid, u8 hopcount, u16 table, u16 route_destid, u8 *route_port)

    Read switch route table entry (port number) associated with specified destID using standard registers defined in RIO specification rev.1.3

    :param mport:
        Master port to issue transaction
    :type mport: struct rio_mport \*

    :param destid:
        Destination ID of the device
    :type destid: u16

    :param hopcount:
        Number of switch hops to the device
    :type hopcount: u8

    :param table:
        routing table ID (global or port-specific)
    :type table: u16

    :param route_destid:
        destID entry in the RT
    :type route_destid: u16

    :param route_port:
        returned destination port for specified destID
    :type route_port: u8 \*

.. _`rio_std_route_clr_table`:

rio_std_route_clr_table
=======================

.. c:function:: int rio_std_route_clr_table(struct rio_mport *mport, u16 destid, u8 hopcount, u16 table)

    Clear swotch route table using standard registers defined in RIO specification rev.1.3.

    :param mport:
        Master port to issue transaction
    :type mport: struct rio_mport \*

    :param destid:
        Destination ID of the device
    :type destid: u16

    :param hopcount:
        Number of switch hops to the device
    :type hopcount: u8

    :param table:
        routing table ID (global or port-specific)
    :type table: u16

.. _`rio_lock_device`:

rio_lock_device
===============

.. c:function:: int rio_lock_device(struct rio_mport *port, u16 destid, u8 hopcount, int wait_ms)

    Acquires host device lock for specified device

    :param port:
        Master port to send transaction
    :type port: struct rio_mport \*

    :param destid:
        Destination ID for device/switch
    :type destid: u16

    :param hopcount:
        Hopcount to reach switch
    :type hopcount: u8

    :param wait_ms:
        Max wait time in msec (0 = no timeout)
    :type wait_ms: int

.. _`rio_lock_device.description`:

Description
-----------

Attepts to acquire host device lock for specified device
Returns 0 if device lock acquired or EINVAL if timeout expires.

.. _`rio_unlock_device`:

rio_unlock_device
=================

.. c:function:: int rio_unlock_device(struct rio_mport *port, u16 destid, u8 hopcount)

    Releases host device lock for specified device

    :param port:
        Master port to send transaction
    :type port: struct rio_mport \*

    :param destid:
        Destination ID for device/switch
    :type destid: u16

    :param hopcount:
        Hopcount to reach switch
    :type hopcount: u8

.. _`rio_unlock_device.description`:

Description
-----------

Returns 0 if device lock released or EINVAL if fails.

.. _`rio_route_add_entry`:

rio_route_add_entry
===================

.. c:function:: int rio_route_add_entry(struct rio_dev *rdev, u16 table, u16 route_destid, u8 route_port, int lock)

    Add a route entry to a switch routing table

    :param rdev:
        RIO device
    :type rdev: struct rio_dev \*

    :param table:
        Routing table ID
    :type table: u16

    :param route_destid:
        Destination ID to be routed
    :type route_destid: u16

    :param route_port:
        Port number to be routed
    :type route_port: u8

    :param lock:
        apply a hardware lock on switch device flag (1=lock, 0=no_lock)
    :type lock: int

.. _`rio_route_add_entry.description`:

Description
-----------

If available calls the switch specific \ :c:func:`add_entry`\  method to add a route
entry into a switch routing table. Otherwise uses standard RT update method
as defined by RapidIO specification. A specific routing table can be selected
using the \ ``table``\  argument if a switch has per port routing tables or
the standard (or global) table may be used by passing
\ ``RIO_GLOBAL_TABLE``\  in \ ``table``\ .

Returns \ ``0``\  on success or \ ``-EINVAL``\  on failure.

.. _`rio_route_get_entry`:

rio_route_get_entry
===================

.. c:function:: int rio_route_get_entry(struct rio_dev *rdev, u16 table, u16 route_destid, u8 *route_port, int lock)

    Read an entry from a switch routing table

    :param rdev:
        RIO device
    :type rdev: struct rio_dev \*

    :param table:
        Routing table ID
    :type table: u16

    :param route_destid:
        Destination ID to be routed
    :type route_destid: u16

    :param route_port:
        Pointer to read port number into
    :type route_port: u8 \*

    :param lock:
        apply a hardware lock on switch device flag (1=lock, 0=no_lock)
    :type lock: int

.. _`rio_route_get_entry.description`:

Description
-----------

If available calls the switch specific \ :c:func:`get_entry`\  method to fetch a route
entry from a switch routing table. Otherwise uses standard RT read method
as defined by RapidIO specification. A specific routing table can be selected
using the \ ``table``\  argument if a switch has per port routing tables or
the standard (or global) table may be used by passing
\ ``RIO_GLOBAL_TABLE``\  in \ ``table``\ .

Returns \ ``0``\  on success or \ ``-EINVAL``\  on failure.

.. _`rio_route_clr_table`:

rio_route_clr_table
===================

.. c:function:: int rio_route_clr_table(struct rio_dev *rdev, u16 table, int lock)

    Clear a switch routing table

    :param rdev:
        RIO device
    :type rdev: struct rio_dev \*

    :param table:
        Routing table ID
    :type table: u16

    :param lock:
        apply a hardware lock on switch device flag (1=lock, 0=no_lock)
    :type lock: int

.. _`rio_route_clr_table.description`:

Description
-----------

If available calls the switch specific \ :c:func:`clr_table`\  method to clear a switch
routing table. Otherwise uses standard RT write method as defined by RapidIO
specification. A specific routing table can be selected using the \ ``table``\ 
argument if a switch has per port routing tables or the standard (or global)
table may be used by passing \ ``RIO_GLOBAL_TABLE``\  in \ ``table``\ .

Returns \ ``0``\  on success or \ ``-EINVAL``\  on failure.

.. _`rio_request_mport_dma`:

rio_request_mport_dma
=====================

.. c:function:: struct dma_chan *rio_request_mport_dma(struct rio_mport *mport)

    request RapidIO capable DMA channel associated with specified local RapidIO mport device.

    :param mport:
        RIO mport to perform DMA data transfers
    :type mport: struct rio_mport \*

.. _`rio_request_mport_dma.description`:

Description
-----------

Returns pointer to allocated DMA channel or NULL if failed.

.. _`rio_request_dma`:

rio_request_dma
===============

.. c:function:: struct dma_chan *rio_request_dma(struct rio_dev *rdev)

    request RapidIO capable DMA channel that supports specified target RapidIO device.

    :param rdev:
        RIO device associated with DMA transfer
    :type rdev: struct rio_dev \*

.. _`rio_request_dma.description`:

Description
-----------

Returns pointer to allocated DMA channel or NULL if failed.

.. _`rio_release_dma`:

rio_release_dma
===============

.. c:function:: void rio_release_dma(struct dma_chan *dchan)

    release specified DMA channel

    :param dchan:
        DMA channel to release
    :type dchan: struct dma_chan \*

.. _`rio_dma_prep_xfer`:

rio_dma_prep_xfer
=================

.. c:function:: struct dma_async_tx_descriptor *rio_dma_prep_xfer(struct dma_chan *dchan, u16 destid, struct rio_dma_data *data, enum dma_transfer_direction direction, unsigned long flags)

    RapidIO specific wrapper for device_prep_slave_sg callback defined by DMAENGINE.

    :param dchan:
        DMA channel to configure
    :type dchan: struct dma_chan \*

    :param destid:
        target RapidIO device destination ID
    :type destid: u16

    :param data:
        RIO specific data descriptor
    :type data: struct rio_dma_data \*

    :param direction:
        DMA data transfer direction (TO or FROM the device)
    :type direction: enum dma_transfer_direction

    :param flags:
        dmaengine defined flags
    :type flags: unsigned long

.. _`rio_dma_prep_xfer.description`:

Description
-----------

Initializes RapidIO capable DMA channel for the specified data transfer.
Uses DMA channel private extension to pass information related to remote
target RIO device.

.. _`rio_dma_prep_xfer.return`:

Return
------

pointer to DMA transaction descriptor if successful,
         error-valued pointer or NULL if failed.

.. _`rio_dma_prep_slave_sg`:

rio_dma_prep_slave_sg
=====================

.. c:function:: struct dma_async_tx_descriptor *rio_dma_prep_slave_sg(struct rio_dev *rdev, struct dma_chan *dchan, struct rio_dma_data *data, enum dma_transfer_direction direction, unsigned long flags)

    RapidIO specific wrapper for device_prep_slave_sg callback defined by DMAENGINE.

    :param rdev:
        RIO device control structure
    :type rdev: struct rio_dev \*

    :param dchan:
        DMA channel to configure
    :type dchan: struct dma_chan \*

    :param data:
        RIO specific data descriptor
    :type data: struct rio_dma_data \*

    :param direction:
        DMA data transfer direction (TO or FROM the device)
    :type direction: enum dma_transfer_direction

    :param flags:
        dmaengine defined flags
    :type flags: unsigned long

.. _`rio_dma_prep_slave_sg.description`:

Description
-----------

Initializes RapidIO capable DMA channel for the specified data transfer.
Uses DMA channel private extension to pass information related to remote
target RIO device.

.. _`rio_dma_prep_slave_sg.return`:

Return
------

pointer to DMA transaction descriptor if successful,
         error-valued pointer or NULL if failed.

.. _`rio_find_mport`:

rio_find_mport
==============

.. c:function:: struct rio_mport *rio_find_mport(int mport_id)

    find RIO mport by its ID

    :param mport_id:
        number (ID) of mport device
    :type mport_id: int

.. _`rio_find_mport.description`:

Description
-----------

Given a RIO mport number, the desired mport is located
in the global list of mports. If the mport is found, a pointer to its
data structure is returned.  If no mport is found, \ ``NULL``\  is returned.

.. _`rio_register_scan`:

rio_register_scan
=================

.. c:function:: int rio_register_scan(int mport_id, struct rio_scan *scan_ops)

    enumeration/discovery method registration interface

    :param mport_id:
        mport device ID for which fabric scan routine has to be set
        (RIO_MPORT_ANY = set for all available mports)
    :type mport_id: int

    :param scan_ops:
        enumeration/discovery operations structure
    :type scan_ops: struct rio_scan \*

.. _`rio_register_scan.description`:

Description
-----------

Registers enumeration/discovery operations with RapidIO subsystem and
attaches it to the specified mport device (or all available mports
if RIO_MPORT_ANY is specified).

Returns error if the mport already has an enumerator attached to it.
In case of RIO_MPORT_ANY skips mports with valid scan routines (no error).

.. _`rio_unregister_scan`:

rio_unregister_scan
===================

.. c:function:: int rio_unregister_scan(int mport_id, struct rio_scan *scan_ops)

    removes enumeration/discovery method from mport

    :param mport_id:
        mport device ID for which fabric scan routine has to be
        unregistered (RIO_MPORT_ANY = apply to all mports that use
        the specified scan_ops)
    :type mport_id: int

    :param scan_ops:
        enumeration/discovery operations structure
    :type scan_ops: struct rio_scan \*

.. _`rio_unregister_scan.description`:

Description
-----------

Removes enumeration or discovery method assigned to the specified mport
device. If RIO_MPORT_ANY is specified, removes the specified operations from
all mports that have them attached.

.. _`rio_mport_scan`:

rio_mport_scan
==============

.. c:function:: int rio_mport_scan(int mport_id)

    execute enumeration/discovery on the specified mport

    :param mport_id:
        number (ID) of mport device
    :type mport_id: int

.. This file was automatic generated / don't edit.

