.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/platform_data/mmc-sdhci-s3c.h

.. _`s3c_sdhci_platdata`:

struct s3c_sdhci_platdata
=========================

.. c:type:: struct s3c_sdhci_platdata

    Platform device data for Samsung SDHCI

.. _`s3c_sdhci_platdata.definition`:

Definition
----------

.. code-block:: c

    struct s3c_sdhci_platdata {
        unsigned int max_width;
        unsigned int host_caps;
        unsigned int host_caps2;
        unsigned int pm_caps;
        enum cd_types cd_type;
        int ext_cd_gpio;
        bool ext_cd_gpio_invert;
        int (*ext_cd_init)(void (*notify_func)(struct platform_device *, int state));
        int (*ext_cd_cleanup)(void (*notify_func)(struct platform_device *, int state));
        void (*cfg_gpio)(struct platform_device *dev, int width);
    }

.. _`s3c_sdhci_platdata.members`:

Members
-------

max_width
    The maximum number of data bits supported.

host_caps
    Standard MMC host capabilities bit field.

host_caps2
    The second standard MMC host capabilities bit field.

pm_caps
    *undescribed*

cd_type
    Type of Card Detection method (see cd_types enum above)

ext_cd_gpio
    gpio pin used for external CD line, valid only if
    cd_type == S3C_SDHCI_CD_GPIO

ext_cd_gpio_invert
    invert values for external CD gpio line

ext_cd_init
    Initialize external card detect subsystem. Called on
    sdhci-s3c driver probe when cd_type == S3C_SDHCI_CD_EXTERNAL.
    notify_func argument is a callback to the sdhci-s3c driver
    that triggers the card detection event. Callback arguments:
    dev is pointer to platform device of the host controller,
    state is new state of the card (0 - removed, 1 - inserted).

ext_cd_cleanup
    Cleanup external card detect subsystem. Called on
    sdhci-s3c driver remove when cd_type == S3C_SDHCI_CD_EXTERNAL.
    notify_func argument is the same callback as for ext_cd_init.

cfg_gpio
    Configure the GPIO for a specific card bit-width

.. _`s3c_sdhci_platdata.description`:

Description
-----------

Initialisation data specific to either the machine or the platform
for the device driver to use or call-back when configuring gpio or
card speed information.

.. This file was automatic generated / don't edit.

