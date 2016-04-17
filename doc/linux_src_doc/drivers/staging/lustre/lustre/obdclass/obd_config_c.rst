.. -*- coding: utf-8; mode: rst -*-

============
obd_config.c
============


.. _`class_attach`:

class_attach
============

.. c:function:: int class_attach (struct lustre_cfg *lcfg)

    :param struct lustre_cfg \*lcfg:

        *undescribed*



.. _`class_attach.description`:

Description
-----------

the new device can be accessed by either name or uuid.



.. _`class_config_parse_rec`:

class_config_parse_rec
======================

.. c:function:: int class_config_parse_rec (struct llog_rec_hdr *rec, char *buf, int size)

    :param struct llog_rec_hdr \*rec:

        *undescribed*

    :param char \*buf:

        *undescribed*

    :param int size:

        *undescribed*



.. _`class_config_parse_rec.description`:

Description
-----------

This is separated from :c:func:`class_config_dump_handler` to use
for ioctl needs as well

