.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/pseries/cmm.c

.. _`cmm_alloc_pages`:

cmm_alloc_pages
===============

.. c:function:: long cmm_alloc_pages(long nr)

    Allocate pages and mark them as loaned

    :param nr:
        number of pages to allocate
    :type nr: long

.. _`cmm_alloc_pages.return-value`:

Return value
------------

number of pages requested to be allocated which were not

.. _`cmm_free_pages`:

cmm_free_pages
==============

.. c:function:: long cmm_free_pages(long nr)

    Free pages and mark them as active

    :param nr:
        number of pages to free
    :type nr: long

.. _`cmm_free_pages.return-value`:

Return value
------------

number of pages requested to be freed which were not

.. _`cmm_oom_notify`:

cmm_oom_notify
==============

.. c:function:: int cmm_oom_notify(struct notifier_block *self, unsigned long dummy, void *parm)

    OOM notifier

    :param self:
        notifier block struct
    :type self: struct notifier_block \*

    :param dummy:
        not used
    :type dummy: unsigned long

    :param parm:
        returned - number of pages freed
    :type parm: void \*

.. _`cmm_oom_notify.return-value`:

Return value
------------

NOTIFY_OK

.. _`cmm_get_mpp`:

cmm_get_mpp
===========

.. c:function:: void cmm_get_mpp( void)

    Read memory performance parameters

    :param void:
        no arguments
    :type void: 

.. _`cmm_get_mpp.description`:

Description
-----------

Makes hcall to query the current page loan request from the hypervisor.

.. _`cmm_get_mpp.return-value`:

Return value
------------

nothing

.. _`cmm_thread`:

cmm_thread
==========

.. c:function:: int cmm_thread(void *dummy)

    CMM task thread

    :param dummy:
        not used
    :type dummy: void \*

.. _`cmm_thread.return-value`:

Return value
------------

0

.. _`cmm_sysfs_register`:

cmm_sysfs_register
==================

.. c:function:: int cmm_sysfs_register(struct device *dev)

    Register with sysfs

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`cmm_sysfs_register.return-value`:

Return value
------------

0 on success / other on failure

.. _`cmm_unregister_sysfs`:

cmm_unregister_sysfs
====================

.. c:function:: void cmm_unregister_sysfs(struct device *dev)

    Unregister from sysfs

    :param dev:
        *undescribed*
    :type dev: struct device \*

.. _`cmm_reboot_notifier`:

cmm_reboot_notifier
===================

.. c:function:: int cmm_reboot_notifier(struct notifier_block *nb, unsigned long action, void *unused)

    Make sure pages are not still marked as "loaned"

    :param nb:
        *undescribed*
    :type nb: struct notifier_block \*

    :param action:
        *undescribed*
    :type action: unsigned long

    :param unused:
        *undescribed*
    :type unused: void \*

.. _`cmm_count_pages`:

cmm_count_pages
===============

.. c:function:: unsigned long cmm_count_pages(void *arg)

    Count the number of pages loaned in a particular range.

    :param arg:
        memory_isolate_notify structure with address range and count
    :type arg: void \*

.. _`cmm_count_pages.return-value`:

Return value
------------

0 on success

.. _`cmm_memory_isolate_cb`:

cmm_memory_isolate_cb
=====================

.. c:function:: int cmm_memory_isolate_cb(struct notifier_block *self, unsigned long action, void *arg)

    Handle memory isolation notifier calls

    :param self:
        notifier block struct
    :type self: struct notifier_block \*

    :param action:
        action to take
    :type action: unsigned long

    :param arg:
        struct memory_isolate_notify data for handler
    :type arg: void \*

.. _`cmm_memory_isolate_cb.return-value`:

Return value
------------

NOTIFY_OK or notifier error based on subfunction return value

.. _`cmm_mem_going_offline`:

cmm_mem_going_offline
=====================

.. c:function:: int cmm_mem_going_offline(void *arg)

    Unloan pages where memory is to be removed

    :param arg:
        memory_notify structure with page range to be offlined
    :type arg: void \*

.. _`cmm_mem_going_offline.return-value`:

Return value
------------

0 on success

.. _`cmm_memory_cb`:

cmm_memory_cb
=============

.. c:function:: int cmm_memory_cb(struct notifier_block *self, unsigned long action, void *arg)

    Handle memory hotplug notifier calls

    :param self:
        notifier block struct
    :type self: struct notifier_block \*

    :param action:
        action to take
    :type action: unsigned long

    :param arg:
        struct memory_notify data for handler
    :type arg: void \*

.. _`cmm_memory_cb.return-value`:

Return value
------------

NOTIFY_OK or notifier error based on subfunction return value

.. _`cmm_init`:

cmm_init
========

.. c:function:: int cmm_init( void)

    Module initialization

    :param void:
        no arguments
    :type void: 

.. _`cmm_init.return-value`:

Return value
------------

0 on success / other on failure

.. _`cmm_exit`:

cmm_exit
========

.. c:function:: void cmm_exit( void)

    Module exit

    :param void:
        no arguments
    :type void: 

.. _`cmm_exit.return-value`:

Return value
------------

nothing

.. _`cmm_set_disable`:

cmm_set_disable
===============

.. c:function:: int cmm_set_disable(const char *val, const struct kernel_param *kp)

    Disable/Enable CMM

    :param val:
        *undescribed*
    :type val: const char \*

    :param kp:
        *undescribed*
    :type kp: const struct kernel_param \*

.. _`cmm_set_disable.return-value`:

Return value
------------

0 on success / other on failure

.. This file was automatic generated / don't edit.

