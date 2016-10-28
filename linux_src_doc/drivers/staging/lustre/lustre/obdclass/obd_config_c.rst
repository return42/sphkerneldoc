.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/lustre/lustre/obdclass/obd_config.c

.. _`class_attach`:

class_attach
============

.. c:function:: int class_attach(struct lustre_cfg *lcfg)

    the new device can be accessed by either name or uuid.

    :param struct lustre_cfg \*lcfg:
        *undescribed*

.. _`class_config_parse_rec`:

class_config_parse_rec
======================

.. c:function:: int class_config_parse_rec(struct llog_rec_hdr *rec, char *buf, int size)

    This is separated from \ :c:func:`class_config_dump_handler`\  to use for ioctl needs as well

    :param struct llog_rec_hdr \*rec:
        *undescribed*

    :param char \*buf:
        *undescribed*

    :param int size:
        *undescribed*

.. This file was automatic generated / don't edit.

