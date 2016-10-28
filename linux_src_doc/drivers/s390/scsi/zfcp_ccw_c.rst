.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/s390/scsi/zfcp_ccw.c

.. _`zfcp_ccw_activate`:

zfcp_ccw_activate
=================

.. c:function:: int zfcp_ccw_activate(struct ccw_device *cdev, int clear, char *tag)

    activate adapter and wait for it to finish

    :param struct ccw_device \*cdev:
        pointer to belonging ccw device

    :param int clear:
        Status flags to clear.

    :param char \*tag:
        s390dbf trace record tag

.. _`zfcp_ccw_probe`:

zfcp_ccw_probe
==============

.. c:function:: int zfcp_ccw_probe(struct ccw_device *cdev)

    probe function of zfcp driver

    :param struct ccw_device \*cdev:
        pointer to belonging ccw device

.. _`zfcp_ccw_probe.description`:

Description
-----------

This function gets called by the common i/o layer for each FCP
device found on the current system. This is only a stub to make cio

.. _`zfcp_ccw_probe.work`:

work
----

To only allocate adapter resources for devices actually used,
the allocation is deferred to the first call to ccw_set_online.

.. _`zfcp_ccw_remove`:

zfcp_ccw_remove
===============

.. c:function:: void zfcp_ccw_remove(struct ccw_device *cdev)

    remove function of zfcp driver

    :param struct ccw_device \*cdev:
        pointer to belonging ccw device

.. _`zfcp_ccw_remove.description`:

Description
-----------

This function gets called by the common i/o layer and removes an adapter
from the system. Task of this function is to get rid of all units and
ports that belong to this adapter. And in addition all resources of this
adapter will be freed too.

.. _`zfcp_ccw_set_online`:

zfcp_ccw_set_online
===================

.. c:function:: int zfcp_ccw_set_online(struct ccw_device *cdev)

    set_online function of zfcp driver

    :param struct ccw_device \*cdev:
        pointer to belonging ccw device

.. _`zfcp_ccw_set_online.description`:

Description
-----------

This function gets called by the common i/o layer and sets an
adapter into state online.  The first call will allocate all
adapter resources that will be retained until the device is removed
via zfcp_ccw_remove.

Setting an fcp device online means that it will be registered with
the SCSI stack, that the QDIO queues will be set up and that the
adapter will be opened.

.. _`zfcp_ccw_offline_sync`:

zfcp_ccw_offline_sync
=====================

.. c:function:: int zfcp_ccw_offline_sync(struct ccw_device *cdev, int set, char *tag)

    shut down adapter and wait for it to finish

    :param struct ccw_device \*cdev:
        pointer to belonging ccw device

    :param int set:
        Status flags to set.

    :param char \*tag:
        s390dbf trace record tag

.. _`zfcp_ccw_offline_sync.description`:

Description
-----------

This function gets called by the common i/o layer and sets an adapter
into state offline.

.. _`zfcp_ccw_set_offline`:

zfcp_ccw_set_offline
====================

.. c:function:: int zfcp_ccw_set_offline(struct ccw_device *cdev)

    set_offline function of zfcp driver

    :param struct ccw_device \*cdev:
        pointer to belonging ccw device

.. _`zfcp_ccw_set_offline.description`:

Description
-----------

This function gets called by the common i/o layer and sets an adapter
into state offline.

.. _`zfcp_ccw_notify`:

zfcp_ccw_notify
===============

.. c:function:: int zfcp_ccw_notify(struct ccw_device *cdev, int event)

    ccw notify function

    :param struct ccw_device \*cdev:
        pointer to belonging ccw device

    :param int event:
        indicates if adapter was detached or attached

.. _`zfcp_ccw_notify.description`:

Description
-----------

This function gets called by the common i/o layer if an adapter has gone
or reappeared.

.. _`zfcp_ccw_shutdown`:

zfcp_ccw_shutdown
=================

.. c:function:: void zfcp_ccw_shutdown(struct ccw_device *cdev)

    handle shutdown from cio

    :param struct ccw_device \*cdev:
        device for adapter to shutdown.

.. This file was automatic generated / don't edit.

