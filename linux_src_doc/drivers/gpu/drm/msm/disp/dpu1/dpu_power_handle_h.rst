.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/msm/disp/dpu1/dpu_power_handle.h

.. _`dpu_power_handle_data_bus_client`:

enum dpu_power_handle_data_bus_client
=====================================

.. c:type:: enum dpu_power_handle_data_bus_client

    type of axi bus clients

.. _`dpu_power_handle_data_bus_client.definition`:

Definition
----------

.. code-block:: c

    enum dpu_power_handle_data_bus_client {
        DPU_POWER_HANDLE_DATA_BUS_CLIENT_RT,
        DPU_POWER_HANDLE_DATA_BUS_CLIENT_NRT,
        DPU_POWER_HANDLE_DATA_BUS_CLIENT_MAX
    };

.. _`dpu_power_handle_data_bus_client.constants`:

Constants
---------

DPU_POWER_HANDLE_DATA_BUS_CLIENT_RT
    core real-time bus client

DPU_POWER_HANDLE_DATA_BUS_CLIENT_NRT
    core non-real-time bus client

DPU_POWER_HANDLE_DATA_BUS_CLIENT_MAX
    maximum number of bus client type

.. _`dpu_power_handle_dbus_id`:

enum DPU_POWER_HANDLE_DBUS_ID
=============================

.. c:type:: enum DPU_POWER_HANDLE_DBUS_ID

    data bus identifier

.. _`dpu_power_handle_dbus_id.definition`:

Definition
----------

.. code-block:: c

    enum DPU_POWER_HANDLE_DBUS_ID {
        DPU_POWER_HANDLE_DBUS_ID_MNOC,
        DPU_POWER_HANDLE_DBUS_ID_LLCC,
        DPU_POWER_HANDLE_DBUS_ID_EBI,
        DPU_POWER_HANDLE_DBUS_ID_MAX
    };

.. _`dpu_power_handle_dbus_id.constants`:

Constants
---------

DPU_POWER_HANDLE_DBUS_ID_MNOC
    DPU/MNOC data bus

DPU_POWER_HANDLE_DBUS_ID_LLCC
    MNOC/LLCC data bus

DPU_POWER_HANDLE_DBUS_ID_EBI
    LLCC/EBI data bus

DPU_POWER_HANDLE_DBUS_ID_MAX
    *undescribed*

.. _`dpu_power_client`:

struct dpu_power_client
=======================

.. c:type:: struct dpu_power_client

    stores the power client for dpu driver

.. _`dpu_power_client.definition`:

Definition
----------

.. code-block:: c

    struct dpu_power_client {
        char name[MAX_CLIENT_NAME_LEN];
        short usecase_ndx;
        short refcount;
        u32 id;
        struct list_head list;
        u64 ab[DPU_POWER_HANDLE_DATA_BUS_CLIENT_MAX];
        u64 ib[DPU_POWER_HANDLE_DATA_BUS_CLIENT_MAX];
        bool active;
    }

.. _`dpu_power_client.members`:

Members
-------

name
    name of the client

usecase_ndx
    current regs bus vote type

refcount
    current refcount if multiple modules are using same
    same client for enable/disable. Power module will
    aggregate the refcount and vote accordingly for this
    client.

id
    assigned during create. helps for debugging.

list
    list to attach power handle master list

ab
    arbitrated bandwidth for each bus client

ib
    instantaneous bandwidth for each bus client

active
    inidcates the state of dpu power handle

.. _`dpu_power_handle`:

struct dpu_power_handle
=======================

.. c:type:: struct dpu_power_handle

    power handle main struct

.. _`dpu_power_handle.definition`:

Definition
----------

.. code-block:: c

    struct dpu_power_handle {
        struct list_head power_client_clist;
        struct mutex phandle_lock;
        struct device *dev;
        u32 current_usecase_ndx;
        struct list_head event_list;
    }

.. _`dpu_power_handle.members`:

Members
-------

power_client_clist
    *undescribed*

phandle_lock
    lock to synchronize the enable/disable

dev
    pointer to device structure

current_usecase_ndx
    *undescribed*

event_list
    current power handle event list

.. _`dpu_power_resource_init`:

dpu_power_resource_init
=======================

.. c:function:: void dpu_power_resource_init(struct platform_device *pdev, struct dpu_power_handle *pdata)

    initializes the dpu power handle

    :param pdev:
        platform device to search the power resources
    :type pdev: struct platform_device \*

    :param pdata:
        power handle to store the power resources
    :type pdata: struct dpu_power_handle \*

