.. -*- coding: utf-8; mode: rst -*-

========
genops.c
========


.. _`class_newdev`:

class_newdev
============

.. c:function:: struct obd_device *class_newdev (const char *type_name, const char *name)

    :param const char \*type_name:

        *undescribed*

    :param const char \*name:

        *undescribed*



.. _`class_newdev.find-an-empty-slot-in`:

Find an empty slot in 
----------------------

:obd_devs[], create a new obd device in it.

\param[in] type_name obd device type string.
\param[in] name      obd device name.

\retval NULL if create fails, otherwise return the obd device
pointer created.



.. _`class_num2obd`:

class_num2obd
=============

.. c:function:: struct obd_device *class_num2obd (int num)

    :param int num:

        *undescribed*



.. _`class_num2obd.description`:

Description
-----------


\param num [in] array index

\retval NULL if ::obd_devs[\a num] does not contains an obd device
otherwise return the obd device there.



.. _`class_notify_sptlrpc_conf`:

class_notify_sptlrpc_conf
=========================

.. c:function:: int class_notify_sptlrpc_conf (const char *fsname, int namelen)

    :param const char \*fsname:

        *undescribed*

    :param int namelen:

        *undescribed*



.. _`class_notify_sptlrpc_conf.description`:

Description
-----------

adjust sptlrpc settings accordingly.



.. _`obd_zombie_impexp_cull`:

obd_zombie_impexp_cull
======================

.. c:function:: void obd_zombie_impexp_cull ( void)

    :param void:
        no arguments



.. _`obd_zombie_impexp_check`:

obd_zombie_impexp_check
=======================

.. c:function:: int obd_zombie_impexp_check (void *arg)

    :param void \*arg:

        *undescribed*



.. _`obd_zombie_export_add`:

obd_zombie_export_add
=====================

.. c:function:: void obd_zombie_export_add (struct obd_export *exp)

    :param struct obd_export \*exp:

        *undescribed*



.. _`obd_zombie_import_add`:

obd_zombie_import_add
=====================

.. c:function:: void obd_zombie_import_add (struct obd_import *imp)

    :param struct obd_import \*imp:

        *undescribed*



.. _`obd_zombie_impexp_notify`:

obd_zombie_impexp_notify
========================

.. c:function:: void obd_zombie_impexp_notify ( void)

    :param void:
        no arguments



.. _`obd_zombie_is_idle`:

obd_zombie_is_idle
==================

.. c:function:: int obd_zombie_is_idle ( void)

    :param void:
        no arguments



.. _`obd_zombie_barrier`:

obd_zombie_barrier
==================

.. c:function:: void obd_zombie_barrier ( void)

    :param void:
        no arguments



.. _`obd_zombie_impexp_thread`:

obd_zombie_impexp_thread
========================

.. c:function:: int obd_zombie_impexp_thread (void *unused)

    :param void \*unused:

        *undescribed*



.. _`obd_zombie_impexp_init`:

obd_zombie_impexp_init
======================

.. c:function:: int obd_zombie_impexp_init ( void)

    :param void:
        no arguments



.. _`obd_zombie_impexp_stop`:

obd_zombie_impexp_stop
======================

.. c:function:: void obd_zombie_impexp_stop ( void)

    :param void:
        no arguments

