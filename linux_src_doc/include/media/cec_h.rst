.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/cec.h

.. _`cec_devnode`:

struct cec_devnode
==================

.. c:type:: struct cec_devnode

    cec device node

.. _`cec_devnode.definition`:

Definition
----------

.. code-block:: c

    struct cec_devnode {
        struct device dev;
        struct cdev cdev;
        int minor;
        bool registered;
        bool unregistered;
        struct list_head fhs;
        struct mutex lock;
    }

.. _`cec_devnode.members`:

Members
-------

dev
    cec device

cdev
    cec character device

minor
    device node minor number

registered
    the device was correctly registered

unregistered
    the device was unregistered

fhs
    the list of open filehandles (cec_fh)

lock
    *undescribed*

.. _`cec_devnode.description`:

Description
-----------

This structure represents a cec-related device node.

The \ ``parent``\  is a physical device. It must be set by core or device drivers
before registering the node.

.. _`cec_is_registered`:

cec_is_registered
=================

.. c:function:: bool cec_is_registered(const struct cec_adapter *adap)

    is the CEC adapter registered?

    :param const struct cec_adapter \*adap:
        the CEC adapter, may be NULL.

.. _`cec_is_registered.return`:

Return
------

true if the adapter is registered, false otherwise.

.. _`cec_queue_pin_cec_event`:

cec_queue_pin_cec_event
=======================

.. c:function:: void cec_queue_pin_cec_event(struct cec_adapter *adap, bool is_high, ktime_t ts)

    queue a CEC pin event with a given timestamp.

    :param struct cec_adapter \*adap:
        pointer to the cec adapter

    :param bool is_high:
        when true the CEC pin is high, otherwise it is low

    :param ktime_t ts:
        the timestamp for this event

.. _`cec_queue_pin_hpd_event`:

cec_queue_pin_hpd_event
=======================

.. c:function:: void cec_queue_pin_hpd_event(struct cec_adapter *adap, bool is_high, ktime_t ts)

    queue a pin event with a given timestamp.

    :param struct cec_adapter \*adap:
        pointer to the cec adapter

    :param bool is_high:
        when true the HPD pin is high, otherwise it is low

    :param ktime_t ts:
        the timestamp for this event

.. _`cec_get_edid_phys_addr`:

cec_get_edid_phys_addr
======================

.. c:function:: u16 cec_get_edid_phys_addr(const u8 *edid, unsigned int size, unsigned int *offset)

    find and return the physical address

    :param const u8 \*edid:
        pointer to the EDID data

    :param unsigned int size:
        size in bytes of the EDID data

    :param unsigned int \*offset:
        If not \ ``NULL``\  then the location of the physical address
        bytes in the EDID will be returned here. This is set to 0
        if there is no physical address found.

.. _`cec_get_edid_phys_addr.return`:

Return
------

the physical address or CEC_PHYS_ADDR_INVALID if there is none.

.. _`cec_set_edid_phys_addr`:

cec_set_edid_phys_addr
======================

.. c:function:: void cec_set_edid_phys_addr(u8 *edid, unsigned int size, u16 phys_addr)

    find and set the physical address

    :param u8 \*edid:
        pointer to the EDID data

    :param unsigned int size:
        size in bytes of the EDID data

    :param u16 phys_addr:
        the new physical address

.. _`cec_set_edid_phys_addr.description`:

Description
-----------

This function finds the location of the physical address in the EDID
and fills in the given physical address and updates the checksum
at the end of the EDID block. It does nothing if the EDID doesn't
contain a physical address.

.. _`cec_phys_addr_for_input`:

cec_phys_addr_for_input
=======================

.. c:function:: u16 cec_phys_addr_for_input(u16 phys_addr, u8 input)

    calculate the PA for an input

    :param u16 phys_addr:
        the physical address of the parent

    :param u8 input:
        the number of the input port, must be between 1 and 15

.. _`cec_phys_addr_for_input.description`:

Description
-----------

This function calculates a new physical address based on the input
port number. For example:

PA = 0.0.0.0 and input = 2 becomes 2.0.0.0

PA = 3.0.0.0 and input = 1 becomes 3.1.0.0

PA = 3.2.1.0 and input = 5 becomes 3.2.1.5

PA = 3.2.1.3 and input = 5 becomes f.f.f.f since it maxed out the depth.

.. _`cec_phys_addr_for_input.return`:

Return
------

the new physical address or CEC_PHYS_ADDR_INVALID.

.. _`cec_phys_addr_validate`:

cec_phys_addr_validate
======================

.. c:function:: int cec_phys_addr_validate(u16 phys_addr, u16 *parent, u16 *port)

    validate a physical address from an EDID

    :param u16 phys_addr:
        the physical address to validate

    :param u16 \*parent:
        if not \ ``NULL``\ , then this is filled with the parents PA.

    :param u16 \*port:
        if not \ ``NULL``\ , then this is filled with the input port.

.. _`cec_phys_addr_validate.description`:

Description
-----------

This validates a physical address as read from an EDID. If the
PA is invalid (such as 1.0.1.0 since '0' is only allowed at the end),
then it will return -EINVAL.

The parent PA is passed into \ ``parent``\  and the input port is passed into
\ ``port``\ . For example:

PA = 0.0.0.0: has parent 0.0.0.0 and input port 0.

PA = 1.0.0.0: has parent 0.0.0.0 and input port 1.

PA = 3.2.0.0: has parent 3.0.0.0 and input port 2.

PA = f.f.f.f: has parent f.f.f.f and input port 0.

.. _`cec_phys_addr_validate.return`:

Return
------

0 if the PA is valid, -EINVAL if not.

.. _`cec_phys_addr_invalidate`:

cec_phys_addr_invalidate
========================

.. c:function:: void cec_phys_addr_invalidate(struct cec_adapter *adap)

    set the physical address to INVALID

    :param struct cec_adapter \*adap:
        the CEC adapter

.. _`cec_phys_addr_invalidate.description`:

Description
-----------

This is a simple helper function to invalidate the physical
address.

.. This file was automatic generated / don't edit.

