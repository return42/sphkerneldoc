.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/watchdog/mei_wdt.c

.. _`mei_wdt_state`:

enum mei_wdt_state
==================

.. c:type:: enum mei_wdt_state

    internal watchdog state

.. _`mei_wdt_state.definition`:

Definition
----------

.. code-block:: c

    enum mei_wdt_state {
        MEI_WDT_PROBE,
        MEI_WDT_IDLE,
        MEI_WDT_START,
        MEI_WDT_RUNNING,
        MEI_WDT_STOPPING,
        MEI_WDT_NOT_REQUIRED
    };

.. _`mei_wdt_state.constants`:

Constants
---------

MEI_WDT_PROBE
    wd in probing stage

MEI_WDT_IDLE
    wd is idle and not opened

MEI_WDT_START
    wd was opened, start was called

MEI_WDT_RUNNING
    wd is expecting keep alive pings

MEI_WDT_STOPPING
    wd is stopping and will move to IDLE

MEI_WDT_NOT_REQUIRED
    wd device is not required

.. _`mei_wdt`:

struct mei_wdt
==============

.. c:type:: struct mei_wdt

    mei watchdog driver

.. _`mei_wdt.definition`:

Definition
----------

.. code-block:: c

    struct mei_wdt {
        struct watchdog_device wdd;
        struct mei_cl_device *cldev;
        enum mei_wdt_state state;
        bool resp_required;
        struct completion response;
        struct work_struct unregister;
        struct mutex reg_lock;
        u16 timeout;
        #if IS_ENABLED(CONFIG_DEBUG_FS)
        struct dentry *dbgfs_dir;
        #endif
    }

.. _`mei_wdt.members`:

Members
-------

wdd
    watchdog device

cldev
    mei watchdog client device

state
    watchdog internal state

resp_required
    ping required response

response
    ping response completion

unregister
    unregister worker

reg_lock
    watchdog device registration lock

timeout
    watchdog current timeout

dbgfs_dir
    debugfs dir entry

.. _`mei_wdt_start_request`:

struct mei_wdt_start_request
============================

.. c:type:: struct mei_wdt_start_request


.. _`mei_wdt_start_request.definition`:

Definition
----------

.. code-block:: c

    struct mei_wdt_start_request {
        struct mei_mc_hdr hdr;
        u16 timeout;
        u8 reserved[17];
    }

.. _`mei_wdt_start_request.members`:

Members
-------

hdr
    Management Control Command Header

timeout
    timeout value

reserved
    reserved (legacy)

.. _`mei_wdt_start_response`:

struct mei_wdt_start_response
=============================

.. c:type:: struct mei_wdt_start_response


.. _`mei_wdt_start_response.definition`:

Definition
----------

.. code-block:: c

    struct mei_wdt_start_response {
        struct mei_mc_hdr hdr;
        u8 status;
        u8 wdstate;
    }

.. _`mei_wdt_start_response.members`:

Members
-------

hdr
    Management Control Command Header

status
    operation status

wdstate
    watchdog status bit mask

.. _`mei_wdt_stop_request`:

struct mei_wdt_stop_request
===========================

.. c:type:: struct mei_wdt_stop_request

    watchdog stop

.. _`mei_wdt_stop_request.definition`:

Definition
----------

.. code-block:: c

    struct mei_wdt_stop_request {
        struct mei_mc_hdr hdr;
    }

.. _`mei_wdt_stop_request.members`:

Members
-------

hdr
    Management Control Command Header

.. _`mei_wdt_ping`:

mei_wdt_ping
============

.. c:function:: int mei_wdt_ping(struct mei_wdt *wdt)

    send wd start/ping command

    :param struct mei_wdt \*wdt:
        mei watchdog device

.. _`mei_wdt_ping.return`:

Return
------

0 on success,
negative errno code on failure

.. _`mei_wdt_stop`:

mei_wdt_stop
============

.. c:function:: int mei_wdt_stop(struct mei_wdt *wdt)

    send wd stop command

    :param struct mei_wdt \*wdt:
        mei watchdog device

.. _`mei_wdt_stop.return`:

Return
------

0 on success,
negative errno code on failure

.. _`mei_wdt_ops_start`:

mei_wdt_ops_start
=================

.. c:function:: int mei_wdt_ops_start(struct watchdog_device *wdd)

    wd start command from the watchdog core.

    :param struct watchdog_device \*wdd:
        watchdog device

.. _`mei_wdt_ops_start.return`:

Return
------

0 on success or -ENODEV;

.. _`mei_wdt_ops_stop`:

mei_wdt_ops_stop
================

.. c:function:: int mei_wdt_ops_stop(struct watchdog_device *wdd)

    wd stop command from the watchdog core.

    :param struct watchdog_device \*wdd:
        watchdog device

.. _`mei_wdt_ops_stop.return`:

Return
------

0 if success, negative errno code for failure

.. _`mei_wdt_ops_ping`:

mei_wdt_ops_ping
================

.. c:function:: int mei_wdt_ops_ping(struct watchdog_device *wdd)

    wd ping command from the watchdog core.

    :param struct watchdog_device \*wdd:
        watchdog device

.. _`mei_wdt_ops_ping.return`:

Return
------

0 if success, negative errno code on failure

.. _`mei_wdt_ops_set_timeout`:

mei_wdt_ops_set_timeout
=======================

.. c:function:: int mei_wdt_ops_set_timeout(struct watchdog_device *wdd, unsigned int timeout)

    wd set timeout command from the watchdog core.

    :param struct watchdog_device \*wdd:
        watchdog device

    :param unsigned int timeout:
        timeout value to set

.. _`mei_wdt_ops_set_timeout.return`:

Return
------

0 if success, negative errno code for failure

.. _`__mei_wdt_is_registered`:

__mei_wdt_is_registered
=======================

.. c:function:: bool __mei_wdt_is_registered(struct mei_wdt *wdt)

    check if wdt is registered

    :param struct mei_wdt \*wdt:
        mei watchdog device

.. _`__mei_wdt_is_registered.return`:

Return
------

true if the wdt is registered with the watchdog subsystem

.. _`__mei_wdt_is_registered.locking`:

Locking
-------

should be called under wdt->reg_lock

.. _`mei_wdt_unregister`:

mei_wdt_unregister
==================

.. c:function:: void mei_wdt_unregister(struct mei_wdt *wdt)

    unregister from the watchdog subsystem

    :param struct mei_wdt \*wdt:
        mei watchdog device

.. _`mei_wdt_register`:

mei_wdt_register
================

.. c:function:: int mei_wdt_register(struct mei_wdt *wdt)

    register with the watchdog subsystem

    :param struct mei_wdt \*wdt:
        mei watchdog device

.. _`mei_wdt_register.return`:

Return
------

0 if success, negative errno code for failure

.. _`mei_wdt_event_rx`:

mei_wdt_event_rx
================

.. c:function:: void mei_wdt_event_rx(struct mei_cl_device *cldev)

    callback for data receive

    :param struct mei_cl_device \*cldev:
        bus device

.. _`mei_wdt_event`:

mei_wdt_event
=============

.. c:function:: void mei_wdt_event(struct mei_cl_device *cldev, u32 events, void *context)

    callback for event receive

    :param struct mei_cl_device \*cldev:
        bus device

    :param u32 events:
        event mask

    :param void \*context:
        callback context

.. This file was automatic generated / don't edit.

