.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/soc/tegra/ivc.h

.. _`tegra_ivc_read_get_next_frame`:

tegra_ivc_read_get_next_frame
=============================

.. c:function:: void *tegra_ivc_read_get_next_frame(struct tegra_ivc *ivc)

    Peek at the next frame to receive \ ``ivc``\          pointer of the IVC channel

    :param ivc:
        *undescribed*
    :type ivc: struct tegra_ivc \*

.. _`tegra_ivc_read_get_next_frame.description`:

Description
-----------

Peek at the next frame to be received, without removing it from
the queue.

Returns a pointer to the frame, or an error encoded pointer.

.. _`tegra_ivc_read_advance`:

tegra_ivc_read_advance
======================

.. c:function:: int tegra_ivc_read_advance(struct tegra_ivc *ivc)

    Advance the read queue \ ``ivc``\          pointer of the IVC channel

    :param ivc:
        *undescribed*
    :type ivc: struct tegra_ivc \*

.. _`tegra_ivc_read_advance.description`:

Description
-----------

Advance the read queue

Returns 0, or a negative error value if failed.

.. _`tegra_ivc_write_get_next_frame`:

tegra_ivc_write_get_next_frame
==============================

.. c:function:: void *tegra_ivc_write_get_next_frame(struct tegra_ivc *ivc)

    Poke at the next frame to transmit \ ``ivc``\          pointer of the IVC channel

    :param ivc:
        *undescribed*
    :type ivc: struct tegra_ivc \*

.. _`tegra_ivc_write_get_next_frame.description`:

Description
-----------

Get access to the next frame.

Returns a pointer to the frame, or an error encoded pointer.

.. _`tegra_ivc_write_advance`:

tegra_ivc_write_advance
=======================

.. c:function:: int tegra_ivc_write_advance(struct tegra_ivc *ivc)

    Advance the write queue \ ``ivc``\          pointer of the IVC channel

    :param ivc:
        *undescribed*
    :type ivc: struct tegra_ivc \*

.. _`tegra_ivc_write_advance.description`:

Description
-----------

Advance the write queue

Returns 0, or a negative error value if failed.

.. _`tegra_ivc_notified`:

tegra_ivc_notified
==================

.. c:function:: int tegra_ivc_notified(struct tegra_ivc *ivc)

    handle internal messages \ ``ivc``\          pointer of the IVC channel

    :param ivc:
        *undescribed*
    :type ivc: struct tegra_ivc \*

.. _`tegra_ivc_notified.description`:

Description
-----------

This function must be called following every notification.

Returns 0 if the channel is ready for communication, or -EAGAIN if a channel
reset is in progress.

.. _`tegra_ivc_reset`:

tegra_ivc_reset
===============

.. c:function:: void tegra_ivc_reset(struct tegra_ivc *ivc)

    initiates a reset of the shared memory state \ ``ivc``\          pointer of the IVC channel

    :param ivc:
        *undescribed*
    :type ivc: struct tegra_ivc \*

.. _`tegra_ivc_reset.description`:

Description
-----------

This function must be called after a channel is reserved before it is used
for communication. The channel will be ready for use when a subsequent call
to notify the remote of the channel reset.

.. This file was automatic generated / don't edit.

