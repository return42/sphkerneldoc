.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/llite/lproc_llite.c

.. _`default_easize_show`:

default_easize_show
===================

.. c:function:: ssize_t default_easize_show(struct kobject *kobj, struct attribute *attr, char *buf)

    :param struct kobject \*kobj:
        *undescribed*

    :param struct attribute \*attr:
        *undescribed*

    :param char \*buf:
        *undescribed*

.. _`default_easize_show.description`:

Description
-----------

\see client_obd::cl_default_mds_easize

\param[in] kobj      kernel object for sysfs tree
\param[in] attr      attribute of this kernel object
\param[in] buf       buffer to write data into

\retval positive     \a count on success
\retval negative     negated errno on failure

.. _`default_easize_store`:

default_easize_store
====================

.. c:function:: ssize_t default_easize_store(struct kobject *kobj, struct attribute *attr, const char *buffer, size_t count)

    :param struct kobject \*kobj:
        *undescribed*

    :param struct attribute \*attr:
        *undescribed*

    :param const char \*buffer:
        *undescribed*

    :param size_t count:
        *undescribed*

.. _`default_easize_store.description`:

Description
-----------

Range checking on the passed value is handled by
\ :c:func:`ll_set_default_mdsize`\ .

\see client_obd::cl_default_mds_easize

\param[in] kobj      kernel object for sysfs tree
\param[in] attr      attribute of this kernel object
\param[in] buffer    string passed from user space
\param[in] count     \a buffer length

\retval positive     \a count on success
\retval negative     negated errno on failure

.. This file was automatic generated / don't edit.

