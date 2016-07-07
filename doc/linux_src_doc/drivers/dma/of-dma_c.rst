.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/of-dma.c

.. _`of_dma_find_controller`:

of_dma_find_controller
======================

.. c:function:: struct of_dma *of_dma_find_controller(struct of_phandle_args *dma_spec)

    Get a DMA controller in DT DMA helpers list

    :param struct of_phandle_args \*dma_spec:
        pointer to DMA specifier as found in the device tree

.. _`of_dma_find_controller.description`:

Description
-----------

Finds a DMA controller with matching device node and number for dma cells
in a list of registered DMA controllers. If a match is found a valid pointer
to the DMA data stored is retuned. A NULL pointer is returned if no match is
found.

.. _`of_dma_router_xlate`:

of_dma_router_xlate
===================

.. c:function:: struct dma_chan *of_dma_router_xlate(struct of_phandle_args *dma_spec, struct of_dma *ofdma)

    translation function for router devices

    :param struct of_phandle_args \*dma_spec:
        pointer to DMA specifier as found in the device tree

    :param struct of_dma \*ofdma:
        *undescribed*

.. _`of_dma_router_xlate.description`:

Description
-----------

The function creates new dma_spec to be passed to the router driver's
\ :c:func:`of_dma_route_allocate`\  function to prepare a dma_spec which will be used
to request channel from the real DMA controller.

.. _`of_dma_controller_register`:

of_dma_controller_register
==========================

.. c:function:: int of_dma_controller_register(struct device_node *np, struct dma_chan *(*) of_dma_xlate (struct of_phandle_args *, struct of_dma *, void *data)

    Register a DMA controller to DT DMA helpers

    :param struct device_node \*np:
        device node of DMA controller

    :param (struct dma_chan \*(\*) of_dma_xlate (struct of_phandle_args \*, struct of_dma \*):
        translation function which converts a phandle
        arguments list into a dma_chan structure
        \ ``data``\                 pointer to controller specific data to be used by
        translation function

    :param void \*data:
        *undescribed*

.. _`of_dma_controller_register.description`:

Description
-----------

Returns 0 on success or appropriate errno value on error.

Allocated memory should be freed with appropriate \ :c:func:`of_dma_controller_free`\ 
call.

.. _`of_dma_controller_free`:

of_dma_controller_free
======================

.. c:function:: void of_dma_controller_free(struct device_node *np)

    Remove a DMA controller from DT DMA helpers list

    :param struct device_node \*np:
        device node of DMA controller

.. _`of_dma_controller_free.description`:

Description
-----------

Memory allocated by \ :c:func:`of_dma_controller_register`\  is freed here.

.. _`of_dma_router_register`:

of_dma_router_register
======================

.. c:function:: int of_dma_router_register(struct device_node *np, void *(*) of_dma_route_allocate (struct of_phandle_args *, struct of_dma *, struct dma_router *dma_router)

    Register a DMA router to DT DMA helpers as a controller

    :param struct device_node \*np:
        device node of DMA router

    :param (void \*(\*) of_dma_route_allocate (struct of_phandle_args \*, struct of_dma \*):
        setup function for the router which need to
        modify the dma_spec for the DMA controller to
        use and to set up the requested route.

    :param struct dma_router \*dma_router:
        pointer to dma_router structure to be used when
        the route need to be free up.

.. _`of_dma_router_register.description`:

Description
-----------

Returns 0 on success or appropriate errno value on error.

Allocated memory should be freed with appropriate \ :c:func:`of_dma_controller_free`\ 
call.

.. _`of_dma_match_channel`:

of_dma_match_channel
====================

.. c:function:: int of_dma_match_channel(struct device_node *np, const char *name, int index, struct of_phandle_args *dma_spec)

    Check if a DMA specifier matches name

    :param struct device_node \*np:
        device node to look for DMA channels

    :param const char \*name:
        channel name to be matched

    :param int index:
        index of DMA specifier in list of DMA specifiers

    :param struct of_phandle_args \*dma_spec:
        pointer to DMA specifier as found in the device tree

.. _`of_dma_match_channel.description`:

Description
-----------

Check if the DMA specifier pointed to by the index in a list of DMA
specifiers, matches the name provided. Returns 0 if the name matches and
a valid pointer to the DMA specifier is found. Otherwise returns -ENODEV.

.. _`of_dma_request_slave_channel`:

of_dma_request_slave_channel
============================

.. c:function:: struct dma_chan *of_dma_request_slave_channel(struct device_node *np, const char *name)

    Get the DMA slave channel

    :param struct device_node \*np:
        device node to get DMA request from

    :param const char \*name:
        name of desired channel

.. _`of_dma_request_slave_channel.description`:

Description
-----------

Returns pointer to appropriate DMA channel on success or an error pointer.

.. _`of_dma_simple_xlate`:

of_dma_simple_xlate
===================

.. c:function:: struct dma_chan *of_dma_simple_xlate(struct of_phandle_args *dma_spec, struct of_dma *ofdma)

    Simple DMA engine translation function

    :param struct of_phandle_args \*dma_spec:
        pointer to DMA specifier as found in the device tree

    :param struct of_dma \*ofdma:
        *undescribed*

.. _`of_dma_simple_xlate.description`:

Description
-----------

A simple translation function for devices that use a 32-bit value for the
filter_param when calling the DMA engine \ :c:func:`dma_request_channel`\  function.
Note that this translation function requires that #dma-cells is equal to 1
and the argument of the dma specifier is the 32-bit filter_param. Returns
pointer to appropriate dma channel on success or NULL on error.

.. _`of_dma_xlate_by_chan_id`:

of_dma_xlate_by_chan_id
=======================

.. c:function:: struct dma_chan *of_dma_xlate_by_chan_id(struct of_phandle_args *dma_spec, struct of_dma *ofdma)

    Translate dt property to DMA channel by channel id

    :param struct of_phandle_args \*dma_spec:
        pointer to DMA specifier as found in the device tree

    :param struct of_dma \*ofdma:
        *undescribed*

.. _`of_dma_xlate_by_chan_id.description`:

Description
-----------

This function can be used as the of xlate callback for DMA driver which wants
to match the channel based on the channel id. When using this xlate function
the #dma-cells propety of the DMA controller dt node needs to be set to 1.
The data parameter of of_dma_controller_register must be a pointer to the
dma_device struct the function should match upon.

Returns pointer to appropriate dma channel on success or NULL on error.

.. This file was automatic generated / don't edit.

