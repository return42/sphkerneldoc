.. -*- coding: utf-8; mode: rst -*-
.. src-file: arch/powerpc/platforms/pseries/cmm.c

.. _`cmm_alloc_pages`:

cmm_alloc_pages
===============

.. c:function:: long cmm_alloc_pages(long nr)

    Allocate pages and mark them as loaned

    :param long nr:
        number of pages to allocate

.. _`cmm_alloc_pages.return-value`:

Return value
------------

number of pages requested to be allocated which were not

.. _`cmm_free_pages`:

cmm_free_pages
==============

.. c:function:: long cmm_free_pages(long nr)

    Free pages and mark them as active

    :param long nr:
        number of pages to free

.. _`cmm_free_pages.return-value`:

Return value
------------

number of pages requested to be freed which were not

.. _`cmm_oom_notify`:

cmm_oom_notify
==============

.. c:function:: int cmm_oom_notify(struct notifier_block *self, unsigned long dummy, void *parm)

    OOM notifier

    :param struct notifier_block \*self:
        notifier block struct

    :param unsigned long dummy:
        not used

    :param void \*parm:
        returned - number of pages freed

.. _`cmm_oom_notify.return-value`:

Return value
------------

NOTIFY_OK

.. _`cmm_get_mpp`:

cmm_get_mpp
===========

.. c:function:: void cmm_get_mpp( void)

    Read memory performance parameters

    :param  void:
        no arguments

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

    :param void \*dummy:
        not used

.. _`cmm_thread.return-value`:

Return value
------------

0

.. _`cmm_sysfs_register`:

cmm_sysfs_register
==================

.. c:function:: int cmm_sysfs_register(struct device *dev)

    Register with sysfs

    :param struct device \*dev:
        *undescribed*

.. _`cmm_sysfs_register.return-value`:

Return value
------------

0 on success / other on failure

.. _`cmm_unregister_sysfs`:

cmm_unregister_sysfs
====================

.. c:function:: void cmm_unregister_sysfs(struct device *dev)

    Unregister from sysfs

    :param struct device \*dev:
        *undescribed*

.. _`cmm_reboot_notifier`:

cmm_reboot_notifier
===================

.. c:function:: int cmm_reboot_notifier(struct notifier_block *nb, unsigned long action, void *unused)

    Make sure pages are not still marked as "loaned"

    :param struct notifier_block \*nb:
        *undescribed*

    :param unsigned long action:
        *undescribed*

    :param void \*unused:
        *undescribed*

.. _`cmm_count_pages`:

cmm_count_pages
===============

.. c:function:: unsigned long cmm_count_pages(void *arg)

    Count the number of pages loaned in a particular range.

    :param void \*arg:
        memory_isolate_notify structure with address range and count

.. _`cmm_count_pages.return-value`:

Return value
------------

0 on success

.. _`cmm_memory_isolate_cb`:

cmm_memory_isolate_cb
=====================

.. c:function:: int cmm_memory_isolate_cb(struct notifier_block *self, unsigned long action, void *arg)

    Handle memory isolation notifier calls

    :param struct notifier_block \*self:
        notifier block struct

    :param unsigned long action:
        action to take

    :param void \*arg:
        struct memory_isolate_notify data for handler

.. _`cmm_memory_isolate_cb.return-value`:

Return value
------------

NOTIFY_OK or notifier error based on subfunction return value

.. _`cmm_mem_going_offline`:

cmm_mem_going_offline
=====================

.. c:function:: int cmm_mem_going_offline(void *arg)

    Unloan pages where memory is to be removed

    :param void \*arg:
        memory_notify structure with page range to be offlined

.. _`cmm_mem_going_offline.return-value`:

Return value
------------

0 on success

.. _`cmm_memory_cb`:

cmm_memory_cb
=============

.. c:function:: int cmm_memory_cb(struct notifier_block *self, unsigned long action, void *arg)

    Handle memory hotplug notifier calls

    :param struct notifier_block \*self:
        notifier block struct

    :param unsigned long action:
        action to take

    :param void \*arg:
        struct memory_notify data for handler

.. _`cmm_memory_cb.return-value`:

Return value
------------

NOTIFY_OK or notifier error based on subfunction return value

.. _`cmm_init`:

cmm_init
========

.. c:function:: int cmm_init( void)

    Module initialization

    :param  void:
        no arguments

.. _`cmm_init.return-value`:

Return value
------------

0 on success / other on failure

.. _`cmm_exit`:

cmm_exit
========

.. c:function:: void cmm_exit( void)

    Module exit

    :param  void:
        no arguments

.. _`cmm_exit.return-value`:

Return value
------------

nothing

.. _`cmm_set_disable`:

cmm_set_disable
===============

.. c:function:: int cmm_set_disable(const char *val, const struct kernel_param *kp)

    Disable/Enable CMM

    :param const char \*val:
        *undescribed*

    :param const struct kernel_param \*kp:
        *undescribed*

.. _`cmm_set_disable.return-value`:

Return value
------------

0 on success / other on failure

.. This file was automatic generated / don't edit.

