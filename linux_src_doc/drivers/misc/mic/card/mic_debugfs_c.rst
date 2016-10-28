.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/mic/card/mic_debugfs.c

.. _`mic_intr_test`:

mic_intr_test
=============

.. c:function:: int mic_intr_test(struct seq_file *s, void *unused)

    Send interrupts to host.

    :param struct seq_file \*s:
        *undescribed*

    :param void \*unused:
        *undescribed*

.. _`mic_create_card_debug_dir`:

mic_create_card_debug_dir
=========================

.. c:function:: void mic_create_card_debug_dir(struct mic_driver *mdrv)

    Initialize MIC debugfs entries.

    :param struct mic_driver \*mdrv:
        *undescribed*

.. _`mic_delete_card_debug_dir`:

mic_delete_card_debug_dir
=========================

.. c:function:: void mic_delete_card_debug_dir(struct mic_driver *mdrv)

    Uninitialize MIC debugfs entries.

    :param struct mic_driver \*mdrv:
        *undescribed*

.. _`mic_init_card_debugfs`:

mic_init_card_debugfs
=====================

.. c:function:: void mic_init_card_debugfs( void)

    Initialize global debugfs entry.

    :param  void:
        no arguments

.. _`mic_exit_card_debugfs`:

mic_exit_card_debugfs
=====================

.. c:function:: void mic_exit_card_debugfs( void)

    Uninitialize global debugfs entry

    :param  void:
        no arguments

.. This file was automatic generated / don't edit.