.. _`dpu_power_resource_deinit`:

dpu_power_resource_deinit
=========================

.. c:function:: void dpu_power_resource_deinit(struct platform_device *pdev, struct dpu_power_handle *pdata)

    release the dpu power handle

    :param pdev:
        platform device for power resources
    :type pdev: struct platform_device \*

    :param pdata:
        power handle containing the resources
    :type pdata: struct dpu_power_handle \*

.. _`dpu_power_resource_deinit.return`:

Return
------

error code.

.. _`dpu_power_client_create`:

dpu_power_client_create
=======================

.. c:function:: struct dpu_power_client *dpu_power_client_create(struct dpu_power_handle *pdata, char *client_name)

    create the client on power handle

    :param pdata:
        power handle containing the resources
    :type pdata: struct dpu_power_handle \*

    :param client_name:
        new client name for registration
    :type client_name: char \*

.. _`dpu_power_client_create.return`:

Return
------

error code.

.. _`dpu_power_client_destroy`:

dpu_power_client_destroy
========================

.. c:function:: void dpu_power_client_destroy(struct dpu_power_handle *phandle, struct dpu_power_client *client)

    destroy the client on power handle

    :param phandle:
        *undescribed*
    :type phandle: struct dpu_power_handle \*

    :param client:
        *undescribed*
    :type client: struct dpu_power_client \*

.. _`dpu_power_client_destroy.return`:

Return
------

none

.. _`dpu_power_resource_enable`:

dpu_power_resource_enable
=========================

.. c:function:: int dpu_power_resource_enable(struct dpu_power_handle *pdata, struct dpu_power_client *pclient, bool enable)

    enable/disable the power resources

    :param pdata:
        power handle containing the resources
    :type pdata: struct dpu_power_handle \*

    :param pclient:
        *undescribed*
    :type pclient: struct dpu_power_client \*

    :param enable:
        boolean request for enable/disable
    :type enable: bool

.. _`dpu_power_resource_enable.return`:

Return
------

error code.

.. _`dpu_power_data_bus_bandwidth_ctrl`:

dpu_power_data_bus_bandwidth_ctrl
=================================

.. c:function:: void dpu_power_data_bus_bandwidth_ctrl(struct dpu_power_handle *phandle, struct dpu_power_client *pclient, int enable)

    control data bus bandwidth enable

    :param phandle:
        power handle containing the resources
    :type phandle: struct dpu_power_handle \*

    :param pclient:
        *undescribed*
    :type pclient: struct dpu_power_client \*

    :param enable:
        true to enable bandwidth for data base
    :type enable: int

.. _`dpu_power_data_bus_bandwidth_ctrl.return`:

Return
------

none

.. _`dpu_power_handle_register_event`:

dpu_power_handle_register_event
===============================

.. c:function:: struct dpu_power_event *dpu_power_handle_register_event(struct dpu_power_handle *phandle, u32 event_type, void (*cb_fnc)(u32 event_type, void *usr), void *usr, char *client_name)

    register a callback function for an event. Clients can register for multiple events with a single register. Any block with access to phandle can register for the event notification.

    :param phandle:
        power handle containing the resources
    :type phandle: struct dpu_power_handle \*

    :param event_type:
        event type to register; refer DPU_POWER_HANDLE_EVENT\_\*
    :type event_type: u32

    :param void (\*cb_fnc)(u32 event_type, void \*usr):
        pointer to desired callback function

    :param usr:
        user pointer to pass to callback on event trigger
    :type usr: void \*

    :param client_name:
        *undescribed*
    :type client_name: char \*

.. _`dpu_power_handle_register_event.return`:

Return
------

event pointer if success, or error code otherwise

.. _`dpu_power_handle_unregister_event`:

dpu_power_handle_unregister_event
=================================

.. c:function:: void dpu_power_handle_unregister_event(struct dpu_power_handle *phandle, struct dpu_power_event *event)

    unregister callback for event(s)

    :param phandle:
        power handle containing the resources
    :type phandle: struct dpu_power_handle \*

    :param event:
        event pointer returned after power handle register
    :type event: struct dpu_power_event \*

.. _`dpu_power_handle_get_dbus_name`:

dpu_power_handle_get_dbus_name
==============================

.. c:function:: const char *dpu_power_handle_get_dbus_name(u32 bus_id)

    get name of given data bus identifier

    :param bus_id:
        data bus identifier
    :type bus_id: u32

.. _`dpu_power_handle_get_dbus_name.return`:

Return
------

Pointer to name string if success; NULL otherwise

.. This file was automatic generated / don't edit.

