.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/include/obd.h

.. _`lu_dev_name`:

lu_dev_name
===========

.. c:function:: const char *lu_dev_name(const struct lu_device *lu_dev)

    :param const struct lu_device \*lu_dev:
        *undescribed*

.. _`lu_dev_name.xxx`:

XXX
---

lu_device is declared before obd_device, while a pointer pointing
back to obd_device in lu_device, so this helper function defines here
instead of in lu_object.h

.. This file was automatic generated / don't edit.

