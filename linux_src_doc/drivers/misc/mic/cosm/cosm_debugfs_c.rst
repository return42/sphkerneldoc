.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/cosm/cosm_debugfs.c

.. _`cosm_log_buf_show`:

cosm_log_buf_show
=================

.. c:function:: int cosm_log_buf_show(struct seq_file *s, void *unused)

    Display MIC kernel log buffer

    :param struct seq_file \*s:
        *undescribed*

    :param void \*unused:
        *undescribed*

.. _`cosm_log_buf_show.description`:

Description
-----------

log_buf addr/len is read from System.map by user space
and populated in sysfs entries.

.. _`cosm_force_reset_show`:

cosm_force_reset_show
=====================

.. c:function:: int cosm_force_reset_show(struct seq_file *s, void *pos)

    Force MIC reset

    :param struct seq_file \*s:
        *undescribed*

    :param void \*pos:
        *undescribed*

.. _`cosm_force_reset_show.description`:

Description
-----------

Invokes the force_reset COSM bus op instead of the standard reset
op in case a force reset of the MIC device is required

.. This file was automatic generated / don't edit.

