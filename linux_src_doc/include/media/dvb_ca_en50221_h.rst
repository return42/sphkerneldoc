.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/dvb_ca_en50221.h

.. _`dvb_ca_en50221`:

struct dvb_ca_en50221
=====================

.. c:type:: struct dvb_ca_en50221

    Structure describing a CA interface

.. _`dvb_ca_en50221.definition`:

Definition
----------

.. code-block:: c

    struct dvb_ca_en50221 {
        struct module *owner;
        int (*read_attribute_mem)(struct dvb_ca_en50221 *ca, int slot, int address);
        int (*write_attribute_mem)(struct dvb_ca_en50221 *ca, int slot, int address, u8 value);
        int (*read_cam_control)(struct dvb_ca_en50221 *ca, int slot, u8 address);
        int (*write_cam_control)(struct dvb_ca_en50221 *ca, int slot, u8 address, u8 value);
        int (*read_data)(struct dvb_ca_en50221 *ca, int slot, u8 *ebuf, int ecount);
        int (*write_data)(struct dvb_ca_en50221 *ca, int slot, u8 *ebuf, int ecount);
        int (*slot_reset)(struct dvb_ca_en50221 *ca, int slot);
        int (*slot_shutdown)(struct dvb_ca_en50221 *ca, int slot);
        int (*slot_ts_enable)(struct dvb_ca_en50221 *ca, int slot);
        int (*poll_slot_status)(struct dvb_ca_en50221 *ca, int slot, int open);
        void *data;
        void *private;
    }

.. _`dvb_ca_en50221.members`:

Members
-------

owner
    the module owning this structure

read_attribute_mem
    function for reading attribute memory on the CAM

write_attribute_mem
    function for writing attribute memory on the CAM

read_cam_control
    function for reading the control interface on the CAM

write_cam_control
    function for reading the control interface on the CAM

read_data
    function for reading data (block mode)

write_data
    function for writing data (block mode)

slot_reset
    function to reset the CAM slot

slot_shutdown
    function to shutdown a CAM slot

slot_ts_enable
    function to enable the Transport Stream on a CAM slot

poll_slot_status
    function to poll slot status. Only necessary if
    DVB_CA_FLAG_EN50221_IRQ_CAMCHANGE is not set.

data
    private data, used by caller.

private
    Opaque data used by the dvb_ca core. Do not modify!

.. _`dvb_ca_en50221.note`:

NOTE
----

the read_*, write_* and poll_slot_status functions will be
called for different slots concurrently and need to use locks where
and if appropriate. There will be no concurrent access to one slot.

.. _`dvb_ca_en50221_camchange_irq`:

dvb_ca_en50221_camchange_irq
============================

.. c:function:: void dvb_ca_en50221_camchange_irq(struct dvb_ca_en50221 *pubca, int slot, int change_type)

    A CAMCHANGE IRQ has occurred.

    :param pubca:
        CA instance.
    :type pubca: struct dvb_ca_en50221 \*

    :param slot:
        Slot concerned.
    :type slot: int

    :param change_type:
        One of the DVB_CA_CAMCHANGE_* values
    :type change_type: int

.. _`dvb_ca_en50221_camready_irq`:

dvb_ca_en50221_camready_irq
===========================

.. c:function:: void dvb_ca_en50221_camready_irq(struct dvb_ca_en50221 *pubca, int slot)

    A CAMREADY IRQ has occurred.

    :param pubca:
        CA instance.
    :type pubca: struct dvb_ca_en50221 \*

    :param slot:
        Slot concerned.
    :type slot: int

.. _`dvb_ca_en50221_frda_irq`:

dvb_ca_en50221_frda_irq
=======================

.. c:function:: void dvb_ca_en50221_frda_irq(struct dvb_ca_en50221 *ca, int slot)

    An FR or a DA IRQ has occurred.

    :param ca:
        CA instance.
    :type ca: struct dvb_ca_en50221 \*

    :param slot:
        Slot concerned.
    :type slot: int

.. _`dvb_ca_en50221_init`:

dvb_ca_en50221_init
===================

.. c:function:: int dvb_ca_en50221_init(struct dvb_adapter *dvb_adapter, struct dvb_ca_en50221 *ca, int flags, int slot_count)

    Initialise a new DVB CA device.

    :param dvb_adapter:
        DVB adapter to attach the new CA device to.
    :type dvb_adapter: struct dvb_adapter \*

    :param ca:
        The dvb_ca instance.
    :type ca: struct dvb_ca_en50221 \*

    :param flags:
        Flags describing the CA device (DVB_CA_EN50221_FLAG_*).
    :type flags: int

    :param slot_count:
        Number of slots supported.
    :type slot_count: int

.. _`dvb_ca_en50221_init.description`:

Description
-----------

\ ``return``\  0 on success, nonzero on failure

.. _`dvb_ca_en50221_release`:

dvb_ca_en50221_release
======================

.. c:function:: void dvb_ca_en50221_release(struct dvb_ca_en50221 *ca)

    Release a DVB CA device.

    :param ca:
        The associated dvb_ca instance.
    :type ca: struct dvb_ca_en50221 \*

.. This file was automatic generated / don't edit.

