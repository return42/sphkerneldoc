.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/bt-nokia-h4p.h

.. _`hci_h4p_platform_data`:

struct hci_h4p_platform_data
============================

.. c:type:: struct hci_h4p_platform_data

    hci_h4p Platform data structure

.. _`hci_h4p_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct hci_h4p_platform_data {
        int chip_type;
        int bt_sysclk;
        unsigned int bt_wakeup_gpio;
        unsigned int host_wakeup_gpio;
        unsigned int reset_gpio;
        int reset_gpio_shared;
        unsigned int uart_irq;
        phys_addr_t uart_base;
        const char *uart_iclk;
        const char *uart_fclk;
        void (* set_pm_limits) (struct device *dev, bool set);
    }

.. _`hci_h4p_platform_data.members`:

Members
-------

chip_type
    *undescribed*

bt_sysclk
    *undescribed*

bt_wakeup_gpio
    *undescribed*

host_wakeup_gpio
    *undescribed*

reset_gpio
    *undescribed*

reset_gpio_shared
    *undescribed*

uart_irq
    *undescribed*

uart_base
    *undescribed*

uart_iclk
    *undescribed*

uart_fclk
    *undescribed*

set_pm_limits
    *undescribed*

.. This file was automatic generated / don't edit.

