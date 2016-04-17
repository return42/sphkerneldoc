.. -*- coding: utf-8; mode: rst -*-

==========
brcmfmac.h
==========


.. _`brcmfmac_sdio_pd`:

struct brcmfmac_sdio_pd
=======================

.. c:type:: brcmfmac_sdio_pd

    SDIO Device specific platform data.


.. _`brcmfmac_sdio_pd.definition`:

Definition
----------

.. code-block:: c

  struct brcmfmac_sdio_pd {
    int txglomsz;
    unsigned int drive_strength;
    bool oob_irq_supported;
    unsigned long oob_irq_flags;
    bool broken_sg_support;
    unsigned short sd_head_align;
    unsigned short sd_sgentry_align;
    void (* reset) (void);
  };


.. _`brcmfmac_sdio_pd.members`:

Members
-------

:``txglomsz``:
    SDIO txglom size. Use 0 if default of driver is to be
    used.

:``drive_strength``:
    is the preferred drive_strength to be used for the SDIO
    pins. If 0 then a default value will be used. This is
    the target drive strength, the exact drive strength
    which will be used depends on the capabilities of the
    device.

:``oob_irq_supported``:
    does the board have support for OOB interrupts. SDIO
    in-band interrupts are relatively slow and for having
    less overhead on interrupt processing an out of band
    interrupt can be used. If the HW supports this then
    enable this by setting this field to true and configure
    the oob related fields.

    ``oob_irq_nr``\ ,

:``oob_irq_flags``:
    the OOB interrupt information. The values are used for
    registering the irq using request_irq function.

:``broken_sg_support``:
    flag for broken sg list support of SDIO host controller.
    Set this to true if the SDIO host controller has higher
    align requirement than 32 bytes for each scatterlist
    item.

:``sd_head_align``:
    alignment requirement for start of data buffer.

:``sd_sgentry_align``:
    length alignment requirement for each sg entry.

:``reset``:
    This function can get called if the device communication
    broke down. This functionality is particularly useful in
    case of SDIO type devices. It is possible to reset a
    dongle via sdio data interface, but it requires that
    this is fully functional. This function is chip/module
    specific and this function should return only after the
    complete reset has completed.




.. _`brcmfmac_pd_cc_entry`:

struct brcmfmac_pd_cc_entry
===========================

.. c:type:: brcmfmac_pd_cc_entry

    Struct for translating user space country code (iso3166) to firmware country code and revision.


.. _`brcmfmac_pd_cc_entry.definition`:

Definition
----------

.. code-block:: c

  struct brcmfmac_pd_cc_entry {
    char iso3166[BRCMFMAC_COUNTRY_BUF_SZ];
    char cc[BRCMFMAC_COUNTRY_BUF_SZ];
    s32 rev;
  };


.. _`brcmfmac_pd_cc_entry.members`:

Members
-------

:``iso3166[BRCMFMAC_COUNTRY_BUF_SZ]``:
    iso3166 alpha 2 country code string.

:``cc[BRCMFMAC_COUNTRY_BUF_SZ]``:
    firmware country code string.

:``rev``:
    firmware country code revision.




.. _`brcmfmac_pd_cc`:

struct brcmfmac_pd_cc
=====================

.. c:type:: brcmfmac_pd_cc

    Struct for translating country codes as set by user space to a country code and rev which can be used by firmware.


.. _`brcmfmac_pd_cc.definition`:

Definition
----------

.. code-block:: c

  struct brcmfmac_pd_cc {
    int table_size;
    struct brcmfmac_pd_cc_entry table[0];
  };


.. _`brcmfmac_pd_cc.members`:

Members
-------

:``table_size``:
    number of entries in table (> 0)

:``table[0]``:
    array of 1 or more elements with translation information.




.. _`brcmfmac_pd_device`:

struct brcmfmac_pd_device
=========================

.. c:type:: brcmfmac_pd_device

    Device specific platform data. (id/rev/bus_type) is the unique identifier of the device.


.. _`brcmfmac_pd_device.definition`:

Definition
----------

.. code-block:: c

  struct brcmfmac_pd_device {
    unsigned int id;
    unsigned int rev;
    enum brcmf_bus_type bus_type;
    unsigned int feature_disable;
    struct brcmfmac_pd_cc * country_codes;
    union bus;
  };


.. _`brcmfmac_pd_device.members`:

Members
-------

:``id``:
    ID of the device for which this data is. In case of SDIO
    or PCIE this is the chipid as identified by chip.c In
    case of USB this is the chipid as identified by the
    device query.

:``rev``:
    chip revision, see id.

:``bus_type``:
    The type of bus. Some chipid/rev exist for different bus
    types. Each bus type has its own set of settings.

:``feature_disable``:
    Bitmask of features to disable (override), See feature.c
    in brcmfmac for details.

:``country_codes``:
    If available, pointer to struct for translating country
    codes.

:``bus``:
    Bus specific (union) device settings. Currently only
    SDIO.




.. _`brcmfmac_platform_data`:

struct brcmfmac_platform_data
=============================

.. c:type:: brcmfmac_platform_data

    BRCMFMAC specific platform data.


.. _`brcmfmac_platform_data.definition`:

Definition
----------

.. code-block:: c

  struct brcmfmac_platform_data {
    void (* power_on) (void);
    void (* power_off) (void);
  };


.. _`brcmfmac_platform_data.members`:

Members
-------

:``power_on``:
    This function is called by the brcmfmac driver when the module
    gets loaded. This can be particularly useful for low power
    devices. The platform spcific routine may for example decide to
    power up the complete device. If there is no use-case for this
    function then provide NULL.

:``power_off``:
    This function is called by the brcmfmac when the module gets
    unloaded. At this point the devices can be powered down or
    otherwise be reset. So if an actual power_off is not supported
    but reset is supported by the devices then reset the devices
    when this function gets called. This can be particularly useful
    for low power devices. If there is no use-case for this
    function then provide NULL.


