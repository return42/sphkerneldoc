.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/acpi-dma.c

.. _`acpi_dma_parse_resource_group`:

acpi_dma_parse_resource_group
=============================

.. c:function:: int acpi_dma_parse_resource_group(const struct acpi_csrt_group *grp, struct acpi_device *adev, struct acpi_dma *adma)

    match device and parse resource group

    :param grp:
        CSRT resource group
    :type grp: const struct acpi_csrt_group \*

    :param adev:
        ACPI device to match with
    :type adev: struct acpi_device \*

    :param adma:
        struct acpi_dma of the given DMA controller
    :type adma: struct acpi_dma \*

.. _`acpi_dma_parse_resource_group.description`:

Description
-----------

In order to match a device from DSDT table to the corresponding CSRT device
we use MMIO address and IRQ.

.. _`acpi_dma_parse_resource_group.return`:

Return
------

1 on success, 0 when no information is available, or appropriate errno value
on error.

.. _`acpi_dma_parse_csrt`:

acpi_dma_parse_csrt
===================

.. c:function:: void acpi_dma_parse_csrt(struct acpi_device *adev, struct acpi_dma *adma)

    parse CSRT to exctract additional DMA resources

    :param adev:
        ACPI device to match with
    :type adev: struct acpi_device \*

    :param adma:
        struct acpi_dma of the given DMA controller
    :type adma: struct acpi_dma \*

.. _`acpi_dma_parse_csrt.description`:

Description
-----------

CSRT or Core System Resources Table is a proprietary ACPI table
introduced by Microsoft. This table can contain devices that are not in
the system DSDT table. In particular DMA controllers might be described
here.

We are using this table to get the request line range of the specific DMA
controller to be used later.

.. _`acpi_dma_controller_register`:

acpi_dma_controller_register
============================

.. c:function:: int acpi_dma_controller_register(struct device *dev, struct dma_chan *(*acpi_dma_xlate)(struct acpi_dma_spec *, struct acpi_dma *), void *data)

    Register a DMA controller to ACPI DMA helpers

    :param dev:
        struct device of DMA controller
    :type dev: struct device \*

    :param struct dma_chan \*(\*acpi_dma_xlate)(struct acpi_dma_spec \*, struct acpi_dma \*):
        translation function which converts a dma specifier
        into a dma_chan structure
        \ ``data``\                 pointer to controller specific data to be used by
        translation function

    :param data:
        *undescribed*
    :type data: void \*

.. _`acpi_dma_controller_register.description`:

Description
-----------

Allocated memory should be freed with appropriate \ :c:func:`acpi_dma_controller_free`\ 
call.

.. _`acpi_dma_controller_register.return`:

Return
------

0 on success or appropriate errno value on error.

.. _`acpi_dma_controller_free`:

acpi_dma_controller_free
========================

.. c:function:: int acpi_dma_controller_free(struct device *dev)

    Remove a DMA controller from ACPI DMA helpers list

    :param dev:
        struct device of DMA controller
    :type dev: struct device \*

.. _`acpi_dma_controller_free.description`:

Description
-----------

Memory allocated by \ :c:func:`acpi_dma_controller_register`\  is freed here.

.. _`acpi_dma_controller_free.return`:

Return
------

0 on success or appropriate errno value on error.

.. _`devm_acpi_dma_controller_register`:

devm_acpi_dma_controller_register
=================================

.. c:function:: int devm_acpi_dma_controller_register(struct device *dev, struct dma_chan *(*acpi_dma_xlate)(struct acpi_dma_spec *, struct acpi_dma *), void *data)

    resource managed \ :c:func:`acpi_dma_controller_register`\ 

    :param dev:
        device that is registering this DMA controller
    :type dev: struct device \*

    :param struct dma_chan \*(\*acpi_dma_xlate)(struct acpi_dma_spec \*, struct acpi_dma \*):
        translation function
        \ ``data``\                 pointer to controller specific data

    :param data:
        *undescribed*
    :type data: void \*

.. _`devm_acpi_dma_controller_register.description`:

Description
-----------

Managed \ :c:func:`acpi_dma_controller_register`\ . DMA controller registered by this
function are automatically freed on driver detach. See
\ :c:func:`acpi_dma_controller_register`\  for more information.

.. _`devm_acpi_dma_controller_register.return`:

Return
------

0 on success or appropriate errno value on error.

.. _`devm_acpi_dma_controller_free`:

devm_acpi_dma_controller_free
=============================

.. c:function:: void devm_acpi_dma_controller_free(struct device *dev)

    resource managed \ :c:func:`acpi_dma_controller_free`\ 

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`devm_acpi_dma_controller_free.description`:

Description
-----------

Unregister a DMA controller registered with
\ :c:func:`devm_acpi_dma_controller_register`\ . Normally this function will not need to
be called and the resource management code will ensure that the resource is
freed.

.. _`acpi_dma_update_dma_spec`:

acpi_dma_update_dma_spec
========================

.. c:function:: int acpi_dma_update_dma_spec(struct acpi_dma *adma, struct acpi_dma_spec *dma_spec)

    prepare dma specifier to pass to translation function

    :param adma:
        struct acpi_dma of DMA controller
    :type adma: struct acpi_dma \*

    :param dma_spec:
        dma specifier to update
    :type dma_spec: struct acpi_dma_spec \*

.. _`acpi_dma_update_dma_spec.description`:

Description
-----------

Accordingly to ACPI 5.0 Specification Table 6-170 "Fixed DMA Resource
Descriptor":
DMA Request Line bits is a platform-relative number uniquely
identifying the request line assigned. Request line-to-Controller
mapping is done in a controller-specific OS driver.
That's why we can safely adjust slave_id when the appropriate controller is
found.

.. _`acpi_dma_update_dma_spec.return`:

Return
------

0, if no information is avaiable, -1 on mismatch, and 1 otherwise.

.. _`acpi_dma_parse_fixed_dma`:

acpi_dma_parse_fixed_dma
========================

.. c:function:: int acpi_dma_parse_fixed_dma(struct acpi_resource *res, void *data)

    Parse FixedDMA ACPI resources to a DMA specifier

    :param res:
        struct acpi_resource to get FixedDMA resources from
    :type res: struct acpi_resource \*

    :param data:
        pointer to a helper struct acpi_dma_parser_data
    :type data: void \*

.. _`acpi_dma_request_slave_chan_by_index`:

acpi_dma_request_slave_chan_by_index
====================================

.. c:function:: struct dma_chan *acpi_dma_request_slave_chan_by_index(struct device *dev, size_t index)

    Get the DMA slave channel

    :param dev:
        struct device to get DMA request from
    :type dev: struct device \*

    :param index:
        index of FixedDMA descriptor for \ ``dev``\ 
    :type index: size_t

.. _`acpi_dma_request_slave_chan_by_index.return`:

Return
------

Pointer to appropriate dma channel on success or an error pointer.

.. _`acpi_dma_request_slave_chan_by_name`:

acpi_dma_request_slave_chan_by_name
===================================

.. c:function:: struct dma_chan *acpi_dma_request_slave_chan_by_name(struct device *dev, const char *name)

    Get the DMA slave channel

    :param dev:
        struct device to get DMA request from
    :type dev: struct device \*

    :param name:
        represents corresponding FixedDMA descriptor for \ ``dev``\ 
    :type name: const char \*

.. _`acpi_dma_request_slave_chan_by_name.description`:

Description
-----------

In order to support both Device Tree and ACPI in a single driver we
translate the names "tx" and "rx" here based on the most common case where
the first FixedDMA descriptor is TX and second is RX.

If the device has "dma-names" property the FixedDMA descriptor indices
are retrieved based on those. Otherwise the function falls back using
hardcoded indices.

.. _`acpi_dma_request_slave_chan_by_name.return`:

Return
------

Pointer to appropriate dma channel on success or an error pointer.

.. _`acpi_dma_simple_xlate`:

acpi_dma_simple_xlate
=====================

.. c:function:: struct dma_chan *acpi_dma_simple_xlate(struct acpi_dma_spec *dma_spec, struct acpi_dma *adma)

    Simple ACPI DMA engine translation helper

    :param dma_spec:
        pointer to ACPI DMA specifier
    :type dma_spec: struct acpi_dma_spec \*

    :param adma:
        pointer to ACPI DMA controller data
    :type adma: struct acpi_dma \*

.. _`acpi_dma_simple_xlate.description`:

Description
-----------

A simple translation function for ACPI based devices. Passes \ :c:type:`struct struct <struct>`\ 
dma_spec to the DMA controller driver provided filter function.

.. _`acpi_dma_simple_xlate.return`:

Return
------

Pointer to the channel if found or \ ``NULL``\  otherwise.

.. This file was automatic generated / don't edit.

