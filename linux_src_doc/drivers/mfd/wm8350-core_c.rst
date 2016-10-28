.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/mfd/wm8350-core.c

.. _`wm8350_reg_lock`:

wm8350_reg_lock
===============

.. c:function:: int wm8350_reg_lock(struct wm8350 *wm8350)

    :param struct wm8350 \*wm8350:
        *undescribed*

.. _`wm8350_reg_lock.description`:

Description
-----------

The WM8350 has a hardware lock which can be used to prevent writes to
some registers (generally those which can cause particularly serious
problems if misused).  This function enables that lock.

.. _`wm8350_reg_unlock`:

wm8350_reg_unlock
=================

.. c:function:: int wm8350_reg_unlock(struct wm8350 *wm8350)

    :param struct wm8350 \*wm8350:
        *undescribed*

.. _`wm8350_reg_unlock.description`:

Description
-----------

The WM8350 has a hardware lock which can be used to prevent writes to
some registers (generally those which can cause particularly serious
problems if misused).  This function disables that lock so updates
can be performed.  For maximum safety this should be done only when
required.

.. This file was automatic generated / don't edit.

