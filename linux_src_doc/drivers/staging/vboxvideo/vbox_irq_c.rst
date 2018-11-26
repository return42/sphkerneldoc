.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/vboxvideo/vbox_irq.c

.. _`validate_or_set_position_hints`:

validate_or_set_position_hints
==============================

.. c:function:: void validate_or_set_position_hints(struct vbox_private *vbox)

    shell (i.e. all screens disjoint and hints for all enabled screens) and if not replace them with default ones.  Providing valid hints improves the chances that we will get a known screen layout for pointer mapping.

    :param vbox:
        *undescribed*
    :type vbox: struct vbox_private \*

.. _`vbox_update_mode_hints`:

vbox_update_mode_hints
======================

.. c:function:: void vbox_update_mode_hints(struct vbox_private *vbox)

    :param vbox:
        *undescribed*
    :type vbox: struct vbox_private \*

.. This file was automatic generated / don't edit.

