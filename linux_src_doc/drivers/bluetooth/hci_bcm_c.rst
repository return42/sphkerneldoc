.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/bluetooth/hci_bcm.c

.. _`bcm_device`:

struct bcm_device
=================

.. c:type:: struct bcm_device

    device driver resources

.. _`bcm_device.definition`:

Definition
----------

.. code-block:: c

    struct bcm_device {
        struct hci_uart serdev_hu;
        struct list_head list;
        struct device *dev;
        const char *name;
        struct gpio_desc *device_wakeup;
        struct gpio_desc *shutdown;
        int (*set_device_wakeup)(struct bcm_device *, bool);
        int (*set_shutdown)(struct bcm_device *, bool);
    #ifdef CONFIG_ACPI
        acpi_handle btlp, btpu, btpd;
        int gpio_count;
        int gpio_int_idx;
    #endif
        struct clk *clk;
        bool clk_enabled;
        u32 init_speed;
        u32 oper_speed;
        int irq;
        bool irq_active_low;
    #ifdef CONFIG_PM
        struct hci_uart *hu;
        bool is_suspended;
    #endif
    }

.. _`bcm_device.members`:

Members
-------

serdev_hu
    HCI UART controller struct

list
    bcm_device_list node

dev
    physical UART slave

name
    device name logged by bt_dev\_\*() functions

device_wakeup
    BT_WAKE pin,
    assert = Bluetooth device must wake up or remain awake,
    deassert = Bluetooth device may sleep when sleep criteria are met

shutdown
    BT_REG_ON pin,
    power up or power down Bluetooth device internal regulators

set_device_wakeup
    callback to toggle BT_WAKE pin
    either by accessing \ ``device_wakeup``\  or by calling \ ``btlp``\ 

set_shutdown
    callback to toggle BT_REG_ON pin
    either by accessing \ ``shutdown``\  or by calling \ ``btpu``\ /@btpd

btlp
    Apple ACPI method to toggle BT_WAKE pin ("Bluetooth Low Power")

btpu
    Apple ACPI method to drive BT_REG_ON pin high ("Bluetooth Power Up")

btpd
    Apple ACPI method to drive BT_REG_ON pin low ("Bluetooth Power Down")

gpio_count
    *undescribed*

gpio_int_idx
    *undescribed*

clk
    clock used by Bluetooth device

clk_enabled
    whether \ ``clk``\  is prepared and enabled

init_speed
    default baudrate of Bluetooth device;
    the host UART is initially set to this baudrate so that
    it can configure the Bluetooth device for \ ``oper_speed``\ 

oper_speed
    preferred baudrate of Bluetooth device;
    set to 0 if \ ``init_speed``\  is already the preferred baudrate

irq
    interrupt triggered by HOST_WAKE_BT pin

irq_active_low
    whether \ ``irq``\  is active low

hu
    pointer to HCI UART controller struct,
    used to disable flow control during runtime suspend and system sleep

is_suspended
    whether flow control is currently disabled

.. This file was automatic generated / don't edit.

