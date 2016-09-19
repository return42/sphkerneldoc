.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/spmi.h

.. _`spmi_device`:

struct spmi_device
==================

.. c:type:: struct spmi_device

    Basic representation of an SPMI device

.. _`spmi_device.definition`:

Definition
----------

.. code-block:: c

    struct spmi_device {
        struct device dev;
        struct spmi_controller *ctrl;
        u8 usid;
    }

.. _`spmi_device.members`:

Members
-------

dev
    Driver model representation of the device.

ctrl
    SPMI controller managing the bus hosting this device.

usid
    This devices' Unique Slave IDentifier.

.. _`spmi_controller`:

struct spmi_controller
======================

.. c:type:: struct spmi_controller

    interface to the SPMI master controller

.. _`spmi_controller.definition`:

Definition
----------

.. code-block:: c

    struct spmi_controller {
        struct device dev;
        unsigned int nr;
        int (*cmd)(struct spmi_controller *ctrl, u8 opcode, u8 sid);
        int (*read_cmd)(struct spmi_controller *ctrl, u8 opcode,u8 sid, u16 addr, u8 *buf, size_t len);
        int (*write_cmd)(struct spmi_controller *ctrl, u8 opcode,u8 sid, u16 addr, const u8 *buf, size_t len);
    }

.. _`spmi_controller.members`:

Members
-------

dev
    Driver model representation of the device.

nr
    board-specific number identifier for this controller/bus

cmd
    sends a non-data command sequence on the SPMI bus.

read_cmd
    sends a register read command sequence on the SPMI bus.

write_cmd
    sends a register write command sequence on the SPMI bus.

.. _`spmi_controller_put`:

spmi_controller_put
===================

.. c:function:: void spmi_controller_put(struct spmi_controller *ctrl)

    decrement controller refcount \ ``ctrl``\         SPMI controller.

    :param struct spmi_controller \*ctrl:
        *undescribed*

.. _`spmi_driver`:

struct spmi_driver
==================

.. c:type:: struct spmi_driver

    SPMI slave device driver

.. _`spmi_driver.definition`:

Definition
----------

.. code-block:: c

    struct spmi_driver {
        struct device_driver driver;
        int (*probe)(struct spmi_device *sdev);
        void (*remove)(struct spmi_device *sdev);
    }

.. _`spmi_driver.members`:

Members
-------

driver
    SPMI device drivers should initialize name and owner field of
    this structure.

probe
    binds this driver to a SPMI device.

remove
    unbinds this driver from the SPMI device.

.. _`spmi_driver.description`:

Description
-----------

If PM runtime support is desired for a slave, a device driver can call
\ :c:func:`pm_runtime_put`\  from their \ :c:func:`probe`\  routine (and a balancing
\ :c:func:`pm_runtime_get`\  in \ :c:func:`remove`\ ).  PM runtime support for a slave is
implemented by issuing a SLEEP command to the slave on \ :c:func:`runtime_suspend`\ ,
transitioning the slave into the SLEEP state.  On \ :c:func:`runtime_resume`\ , a WAKEUP
command is sent to the slave to bring it back to ACTIVE.

.. _`spmi_driver_unregister`:

spmi_driver_unregister
======================

.. c:function:: void spmi_driver_unregister(struct spmi_driver *sdrv)

    unregister an SPMI client driver

    :param struct spmi_driver \*sdrv:
        the driver to unregister

.. This file was automatic generated / don't edit.

